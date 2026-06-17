def analyze_sentiment(text):
    text = text.lower()

    positive_words = ["good", "great", "excellent", "amazing"]
    negative_words = ["bad", "poor", "terrible", "awful"]

    for word in positive_words:
        if word in text:
            return "Positive"

    for word in negative_words:
        if word in text:
            return "Negative"

    return "Neutral"


print(analyze_sentiment("This movie is excellent"))