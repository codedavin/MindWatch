import streamlit as st
import matplotlib.pyplot as plt

from sentiment.analysis import predict_emotion, labels
from llm.groq_integration import generate_suggestion
from utils.visuals import get_sentiment_emoji, plot_mood_bar_chart, plot_mood_trend

# --- Streamlit UI Setup ---
st.set_page_config(page_title="MindWatch Chat", page_icon="🧠")
st.title("🧠 MindWatch Chat")
st.markdown("Hey there, I'm **MindWatch** 👋 — your friendly AI buddy. Let's chat. How are you feeling today?")

# --- Session State Setup ---
if "messages" not in st.session_state:
    st.session_state.messages = []
if "sentiments" not in st.session_state:
    st.session_state.sentiments = []  # Track sentiments over conversation

# --- Sidebar Options ---
st.sidebar.header("Options")
show_details = st.sidebar.checkbox("Show Detailed Mood Visualizations", value=False)
if st.sidebar.button("Show Mood Dashboard"):
    if st.session_state.sentiments:
        st.sidebar.subheader("Mood Frequency")
        bar_fig = plot_mood_bar_chart(st.session_state.sentiments)
        st.sidebar.pyplot(bar_fig)
        st.sidebar.subheader("Mood Trend")
        trend_fig = plot_mood_trend(st.session_state.sentiments)
        st.sidebar.pyplot(trend_fig)
    else:
        st.sidebar.info("No mood data yet. Chat a bit and come back!")

# --- Display Chat History ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        content = message["content"]
        if message["role"] == "assistant" and "sentiment" in message:
            emoji = get_sentiment_emoji(message["sentiment"])
            content = f"{emoji} {content}"
        st.markdown(content)
        # Display detailed visualization if available
        if message["role"] == "assistant" and "pie_chart" in message and show_details:
            if message["pie_chart"] is not None:
                st.pyplot(message["pie_chart"])

# --- User Input ---
user_input = st.chat_input("Tell me what's on your mind...")

if user_input:
    # Append the user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Just a sec, let me think..."):
            try:
                # Predict mood and update mood log
                prediction, probabilities = predict_emotion(user_input)
                st.session_state.sentiments.append(prediction)

                # Generate a smaller pie chart for detailed view (if enabled)
                fig = None
                if show_details:
                    fig, ax = plt.subplots(figsize=(2, 2))
                    ax.pie(probabilities, labels=labels, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 6})
                    ax.axis("equal")
                    plt.title("Mood Breakdown", fontsize=8)

                # Generate assistant response text via the LLM
                response = generate_suggestion(prediction, user_input)

                # Append assistant's response to session state
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response,
                    "sentiment": prediction,
                    "pie_chart": fig
                })

                emoji = get_sentiment_emoji(prediction)
                st.markdown(f"{response}")
                if show_details and fig is not None:
                    st.pyplot(fig)

            except Exception as e:
                st.error(f"Oops, something went wrong: {str(e)}")
