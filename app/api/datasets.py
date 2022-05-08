import pickle
import math
import pandas as pd
from abc import ABC, abstractmethod
from typing import Dict, Set, Any


class Dataset(ABC):
    def __init__(self):
        self.data = self._load_data()

    @abstractmethod
    def __getitem__(self, item):
        pass

    @abstractmethod
    def _load_data(self):
        pass


class InvertedIndex(Dataset):
    def __getitem__(self, item: str) -> Set[int]:
        return self.data.get(item, {})

    def _load_data(self) -> Dict[str, Set[int]]:
        with open("data/inverted_index.pkl", "rb") as f:
            return pickle.load(f)


class TermFrequency(Dataset):
    def __getitem__(self, item: int) -> Dict[str, Any]:
        return self.data[item]

    def _load_data(self) -> Dict[int, Dict[str, Any]]:
        with open("data/term_frequency.pkl", "rb") as f:
            term_frequency = pickle.load(f)

        for doc in term_frequency.keys():
            total = sum(term_frequency[doc].values())
            for token, tf in term_frequency[doc].items():
                term_frequency[doc][token] = tf / total

        return term_frequency


class DocumentFrequency(Dataset):
    def __getitem__(self, item: str) -> float:
        return math.log(len(self.data) / self.data[item])

    def _load_data(self) -> Dict[str, int]:
        with open("data/document_frequency.pkl", "rb") as f:
            document_frequency = pickle.load(f)

        total = len(document_frequency)
        for token, df in document_frequency.items():
            document_frequency[token] = math.log(total / df)

        return document_frequency


class ItemMeta(Dataset):
    def __getitem__(self, item: int) -> str:
        return self.data[item]

    def _load_data(self) -> Dict[int, str]:
        return pd.read_csv("data/movies.csv").set_index("item_id").to_dict()["title"]
