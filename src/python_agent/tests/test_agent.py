from agent.service import LangAgent


def test_ingest_and_query():
    a = LangAgent()
    a.ingest_text('Hello world.\n\nThis is a test document.', source='doc1')
    res = a.answer('test')
    assert 'Answer (simple)' in res['answer']
    assert 'doc1' in res['sources']
