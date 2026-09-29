from pathlib import Path

import pytest
from fastapi.testclient import TestClient

import app.main as main
from app.contract import MAX_BYTES, ProviderError

ROOT = Path(__file__).resolve().parent.parent
client = TestClient(main.app)
PNG = b"\x89PNG\r\n\x1a\n" + b"\0" * 64


def post(data, mime, name="x.png"):
    return client.post("/describe", files={"image": (name, data, mime)})


def test_ok_with_stub():
    r = post(PNG, "image/png")
    assert r.status_code == 200
    body = r.json()
    assert body["alt"].strip() and body["provider"] == "stub"


def test_wrong_type_is_415_even_with_png_name():
    r = post(b"hello", "text/plain", name="x.png")
    assert r.status_code == 415 and r.json() == {"error": "unsupported_type"}


def test_over_limit_is_413():
    r = post(b"\0" * (MAX_BYTES + 1), "image/png")
    assert r.status_code == 413 and r.json() == {"error": "too_large"}


def test_provider_error_is_502(monkeypatch):
    class Boom:
        name = "stub"
        def describe(self, data, mime):
            raise ProviderError("down")
    monkeypatch.setattr(main, "get_provider", lambda: Boom())
    r = post(PNG, "image/png")
    assert r.status_code == 502 and r.json() == {"error": "provider_failed"}


SAMPLES = sorted((ROOT / "samples").glob("*.*")) if (ROOT / "samples").is_dir() else []
MIME = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp", ".gif": "image/gif"}


@pytest.mark.skipif(not SAMPLES, reason="samples/ not there yet")
@pytest.mark.parametrize("path", SAMPLES, ids=lambda p: p.name)
def test_samples_end_to_end(path):
    mime = MIME.get(path.suffix.lower(), "application/octet-stream")
    r = post(path.read_bytes(), mime, name=path.name)
    if mime == "application/octet-stream":
        assert r.status_code == 415
    elif path.stat().st_size > MAX_BYTES:
        assert r.status_code == 413
    else:
        assert r.status_code == 200 and r.json()["alt"].strip()


@pytest.mark.skipif(not (ROOT / "web" / "index.html").exists(), reason="web/ not there yet")
def test_root_serves_the_page():
    r = client.get("/")
    assert r.status_code == 200 and "Seen" in r.text
