from src.model import analyze_sentiment


def test_positive_sentiment():
    assert analyze_sentiment("This is good") == "Positive"


def test_negative_sentiment():
    assert analyze_sentiment("This is bad") == "Negative"


def test_neutral_sentiment():
    assert analyze_sentiment("Hello world") == "Neutral"