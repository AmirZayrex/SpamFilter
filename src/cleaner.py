import string
from nltk.corpus import stopwords

def clean_text(text: str):
    """
    تمیزکاری متن:
    ۱. حذف علائم نگارشی
    ۲. تبدیل به حروف کوچک
    ۳. حذف کلمات توقف (stopwords)

    Args:
        text: متن خام پیام
    Returns:
        لیست کلمات تمیز شده
    """
    text = text.lower()

    text = ''.join(char for char in text if char not in string.punctuation)

    words = text.split()

    words = [w for w in words if w not in stopwords.words('english')]

    return words
