from sqlalchemy.orm import Session

import crud
import schemas
from database import SessionLocal
from fastapi import APIRouter
from fastapi import Depends, HTTPException
from fastapi_pagination import Page, paginate


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/api/shows/", response_model=Page[schemas.Show])
def read_shows(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    shows = crud.get_shows(db, skip=skip, limit=limit)
    return paginate(shows)


@router.get("/api/shows/{show_id}", response_model=schemas.Show)
def read_show(show_id: int, db: Session = Depends(get_db)):
    show = crud.get_show(db, show_id=show_id)
    if show is None:
        raise HTTPException(status_code=404, detail="Show not found")
    return show
