from sqlalchemy.orm import Session
from . import models, schemas


def get_cari_kart(db: Session, kart_id: int):
    return db.query(models.CariKart).filter(models.CariKart.id == kart_id).first()


def get_cari_kartlar(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.CariKart).offset(skip).limit(limit).all()


def create_cari_kart(db: Session, kart: schemas.CariKartCreate):
    db_kart = models.CariKart(**kart.dict())
    db.add(db_kart)
    db.commit()
    db.refresh(db_kart)
    return db_kart


def update_cari_kart(db: Session, kart_id: int, kart: schemas.CariKartUpdate):
    db_kart = get_cari_kart(db, kart_id)
    if not db_kart:
        return None
    for field, value in kart.dict(exclude_unset=True).items():
        setattr(db_kart, field, value)
    db.commit()
    db.refresh(db_kart)
    return db_kart


def delete_cari_kart(db: Session, kart_id: int):
    db_kart = get_cari_kart(db, kart_id)
    if not db_kart:
        return None
    db.delete(db_kart)
    db.commit()
    return db_kart
