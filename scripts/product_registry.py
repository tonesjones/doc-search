from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping, Sequence


REGISTRY_FILE = "products.json"
EXPECTED_PRODUCT_IDS = frozenset(
    {"black-duck-sca", "bridge", "coverity", "polaris", "sigma", "signal", "srm"}
)
REQUIRED_FIELDS = ("id", "name", "root", "skill", "verifier", "versions", "aliases")


class RegistryError(ValueError):
    """Raised when the root registry cannot safely describe the repository."""


@dataclass(frozen=True)
class ProductSpec:
    """The root router's product-level contract."""

    id: str
    name: str
    root: str
    skill: str
    verifier: str
    versions: tuple[str, ...]
    aliases: tuple[str, ...]

    @classmethod
    def from_mapping(cls, value: Mapping[str, object]) -> "ProductSpec":
        missing = [field for field in REQUIRED_FIELDS if field not in value]
        if missing:
            raise RegistryError(f"Product entry is missing required fields: {', '.join(missing)}")

        def text_field(field: str) -> str:
            raw = value[field]
            if not isinstance(raw, str) or not raw.strip():
                raise RegistryError(f"Product field {field!r} must be a non-empty string")
            return raw.strip()

        def string_list(field: str) -> tuple[str, ...]:
            raw = value[field]
            if not isinstance(raw, list) or not raw:
                raise RegistryError(f"Product field {field!r} must be a non-empty list")
            items = tuple(item.strip() for item in raw if isinstance(item, str) and item.strip())
            if len(items) != len(raw):
                raise RegistryError(f"Product field {field!r} must contain only non-empty strings")
            if len({item.casefold() for item in items}) != len(items):
                raise RegistryError(f"Product field {field!r} contains duplicates")
            return items

        raw_aliases = value["aliases"]
        if not isinstance(raw_aliases, list):
            raise RegistryError("Product field 'aliases' must be a list")
        aliases = tuple(item.strip() for item in raw_aliases if isinstance(item, str) and item.strip())
        if len(aliases) != len(raw_aliases):
            raise RegistryError("Product field 'aliases' must contain only non-empty strings")
        if len({item.casefold() for item in aliases}) != len(aliases):
            raise RegistryError("Product field 'aliases' contains duplicates")

        return cls(
            id=text_field("id"),
            name=text_field("name"),
            root=text_field("root"),
            skill=text_field("skill"),
            verifier=text_field("verifier"),
            versions=string_list("versions"),
            aliases=aliases,
        )


def _repo_relative_path(repo_root: Path, raw_path: str, field: str) -> Path:
    candidate = Path(raw_path)
    if candidate.is_absolute() or ".." in candidate.parts:
        raise RegistryError(f"Product {field} path escapes the repository: {raw_path!r}")
    resolved_root = repo_root.resolve()
    resolved_path = (resolved_root / candidate).resolve()
    try:
        resolved_path.relative_to(resolved_root)
    except ValueError as exc:
        raise RegistryError(f"Product {field} path escapes the repository: {raw_path!r}") from exc
    return resolved_path


def validate_registry(products: Sequence[ProductSpec], repo_root: Path) -> None:
    """Validate product identity, paths, and physical product roots."""
    if frozenset(product.id for product in products) != EXPECTED_PRODUCT_IDS:
        actual = sorted(product.id for product in products)
        expected = sorted(EXPECTED_PRODUCT_IDS)
        raise RegistryError(f"Registry product ids are {actual!r}; expected {expected!r}")

    ids = {product.id.casefold() for product in products}
    if len(ids) != len(products):
        raise RegistryError("Duplicate product id")
    names: set[str] = set()
    aliases: dict[str, str] = {}
    for product in products:
        folded_id = product.id.casefold()
        folded_name = product.name.casefold()
        if folded_name in names:
            raise RegistryError(f"Duplicate product name: {product.name!r}")
        names.add(folded_name)

        root_path = _repo_relative_path(repo_root, product.root, "root")
        _repo_relative_path(repo_root, product.skill, "skill")
        _repo_relative_path(repo_root, product.verifier, "verifier")
        if not root_path.is_dir():
            raise RegistryError(f"Product root does not exist: {product.root!r}")

        for alias in product.aliases:
            folded_alias = alias.casefold()
            if folded_alias in ids:
                raise RegistryError(f"Alias collides with a product id: {alias!r}")
            previous = aliases.get(folded_alias)
            if previous is not None:
                raise RegistryError(f"Duplicate product alias: {alias!r} used by {previous!r} and {product.id!r}")
            aliases[folded_alias] = product.id


def load_registry(repo_root: Path) -> tuple[ProductSpec, ...]:
    """Load the root registry from a repository checkout."""
    path = repo_root / REGISTRY_FILE
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise RegistryError(f"Registry file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise RegistryError(f"Registry file is not valid JSON: {path}") from exc

    if not isinstance(payload, dict) or payload.get("schema_version") != 1:
        raise RegistryError("Registry schema_version must be 1")
    entries = payload.get("products")
    if not isinstance(entries, list):
        raise RegistryError("Registry products must be a list")
    try:
        products = tuple(ProductSpec.from_mapping(entry) for entry in entries)
    except (TypeError, AttributeError) as exc:
        raise RegistryError("Each registry product must be an object") from exc
    validate_registry(products, repo_root)
    return products


def resolve_products(names: Iterable[str], products: Sequence[ProductSpec]) -> tuple[ProductSpec, ...]:
    """Resolve product ids or aliases while preserving request order."""
    requests = tuple(name.strip() for name in names)
    if not requests or any(not name for name in requests):
        raise RegistryError("At least one non-empty product id or alias is required")

    lookup: dict[str, ProductSpec] = {}
    for product in products:
        lookup[product.id.casefold()] = product
        for alias in product.aliases:
            lookup[alias.casefold()] = product

    resolved: list[ProductSpec] = []
    seen: set[str] = set()
    for requested in requests:
        product = lookup.get(requested.casefold())
        if product is None:
            known = ", ".join(sorted(lookup))
            raise RegistryError(f"Unknown product or alias {requested!r}. Known values: {known}")
        if product.id not in seen:
            resolved.append(product)
            seen.add(product.id)
    return tuple(resolved)
