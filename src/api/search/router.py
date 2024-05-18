from fastapi import APIRouter, File, HTTPException, UploadFile
from fastapi.responses import JSONResponse

from api.exceptions import UnsupportedMediaTypeError

search_router = APIRouter()


@search_router.post("/search_one")
def search_one(product_name: str):
    pass


@search_router.post("/search_many")
def search_many(products_list: UploadFile = File(...)):
    if products_list.content_type not in [
        "application/json",
        "text/csv",
    ]:  # TODO: add more types
        return HTTPException(status_code=415, detail="Unsupported Media Type")
    return JSONResponse(content="haha")
