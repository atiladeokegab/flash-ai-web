from dataclasses import dataclass

ALLOWED_TYPES = {"image/png", "image/jpeg", "image/webp", "image/gif"}
MAX_BYTES = 5 * 1024 * 1024


@dataclass
class DescribeResult:
    alt: str
    provider: str


class ProviderError(Exception):
    """A provider could not describe the image."""
