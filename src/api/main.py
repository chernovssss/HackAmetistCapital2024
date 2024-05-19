from turtle import pd
from fastapi import APIRouter, FastAPI, File, HTTPException, UploadFile
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
search_service = SearchService(model=clsf_model)


@app.get("/")
async def root():
    return HTMLResponse(content=app_config.MOTD, status_code=200)


@app.get("/healthcheck")
async def healthcheck():
    return HTMLResponse(content=app_config.MOTD, status_code=200)


search_router = APIRouter()


@search_router.post("/search_one")
def search_one(product_name: str):
    return JSONResponse(content=f"{search_service(product_name)}")


@search_router.post("/search_many")
def search_many(products_list: UploadFile = File(...), column_name: str = "name"):
    if products_list.content_type not in [
        "application/json",
        "text/csv",
    ]:  # TODO: add more types
        return HTTPException(status_code=415, detail="Unsupported Media Type")
    return JSONResponse(content="")


app.include_router(search_router, prefix="/search", tags=["search"])
