# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message": "Backend is running!"}


from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
import asyncio

from modules.research_agent import process_topic

app = FastAPI()

# CORS for frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryInput(BaseModel):
    topics: List[str]
    sources: List[str] = ["news", "arxiv"]
    time_range: str = "7d"  # 7d, 30d, etc.

@app.post("/search")
async def search_query(data: QueryInput):
    results = await process_topic(data.topics, data.sources, data.time_range)
    return {"summary": results}