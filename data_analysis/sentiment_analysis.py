from textblob import TextBlob
import pandas as pd

def preprocess_and_analyze(file_path="tweets.csv"):
    df = pd.read_csv(file_path)
    df['Cleaned_Text'] = df['Text'].str.replace(r'http\S+', '', regex=True).str.replace(r'@\S+', '', regex=True).str.replace(r'#', '', regex=True)
    df['Sentiment'] = df['Cleaned_Text'].apply(lambda x: TextBlob(x).sentiment.polarity)
    df['Label'] = df['Sentiment'].apply(lambda x: 1 if x > 0 else (0 if x == 0 else -1))
    df.to_csv("processed_tweets.csv", index=False)
    print("Sentiment analysis complete. Saved to processed_tweets.csv")
    return df

if __name__ == "__main__":
    processed_data = preprocess_and_analyze()
