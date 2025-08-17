# LangNet.Agent - Python Minimal Implementation

This folder contains a compact, runnable Python implementation that demonstrates core concepts from the LangNet.Agent project:

- Modular agent architecture
- FastAPI gateway
- Simple in-memory retrieval-augmented generation (RAG)
- Document ingestion (text/PDF placeholder)

Quickstart

1. Create a virtual environment (Python 3.11+ recommended)
2. Install: pip install -e .
3. Run the API: uvicorn agent.app:app --reload
4. Try POST /ask with JSON {"query":"..."}
