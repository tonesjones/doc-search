"""Cache official topic bodies, then run the existing product scraper.

Use a new cache directory for each refresh. Reruns resume that same snapshot.
Conversion, manifest writes, and file paths remain owned by the product scraper.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import io
import json
from pathlib import Path
import runpy
import sys
import time
import urllib.request


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("corpus", type=Path)
    parser.add_argument("product")
    parser.add_argument("--cache", type=Path, required=True)
    parser.add_argument("--workers", type=int, default=4, choices=range(1, 9))
    parser.add_argument("--mode", choices=("pending", "changed", "both"), default="both")
    args = parser.parse_args()
    root = args.corpus.resolve()
    manifest_path = root / "sources" / args.product / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    cache = args.cache.resolve() / args.product
    cache.mkdir(parents=True, exist_ok=True)
    url_prefix = f"https://docs.blackduck.com/api/khub/maps/{manifest['mapId']}/topics/"
    topics = [t for t in manifest["topics"] if not t["id"].startswith("local-")]
    statuses = {"pending", "error"} if args.mode == "pending" else {"done"} if args.mode == "changed" else {"pending", "error", "done"}
    ids = sorted({t["id"] for t in topics if t["status"] in statuses})
    original_open = urllib.request.urlopen

    def download(content_id: str) -> None:
        destination = cache / (content_id + ".html")
        if destination.is_file():
            return
        for attempt in range(3):
            try:
                request = urllib.request.Request(url_prefix + content_id + "/content", headers={"Accept": "text/html"})
                with original_open(request, timeout=60) as response:
                    body = response.read()
                temporary = destination.with_suffix(".tmp")
                temporary.write_bytes(body)
                temporary.replace(destination)
                return
            except OSError:
                if attempt == 2:
                    raise
                time.sleep(2 * (attempt + 1))

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(download, content_id) for content_id in ids]
        for count, future in enumerate(as_completed(futures), 1):
            future.result()
            if count % 100 == 0 or count == len(ids):
                print(f"[{args.product}] cached {count}/{len(ids)} bodies", flush=True)

    def cached_open(request, *positional, **keywords):
        url = request.full_url if isinstance(request, urllib.request.Request) else request
        if url.startswith(url_prefix) and url.endswith("/content"):
            content_id = url[len(url_prefix):-len("/content")]
            return io.BytesIO((cache / (content_id + ".html")).read_bytes())
        return original_open(request, *positional, **keywords)

    urllib.request.urlopen = cached_open
    sys.path.insert(0, str(root / "scripts"))
    modes = ["--all-pending", "--retry-errors", "--refresh-changed"] if args.mode == "both" else ["--all-pending", "--retry-errors"] if args.mode == "pending" else ["--refresh-changed"]
    for mode in modes:
        sys.argv = [str(root / "scripts/scrape-pending.py"), "--product", args.product, mode, "--delay", "0"]
        try:
            runpy.run_path(sys.argv[0], run_name="__main__")
        except SystemExit as error:
            if error.code:
                return int(error.code)
    result = json.loads(manifest_path.read_text(encoding="utf-8"))
    failures = [t for t in result["topics"] if t["status"] in {"pending", "error"}]
    print(f"[{args.product}] remaining pending/errors: {len(failures)}", flush=True)
    return bool(failures)


if __name__ == "__main__":
    raise SystemExit(main())
