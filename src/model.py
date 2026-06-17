# def analyze_sentiment(text):
#     return "Neutral"


# class BERTModel:
#     def predict(self, text):
#         return "Positive"


# version = "1.0"

# class TransformerModel:
#     pass

def analyze_sentiment(text):
    text = text.lower()

    if "good" in text:
        return "Positive"
    elif "bad" in text:
        return "Negative"
    return "Neutral"

