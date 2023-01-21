from fastapi import APIRouter, Request, Response, HTTPException
from starlette.responses import RedirectResponse

from service.url_handle import shorten_url_service, get_original_url_service
from schemas.base_schema import PostUrlShortenSchema
from errors import UrlNotFoundError, UrlExpiredError, InvalidUrlError

router = APIRouter()


@router.get("/{shortened_url}")
def redirect_request(shortened_url: str, response: Response, request: Request):
    try:
        res = get_original_url_service(shortened_url=shortened_url)
    except UrlNotFoundError as e:
        raise HTTPException(status_code=e.code, detail=e.message)
    except UrlExpiredError as e:
        raise HTTPException(status_code=e.code, detail=e.message)
    return RedirectResponse(url=res)


@router.post("/shorten_url")
def shorten_url(request: Request, response: Response, data: PostUrlShortenSchema):
    try:
        res = shorten_url_service(original_url=data.url, valid_days=data.valid_days)
        return {"url": res}
    except InvalidUrlError as e:
        raise HTTPException(status_code=e.code, detail=e.message)
