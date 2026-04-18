# demo-service-api

Golden-path showcase service. This repo consumes the shared workflow from the org
`.github` repo and deploys on merge to `main`.

## Local Commands

- Lint: `python -m compileall src tests`
- Run tests: `PYTHONPATH=src uv run python -m unittest discover -s tests -v`
- Start the API: `PYTHONPATH=src uv run python -m demo_service_api.main`
- Build the image: `docker build -t demo-service-api:dev .`
- Render shared chart: `helm template demo-service-api oci://ghcr.io/primetime-dev/charts/flask-service --version 0.1.0 -f deploy/values.yaml --set image.repository=ghcr.io/primetime-dev/demo-service-api --set image.tag=dev`

## Quick Start

Start the service directly:

```bash
uv sync --frozen
PYTHONPATH=src uv run --frozen python -m demo_service_api.main
```

In another terminal, verify it is serving traffic:

```bash
curl http://127.0.0.1:8080/
curl http://127.0.0.1:8080/healthz
curl http://127.0.0.1:8080/readyz
```

Build and run the container:

```bash
docker build -t demo-service-api:dev .
docker run --rm -p 8080:8080 demo-service-api:dev
```

Then verify the containerized service:

```bash
curl http://127.0.0.1:8080/
curl http://127.0.0.1:8080/healthz
curl http://127.0.0.1:8080/readyz
```

## Endpoints

- `GET /`
- `GET /healthz`
- `GET /readyz`

## CI/CD Story

- pull requests call the shared reusable API workflow for simple placeholder checks
- pushes to `main` build and push `ghcr.io` images tagged with the commit SHA
- deploy runs `helm upgrade --install` against the shared `flask-service` chart
- repo-owned settings live in `deploy/values.yaml`
- the app repo owns the image and values, while the shared chart owns the deployment shape
