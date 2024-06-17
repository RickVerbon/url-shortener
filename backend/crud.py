from sqlalchemy.orm import Session
from shortuuid import ShortUUID
from config import settings
from datetime import datetime
import models, schemas


def get_all_urls(db: Session) -> list[schemas.UrlInfo]:
    return db.query(models.Url).all()

def create_url(db: Session, url_create: schemas.UrlCreate) -> schemas.UrlResponse:
    short_url = ShortUUID().random(length=settings.url_length)
    created_at = datetime.utcnow()

    # Create database record
    db_url = models.Url(
        url=str(url_create.url),
        short_url=short_url,
        created_at=created_at
    )
    db.add(db_url)
    db.commit()
    db.refresh(db_url)

    return schemas.UrlResponse(
        base_url=settings.base_url,
        short_url=db_url.short_url,
    )


def get_url_by_short_url(db: Session, short_url: str) -> schemas.UrlInfo:
    return db.query(models.Url).filter(models.Url.short_url == short_url).first()