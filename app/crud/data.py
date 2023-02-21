from typing import Union
from sqlalchemy.orm import Session

from models.data import Data


def url_is_unique(shortened_url: str, db: Session) -> bool:
    if db.query(Data).filter(Data.shortened_url == shortened_url).first():
        return False
    return True


def add_new_url(original_url, shortened_url, created_at, valid_days, db: Session) -> None:
    item = Data(
        original_url=original_url,
        shortened_url=shortened_url,
        created_at=created_at,
        valid_days=valid_days
    )
    db.add(item)
    db.commit()
    return


def get_original_url_item(shortened_url: str, db: Session) -> Union[Data, None]:
    return db.query(Data).filter(Data.shortened_url == shortened_url).first()
