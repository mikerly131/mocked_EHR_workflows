"""
File that runs the FastAPI application
"""
from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
from db import pg_database


# app = FastAPI()
# To hide the docs, which is better for websites
# alternatively, use first app and modify each route to hide: @router.get('/account', include_in_schema=False)
app = FastAPI(docs_url=None, redoc_url=None)


@app.on_event("startup")
async def on_startup():
    await pg_database.init_db()
