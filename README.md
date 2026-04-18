# demo-service-api

Golden-path showcase service. This repo consumes the shared workflow from the org
`.github` repo and deploys on merge to `main`.

## Local Commands

- Lint: `python -m compileall src tests`
- Run tests: `PYTHONPATH=src uv run python -m unittest discover -s tests -v`
- Start the API: `PYTHONPATH=src uv run python -m demo_service_api.main`
- Build the image: `docker build -t demo-service-api:dev .`
- Apply manifests: `kubectl apply -f k8s/`

## Quick Start

Start the service directly:

```bash
uv sync --frozen
PYTHONPATH=src uv run --frozen python -m demo_service_api.main
```

In another terminal, verify it is serving traffic:

```bash
curl http://127.0.0.1:8000/
curl http://127.0.0.1:8000/health
```

Build and run the container:

```bash
docker build -t demo-service-api:dev .
docker run --rm -p 8000:8000 demo-service-api:dev
```

Then verify the containerized service:

```bash
curl http://127.0.0.1:8000/
curl http://127.0.0.1:8000/health
```

## Endpoints

- `GET /`
- `GET /health`

## CI/CD Story

- pull requests call the shared reusable API workflow for simple placeholder checks
- pushes to `main` build and push `ghcr.io` images tagged with the commit SHA
- deploy runs `kubectl apply -f k8s/` and then updates the running Deployment image with
  `kubectl set image`
