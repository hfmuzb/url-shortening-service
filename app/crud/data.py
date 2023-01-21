from typing import Union

from crud.db_setup import SessionLocal
from models.data import Data


def url_is_unique(shortened_url: str) -> bool:
    with SessionLocal() as session:
        item = session.query(Data).filter(Data.shortened_url == shortened_url).first()
    if item:
        return False
    return True


def add_new_url(original_url, shortened_url, created_at, valid_days) -> None:
    with SessionLocal() as session:
        item = Data(
            original_url=original_url,
            shortened_url=shortened_url,
            created_at=created_at,
            valid_days=valid_days
        )
        session.add(item)
        session.commit()
    return


def get_original_url_item(shortened_url: str) -> Union[Data, None]:
    with SessionLocal() as session:
        item = session.query(Data).filter(Data.shortened_url == shortened_url).first()
    return item
