import pandas as pd
from app.utils.tokenizer import Tokenizer
from app.utils.transformer import Transformer

transformer = Transformer()
tokenizer = Tokenizer()


if __name__ == "__main__":
    item_df = pd.read_csv("data/movies.csv")

    item_df \
        .assign(text=lambda df: df["title"] + df["genres"].apply(transformer.refine_genres),
                tokens=lambda df: df["text"].apply(tokenizer.tokenize)) \
        .drop(columns="text") \
        .to_json("data/tokenized.json", orient="records", force_ascii=False)
