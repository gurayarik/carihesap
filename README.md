# CariHesap - Cari Kart Yönetim Sistemi

Angular 18 frontend ve FastAPI backend kullanan cari hesap yönetim uygulaması.

## Teknolojiler

- **Frontend**: Angular 18, TypeScript, RxJS
- **Backend**: FastAPI, SQLAlchemy, SQLite
- **Container**: Docker, Docker Compose

## Proje Yapısı

```
carihesap/
├── frontend/          # Angular uygulaması
│   ├── src/
│   ├── package.json
│   ├── tsconfig.json
│   ├── angular.json
│   └── Dockerfile
├── backend/           # FastAPI uygulaması
│   ├── app/
│   ├── requirements.txt
│   └── Dockerfile
├── docker-compose.yml
└── .env.example
```

## Kurulum

### Ön Gereksinimler

- Docker
- Docker Compose
- (Ya da) Node.js 20+ ve Python 3.11+

### 1. Çevresel Değişkenler

```bash
cp .env.example .env
```

### 2. Docker Compose ile Çalıştırma

#### Geliştirme Ortamında
```bash
docker-compose up -d
```

#### Portainer Stack Olarak
Detaylı adım adım rehber için bkz: [PORTAINER_DEPLOYMENT.md](PORTAINER_DEPLOYMENT.md)

Özet:
1. Portainer'da "Stacks" → "Add Stack"
2. "Web editor" seç
3. `docker-compose.prod.yml` veya `docker-compose.yml` içeriğini yapıştır
4. "Deploy the stack" bas

### 3. Uygulamaya Erişim

- **Frontend**: http://localhost:4200
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## Durdurma

```bash
docker-compose down
```

## Docker Compose Yapılandırmaları

### Production (`docker-compose.yml`)
- Nginx ile optimized frontend serving
- Health checks ile otomatik restart
- Volume-based database persistence
- Resource limits

### Development (`docker-compose.dev.yml`)
- `ng serve` ile hot-reload frontend
- `uvicorn --reload` ile hot-reload backend
- Source code mount'ları ile anlık değişiklik izleme

Dev ortamında çalıştırmak için:
```bash
docker-compose -f docker-compose.dev.yml up --build
```

### Production Optimized (`docker-compose.prod.yml`)
Portainer veya prod sunucuları için önerilen yapılandırma. Ayrıntılar için: [PORTAINER_DEPLOYMENT.md](PORTAINER_DEPLOYMENT.md)

## Geliştirme

### Local'de Çalıştırma (Docker olmadan)

#### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

#### Frontend

```bash
cd frontend
npm install
ng serve --open
```

## API Endpoints

- `GET /cari-kartlar` - Tüm cari kartları listele
- `POST /cari-kartlar` - Yeni cari kart oluştur
- `GET /cari-kartlar/{id}` - Belirli cari kartı getir
- `PATCH /cari-kartlar/{id}` - Cari kartı güncelle
- `DELETE /cari-kartlar/{id}` - Cari kartı sil

## Veritabanı

SQLite veritabanı `backend/cari.db` dosyasında saklanır. Docker Compose kullanırken volume ile kalıcıdır.

## Sorun Giderme

### "Port already in use" hatası
```bash
# Farklı portları kullan
docker-compose down
docker-compose up -d --build
```

### CORS hatası
Backend `CORS` middleware'i Angular adresi için yapılandırılmıştır.

### Database lock hatası
```bash
# SQLite database'i temizle
rm backend/cari.db
docker-compose restart backend
```

## Lisans

MIT
