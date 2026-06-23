# Multi-stage build: build Angular app with Node, then serve with nginx

# Builder
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --allow-root --legacy-peer-deps
COPY . .
RUN npm run build -- --configuration production

# Production image
FROM nginx:stable-alpine
COPY --from=builder /app/dist/carihesap-frontend /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
