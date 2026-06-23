export interface CariKart {
  id: number;
  cari_kodu: string;
  unvan1: string;
  unvan2?: string;
  yurt_ici_dis?: string;
  cari_turu?: string;
  sahis_tuzel?: string;
  tc_no_vergi_no?: string;
  vergi_dairesi?: string;
  il?: string;
  ilce?: string;
  mahalle?: string;
  cadde?: string;
  sokak?: string;
  kapino?: string;
  posta_kodu?: string;
  bolge?: string;
  ulke?: string;
  sorumlu_kisi?: string;
  cep_telefon?: string;
  email?: string;
  yetkili_kisi?: string;
  yetkili_telefon?: string;
  web_adresi?: string;
  bakiye: number;
  aciklama?: string;
}
