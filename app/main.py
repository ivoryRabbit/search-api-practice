from operator import itemgetter
from fastapi import FastAPI

from app.api.models import ResponseOut
from app.api.datasets import InvertedIndex, TermFrequency, DocumentFrequency, ItemMeta
from app.utils.tokenizer import Tokenizer

app = FastAPI()
tokenizer = Tokenizer()

inverted_index = InvertedIndex()
term_frequency = TermFrequency()
document_frequency = DocumentFrequency()
item_meta = ItemMeta()


@app.get("/search", response_model=ResponseOut)
def get_score(query: str):
    tokens = tokenizer.tokenize(query)
    docs = [inverted_index[token] for token in tokens]
    comm_docs = set.intersection(*docs)

    data = []
    for doc in comm_docs:
        # tf-idf(tokens, doc) := max{ tf-idf(token, doc) | token in tokens }
        score = max(term_frequency[doc][token] * document_frequency[token] for token in tokens)

        data.append({
            "item_id": str(doc),
            "title": item_meta[doc],
            "score": score
        })

    # expose top-10 movies
    data = sorted(data, key=itemgetter("score"), reverse=True)[:10]
    return {"data": data}
