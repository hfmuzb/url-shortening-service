from typing import Optional
import datetime

from functional.url_handle import generate_shortened_url
from crud.data import url_is_unique, add_new_url
from config import config

DEFAULT_DAYS_VALID = config.DEFAULT_DAYS_VALID
ROOT_URL = config.ROOT_URL


def shorten_url_service(original_url: str, valid_days: Optional[int] = None):
    if valid_days is None:
        valid_days = DEFAULT_DAYS_VALID
    while True:
        shortened_url = generate_shortened_url()
        # check if generated short url is unique
        if url_is_unique(shortened_url):
            break
    # add db record
    add_new_url(original_url=original_url, shortened_url=shortened_url,
                created_at=datetime.date.today(), valid_days=valid_days)
    return f"{ROOT_URL}/{shortened_url}"
