# Use the official Nginx base image
FROM nginx:latest

# Copy Nginx configuration files
COPY ./conf/nginx /etc/nginx/conf.d

# Expose port 80 (default for HTTP)
EXPOSE 80

# Start Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
