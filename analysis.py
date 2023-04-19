import pandas as pd
import nltk
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer

data = pd.read_csv(r"D:\Github\NLP\Spam_classification\preprocessed_data.csv")

nltk.download('vader_lexicon')

def perform_textblob_sentiment(text):
    
    analysis = TextBlob(text)
    
    return analysis.sentiment.polarity

analyzer = SentimentIntensityAnalyzer()

def get_vader_sentiment(text):
    
    scores = analyzer.polarity_scores(text)
    
    return scores['compound']

data["tb_score"] = data["processed_message"].apply(perform_textblob_sentiment)

data["tb_label"] = data["tb_score"].apply(lambda x: "Positive" if x>0 else "Negative" if x<0 else "Neutral")

data["vader_intensity"] = data["processed_message"].apply(get_vader_sentiment)

data["vader_sentiment"] = data["vader_intensity"].apply(lambda x: "Positive" if x>0 else "Negative" if x<0 else "Neutral")

data.to_csv("data_with_sentiment.csv")