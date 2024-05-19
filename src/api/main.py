from turtle import pd
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from contextlib import asynccontextmanager

from api.configs.app_config import AppConfig
from api.search.router import search_router
from api.search.service import ClassificationModel, SearchService
import pymorphy3

json_config = open("api/configs/app_config.json", "r").read()
app_config: AppConfig = AppConfig.model_validate_json(json_config)


@asynccontextmanager
async def lifespan(app: FastAPI) -> None:  # type: ignore
    """Async context manager for managing the lifespan of the application.
    Args:
        app (FastAPI): The FastAPI instance.
    Returns:
        None
    """
    yield


app = FastAPI(lifespan=lifespan)
clsf_model = ClassificationModel(name="bow", model_path="../../data/inf_data/clsf.csv")


@app.get("/")
async def root():
    return HTMLResponse(content=app_config.MOTD, status_code=200)


@app.get("/healthcheck")
async def healthcheck():
    return HTMLResponse(content=app_config.MOTD, status_code=200)


app.include_router(search_router, prefix="/search", tags=["search"])
