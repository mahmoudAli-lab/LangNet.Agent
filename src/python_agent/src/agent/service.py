from typing import List, Dict, Any
from dataclasses import dataclass, field
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np


@dataclass
class Document:
    text: str
    source: str
    embedding: np.ndarray = field(repr=False)


class InMemoryVectorStore:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.texts: List[str] = []
        self.sources: List[str] = []
        self.matrix = None

    def add(self, text: str, source: str = ''):
        self.texts.append(text)
        self.sources.append(source)
        # rebuild matrix (small-scale demo)
        self.matrix = self.vectorizer.fit_transform(self.texts)

    def search(self, query: str, k: int = 3):
        if not self.texts:
            return []
        q_vec = self.vectorizer.transform([query])
        # cosine similarity
        sims = (self.matrix @ q_vec.T).toarray().ravel()
        idx = np.argsort(sims)[::-1][:k]
        from dataclasses import asdict
        results = []
        for i in idx:
            doc = Document(text=self.texts[i], source=self.sources[i], embedding=None)
            results.append(doc)
        return results


class LangAgent:
    def __init__(self):
        self.store = InMemoryVectorStore()

    def ingest_text(self, text: str, source: str = '<inline>'):
        # naive split by paragraphs
        parts = [p.strip() for p in text.split('\n\n') if p.strip()]
        for p in parts:
            self.store.add(p, source=source)

    def answer(self, query: str) -> Dict[str, Any]:
        # retrieve
        hits = self.store.search(query, k=3)
        context = '\n\n'.join([h.text for h in hits]) if hits else ''
        # simplistic generation: echo + context
        response = f"Answer (simple): Based on retrieved documents:\n{context}\n\nQuery: {query}"
        return {"answer": response, "sources": [h.source for h in hits]}
