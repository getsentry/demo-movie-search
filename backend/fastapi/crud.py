from sqlalchemy.orm import Session

import models


def get_show(db: Session, show_id: int):
    return db.query(models.Show).filter(models.Show.id == show_id).first()


def get_shows(db: Session, skip: int = 0, limit: int = 100, q: str = None):
    shows = db.query(models.Show)

    if q:
        shows = shows.filter(models.Show.title.ilike(f"%{q}%"))    
    
    return shows.offset(skip).limit(limit).all()
