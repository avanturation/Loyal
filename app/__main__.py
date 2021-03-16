import uvicorn
from fastapi import FastAPI

app = FastAPI()

uvicorn.run(app)
