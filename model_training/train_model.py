import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_model(tweets_file="processed_tweets.csv", stock_file="stock_prices.csv"):

    # Load datasets
    sentiment_data = pd.read_csv(tweets_file)
    stock_data = pd.read_csv(stock_file)  # Ensure this file contains a "Date" and "Stock_Movement" column
    
    # Merge datasets on the date
    merged_data = pd.merge(sentiment_data, stock_data, on="Date")  # Replace "Date" with the actual column name
    X = merged_data[['Sentiment']].values
    y = merged_data['Stock_Movement']  # Replace with actual column for stock trend

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Evaluate model
    predictions = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, predictions)}")

if __name__ == "__main__":
    train_model()
