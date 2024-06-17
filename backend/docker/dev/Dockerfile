FROM python:3.12

WORKDIR /opt/urlshortener/backend

COPY ./backend/ /opt/urlshortener/backend

RUN pip install --no-cache-dir -r /opt/urlshortener/backend/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]