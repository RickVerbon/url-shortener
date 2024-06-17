from pydantic import BaseModel, AnyUrl
from datetime import datetime


class UrlCreate(BaseModel):
    url: AnyUrl


class UrlResponse(BaseModel):
    base_url: str
    short_url: str

    class Config:
        from_attributes = True


class UrlInfo(BaseModel):
    id: int
    url: str
    short_url: str
    created_at: datetime

    class Config:
        from_attributes = True