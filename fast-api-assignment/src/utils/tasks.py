from gensim.summarization.summarizer import summarize

from src.db.database import get_document_by_id, update_by_id


async def summarize_text(document_id: int):
    document = await get_document_by_id(document_id)
    summary = summarize(document[1])
    await update_by_id(document_id, summary)