from fastapi import FastAPI

from src.core.routers import hello


app = FastAPI(docs_url='/api/first/docs', redoc_url='/api/first/redoc', openapi_url='/api/first/opneapi_path')
app.include_router(hello.router, tags=['first app'])
