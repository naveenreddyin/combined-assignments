from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src import app

client = TestClient(app)

BIG_TEXT = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
It has survived not only five centuries, but also the leap into electronic typesetting, 
remaining essentially unchanged. It was popularised in the 1960s with the release of 
etraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software 
like Aldus PageMaker including versions of Lorem Ipsum.
Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
It has survived not only five centuries, but also the leap into electronic typesetting, 
remaining essentially unchanged. It was popularised in the 1960s with the release of 
etraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software 
like Aldus PageMaker including versions of Lorem Ipsum.
Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
It has survived not only five centuries, but also the leap into electronic typesetting, 
remaining essentially unchanged. It was popularised in the 1960s with the release of 
etraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software 
like Aldus PageMaker including versions of Lorem Ipsum.
    """


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_create_document_with_exception():
    """
    Test creating document with POST request without sending text, should except 422 status code
    """
    response = client.post("/document")
    assert response.status_code == 422


def test_create_document():
    """
    Test creating a new document using POST request with sending only big text. It should return just document_id
    """
    response = client.post("/document", json={"text": BIG_TEXT})
    assert response.status_code == 201
    assert len(response.json()) == 1
    assert "document_id" in response.json()


def test_get_document():
    """
    Test GET endpoint for document, it will return the list of all available documents.
    """
    response = client.get("/document/")
    assert response.status_code == 200


def test_get_document_by_id():
    """
    Test GET endpointto get document by id
    """
    # id given is by test database
    response = client.get("/document/1")
    assert response.status_code == 200


def test_get_document_by_id_with_exception():
    """
    Test to check exception if document id is not present
    """
    response = client.get("/document/100")
    assert response.status_code == 400


def test_get_document_by_id_with_type_exception():
    """
    Test to check exception if document id not int
    """
    response = client.get("/document/hello")
    assert response.status_code == 422


def test_get_summary_by_id_with_exception():
    """
    Test to GET summary by given document_id as path param and if not found it should throw 400 NOT 404 (SECURITY!!)
    """
    response = client.get("/summary/0")
    assert response.status_code == 400


def test_get_summary_by_id():
    """
    Test to GET summary by given document_id as path param.
    """
    response = client.post("/document", json={"text": BIG_TEXT})
    document_id = response.json()["document_id"]
    response = client.get(f"/summary/{document_id}")
    assert response.status_code == 200
    assert "summary" in response.json()
