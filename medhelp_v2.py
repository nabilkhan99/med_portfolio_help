import streamlit as st
from st_copy_to_clipboard import st_copy_to_clipboard
import anthropic
import openai
import re
import config


st.set_page_config(
        page_title="GP Portfolio Case Review Generator",
        page_icon="🏥",
        layout="wide"
    )


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
            "brief_description": "",
            "capabilities": {},
            "reflection": "",
            "learning_needs": ""
        }
        
        # Extract brief description
        summary_pattern = r"Brief Description:\s*(.*?)(?=\n\n|$)"
        summary_match = re.search(summary_pattern, text, re.DOTALL)
        if summary_match:
            sections["brief_description"] = summary_match.group(1).strip()
        
        # Extract capabilities - handle both formats
        for cap_name in selected_capabilities:
            # Try multiple patterns to match different formats
            patterns = [
                # Pattern 1: Full format with "Capability:" prefix and "Justification:"
                f"Capability: {re.escape(cap_name)}.*?Justification.*?:(.*?)(?=Capability:|Reflection:|Learning needs|$)",
                # Pattern 2: Just capability name with colon
                f"{re.escape(cap_name)}:(.*?)(?=\n\n[A-Za-z]|Reflection:|Learning needs|$)",
                # Pattern 3: Just capability name without colon
                f"{re.escape(cap_name)}\n(.*?)(?=\n\n[A-Za-z]|Reflection:|Learning needs|$)"
            ]
            
            content = None
            for pattern in patterns:
                match = re.search(pattern, text, re.DOTALL)
                if match:
                    content = match.group(1).strip()
                    break
            
            if content:
                sections["capabilities"][cap_name] = content
            else:
                st.warning(f"Could not find content for capability: {cap_name}")
                sections["capabilities"][cap_name] = ""
        
        # Extract reflection (handle with or without question mark)
        reflection_patterns = [
            r"Reflection: What will I maintain, improve or stop\?(.*?)(?=Learning needs|$)",
            r"Reflection: What will I maintain, improve or stop(.*?)(?=Learning needs|$)",
            r"Reflection:(.*?)(?=Learning needs|$)"
        ]
        
        for pattern in reflection_patterns:
            reflection_match = re.search(pattern, text, re.DOTALL)
            if reflection_match:
                sections["reflection"] = reflection_match.group(1).strip()
                break
        
        # Extract learning needs
        learning_pattern = r"Learning needs identified from this event:(.*?)(?=$)"
        learning_match = re.search(learning_pattern, text, re.DOTALL)
        if learning_match:
            sections["learning_needs"] = learning_match.group(1).strip()
        
        return sections
    except Exception as e:
        st.error(f"Error extracting sections: {str(e)}")
        return None
    

def improve_case_with_ai(original_case, improvement_prompt, session_state):
    """Improve the case review while maintaining structure and conversation context."""
    try:
        client = init_openai_client()
        messages = [
            {"role": "system", "content": config.SYSTEM_PROMPT},
            {"role": "user", "content": config.EXAMPLE_1},
            {"role": "assistant", "content": config.EXAMPLE_1_RESPONSE},
            {"role": "user", "content": config.EXAMPLE_2},
            {"role": "assistant", "content": config.EXAMPLE_2_RESPONSE}
        ]
        
        if hasattr(session_state, 'llm_conversation_history') and session_state.llm_conversation_history:
            initial_generation = next(
                (msg for msg in session_state.llm_conversation_history 
                 if "Generate a structured case review" in msg.get("content", "")), 
                None
            )
            if initial_generation:
                messages.extend([
                    initial_generation,
                    session_state.llm_conversation_history[
                        session_state.llm_conversation_history.index(initial_generation) + 1
                    ]
                ])
            
            recent_improvements = [
                msg for msg in session_state.llm_conversation_history[-4:]
                if "Improve the case" in msg.get("content", "")
            ]
            for improve_msg in recent_improvements:
                msg_index = session_state.llm_conversation_history.index(improve_msg)
                messages.extend([improve_msg, session_state.llm_conversation_history[msg_index + 1]])
        
        formatted_capabilities = format_capabilities(session_state.selected_caps)
        
        # Get improved version
        response = client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            max_tokens=4000,
            temperature=0.7
        )
        
        if response.choices and len(response.choices) > 0:
            improved_content = response.choices[0].message.content
            improved_content = improved_content.replace('*', '').replace('#', '')
            
            # Extract sections from improved content
            new_sections = extract_sections(improved_content, session_state.selected_caps)
            
            if new_sections:
                # Update session state
                session_state.review_content = improved_content
                session_state.sections = new_sections
                
                # Update title based on improved content
                brief_description = new_sections.get("brief_description", "")
                if brief_description:
                    session_state.case_title = generate_title(brief_description)
                
                # Store the improvement interaction
                session_state.interaction_history.append({
                    "original": original_case,
                    "prompt": improvement_prompt,
                    "improved": improved_content
                })
                
                session_state.llm_conversation_history.extend([
                    {"role": "user", "content": f"Improve the case: {improvement_prompt}"},
                    {"role": "assistant", "content": improved_content}
                ])
                
                return improved_content
            else:
                raise Exception("Failed to extract sections from improved content")
        else:
            raise Exception("No content in OpenAI response")
            
    except Exception as e:
        raise Exception(f"Error improving case: {str(e)}")



# Update session state initialization
if 'initialized' not in st.session_state:
    st.session_state.initialized = True
    st.session_state.review_content = None
    st.session_state.sections = None
    st.session_state.selected_caps = []
    st.session_state.capabilities_select = []
    st.session_state.case_title = None
    st.session_state.case_description = ""
    st.session_state.previous_reviews = []
    st.session_state.interaction_history = []
    st.session_state.llm_conversation_history = []  # Add this line


def generate_title(case_description):
    """Generate a brief title from the case description."""
    try:
        client = init_openai_client()
        messages = [
            {
                "role": "system",
                "content": "You are a medical assistant that generates brief (4-6 words) clinical case titles. Make them professional and medical in nature."
            },
            {
                "role": "user",
                "content": f"Generate a brief clinical case title from this description:\n{case_description}"
            }
        ]
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=50,
            temperature=0.7
        )
        
        if response.choices and len(response.choices) > 0:
            return response.choices[0].message.content.strip().replace('"',"")
        else:
            return "Case Review"
            
    except Exception as e:
        return "Case Review"

def generate_case_review(case_description, selected_capabilities):
    """Generate initial case review using selected AI model."""
    formatted_capabilities = format_capabilities(selected_capabilities)
    
    try:
        client = init_openai_client()
        messages = [
            {
                "role": "system",
                "content": config.SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": config.EXAMPLE_1
            },
            {
                "role": "assistant",
                "content": config.EXAMPLE_1_RESPONSE
            },
            {
                "role": "user",
                "content": config.EXAMPLE_2
            },
            {
                "role": "assistant",
                "content": config.EXAMPLE_2_RESPONSE
            },
            {
                "role": "user",
                "content": f"""Generate a structured case review with the following:
            {config.MAIN_PROMPT.format(
                formatted_capabilities=formatted_capabilities,
                case_description=case_description
            )}"""
            }
        ]
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=4000,
            temperature=0.7
        )
        
        if response.choices and len(response.choices) > 0:
            content = response.choices[0].message.content
            content = content.replace('*', '').replace('#', '')
            
            # Store the initial generation in conversation history
            if 'llm_conversation_history' not in st.session_state:
                st.session_state.llm_conversation_history = []
                
            st.session_state.llm_conversation_history.extend([
                messages[-1],  # The generation request
                {
                    "role": "assistant",
                    "content": content
                }
            ])
            
            return content
        else:
            raise Exception("No content in OpenAI response")
            
    except Exception as e:
        raise Exception(f"Error generating review: {str(e)}")
    

def main():
    # Initialize session state variables
    if 'initialized' not in st.session_state:
        st.session_state.initialized = True
        st.session_state.is_improve_mode = False
        st.session_state.review_content = None
        st.session_state.sections = None
        st.session_state.selected_caps = []
        st.session_state.capabilities_select = []
        st.session_state.case_title = None
        st.session_state.case_description = ""
        st.session_state.previous_reviews = []
        st.session_state.interaction_history = []
        st.session_state.llm_conversation_history = []
    
    # Ensure is_improve_mode exists in session state
    if 'is_improve_mode' not in st.session_state:
        st.session_state.is_improve_mode = False
    
    st.title("GP Portfolio Case Review Generator 🏥")
    
    capabilities = parse_capabilities(config.capability_content)
    
    col1, col2 = st.columns([2, 1], gap="large")
    
    with col1:
        if not st.session_state.is_improve_mode:
            st.subheader("Edit Case Description")
            if not st.session_state.case_description:
                st.session_state.case_description = st.text_area(
                    "Enter your case description",
                    height=200,
                    help="Provide a detailed description of the clinical case",
                    key="case_description_input"
                )
            else:
                new_description = st.text_area(
                    "Edit your case description",
                    value=st.session_state.case_description,
                    height=200,
                    key="case_description_edit"
                )
                if new_description != st.session_state.case_description:
                    st.session_state.case_description = new_description
                    # Update the title when description changes
                    try:
                        st.session_state.case_title = generate_title(new_description)
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error updating title: {str(e)}")
        else:
            st.subheader("Improve with AI")
            improvement_prompt = st.text_area(
                "How would you like to improve the case?",
                help="E.g., 'Make it shorter', 'Change patient's age to 25', 'Add more clinical details'",
                height=100,
                key="improvement_prompt"
            )
            
            if st.button("Improve Case"):
                with st.spinner("Improving case description..."):
                    try:
                        improved_case = improve_case_with_ai(
                            st.session_state.case_description,
                            improvement_prompt,
                            st.session_state
                        )
                        if improved_case:
                            st.session_state.case_title = generate_title(st.session_state.sections["brief_description"])
                            st.success("Case improved successfully!")
                            st.rerun()
                    except Exception as e:
                        st.error(f"Error improving case: {str(e)}")

        if not st.session_state.is_improve_mode:
            generate_disabled = len(st.session_state.get('capabilities_select', [])) == 0 or \
                            len(st.session_state.get('capabilities_select', [])) > 3 or \
                            not st.session_state.case_description
            
            if st.button("Generate Case Review", 
                        disabled=generate_disabled,
                        type="primary",
                        key="generate_button"):
                if len(st.session_state.get('capabilities_select', [])) == 0:
                    st.error("Please select at least one capability")
                elif len(st.session_state.get('capabilities_select', [])) > 3:
                    st.error("Please select no more than three capabilities")
                elif not st.session_state.case_description:
                    st.error("Please enter a case description")
                else:
                    with st.spinner("Generating case review..."):
                        try:
                            st.session_state.case_title = generate_title(st.session_state.case_description)
                            review = generate_case_review(
                                st.session_state.case_description,
                                st.session_state.capabilities_select
                            )
                            
                            if review:
                                st.session_state.previous_reviews.append({
                                    "case_description": st.session_state.case_description,
                                    "capabilities": st.session_state.capabilities_select.copy(),
                                    "review": review
                                })
                                
                                st.session_state.review_content = review
                                st.session_state.sections = extract_sections(review, st.session_state.capabilities_select)
                                st.session_state.selected_caps = st.session_state.capabilities_select.copy()
                                st.session_state.is_improve_mode = True
                                
                                if not st.session_state.sections:
                                    st.error("Failed to parse the generated review. Please try again.")
                                    return
                                
                                st.rerun()
                        except Exception as e:
                            st.error(f"Error generating review: {str(e)}")
        
        # New Case button (only shown in improve mode)
        if st.session_state.is_improve_mode:
            if st.button("New Case", type="secondary"):
                # Reset all state variables
                st.session_state.review_content = None
                st.session_state.sections = None
                st.session_state.selected_caps = []
                st.session_state.capabilities_select = []
                st.session_state.case_title = None
                st.session_state.case_description = ""
                st.session_state.previous_reviews = []
                st.session_state.interaction_history = []
                st.session_state.llm_conversation_history = []
                st.session_state.is_improve_mode = False
                st.rerun()

    # Sidebar column (col2)
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
    
# Display generated review sections
    if st.session_state.sections:
        st.header(st.session_state.case_title or "Case Review")
        
        # Brief Description section
        st.subheader("Brief Description")
        edited_summary = st.text_area(
            "Edit Brief Description",
            st.session_state.sections["brief_description"],
            height=150,
            key="brief_description"
        )
        st_copy_to_clipboard(edited_summary, "Copy Brief Description")
        
        # Capabilities sections
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
        
        # Reflection section
        st.subheader("Reflection: What will I maintain, improve or stop?")
        edited_reflection = st.text_area(
            "Edit Reflection", 
            st.session_state.sections["reflection"],
            height=150,
            key="reflection"
        )
        st_copy_to_clipboard(edited_reflection, "Copy Reflection")
        
        # Learning needs section
        st.subheader("Learning needs identified from this event")
        edited_learning = st.text_area(
            "Edit Learning Needs", 
            st.session_state.sections["learning_needs"],
            height=150,
            key="learning"
        )
        st_copy_to_clipboard(edited_learning, "Copy Learning Needs")

    # Sidebar help section
    st.sidebar.markdown("## How to use")
    st.sidebar.markdown("""
    1. Enter your case description in the text area
    2. Select 1-3 capabilities from the dropdown
    3. Click 'Generate Case Review'
    4. Edit the generated sections as needed
    5. Copy individual sections as needed
    """)

if __name__ == "__main__":
    main()
    
