"""Contract tests for the demo service."""

import unittest

from demo_service_api.main import create_app


class DemoServiceTests(unittest.TestCase):
    """Verify the demo service contract."""

    def test_root_returns_service_specific_hello_world(self) -> None:
        """The root endpoint returns a simple service-specific payload."""
        client = create_app().test_client()

        response = client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json(),
            {"message": "hello world from demo-service-api"},
        )

    def test_health_returns_ok(self) -> None:
        """The golden-path service exposes a basic health endpoint."""
        client = create_app().test_client()

        response = client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json(),
            {"service": "demo-service-api", "status": "ok"},
        )
