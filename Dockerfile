FROM python:3.11-slim
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ ./src/
EXPOSE 8000
CMD ["python", "src/app.py"]

# Gunicorn entrypoint for production
#CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8000", "src.app:app"]
