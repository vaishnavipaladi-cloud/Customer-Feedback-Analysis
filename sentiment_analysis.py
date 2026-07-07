import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
import re
from nltk.corpus import stopwords

nltk.download('vader_lexicon', quiet=True)
nltk.download('stopwords', quiet=True)

def load_data(filepath):
    df = pd.read_csv(filepath)
    df['date'] = pd.to_datetime(df['date'])
    return df

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z\s]', '', text)
    stop_words = set(stopwords.words('english'))
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return ' '.join(words)

def analyze_sentiment_vader(text):
    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(str(text))['compound']
    if score >= 0.05:
        return 'Positive', score
    elif score <= -0.05:
        return 'Negative', score
    else:
        return 'Neutral', score

def analyze_sentiment_textblob(text):
    score = TextBlob(str(text)).sentiment.polarity
    if score > 0:
        return 'Positive', score
    elif score < 0:
        return 'Negative', score
    else:
        return 'Neutral', score

def get_keywords(df, n=20):
    all_text = ' '.join(df['review_text'].apply(clean_text))
    words = all_text.split()
    freq = pd.Series(words).value_counts().head(n)
    return freq