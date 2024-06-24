from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from schemas import UrlCreate, UrlResponse
from database import SessionLocal, engine
from config import settings
import crud, models
import os

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

origins = [
    os.getenv("URLSHORT_FRONTEND_URL"),
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/v1/")
async def create_url(url_create: UrlCreate, db: Session = Depends(get_db)) -> UrlResponse:
    return crud.create_url(db=db, url_create=url_create)


@app.get("/api/v1/{short_url}/")
async def get_url(short_url: str, db: Session = Depends(get_db)):
    url = crud.get_url_by_short_url(db, short_url)
    return url


if settings.environment == "development":
    @app.get("/api/v1/")
    async def get_all_urls(db: Session = Depends(get_db)):
        urls = crud.get_all_urls(db)
        return urls
