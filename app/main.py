from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

from app.contract import ALLOWED_TYPES, MAX_BYTES, DescribeResult, ProviderError

load_dotenv()

try:
    from app.describe import get_provider
except ImportError:  # ponytail: inline stub until the describe vertical lands; delete then
    class _Stub:
        name = "stub"
        def describe(self, data: bytes, mime: str) -> str:
            return "A placeholder description from the offline stub."
    def get_provider():
        return _Stub()

app = FastAPI(title="Seen")


@app.post("/describe")
async def describe(image: UploadFile = File(...)):
    if image.content_type not in ALLOWED_TYPES:
        return JSONResponse({"error": "unsupported_type"}, status_code=415)
    data = await image.read(MAX_BYTES + 1)
    if len(data) > MAX_BYTES:
        return JSONResponse({"error": "too_large"}, status_code=413)
    provider = get_provider()
    try:
        alt = provider.describe(data, image.content_type)
    except ProviderError:
        return JSONResponse({"error": "provider_failed"}, status_code=502)
    return DescribeResult(alt=alt, provider=provider.name).__dict__


WEB = Path(__file__).resolve().parent.parent / "web"
app.mount("/", StaticFiles(directory=WEB, html=True, check_dir=False), name="web")
