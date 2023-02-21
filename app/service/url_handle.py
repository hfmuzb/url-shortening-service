from typing import Optional
import datetime
import validators
from sqlalchemy.orm import Session

from functional.url_handle import generate_shortened_url
from crud.data import url_is_unique, add_new_url, get_original_url_item
from config import config
from errors import UrlExpiredError, UrlNotFoundError, InvalidUrlError, InvalidDaysError

DEFAULT_DAYS_VALID = config.DEFAULT_DAYS_VALID
ROOT_URL = config.ROOT_URL


def shorten_url_service(original_url: str, db: Session, valid_days: Optional[int] = None) -> str:
    if not validators.url(original_url):
        raise InvalidUrlError
    if valid_days is None:
        valid_days = DEFAULT_DAYS_VALID
    if valid_days < 1 or valid_days > 365:
        raise InvalidDaysError
    while True:
        shortened_url = generate_shortened_url()
        # check if generated short url is unique
        if url_is_unique(shortened_url, db=db):
            break
    # add db record
    add_new_url(original_url=original_url, shortened_url=shortened_url,
                created_at=datetime.date.today(), valid_days=valid_days, db=db)
    return f"{ROOT_URL}/{shortened_url}"


def get_original_url_service(shortened_url: str, db: Session) -> str:
    res = get_original_url_item(shortened_url=shortened_url, db=db)
    if not res:
        raise UrlNotFoundError
    days_passed = datetime.date.today() - res.created_at
    if days_passed.days > res.valid_days:
        raise UrlExpiredError
    return res.original_url
