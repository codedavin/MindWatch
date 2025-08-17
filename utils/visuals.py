import matplotlib.pyplot as plt

def get_sentiment_emoji(sentiment: str) -> str:
    """Return an emoji representing the sentiment."""
    emoji_map = {
        "Positive": "😊",
        "Neutral": "😐",
        "Negative": "😞"
    }
    return emoji_map.get(sentiment, "")

def plot_mood_bar_chart(sentiments: list):
    """Plot a bar chart showing the frequency of each sentiment."""
    counts = {label: sentiments.count(label) for label in ["Negative", "Neutral", "Positive"]}
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.bar(counts.keys(), counts.values(), color=['red', 'gray', 'green'])
    ax.set_xlabel("Mood")
    ax.set_ylabel("Frequency")
    ax.set_title("Mood Frequency")
    return fig

def plot_mood_trend(sentiments: list):
    """Plot a trend chart based on mood score mapping: Negative=0, Neutral=1, Positive=2."""
    mapping = {"Negative": 0, "Neutral": 1, "Positive": 2}
    trend = [mapping[s] for s in sentiments]
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.plot(range(1, len(trend) + 1), trend, marker='o')
    ax.set_xlabel("Message Number")
    ax.set_ylabel("Mood Score (0=Negative, 1=Neutral, 2=Positive)")
    ax.set_title("Mood Trend")
    ax.set_ylim(-0.5, 2.5)
    return fig
