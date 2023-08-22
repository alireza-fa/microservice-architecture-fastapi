from fastapi import FastAPI

from src.core.routers import hello


app = FastAPI(docs_url='/api/third/docs', redoc_url='/api/third/redoc', openapi_url='/api/third/opneapi_path')
app.include_router(hello.router, tags=['third app'])
