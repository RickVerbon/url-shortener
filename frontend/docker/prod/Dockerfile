# Stage 1: Build the Vue.js app
FROM node:22.3-alpine as build

WORKDIR /opt/urlshortener/frontend

COPY ./frontend/ .

RUN npm install
RUN npm run build

# Stage 2: Serve the app with NGINX
FROM nginx:alpine

# Copy the built files from the previous stage
COPY --from=build /opt/urlshortener/frontend/dist /usr/share/nginx/html

# Copy custom NGINX configuration
COPY ./frontend/nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]