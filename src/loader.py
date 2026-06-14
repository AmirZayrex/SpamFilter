import pandas as pd
from .config import DATA_PATH

def load_data():
    df = pd.read_csv(
    DATA_PATH,
    header=None,
    names=['label', 'message'],
    sep='\t')

    df['length'] = df['message'].apply(len)
    return df