# 📝 Essay Grading and Summarization System

## 🌟 Overview
This advanced Essay Grading and Summarization System leverages Google's Gemini AI to provide comprehensive essay evaluation and concise summarization. Built with Python, Gemini API, and Gradio, the system offers:
- Detailed essay grading
- Automated summarization
- Interactive web interface
- Rubric-based assessment

## 🚀 Key Features
- **Intelligent Grading**: 100-point scoring system
- **Comprehensive Feedback**: Detailed analysis across multiple categories
- **AI-Powered Summarization**: Concise essay summaries
- **User-Friendly Interface**: Web-based interaction using Gradio
- **Flexible Rubric**: Customizable grading criteria

## 📋 System Architecture
- **Backend**: Python
- **AI Model**: Google Gemini Pro
- **Web Interface**: Gradio
- **Key Libraries**: 
  - `google-generativeai`
  - `gradio`
  - `json`

## 🛠 Prerequisites
- Python 3.10+
- Google Cloud Account
- Gemini API Key

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/osamaalschame/Eassy-grading-system-using-LLMs
cd Eassy-grading-system-using-LLMs
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up API Key:
- Create a `.env` file in the project root
- Add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

## 📝 Grading Rubric Breakdown
The system uses a comprehensive 100-point grading rubric:

### 1. Content and Ideas (30 points)
- Main argument clarity (10 points)
- Supporting evidence (10 points)
- Depth of analysis (10 points)

### 2. Organization and Structure (25 points)
- Clear introduction and conclusion (10 points)
- Logical flow between paragraphs (10 points)
- Effective transitions (5 points)

### 3. Language Usage (25 points)
- Grammar and mechanics (10 points)
- Vocabulary and word choice (10 points)
- Sentence structure variety (5 points)

### 4. Critical Thinking (20 points)
- Original insights (10 points)
- Counter-arguments addressed (10 points)

## 🖥 Usage

### Running the Web Interface
```bash
python app.py
```

## Example Workflow
1. Upload essay
2. System processes essay
3. Receive detailed grading report
4. Get concise summary
5. View interactive visualization of scores

## 🔍 Upcoming Features
- Multi-language support
- Plagiarism detection
- Detailed learning analytics
- Export functionality

## 🙏 Acknowledgments
- Google AI Gemini Team
- Gradio Developers
- Open-Source Community



---

**Disclaimer**: This system is an AI-assisted tool and should not replace human judgment in academic assessment.
