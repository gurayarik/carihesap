FROM node:20-alpine

WORKDIR /app

# Paketleri yükle
COPY package*.json ./
RUN npm install --force

# Uygulama kodunu kopyala
COPY . .

EXPOSE 4200

CMD ["ng", "serve", "--host", "0.0.0.0", "--port", "4200", "--disable-host-check"]
