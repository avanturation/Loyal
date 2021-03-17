import uvicorn
import asyncio
from fastapi import FastAPI
from .routes import router, cache

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    asyncio.create_task(cache.cache(2400 * 36))


app.include_router(router)

uvicorn.run(app, port=2400)
