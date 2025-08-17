# MindWatch Chat

MindWatch Chat is a mental health chatbot that leverages a RoBERTa model for sentiment analysis and a Groq-powered language model for generating empathetic responses. The chatbot features interactive, detailed mood visualizations (such as a pie chart per response and an aggregated mood dashboard) and contextual cues to help track the user’s emotional state over time.

## Features

- Real-time Sentiment Analysis: Uses a RoBERTa model to predict if a message is Negative, Neutral, or Positive.
- Empathetic Responses: Integrates a Groq-powered language model that provides conversational responses with mood-specific suggestions.
- Interactive Visualizations:
  - Detailed per-message mood pie chart (toggleable).
  - Aggregated mood dashboard (frequency bar chart and mood trend).
  - Contextual emojis added to chatbot responses.
- Modular Code Structure: The project is divided into modules for sentiment analysis, LLM integration, and visualization utilities.

## Repository Structure

mindwatch-chat/
├── .gitignore
├── README.md
├── requirements.txt
├── app.py                    # Main Streamlit app
├── llm/
│   ├── __init__.py
│   └── groq_integration.py   # Groq LLM setup and response generation
├── sentiment/
│   ├── __init__.py
│   └── analysis.py          # Text cleaning and sentiment analysis functions
└── utils/
    ├── __init__.py
    └── visuals.py           # Plotting functions and visual helpers

## Getting Started

### Prerequisites

- Python 3.7+
- Install dependencies via pip:
  
  pip install -r requirements.txt

### Setup

1. Clone the Repository  
   
   git clone https://github.com/codedavin/MindWatch  
   cd MindWatch

2. Configure your Groq API Key:  
   
   Open the file llm/groq_integration.py and replace the placeholder Groq API key with your actual API key.

### Running the App

Launch the Streamlit app via the command line:
  
  streamlit run app.py

The chatbot interface will launch in your browser. Use the sidebar to toggle detailed mood visualizations or view the mood dashboard.

## Contributing

Contributions are welcome! Please open issues or pull requests on GitHub. For major changes, open an issue first to discuss what you’d like to change.

## License

This project is licensed under the MIT License.

Happy Coding!
