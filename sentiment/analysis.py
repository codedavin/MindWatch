import re
import nltk
import torch
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Download required NLTK data if not already present
nltk.download('stopwords')
nltk.download('punkt')

# Setup stopwords and model
stop_words = set(stopwords.words('english'))
MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
labels = ['Negative', 'Neutral', 'Positive']

def clean_text(text: str) -> str:
    """Clean input text by removing URLs, mentions, hashtags and punctuation."""
    text = re.sub(r"http\S+|@\w+|#\w+|[^\w\s]", "", text)
    tokens = word_tokenize(text.lower())
    tokens = [t for t in tokens if t not in stop_words]
    return " ".join(tokens)

def predict_emotion(text: str):
    """Predict sentiment of the text and return sentiment label along with probabilities."""
    cleaned = clean_text(text)
    inputs = tokenizer(cleaned, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        logits = model(**inputs).logits
    probs = torch.nn.functional.softmax(logits, dim=1).squeeze().numpy()
    prediction = labels[np.argmax(probs)]
    return prediction, probs
