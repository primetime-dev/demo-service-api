FROM python:3.13-slim

WORKDIR /app
RUN pip install --no-cache-dir flask==3.1.1
COPY src ./src
ENV PYTHONPATH=/app/src

EXPOSE 8080

CMD ["flask", "--app", "demo_service_api.main:app", "run", "--host=0.0.0.0", "--port=8080"]
