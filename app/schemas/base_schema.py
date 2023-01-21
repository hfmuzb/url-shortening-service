from pydantic import BaseModel


class PostUrlShortenSchema(BaseModel):
    url: str
    valid_days: int
