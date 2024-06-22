# Stage 1: Build the Vue.js app
FROM node:22.3-alpine AS build

# Set the working directory
WORKDIR /opt/urlshortener/frontend

# Copy package.json and package-lock.json first for better caching
COPY ./frontend/package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY ./frontend/ .

# Build the application
RUN npm run build

# Stage 2: Serve the app with NGINX
FROM nginx:alpine

# Copy the built files from the previous stage
COPY --from=build /opt/urlshortener/frontend/dist /usr/share/nginx/html

# Copy custom NGINX configuration
COPY ./frontend/docker/prod/nginx.conf /etc/nginx/default.conf

# Expose port 80
EXPOSE 80

# Start NGINX
CMD ["nginx", "-g", "daemon off;"]
