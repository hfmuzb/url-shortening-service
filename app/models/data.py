import uuid

from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID, DATE

from models.base_model import Base


class Data(Base):
    __tablename__ = 'data'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    original_url = Column(String)
    shortened_url = Column(String)
    created_at = Column(DATE)
    valid_days = Column(Integer)
