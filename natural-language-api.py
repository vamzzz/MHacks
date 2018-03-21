import argparse

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


def print_result(comments):
    score = comments.document_sentiment.score
    magnitude = comments.document_sentiment.magnitude
    polarity = comments.document_sentiment.polarity

    print("Overall Comments Sentiment\nScore: {0}\nMagnitude: {1}\nPolarity: {2}")
        .format(score,magnitude,polarity)

    return 0

def analyze(text):
    """Run a sentiment analysis request on text within a passed filename."""
    client = language.LanguageServiceClient()

    if isInstance(text, six.binary_type):
    	text = text.decode('utf-8')

    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    sentiment = client.analyze_sentiment(document).document_sentiment

    print('Score: {}'.format(sentiment.score))
    print('Magnitude: {}'.format(sentiment.magnitude))


