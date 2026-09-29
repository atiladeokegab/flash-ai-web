# The idea

The lead writes this once the team has agreed the idea, and no issue is created before it is
complete. If your task doesn't fit this page, open a change-request (AGENTS.md §7).

Grew from: Atilade's pitch ("a website with a cool UI that does something simple on the back end"), in the Accessibility Enhancers track.

## Problem

Screen readers announce an image by its alt text. Most images on the web have none, so a blind
user hears "image" or a file name. Writing good alt text by hand is slow, so it doesn't get done.

## The idea

**Seen** is a web page: drop an image on it and it shows the alt text a screen reader should
announce, with a button that reads it aloud. One API endpoint sends the image to a vision model
(Claude Haiku 4.5) and returns one or two sentences. Offline, a stub provider answers instead,
so the page always works.

## What we build

- A showpiece page in `web/`: drop zone, image preview, the alt text, Copy, and Read aloud (browser `speechSynthesis`)
- `POST /describe`: a multipart `image` (png, jpg, webp or gif, up to 5 MB) returns `{"alt": "...", "provider": "stub" | "claude"}`
- Providers chosen by `DESCRIBE_PROVIDER`: `stub` (default, offline) or `claude` (`ANTHROPIC_API_KEY` in `.env`)
- A few sample images for tests and the demo

## What we don't build

- A drop-in script for other websites, crawling or fixing live pages
- Accounts, history or storage: nothing is saved
- Image URLs as input (upload or drop only)
- Deployment: the demo runs on localhost from `main`

## The demo, in one line

Drop a photo of a product on the page, and within a couple of seconds Seen shows and speaks its alt text.

## Areas and owners

Each person owns their area's directories outright (AGENTS.md §6). The core is the shared
contracts; only the lead changes it.

| Area | Directories | Owner | Issues |
|---|---|---|---|
| core | `pyproject.toml`, `app/__init__.py`, `app/main.py`, `app/contract.py`, `tests/__init__.py`, `tests/test_api.py` | @atiladeokegab (Zeus builds) | — |
| describe | `app/describe/`, `tests/describe/` | @atiladeokegab (Zeus builds) | — |
| web | `web/` | @Atilmatrix | — |
| submission | `docs/pitch.md`, `docs/architecture/`, `README.md` | @atiladeokegab (Zeus builds the diagrams) | — |
| pool | `samples/`, `docs/demo.md` | pool | — |
