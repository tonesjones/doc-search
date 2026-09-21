from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path

from scripts.product_registry import (
    RegistryError,
    load_registry,
    resolve_products,
    validate_registry,
)


ROOT = Path(__file__).resolve().parents[1]


class ProductRegistryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.products = load_registry(ROOT)

    def test_real_registry_has_exactly_seven_products(self) -> None:
        self.assertEqual(
            [product.id for product in self.products],
            ["black-duck-sca", "bridge", "coverity", "polaris", "sigma", "signal", "srm"],
        )

    def test_aliases_resolve_to_canonical_products(self) -> None:
        resolved = resolve_products(["sca", "cov", "software-risk-manager"], self.products)
        self.assertEqual([product.id for product in resolved], ["black-duck-sca", "coverity", "srm"])

    def test_resolution_preserves_order_and_deduplicates(self) -> None:
        resolved = resolve_products(["polaris", "bridge-cli", "polaris", "bridge"], self.products)
        self.assertEqual([product.id for product in resolved], ["polaris", "bridge"])

    def test_unknown_product_names_fail(self) -> None:
        with self.assertRaisesRegex(RegistryError, "Unknown product or alias"):
            resolve_products(["unknown"], self.products)

    def test_duplicate_aliases_fail(self) -> None:
        duplicate = replace(self.products[1], aliases=("sca",))
        products = (self.products[0], duplicate, *self.products[2:])
        with self.assertRaisesRegex(RegistryError, "Duplicate product alias"):
            validate_registry(products, ROOT)

    def test_duplicate_product_ids_fail(self) -> None:
        duplicate = replace(self.products[1], id=self.products[0].id)
        products = (self.products[0], duplicate, *self.products[2:])
        with self.assertRaises(RegistryError):
            validate_registry(products, ROOT)

    def test_missing_root_fails(self) -> None:
        missing = replace(self.products[0], root="does-not-exist")
        products = (missing, *self.products[1:])
        with self.assertRaisesRegex(RegistryError, "Product root does not exist"):
            validate_registry(products, ROOT)

    def test_traversal_paths_fail(self) -> None:
        traversal = replace(self.products[0], skill="../outside/SKILL.md")
        products = (traversal, *self.products[1:])
        with self.assertRaisesRegex(RegistryError, "escapes the repository"):
            validate_registry(products, ROOT)

    def test_fixture_registry_can_validate_without_future_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repo_root = Path(directory)
            for product in self.products:
                (repo_root / product.root).mkdir(parents=True, exist_ok=True)
            validate_registry(self.products, repo_root)

    def test_registry_schema_is_dependency_free_and_strict(self) -> None:
        schema = json.loads((ROOT / "verification-report.schema.json").read_text(encoding="utf-8"))
        self.assertEqual(schema["required"], ["product", "version", "checks", "evidence", "failures", "status"])
        self.assertFalse(schema["additionalProperties"])
        self.assertFalse(schema["$defs"]["check"]["additionalProperties"])

    def test_validation_cli_prints_success_line(self) -> None:
        result = subprocess.run(
            [sys.executable, "scripts/check_product_registry.py"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), "Product registry valid with 7 products")


if __name__ == "__main__":
    unittest.main()
