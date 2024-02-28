from pydantic import BaseModel
from typing import Optional


class NewDocument(BaseModel):
    text: str


class SummaryOut(BaseModel):
    document_id: int
    summary: str = None


class Document(SummaryOut):
    text: str = None
