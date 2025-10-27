FROM python:3.11-slim

# Create app user early and dirs with correct perms
RUN useradd -m appuser
WORKDIR /app

# Install deps first for better layer caching
COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy code and data
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

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]