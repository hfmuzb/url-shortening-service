from crud.db_setup import SessionLocal
from models.data import Data


def url_is_unique(shortened_url) -> bool:
    return True


def add_new_url(original_url, shortened_url, created_at, valid_days) -> None:
    return
