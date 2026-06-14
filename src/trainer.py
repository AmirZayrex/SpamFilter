import pickle
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

from .cleaner import clean_text
from .config import MODEL_PATH

def train_and_save_model(df):
    """
    آموزش مدل و ذخیره کل Pipeline
    """
    # Pipeline
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(analyzer=clean_text)),
        ('classifier', MultinomialNB()),
    ])

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        df['message'],
        df['label'],
        test_size=0.2,
        random_state=42
    )

    # Train کل Pipeline
    pipeline.fit(X_train, y_train)

    # ذخیره کل Pipeline (نه فقط مدل) wb -> Write Binary
    with open(MODEL_PATH, 'wb') as model_file:
        pickle.dump(pipeline, model_file)

    # Evaluation
    y_pred = pipeline.predict(X_test)

    print(f"Classification Report: \n{classification_report(y_test, y_pred)}")
    print(f"\nConfusion Matrix: \n{confusion_matrix(y_test, y_pred)}")

    return pipeline

