# Portainer'da CariHesap Stack Deploy Rehberi

Bu dokümantasyon, CariHesap uygulamasını Portainer kullanarak Docker stack olarak deploy etmek için adım adım talimatlar sağlar.

## Ön Gereksinimler

- **Portainer CE** veya **Portainer BE** kurulu ve çalışır durumda
- Portainer'ın erişimi olan **Docker Daemon** veya **Kubernetes**
- Git reprosunuz Portainer sunucusundan erişilebilir (veya docker-compose.yml el ile kopyalanacak)

## Adım 1: Portainer Admin Panel'e Erişim

1. Portainer admin panel'e (örn: `http://<portainer-sunucu>:9000`) tarayıcıdan erişin
2. Admin kullanıcı adı/şifre ile giriş yapın

## Adım 2: Stack Oluşturma (3 Seçenek)

### Seçenek A: Web Editor'den (En Basit)

1. **Stacks** → **+ Add Stack**
2. **Stack Name** alanına `carihesap` yazın
3. **Build method** olarak **Web editor** seçin
4. Aşağıdaki `docker-compose.yml` içeriğini yapıştırın:

```yaml
version: '3.8'

services:
  backend:
    image: carihesap-backend:latest
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: carihesap-backend
    ports:
      - "8000:8000"
    environment:
      - PYTHONUNBUFFERED=1
      - PYTHONPATH=/app
    volumes:
      - backend_data:/app
      - db_volume:/app/data
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000
    networks:
      - carihesap-network
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/"]
      interval: 10s
      timeout: 5s
      retries: 5
    restart: unless-stopped

  frontend:
    image: carihesap-frontend:latest
    build:
      context: ./frontend
      dockerfile: Dockerfile
    container_name: carihesap-frontend
    ports:
      - "4200:80"
    networks:
      - carihesap-network
    depends_on:
      - backend
    restart: unless-stopped

networks:
  carihesap-network:
    driver: bridge

volumes:
  backend_data:
    driver: local
  db_volume:
    driver: local
```

5. **Advanced mode** (isteğe bağlı):
   - Git başında repo URL'si belirtebilirsiniz (Portainer Github entegrasyonu yapılmışsa)
   - Veya dosyayı başında Upload seçeneğinden yükleyebilirsiniz

6. **Deploy the stack** düğmesine basın

### Seçenek B: Git Repository'den

1. **Stacks** → **+ Add Stack**
2. **Stack Name** alanına `carihesap` yazın
3. **Build method** olarak **Git repository** seçin
4. **Repository URL** alanına projenizin Git URL'sini yazın (örn: `https://github.com/username/carihesap.git`)
5. **Compose path** alanına `docker-compose.yml` yazın
6. **Deploy the stack** düğmesine basın

### Seçenek C: File Upload'tan

1. **Stacks** → **+ Add Stack**
2. **Stack Name** alanına `carihesap` yazın
3. **Build method** olarak **Upload** seçin
4. `docker-compose.yml` dosyasını seçin
5. **Deploy the stack** düğmesine basın

## Adım 3: Stack Durumunu Kontrol Etme

1. **Stacks** listesine gidin
2. `carihesap` stack'ini bulun ve tıklayın
3. **Containers** sekmesinde iki container'ın da çalışıp çalışmadığını kontrol edin:
   - `carihesap-backend` (üzerindeki yeşil gösterge)
   - `carihesap-frontend` (üzerindeki yeşil gösterge)

### Container Loglarını Görüntüleme

1. Stack adı → **Containers** sekmesi
2. Container adına tıklayın (örn: `carihesap-backend`)
3. **Logs** sekmesine gidin
4. Hata oluşmuşsa burada görülecektir

## Adım 4: Uygulamaya Erişim

- **Frontend**: `http://<portainer-sunucu-ip>:4200`
- **Backend API**: `http://<portainer-sunucu-ip>:8000`
- **API Docs (Swagger)**: `http://<portainer-sunucu-ip>:8000/docs`

## Adım 5: Port Yönlendirmesi (Opsiyonel - Reverse Proxy)

Eğer Portainer sunucusu ağ içinde yer alıyorsa ve dış erişim için proxy ayarlanacaksa:

### Nginx Reverse Proxy Örneği

```nginx
upstream carihesap_api {
    server <portainer-sunucu-ip>:8000;
}

upstream carihesap_web {
    server <portainer-sunucu-ip>:4200;
}

server {
    listen 80;
    server_name carihesap.example.com;

    # Frontend
    location / {
        proxy_pass http://carihesap_web;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    # Backend API
    location /api/ {
        rewrite ^/api/(.*)$ /$1 break;
        proxy_pass http://carihesap_api;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## Sorun Giderme

### Konteyner başlamıyor
1. Container loglarını kontrol edin (`Logs` sekmesi)
2. Yaygın sebepler:
   - **Backend**: "ModuleNotFoundError: No module named 'app'" → `PYTHONPATH=/app` environment değişkeninin ayarlanmadığı anlamına gelir
   - **Frontend**: Build hatası → `node_modules` kurulumu başarısız olmuş olabilir

### Backend "app" modülü bulunamadı hatası
Portainer'da backend servisi için:
1. Stack adı → **Services** → `carihesap-backend`
2. **Environment** sekmesinde `PYTHONPATH` değişkeninin `/app` olarak ayarlandığından emin olun
3. Gerekirse stack'i redeploy edin

### Frontend beyaz sayfa gösteriyor
1. Tarayıcı konsolu (`F12` → `Console`) hata olup olmadığını kontrol edin
2. Backend API'nin çalışıp çalışmadığını kontrol edin (http://localhost:8000/docs)
3. Frontend build hatası varsa container loglarını kontrol edin

### Containerlar başlıyor ama API yanıt vermiyor
1. Health check başarısız olmuş olabilir
2. Backend container loglarında hata varsa kontrol edin
3. Port yönlendirmesinin doğru olduğundan emin olun (8000:8000 vs)

## Stack Güncelleme

Kod değişiklikleri yapmak ve uygulamayı güncellemek için:

1. Git repo'ya push yapın (veya local kod düzenlediyseniz)
2. Portainer'da Stack adı → **Edit**
3. **Redeploy** düğmesine basın

Portainer yeni image'ları build edecek ve containerları yeniden başlatacaktır.

## Stack Silme

Ortamı temizlemek için:

1. **Stacks** listesine gidin
2. `carihesap` stack'inin sağında **Delete** düğmesine basın
3. Onay verin

Tüm containerlar ve volume'ler silinecektir.

## İleri Seviye: Environment Değişkenleri Ayarlamak

Bazı ortamlar için farklı ayarlar (örn: production database URL'si) gerekebilirse:

1. Stack adı → **Editor** (veya Web editor'den tekrar açın)
2. `environment:` bölümüne değişkenler ekleyin:

```yaml
environment:
  - PYTHONUNBUFFERED=1
  - PYTHONPATH=/app
  - DATABASE_URL=postgresql://user:pass@db:5432/carihesap
```

3. **Redeploy** yapın

## Backup ve Restore

### Veritabanı Backup'ı (SQLite)

```bash
# Portainer sunucusuna SSH ile bağlan ve database'i download et
docker exec carihesap-backend cp /app/cari.db /tmp/cari.db
docker cp carihesap-backend:/tmp/cari.db ./cari.db.backup
```

### Restore

```bash
docker cp ./cari.db.backup carihesap-backend:/app/cari.db
docker exec carihesap-backend chown 1000:1000 /app/cari.db
```

## Monitoring (Portainer Dashboards)

1. **Dashboard** bölümünden stack kaynak kullanımını görebilirsiniz
2. Her container'ın CPU, Memory gibi metrikleri izlenebilir
3. Long-term monitoring için Prometheus entegrasyonu eklenebilir

---

**Not:** Produksiyonda, `--reload` flag'ı asla kullanılmamalıdır. `docker-compose.yml`'de `--reload` kaldırıldığından emin olun.
