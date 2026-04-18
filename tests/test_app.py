"""Contract tests for the demo service."""

import unittest

from demo_service_api.main import build_response


class DemoServiceTests(unittest.TestCase):
    """Verify the demo service contract."""

    def test_health_returns_ok(self) -> None:
        """The golden-path service exposes a basic health endpoint."""
        status_code, payload = build_response("/health")

        self.assertEqual(status_code, 200)
        self.assertEqual(payload, {"service": "demo-service-api", "status": "ok"})

    def test_demo_endpoint_describes_standardized_pipeline(self) -> None:
        """The demo endpoint explains what the golden path standardizes."""
        status_code, payload = build_response("/demo")

        self.assertEqual(status_code, 200)
        self.assertEqual(
            payload,
            {
                "deploy_on_merge": True,
                "pipeline": [
                    "lint-hooks",
                    "sast",
                    "test-hooks",
                    "policy-management",
                    "build-hooks",
                ],
            },
        )
