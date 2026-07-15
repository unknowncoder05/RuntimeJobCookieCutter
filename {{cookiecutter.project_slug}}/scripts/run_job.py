"""Call one API endpoint and append the response as JSON Lines."""
from __future__ import annotations

import json
import os
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


DEFAULT_API_URL = "{{ cookiecutter.api_url }}"
DEFAULT_OUTPUT_PATH = "{{ cookiecutter.output_path }}"


def fetch_json(api_url: str) -> dict:
    request = urllib.request.Request(api_url, headers={"User-Agent": "{{ cookiecutter.project_slug_dashed }}/0.1"})
    with urllib.request.urlopen(request, timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))


def build_record(payload: dict) -> dict:
    return {
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "source": os.environ.get("JOB_API_URL", DEFAULT_API_URL),
        "payload": payload,
    }


def append_jsonl(record: dict, output_path: str) -> None:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, sort_keys=True) + "\n")


def main() -> None:
    api_url = os.environ.get("JOB_API_URL", DEFAULT_API_URL)
    output_path = os.environ.get("JOB_OUTPUT_PATH", DEFAULT_OUTPUT_PATH)
    payload = fetch_json(api_url)
    record = build_record(payload)
    append_jsonl(record, output_path)
    print(json.dumps(record, sort_keys=True))


if __name__ == "__main__":
    main()
