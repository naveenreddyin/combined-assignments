from typing import List, Optional
from fastapi import APIRouter, HTTPException, BackgroundTasks
from fastapi.responses import ORJSONResponse


from src.db.database import get_documents, insert_document, get_document_by_id
from src.schema.models import Document, NewDocument, SummaryOut
from src.utils.exceptions import DocumentNotFound
from src.utils.tasks import summarize_text

routes = APIRouter(default_response_class=ORJSONResponse)


@routes.get("/")
async def read_root():
    return {"Hello": "World"}


@routes.get("/document/{document_id}/", response_model=Document)
async def read_document_by_id(document_id: Optional[int] = None):
    """
    Get document by id
    """
    try:
        response = await get_document_by_id(document_id)
    except DocumentNotFound as e:
        raise HTTPException(status_code=400, detail={"document_id": str(e)})
    return response


@routes.get("/summary/{document_id}/", response_model=SummaryOut)
async def read_summary_by_id(document_id: Optional[int] = None):
    """
    Get summary by id
    """
    try:
        response = await get_document_by_id(document_id)
    except DocumentNotFound as e:
        raise HTTPException(status_code=400, detail={"summary_id": str(e)})
    return response


@routes.get("/document/", response_model=List[Document])
async def read_documents():
    """
    get all documents
    """
    return await get_documents()


@routes.post(
    "/document",
    response_model=Document,
    status_code=201,
    response_model_exclude={
        "summary",
        "text",
    },
)
async def create_document(document: NewDocument, background_tasks: BackgroundTasks):
    """
    creates new document
    It also runs backgroung task to get summary
    """
    last_inserted_id = await insert_document(document)
    # run backgroun task to generate summary
    background_tasks.add_task(summarize_text, last_inserted_id)
    # return response without waiting for summarization
    return {**document.dict(), "document_id": last_inserted_id}
