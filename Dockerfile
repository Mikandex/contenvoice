# Base image
FROM python:3.10-slim


# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app


# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . .

# Create directories for static and media
RUN mkdir -p /app/staticfiles /app/media

VOLUME ["/app/staticfiles", "/app/media"]

# Expose port
EXPOSE 8009

# Run migrations, collect static, and start with Gunicorn
#CMD sh -c "python manage.py run_huey & uvicorn Mtnservices.asgi:application --host 0.0.0.0 --port 8001 "
CMD sh -c "gunicorn contentvoice.wsgi:application --host 0.0.0.0 --port 8009"

