# Multi-stage build: build Angular app with Node, then serve with nginx

# Builder
FROM node:20-alpine AS builder
WORKDIR /app

# Install system dependencies - including bash for better shell compatibility
RUN apk add --no-cache bash git python3 make g++ curl

# Verify npm is available
RUN npm --version && npx --version

COPY package*.json ./
RUN npm install --legacy-peer-deps
COPY . .
RUN npx ng build --configuration production

# Production image
FROM nginx:stable-alpine
COPY --from=builder /app/dist/carihesap-frontend /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
