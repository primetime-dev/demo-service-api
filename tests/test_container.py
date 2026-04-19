"""Container image contract tests for the demo service."""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ContainerImageTests(unittest.TestCase):
    """Verify the image contract required by the shared Helm chart."""

    def test_dockerfile_declares_non_root_runtime_user(self) -> None:
        """The image must satisfy Kubernetes runAsNonRoot admission checks."""
        dockerfile = (ROOT / "Dockerfile").read_text(encoding="utf-8")

        user_match = re.search(r"^USER\s+([0-9]+)\s*$", dockerfile, re.MULTILINE)

        self.assertIsNotNone(user_match, "Dockerfile should declare a numeric USER")
        assert user_match is not None
        self.assertNotEqual(user_match.group(1), "0")

    def test_dockerfile_installs_dependencies_with_uv(self) -> None:
        """The image should use project metadata instead of duplicate pip pins."""
        dockerfile = (ROOT / "Dockerfile").read_text(encoding="utf-8")

        self.assertIn("COPY pyproject.toml uv.lock ./", dockerfile)
        self.assertIn("uv sync --no-dev --no-install-project", dockerfile)
        self.assertNotIn("pip install --no-cache-dir flask", dockerfile)


if __name__ == "__main__":
    unittest.main()
