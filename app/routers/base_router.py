from fastapi import APIRouter, Request

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
    return {"message": "OK"}
