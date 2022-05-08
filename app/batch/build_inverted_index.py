import pandas as pd
import pickle
from collections import Counter


def calculate_term_frequency(df: pd.DataFrame) -> pd.Series:
    return df["tokens"].apply(Counter)


if __name__ == "__main__":
    nested_df = pd.read_json("data/tokenized.json", typ="frame")

    exploded_df = nested_df \
        .explode("tokens") \
        .rename(columns={"tokens": "token"})

    # Inverted Index 계산
    inverted_index = exploded_df \
        .groupby("token") \
        .agg(item_ids=("item_id", set)) \
        .to_dict()["item_ids"]

    with open("data/inverted_index.pkl", "wb") as f:
        pickle.dump(inverted_index, f)

    # Term Frequency 계산
    term_frequency = nested_df \
        .assign(TF=calculate_term_frequency) \
        .set_index("item_id") \
        .to_dict()["TF"]

    with open("data/term_frequency.pkl", "wb") as f:
        pickle.dump(term_frequency, f)

    # Document Frequency 계산
    document_frequency = exploded_df \
        .groupby("token") \
        .agg(DF=("item_id", "nunique")) \
        .to_dict()["DF"]

    with open("data/document_frequency.pkl", "wb") as f:
        pickle.dump(document_frequency, f)
