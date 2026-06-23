from sqlalchemy import Column, Float, Integer, String, Text
from .database import Base


class CariKart(Base):
    __tablename__ = "cari_kartlar"

    id = Column(Integer, primary_key=True, index=True)
    cari_kodu = Column(String(40), nullable=False, unique=True, index=True)
    unvan1 = Column(String(180), nullable=False, index=True)
    unvan2 = Column(String(180), nullable=True)
    yurt_ici_dis = Column(String(20), default="YURT İÇİ")
    cari_turu = Column(String(30), default="TOPTAN")
    sahis_tuzel = Column(String(20), default="TÜZEL")
    tc_no_vergi_no = Column(String(50), nullable=True)
    vergi_dairesi = Column(String(80), nullable=True)
    il = Column(String(60), nullable=True)
    ilce = Column(String(60), nullable=True)
    mahalle = Column(String(80), nullable=True)
    cadde = Column(String(120), nullable=True)
    sokak = Column(String(120), nullable=True)
    kapino = Column(String(40), nullable=True)
    posta_kodu = Column(String(20), nullable=True)
    bolge = Column(String(60), nullable=True)
    ulke = Column(String(60), nullable=True)
    sorumlu_kisi = Column(String(120), nullable=True)
    cep_telefon = Column(String(40), nullable=True)
    email = Column(String(120), nullable=True)
    yetkili_kisi = Column(String(120), nullable=True)
    yetkili_telefon = Column(String(40), nullable=True)
    web_adresi = Column(String(160), nullable=True)
    bakiye = Column(Float, default=0.0, nullable=False)
    aciklama = Column(Text, default="")
