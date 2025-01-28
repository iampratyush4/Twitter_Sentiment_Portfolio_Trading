from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import joblib  # To save/load models

# Initialize VADER
sia = SentimentIntensityAnalyzer()

# Train simple ML model (run once)
def train_model():
    df = pd.read_csv('sentiment140.csv')  # From https://www.kaggle.com/datasets/kazanova/sentiment140
    vectorizer = TfidfVectorizer(max_features=1000)
    X = vectorizer.fit_transform(df['text'])
    model = LogisticRegression()
    model.fit(X, df['sentiment'])
    joblib.dump(model, 'sentiment_model.pkl')
    joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')

def predict_sentiment(text):
    # Load pre-trained model
    model = joblib.load('sentiment_model.pkl')
    vectorizer = joblib.load('tfidf_vectorizer.pkl')
    X = vectorizer.transform([text])
    return model.predict(X)[0]