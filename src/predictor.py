import string
import os
import sys
import pandas as pd
from nltk.corpus import stopwords
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


def clean_text(text: str):
    text = text.lower()
    text = ''.join(char for char in text if char not in string.punctuation)
    words = text.split()
    words = [w for w in words if w not in stopwords.words('english')]
    return words


"""مسیر فایل اجرایی (exe) یا سورس رو پیدا می‌کنه"""
def _get_base_path():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        # از src به ریشه پروژه (دو سطح بالا)
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(_get_base_path(), 'Data', 'SMSSpamCollection')


# Cached model in 'RAM' (Singleton pattern) — replacing pickle for simplicity
# The model is trained once and stays in memory while the app is running.
# No need to write/read a .pkl file, which caused path issues with PyInstaller.
_pipeline = None

def _load_or_train():
    """مدل رو یا از حافظه برمی‌گردونه یا از نو آموزش میده"""
    global _pipeline
    if _pipeline is not None:
        return _pipeline

    df = pd.read_csv(DATA_PATH, header=None, names=['label', 'message'], sep='\t')
    _pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(analyzer=clean_text)),
        ('classifier', MultinomialNB())
    ])
    _pipeline.fit(df['message'], df['label'])
    return _pipeline


def predict_message(text: str):
    """
    پیش‌بینی یک پیام (Spam یا Ham)
    """
    pipeline = _load_or_train()

    prediction = pipeline.predict([text])[0]
    prob = pipeline.predict_proba([text])[0]

    classes = pipeline.classes_
    ham_idx = list(classes).index("ham")
    spam_idx = list(classes).index("spam")

    return {
        'prediction': prediction,
        'ham_prob': prob[ham_idx],
        'spam_prob': prob[spam_idx]
    }


if __name__ == "__main__":
    test_msg = "Congratulations! You won a free iPhone!"
    result = predict_message(test_msg)
    print(f"Message: {test_msg}")
    print(f"Prediction: {result['prediction']}")
    print(f"Ham: {result['ham_prob']:.2%} | Spam: {result['spam_prob']:.2%}")