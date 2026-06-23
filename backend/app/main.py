from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Cari Kart API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200", "http://127.0.0.1:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/cari-kartlar", response_model=schemas.CariKart, status_code=201)
def create_cari_kart(kart: schemas.CariKartCreate, db: Session = Depends(get_db)):
    return crud.create_cari_kart(db=db, kart=kart)


@app.get("/cari-kartlar", response_model=list[schemas.CariKart])
def read_cari_kartlar(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_cari_kartlar(db, skip=skip, limit=limit)


@app.get("/cari-kartlar/{kart_id}", response_model=schemas.CariKart)
def read_cari_kart(kart_id: int, db: Session = Depends(get_db)):
    db_kart = crud.get_cari_kart(db, kart_id=kart_id)
    if db_kart is None:
        raise HTTPException(status_code=404, detail="Cari kart bulunamadı")
    return db_kart


@app.patch("/cari-kartlar/{kart_id}", response_model=schemas.CariKart)
def update_cari_kart(kart_id: int, kart: schemas.CariKartUpdate, db: Session = Depends(get_db)):
    db_kart = crud.update_cari_kart(db, kart_id=kart_id, kart=kart)
    if db_kart is None:
        raise HTTPException(status_code=404, detail="Cari kart bulunamadı")
    return db_kart


@app.delete("/cari-kartlar/{kart_id}", response_model=schemas.CariKart)
def delete_cari_kart(kart_id: int, db: Session = Depends(get_db)):
    db_kart = crud.delete_cari_kart(db, kart_id=kart_id)
    if db_kart is None:
        raise HTTPException(status_code=404, detail="Cari kart bulunamadı")
    return db_kart
