# Use a slimmer base image for production
FROM python:3.12-slim

# Set the working directory
WORKDIR /opt/urlshortener/backend

# Copy only the necessary files
COPY ./backend/requirements.txt /opt/urlshortener/backend/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r /opt/urlshortener/backend/requirements.txt

# Copy the rest of the application code
COPY ./backend/ /opt/urlshortener/backend

# Set the command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]