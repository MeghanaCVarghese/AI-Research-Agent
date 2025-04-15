import asyncio
from utils.scraper import fetch_news, fetch_arxiv
from utils.summarizer import summarize_text

async def process_topic(topics, sources, time_range):
    raw_data = []

    if "news" in sources:
        news = await fetch_news(topics, time_range)
        raw_data.extend(news)
    
    if "arxiv" in sources:
        arxiv = await fetch_arxiv(topics)
        raw_data.extend(arxiv)

    summarized = summarize_text(raw_data)
    return summarized