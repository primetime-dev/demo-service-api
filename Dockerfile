FROM python:3.13-slim

WORKDIR /app
COPY src ./src
ENV PYTHONPATH=/app/src

EXPOSE 8000

CMD ["python", "-m", "demo_service_api.main"]
