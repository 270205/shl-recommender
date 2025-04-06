from engine.utils import clean_text
import pandas as pd

def keyword_match(user_input, catalog_df):
    user_input = clean_text(user_input)
    user_keywords = [term.strip() for term in user_input.split(",")]

    matched_rows = []

    for _, row in catalog_df.iterrows():
        traits = clean_text(row["Traits"])
        roles = clean_text(row["Suitable For Roles"])

        if any(term in traits or term in roles for term in user_keywords):
            matched_rows.append(row)

    if not matched_rows:
        return pd.DataFrame(columns=catalog_df.columns)

    return pd.DataFrame(matched_rows).drop_duplicates()
