import requests

class SampleClient:
    def __init__(self, base_url: str = 'http://localhost:8000'):
        self.base = base_url

    def ingest_text(self, text: str, filename: str = 'inline.txt'):
        files = {'file': (filename, text)}
        r = requests.post(f"{self.base}/ingest", files=files)
        return r.json()

    def ask(self, query: str):
        r = requests.post(f"{self.base}/ask", json={'query': query})
        return r.json()
