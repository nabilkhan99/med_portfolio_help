




import streamlit as st
from st_copy_to_clipboard import st_copy_to_clipboard
import anthropic
import openai
import re
import config

def init_anthropic_client():
    return anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])

def init_openai_client():
    """Initialize OpenAI client with API key from secrets."""
    client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    return client

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
    try:
        sections = {
            "case_summary": "",
            "capabilities": {},
            "reflection": "",
            "learning_needs": ""
        }
        
        # Extract case summary
        summary_pattern = r"Case Summary:(.*?)(?=Capability:|$)"
        summary_match = re.search(summary_pattern, text, re.DOTALL)
        if summary_match:
            sections["case_summary"] = summary_match.group(1).strip()
        
        # Extract capabilities with better error handling
        text_chunks = text.split("Capability: ")
        for cap_name in selected_capabilities:
            found = False
            for chunk in text_chunks:
                if chunk.startswith(cap_name):
                    justification = re.split(r"Justification.*?:", chunk, maxsplit=1)[-1]
                    justification = re.split(r"(?=Capability:|Reflection:|Learning needs)", justification)[0]
                    sections["capabilities"][cap_name] = justification.strip()
                    found = True
                    break
            if not found:
                st.warning(f"Could not find content for capability: {cap_name}")
                sections["capabilities"][cap_name] = ""
        
        # Extract reflection
        reflection_pattern = r"Reflection: What will I maintain, improve or stop\?(.*?)(?=Learning needs|$)"
        reflection_match = re.search(reflection_pattern, text, re.DOTALL)
        if reflection_match:
            sections["reflection"] = reflection_match.group(1).strip()
        
        # Extract learning needs
        learning_pattern = r"Learning needs identified from this event:(.*?)(?=\Z)"
        learning_match = re.search(learning_pattern, text, re.DOTALL)
        if learning_match:
            sections["learning_needs"] = learning_match.group(1).strip()
        
        return sections
    except Exception as e:
        st.error(f"Error extracting sections: {str(e)}")
        return None

def generate_case_review(case_description, selected_capabilities):
    """Generate case review using selected AI model."""
    formatted_capabilities = format_capabilities(selected_capabilities)
    full_prompt = st.session_state.current_prompt.format(
        case_description=case_description,
        capabilities=formatted_capabilities
    )
    
    try:
        # OpenAI (GPT-4) implementation
        client = init_openai_client()
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "system",
                "content": st.session_state.current_system_prompt,
                "role": "user",
                "content": full_prompt,
            }],
            max_tokens=4000,
            temperature=0.7
        )
        
        if response.choices and len(response.choices) > 0:
            content = response.choices[0].message.content
            content = content.replace('*', '').replace('#', '').replace('-','')
        else:
            raise Exception("No content in OpenAI response")
            
        return content
        
    except Exception as e:
        raise Exception(f"Error generating review: {str(e)}")

def main():
    st.set_page_config(
        page_title="GP Portfolio Case Review Generator",
        page_icon="🏥",
        layout="wide"
    )

    # Initialize session state
    if 'initialized' not in st.session_state:
        st.session_state.initialized = True
        st.session_state.review_content = None
        st.session_state.sections = None
        st.session_state.selected_caps = []
        st.session_state.capabilities_select = []
        st.session_state.current_prompt = config.prompt_content
        st.session_state.current_system_prompt = config.system_prompt
        st.session_state.show_prompt_editor = False
    
    st.title("GP Portfolio Case Review Generator 🏥")
    
    # Add prompt editor toggle in sidebar
    with st.sidebar:
        st.markdown("## How to use")
        st.markdown("""
        1. Enter your case description in the text area
        2. Select 1-3 capabilities from the dropdown
        3. Click 'Generate Case Review'
        4. Edit the generated sections as needed
        5. Copy individual sections as needed
        """)
        
        st.markdown("---")
        st.markdown("## Advanced Settings")
        show_prompt_editor = st.toggle("Show Prompt Editors", value=st.session_state.show_prompt_editor)
        st.session_state.show_prompt_editor = show_prompt_editor
    
    # Show prompt editors if toggled
    if st.session_state.show_prompt_editor:
        st.markdown("---")
        
        # System Prompt Editor
        st.subheader("System Prompt Editor")
        edited_system_prompt = st.text_area(
            "Edit System Prompt",
            value=st.session_state.current_system_prompt,
            height=200,
            help="Edit the system prompt that sets the AI's behavior and context."
        )
        
        col1, col2 = st.columns([1, 4])
        with col1:
            if st.button("Update System Prompt", type="primary", key="update_system"):
                st.session_state.current_system_prompt = edited_system_prompt
                st.success("System prompt updated successfully!")
        with col2:
            if st.button("Reset System Prompt", key="reset_system"):
                st.session_state.current_system_prompt = config.system_prompt
                st.success("System prompt reset to default!")
        
        st.markdown("---")
        
        # Main Prompt Editor
        st.subheader("Main Prompt Template Editor")
        edited_prompt = st.text_area(
            "Edit Prompt Template",
            value=st.session_state.current_prompt,
            height=300,
            help="Edit the prompt template. Use {case_description} and {capabilities} as placeholders."
        )
        
        col1, col2 = st.columns([1, 4])
        with col1:
            if st.button("Update Prompt", type="primary", key="update_main"):
                st.session_state.current_prompt = edited_prompt
                st.success("Main prompt updated successfully!")
        with col2:
            if st.button("Reset Prompt", key="reset_main"):
                st.session_state.current_prompt = config.prompt_content
                st.success("Main prompt reset to default!")
        
        st.markdown("---")
    
    capabilities = parse_capabilities(config.capability_content)
    
    col1, col2 = st.columns([2, 1], gap="large")
    
    with col1:
        case_description = st.text_area(
            "Enter your case description",
            height=200,
            help="Provide a detailed description of the clinical case",
            key="case_description"
        )
        
        # Button logic with better state handling
        generate_disabled = len(st.session_state.get('capabilities_select', [])) == 0 or \
                          len(st.session_state.get('capabilities_select', [])) > 3 or \
                          not case_description
        
        if st.button("Generate Case Review", 
                    disabled=generate_disabled,
                    type="primary",
                    key="generate_button"):
            if len(st.session_state.get('capabilities_select', [])) == 0:
                st.error("Please select at least one capability")
            elif len(st.session_state.get('capabilities_select', [])) > 3:
                st.error("Please select no more than three capabilities")
            elif not case_description:
                st.error("Please enter a case description")
            else:
                with st.spinner("Generating case review..."):
                    try:
                        review = generate_case_review(
                            case_description,
                            st.session_state.capabilities_select
                        )
                        
                        if review:
                            st.session_state.review_content = review
                            st.session_state.sections = extract_sections(review, st.session_state.capabilities_select)
                            st.session_state.selected_caps = st.session_state.capabilities_select.copy()
                            
                            if not st.session_state.sections:
                                st.error("Failed to parse the generated review. Please try again.")
                                return
                    except Exception as e:
                        st.error(f"Error generating review: {str(e)}")
    
    with col2:
        selected_capabilities = st.multiselect(
            "Choose up to 3 capabilities",
            options=list(capabilities.keys()),
            max_selections=3,
            help="Select 1-3 capabilities that this case demonstrates",
            key="capabilities_select"
        )
        
        if selected_capabilities:
            st.subheader("Selected Capabilities Details")
            for cap in selected_capabilities:
                with st.expander(cap):
                    for point in capabilities[cap]:
                        st.write(point)
    
    if st.session_state.sections:
        st.header("Generated Case Review")
        
        # Case Summary
        st.subheader("Case Summary")
        edited_summary = st.text_area(
            "Edit Case Summary",
            st.session_state.sections["case_summary"],
            height=150,
            key="case_summary"
        )
        st_copy_to_clipboard(edited_summary, "Copy Case Summary")
        
        # Capabilities
        capabilities_text = {}
        for cap_name in st.session_state.selected_caps:
            if cap_name in st.session_state.sections.get("capabilities", {}):
                st.subheader(cap_name)
                edited_cap = st.text_area(
                    f"Edit justification for {cap_name}", 
                    st.session_state.sections["capabilities"][cap_name],
                    height=150,
                    key=f"cap_{cap_name}"
                )
                capabilities_text[cap_name] = edited_cap
                st_copy_to_clipboard(edited_cap, f"Copy {cap_name} justification")
        
        # Reflection
        st.subheader("Reflection: What will I maintain, improve or stop?")
        edited_reflection = st.text_area(
            "Edit Reflection", 
            st.session_state.sections["reflection"],
            height=150,
            key="reflection"
        )
        st_copy_to_clipboard(edited_reflection, "Copy Reflection")
        
        # Learning needs
        st.subheader("Learning needs identified from this event")
        edited_learning = st.text_area(
            "Edit Learning Needs", 
            st.session_state.sections["learning_needs"],
            height=150,
            key="learning"
        )
        st_copy_to_clipboard(edited_learning, "Copy Learning Needs")

if __name__ == "__main__":
    main()
