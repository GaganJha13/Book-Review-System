import json
from mockredis import MockRedis

cache = MockRedis()

async def get_books_from_cache():
    books = await cache.get("books")
    return json.loads(books) if books else None

async def save_books_to_cache(data):
    await cache.set("books", json.dumps(data))