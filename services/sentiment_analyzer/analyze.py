import sys
from textblob import TextBlob

def analyze_sentiment(text):
    try:
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        if polarity > 0:
            return "Positive"
        elif polarity < 0:
            return "Negative"
        else:
            return "Neutral"
    except Exception as e:
        return f"Error analyzing sentiment: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyze.py '<text>'")
        sys.exit(1)
    text = sys.argv[1]
    result = analyze_sentiment(text)
    print(result)