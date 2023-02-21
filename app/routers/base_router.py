from fastapi import APIRouter, Request, Response, HTTPException, Depends
from starlette.responses import RedirectResponse
from sqlalchemy.orm import Session

from service.url_handle import shorten_url_service, get_original_url_service
from schemas.base_schema import PostUrlShortenSchema
from errors import UrlNotFoundError, UrlExpiredError, InvalidUrlError, InvalidDaysError
from config import config
from dependencies import get_db

router = APIRouter()


@router.get("/")
def root():
    return {"msg": f"App is up and working. Please visit {config.ROOT_URL}/docs for more information. "}


@router.get("/{shortened_url}")
def redirect_request(shortened_url: str, response: Response, request: Request, db: Session = Depends(get_db)):
    try:
        res = get_original_url_service(shortened_url=shortened_url, db=db)
    except UrlNotFoundError as e:
        raise HTTPException(status_code=e.code, detail=e.message)
    except UrlExpiredError as e:
        raise HTTPException(status_code=e.code, detail=e.message)
    return RedirectResponse(url=res)


@router.post("/shorten_url")
def shorten_url(request: Request, response: Response, data: PostUrlShortenSchema, db: Session = Depends(get_db)):
    try:
        res = shorten_url_service(original_url=data.url, valid_days=data.valid_days, db=db)
        return {"url": res}
    except InvalidUrlError as e:
        raise HTTPException(status_code=e.code, detail=e.message)
    except InvalidDaysError as e:
        raise HTTPException(status_code=e.code, detail=e.message)
