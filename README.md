# demo-service-api

Golden-path showcase service. This repo consumes the shared workflow from the org
`.github` repo and deploys on merge to `main`.

## Local Commands

- Lint: `python -m compileall src tests`
- Run tests: `PYTHONPATH=src uv run python -m unittest discover -s tests -v`
- Start the API: `PYTHONPATH=src uv run python -m demo_service_api.main`
- Build the image: `docker build -t demo-service-api:dev .`
- Apply manifests: `kubectl apply -f k8s/`

## Endpoints

- `GET /health`
- `GET /demo`

## CI/CD Story

- pull requests call the shared reusable API workflow for simple placeholder checks
- pushes to `main` build and push `ghcr.io` images tagged with the commit SHA
- deploy runs `kubectl apply -f k8s/` and then updates the running Deployment image with
  `kubectl set image`
