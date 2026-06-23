from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class CariKartBase(BaseModel):
    cari_kodu: str = Field(..., title="Cari Kodu", max_length=40)
    unvan1: str = Field(..., title="Ünvan (Soyadı)", max_length=180)
    unvan2: Optional[str] = Field(None, title="Ünvan (Adı)", max_length=180)
    yurt_ici_dis: Optional[str] = Field("YURT İÇİ", title="Yurt İçi / Yurt Dışı")
    cari_turu: Optional[str] = Field("TOPTAN", title="Cari Türü")
    sahis_tuzel: Optional[str] = Field("TÜZEL", title="Şahıs / Tüzel")
    tc_no_vergi_no: Optional[str] = Field(None, title="TC No / Vergi No")
    vergi_dairesi: Optional[str] = Field(None, title="Vergi Dairesi")
    il: Optional[str] = Field(None, title="İl")
    ilce: Optional[str] = Field(None, title="İlçe")
    mahalle: Optional[str] = Field(None, title="Mahalle")
    cadde: Optional[str] = Field(None, title="Cadde")
    sokak: Optional[str] = Field(None, title="Sokak")
    kapino: Optional[str] = Field(None, title="Kapı No")
    posta_kodu: Optional[str] = Field(None, title="Posta Kodu")
    bolge: Optional[str] = Field(None, title="Bölge")
    ulke: Optional[str] = Field(None, title="Ülke")
    sorumlu_kisi: Optional[str] = Field(None, title="Sorumlu Kişi")
    cep_telefon: Optional[str] = Field(None, title="Cep Telefonu")
    email: Optional[EmailStr] = Field(None, title="E-mail Adresi")
    yetkili_kisi: Optional[str] = Field(None, title="Yetkili Kişi")
    yetkili_telefon: Optional[str] = Field(None, title="Yetkili Cep Telefonu")
    web_adresi: Optional[str] = Field(None, title="Web Adresi")
    bakiye: float = Field(0.0, title="Cari Bakiye")
    aciklama: Optional[str] = Field("", title="Cari Açıklama")


class CariKartCreate(CariKartBase):
    pass


class CariKartUpdate(BaseModel):
    cari_kodu: Optional[str] = Field(None, max_length=40)
    unvan1: Optional[str] = Field(None, max_length=180)
    unvan2: Optional[str] = Field(None, max_length=180)
    yurt_ici_dis: Optional[str] = None
    cari_turu: Optional[str] = None
    sahis_tuzel: Optional[str] = None
    tc_no_vergi_no: Optional[str] = None
    vergi_dairesi: Optional[str] = None
    il: Optional[str] = None
    ilce: Optional[str] = None
    mahalle: Optional[str] = None
    cadde: Optional[str] = None
    sokak: Optional[str] = None
    kapino: Optional[str] = None
    posta_kodu: Optional[str] = None
    bolge: Optional[str] = None
    ulke: Optional[str] = None
    sorumlu_kisi: Optional[str] = None
    cep_telefon: Optional[str] = None
    email: Optional[EmailStr] = None
    yetkili_kisi: Optional[str] = None
    yetkili_telefon: Optional[str] = None
    web_adresi: Optional[str] = None
    bakiye: Optional[float] = None
    aciklama: Optional[str] = None


class CariKart(CariKartBase):
    id: int

    class Config:
        orm_mode = True
