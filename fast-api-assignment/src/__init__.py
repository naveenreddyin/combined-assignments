from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routing import routes
from src.db.database import configure_db

app = FastAPI(title="fast-api-assignment API", version="0.1.0")

# create table and configure db engine
metadata, database = configure_db()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes, tags=["fast-api-assignment"])
