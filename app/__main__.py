import asyncio

import uvicorn
from fastapi import FastAPI
from routes import cache, limiter, router
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

app = FastAPI(
    title="Loyal",
    description="Fast, Simple API for Apple Firmwares",
    version="1.0.0",
    redoc_url="/docs",
    docs_url=None,
)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


@app.on_event("startup")
async def startup_event():
    asyncio.create_task(cache.cache(2400 * 36))


@app.get("/")
async def main():
    return {"code": 200, "status": "Loyal API is working!"}


app.include_router(router, prefix="/v1")

uvicorn.run(app, host="0.0.0.0", port=80)
