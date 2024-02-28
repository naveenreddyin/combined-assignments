import databases
import sqlalchemy

from sqlalchemy import text
from sqlalchemy.sql.sqltypes import String

from src.utils.exceptions import DocumentNotFound

metadata = sqlalchemy.MetaData()

DATABASE_URL = "sqlite:///./data.db"
database = databases.Database(DATABASE_URL)
document = sqlalchemy.Table(
    "documents",
    metadata,
    sqlalchemy.Column("document_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("text", sqlalchemy.Text),
    sqlalchemy.Column("summary", sqlalchemy.String),
)


def check_conn():

    pass
def configure_db():
    """
    configuration of db happens in this method
    """
    engine = sqlalchemy.create_engine(
        DATABASE_URL, connect_args={"check_same_thread": False}
    )

    metadata.create_all(engine)
    return metadata, database


async def get_document_by_id(document_id: int):
    """
    get document by id
    """
    whereclause = text(f"document_id = {document_id}")

    query = document.select(whereclause=whereclause)

    try:
        result = await database.fetch_one(query)
    except TimeoutError as e:
        raise TimeoutError("Timeout happened")
    if result is None:
        raise DocumentNotFound("Problem fetching the document")
    return result


async def update_by_id(document_id: int, summary: String):
    """
    update a given document by its id
    """
    whereclause = text(f"document_id = {document_id}")
    query = document.update(whereclause=whereclause).values(summary=summary)
    last_record_id = await database.execute(query)
    print(last_record_id)


async def get_documents():
    """
    get all the documents stored
    """

    query = document.select()

    result = await database.fetch_all(query)

    return result


async def insert_document(newdocument):
    """
    create new document in the database and returns last recorded id.
    """
    query = document.insert().values(text=newdocument.text)
    last_record_id = await database.execute(query)
    return last_record_id
