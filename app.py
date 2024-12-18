
# Import necessary libraries
import os, re
import google.generativeai as genai
import gradio as gr

rubric_text = """
1. Content and Ideas (30 points):
    - Main argument clarity (10 points)
    - Supporting evidence (10 points)
    - Depth of analysis (10 points)

    2. Organization and Structure (25 points):
    - Clear introduction and conclusion (10 points)
    - Logical flow between paragraphs (10 points)
    - Effective transitions (5 points)

    3. Language Usage (25 points):
    - Grammar and mechanics (10 points)
    - Vocabulary and word choice (10 points)
    - Sentence structure variety (5 points)

    4. Critical Thinking (20 points):
    - Original insights (10 points)
    - Counter-arguments addressed (10 points)
"""
def format_output(response_text):
    """
    Format the Gemini output for display in a structured and styled HTML format.
    Args:
        response_text (str): The raw text output from Gemini.
    Returns:
        str: Formatted HTML content.
    """
    # Remove small dots or stray bullet-like characters
    response_text = re.sub(r'^\s*[\u2022•·]\s*', '', response_text, flags=re.MULTILINE)

    # Highlight the overall grade
    response_text = re.sub(r'(?<=Overall Grade: )(\d+/\d+)', r"<strong style='color:green;'>\1</strong>", response_text)

    # Format main sections like "1. Content and Ideas (20/30)"
    response_text = re.sub(r'(\d+\..*?\([\d/]+.*?\))', r"<li style='margin-top:10px;'><strong>\1</strong></li>", response_text)

    # Handle correctly formatted bullet points
    response_text = re.sub(r'\*\*\s*([^*]+?):', r"<li style='margin-left:15px;'><strong>\1:</strong>", response_text)

    # Handle stray asterisks used for emphasis
    response_text = re.sub(r'\*\*', '', response_text)  # Remove extra "**"
    response_text = re.sub(r'\*([^*]+)\*', r"<em>\1</em>", response_text)  # Convert *text* to italicized text

    # Close any unclosed bullet points
    response_text = re.sub(r'\*\*([^*]+?)$', r"<li style='margin-left:15px;'>\1</li>", response_text)

    # Replace newlines with HTML breaks for better spacing
    response_text = re.sub(r'\n', '<br>', response_text)

    # Wrap the formatted text into a styled HTML structure
    formatted_text = f"""
    <div style="font-family: Arial, sans-serif; line-height: 1.8; margin: 15px;">
        <h3 style="color:#4CAF50;">📋 Detailed Rating Feedback</h3>
        <ul>
            {response_text}
        </ul>
    </div>
    """
    return formatted_text
# Initialize Gemini API
genai.configure(api_key="AIzaSyBNrZYC_VIJLWLp4-zBc_PSYm6o8q94SXs")

def grade_and_summarize(essay):
    # Initialize Gemini
    model = genai.GenerativeModel('gemini-2.0-flash-exp')
    # Start a new chat
    chat = model.start_chat(history=[])
    
    # Set up the system prompt and context
    system_prompt = "You are a English bot, you are supposed to carefully grade the essay based on the given rubric and respond in English only." + rubric_text
    
    # Generate response using Gemini's chat format
    response = chat.send_message([
        system_prompt,
        "ESSAY : " + essay
    ])
    
    # Process the response
    data = response.text
    data = re.sub(r'\n', '<br>', data)
    return format_output(data)
    # return data
# Define Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("## 📄 **Essay Grading and Summarization System**")
    gr.Markdown("Enter the grading rubric and essay content below to generate detailed feedback and a summary.")

    # Inputs
    with gr.Row():
        # rubric_input = gr.Textbox(label="Grading Rubric", placeholder="Enter the grading rubric here...", lines=4)
        essay_input = gr.Textbox(label="Essay Content", placeholder="Paste the essay here...", lines=8)

    # Submit button with loading
    with gr.Row():
        submit_btn = gr.Button("🚀 Generate Feedback")
    
    # Outputs
    with gr.Row():
        detailed_output = gr.HTML(label="Detailed Grading Feedback")
        # summary_output = gr.HTML(label="Summary Result")

    # Add a loading indicator
    with gr.Row():
        gr.Markdown("### ⏳ **Processing, please wait...**", visible=False, elem_id="loading_indicator")

    # Function to trigger with loading state
    def process_with_loading(rubric, essay):
        # Show loading indicator
        gr.update(visible=True, elem_id="loading_indicator")
        result = grade_and_summarize(rubric, essay)
        # Hide loading indicator
        gr.update(visible=False, elem_id="loading_indicator")
        return result

    # Connect inputs and outputs
    submit_btn.click(grade_and_summarize, 
                     inputs=[essay_input], 
                     outputs=[detailed_output])

# Launch the Gradio interface
demo.launch()



