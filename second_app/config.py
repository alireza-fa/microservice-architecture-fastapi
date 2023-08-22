from fastapi import FastAPI

from src.core.routers import hello


app = FastAPI(docs_url='/api/second/docs', redoc_url='/api/second/redoc', openapi_url='/api/second/opneapi_path')
app.include_router(hello.router, tags=['second app'])
