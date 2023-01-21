from typing import Union
from pydantic import BaseModel


class PostUrlShortenSchema(BaseModel):
    url: str
    valid_days: Union[int, None] = None
