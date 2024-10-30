Med Portfolio Helper: https://caseforge.streamlit.app/


# CaseForge: GP Portfolio Case Review Generator 🏥

CaseForge is a streamlined tool designed to help GP trainees generate and format portfolio case reviews. Using Claude AI, it produces structured reviews complete with capabilities, reflections, and learning needs.

## Setup Instructions

### Windows

1. Install Python 3.12 from the [official Python website](https://www.python.org/downloads/windows/)
   - During installation, make sure to check "Add Python 3.12 to PATH"
   - Click "Install Now"

2. Open Command Prompt (cmd.exe) and clone the repository:
   ```cmd
   git clone https://github.com/nabilkhan99/med_portfolio_help.git
   cd med_portfolio_help
   ```

3. Create and activate a virtual environment:
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```

4. Install requirements:
   ```cmd
   pip install -r requirements.txt
   ```

5. Create `.streamlit/secrets.toml` and add your API key:
   ```toml
   ANTHROPIC_API_KEY = "your-api-key-here"
   ```

6. Run the application:
   ```cmd
   streamlit run medhelp_v2.py
   ```

### macOS

1. Install Python 3.12 via Homebrew:
   ```bash
   brew install python@3.12
   ```

2. Clone the repository:
   ```bash
   git clone https://github.com/nabilkhan99/med_portfolio_help.git
   cd med_portfolio_help
   ```

3. Create and activate a virtual environment:
   ```bash
   python3.12 -m venv venv
   source venv/bin/activate
   ```

4. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

5. Create `.streamlit/secrets.toml` and add your API key:
   ```bash
   mkdir -p .streamlit
   echo 'ANTHROPIC_API_KEY = "your-api-key-here"' > .streamlit/secrets.toml
   ```

6. Run the application:
   ```bash
   streamlit run medhelp_v2.py
   ```

## Usage

1. Enter your case description in the main text area
2. Select exactly 3 capabilities from the dropdown menu
3. Click "Generate Case Review"
4. Edit the generated sections as needed
5. Use the clipboard icons to copy individual sections
6. Download the complete review when finished

## Requirements

- Python 3.12
- See requirements.txt for package dependencies
- Anthropic API key (Claude AI)

## Problems?

- Ensure Python 3.12 is correctly installed (`python --version` or `python3.12 --version`)
- Check that your virtual environment is activated
- Verify your API key is correctly set in `.streamlit/secrets.toml`
- Make sure all requirements are installed correctly
