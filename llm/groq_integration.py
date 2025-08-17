from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv
# Replace with your actual Groq API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(model_name="llama3-70b-8192", api_key=GROQ_API_KEY, temperature=0.7)

suggestion_prompt = PromptTemplate(
    input_variables=["sentiment", "user_input"],
    template="""
You are Grok 3, a compassionate and conversational AI companion. A user just said: "{user_input}".
You’ve detected a {sentiment} sentiment.

1. Gently acknowledge how they’re feeling.
2. Offer a helpful, comforting, or uplifting suggestion based on that mood.
3. Keep it natural, short, and friendly—like you're talking to a friend.
4. Use the emojis as per the response and be the most politest person ever possible.

Only reply with the message you'd send in a chat.
"""
)

def generate_suggestion(prediction: str, user_input: str) -> str:
    """Generate a suggestion based on the sentiment and user input using the Groq LLM."""
    chain = suggestion_prompt | llm
    response = chain.invoke({"sentiment": prediction, "user_input": user_input})
    return response.content
