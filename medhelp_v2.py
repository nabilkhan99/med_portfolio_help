import streamlit as st
from st_copy_to_clipboard import st_copy_to_clipboard
import anthropic
import re
import config

def init_anthropic_client():
    return anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])

def parse_capabilities(content):
    """Parse capabilities from config content."""
    capabilities = {}
    current_capability = None
    current_points = []
    
    lines = [line.rstrip() for line in content.split('\n') if line.strip()]
    
    for line in lines:
        if not line.startswith('-'):
            if current_capability and current_points:
                capabilities[current_capability] = current_points
            current_capability = line
            current_points = []
        else:
            current_points.append(line)
    
    if current_capability and current_points:
        capabilities[current_capability] = current_points
    
    return capabilities

def format_capabilities(selected_capabilities):
    """Format selected capabilities into text format."""
    formatted_text = ""
    for cap in selected_capabilities:
        formatted_text += f"Capability: {cap}\n"
        formatted_text += "Justification [describe how your actions and approach link to the capability]:\n\n"
    return formatted_text

def extract_sections(text, selected_capabilities):
    """Extract the different sections from the generated text."""
    sections = {
        "capabilities": {},
        "reflection": "",
        "learning_needs": ""
    }
    
    text_chunks = text.split("Capability: ")
    
    for cap_name in selected_capabilities:
        for chunk in text_chunks:
            if chunk.startswith(cap_name):
                justification = re.split(r"Justification.*?:", chunk, maxsplit=1)[-1]
                justification = re.split(r"(?:Capability:|Reflection:|Learning needs)", justification)[0]
                sections["capabilities"][cap_name] = justification.strip()
                break
    
    reflection_pattern = r"Reflection: What will I maintain, improve or stop\?(.*?)(?=Learning needs|$)"
    reflection_match = re.search(reflection_pattern, text, re.DOTALL)
    if reflection_match:
        sections["reflection"] = reflection_match.group(1).strip()
    
    learning_pattern = r"Learning needs identified from this event:(.*?)$"
    learning_match = re.search(learning_pattern, text, re.DOTALL)
    if learning_match:
        sections["learning_needs"] = learning_match.group(1).strip()
    
    return sections

def generate_case_review(case_description, selected_capabilities):
    """Generate case review using Claude."""
    client = init_anthropic_client()
    
    formatted_capabilities = format_capabilities(selected_capabilities)
    
    full_prompt = config.prompt_content.format(
        case_description=case_description,
        capabilities=formatted_capabilities
    )
    
    try:
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=4000,
            messages=[{
                "role": "user",
                "content": full_prompt
            }]
        )
        
        if hasattr(message, 'content') and isinstance(message.content, list):
            content = ' '.join([block.text for block in message.content if hasattr(block, 'text')])
        elif hasattr(message, 'content'):
            content = str(message.content)
        else:
            raise Exception("Unexpected response format from Claude")
            
        return content
        
    except Exception as e:
        raise Exception(f"Error generating review: {str(e)}")

def main():
    st.set_page_config(
        page_title="GP io Case Review Generator",
        page_icon="🏥",
        layout="wide"
    )

    if 'initialized' not in st.session_state:
        st.session_state.initialized = True
        st.session_state.review_content = None
        st.session_state.sections = None
        st.session_state.selected_caps = None
    
    st.title("GP Portfolio Case Review Generator 🏥")
    
    capabilities = parse_capabilities(config.capability_content)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        case_description = st.text_area(
            "Enter your case description",
            height=200,
            help="Provide a detailed description of the clinical case",
            key="case_description"
        )
    
    with col2:
        selected_capabilities = st.multiselect(
            "Choose exactly 3 capabilities",
            options=list(capabilities.keys()),
            max_selections=3,
            help="Select three capabilities that this case demonstrates",
            key="capabilities_select"
        )
        
        if selected_capabilities:
            st.subheader("Selected Capabilities Details")
            for cap in selected_capabilities:
                with st.expander(cap):
                    for point in capabilities[cap]:
                        st.write(point)
    
    generate_disabled = len(selected_capabilities) != 3 or not case_description
    if st.button("Generate Case Review", 
                 disabled=generate_disabled,
                 type="primary",
                 key="generate_button"):
        if len(selected_capabilities) != 3:
            st.error("Please select exactly 3 capabilities")
        elif not case_description:
            st.error("Please enter a case description")
        else:
            with st.spinner("Generating case review..."):
                try:
                    review = generate_case_review(
                        case_description,
                        selected_capabilities
                    )
                    
                    if review:
                        st.session_state.review_content = review
                        st.session_state.sections = extract_sections(review, selected_capabilities)
                        st.session_state.selected_caps = selected_capabilities
                
                except Exception as e:
                    st.error(f"Error generating review: {str(e)}")
    
    if st.session_state.sections:
        st.header("Generated Case Review")
        
        for cap_name, justification in st.session_state.sections["capabilities"].items():
            st.subheader(cap_name)
            edited_cap = st.text_area(
                f"Edit justification for {cap_name}", 
                justification, 
                height=150, 
                key=f"cap_{cap_name}"
            )
            st_copy_to_clipboard(edited_cap, f"Copy {cap_name} justification")
        
        st.subheader("Reflection: What will I maintain, improve or stop?")
        edited_reflection = st.text_area(
            "Edit Reflection", 
            st.session_state.sections["reflection"], 
            height=150,
            key="reflection"
        )
        st_copy_to_clipboard(edited_reflection, "Copy Reflection")
        
        st.subheader("Learning needs identified from this event")
        edited_learning = st.text_area(
            "Edit Learning Needs", 
            st.session_state.sections["learning_needs"], 
            height=150,
            key="learning"
        )
        st_copy_to_clipboard(edited_learning, "Copy Learning Needs")
        
        complete_review = ""
        for cap_name in st.session_state.selected_caps:
            complete_review += f"Capability: {cap_name}\n"
            complete_review += "Justification [describe how your actions and approach link to the capability]:\n"
            complete_review += st.session_state.sections["capabilities"][cap_name] + "\n\n"
        
        complete_review += "Reflection: What will I maintain, improve or stop?\n"
        complete_review += edited_reflection + "\n\n"
        complete_review += "Learning needs identified from this event:\n"
        complete_review += edited_learning
        
        st.download_button(
            "Download Complete Review",
            complete_review,
            file_name="case_review.md",
            mime="text/markdown"
        )

    st.sidebar.markdown("## How to use")
    st.sidebar.markdown("""
    1. Enter your case description in the text area
    2. Select exactly 3 capabilities from the dropdown
    3. Click 'Generate Case Review'
    4. Edit the generated sections as needed
    5. Copy individual sections or download the complete review
    """)

if __name__ == "__main__":
    main()
