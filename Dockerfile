# syntax=docker/dockerfile:1
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8080

WORKDIR /app

# System deps for building psycopg2 and Pillow
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev gcc libjpeg62-turbo-dev zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app

# Collect static at build time (safe if settings configured)
RUN python manage.py collectstatic --noinput || true

EXPOSE 8080
CMD ["bash", "-lc", "gunicorn car_rental.wsgi:application --bind 0.0.0.0:${PORT} --workers ${WEB_CONCURRENCY:-2} --timeout 60"]


