from fastapi import APIRouter, Request

from service.url_handle import shorten_url_service
from schemas.base_schema import PostUrlShortenSchema

router = APIRouter()


@router.get("/")
def welcome():
    return {"msg": "hello world!"}


@router.get("/{shortened_url}")
def redirect_request(shortened_url: str):
    return shortened_url


@router.post("/shorten_url")
def shorten_url(request: Request, data: PostUrlShortenSchema):
    res = shorten_url_service(original_url=data.url, valid_days=data.valid_days)
    return {"url": res}
