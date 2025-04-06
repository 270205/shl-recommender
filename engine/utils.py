import pandas as pd

def load_catalog(path="data/shl_product_catalog.csv"):
    return pd.read_csv(path, on_bad_lines='skip')  # ✅ 'skip' in quotes


def clean_text(text):
    return text.lower().strip()
