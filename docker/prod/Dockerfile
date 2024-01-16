# Use an official Python runtime as a parent image
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app
WORKDIR /app

COPY . /app/
# Install any needed packages specified in requirements.txt (later add --no-cache-dir)
RUN pip install -r requirements.txt

# Collect static files
RUN python manage.py collectstatic --noinput

copy . /app/
# Make port 8000 available to the world outside this container
EXPOSE 8000

# Specify the full path to the gunicorn binary
CMD ["gunicorn", "urlshortener.wsgi:application", "--bind", "0.0.0.0:8000"]
