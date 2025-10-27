# Use this base image with light weight Ubuntu OS
FROM python:3.11-slim

# Create app user early and dirs with correct perms
RUN useradd -m appuser
WORKDIR /app

# Install dependecies first from requirements.txt for better layer caching
COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy code and data to the base image
COPY src/ /app/src/
COPY data/ /app/data/

# Ensure data dir is writable by non-root user
RUN chown -R appuser:appuser /app
USER appuser

# Make sure imports from src/ work regardless of WORKDIR
ENV PYTHONPATH=/app/src

# Expose web port
EXPOSE 8000

# Stay in src so "main:app" resolves cleanly
WORKDIR /app/src

# Start the App
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
