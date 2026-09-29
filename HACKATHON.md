# Flash Hackathon: AI Web Integrations

We're building **Seen**, in the Accessibility Enhancers track: a web page where you drop an image and
get the alt text a screen reader should announce, shown and read aloud, from one `POST /describe`
endpoint backed by Claude Haiku 4.5 vision (with an offline stub).

Official rules: the event brief handed out at kickoff (no public link). In short: build and demo a
working AI capability embedded in a web environment, using existing APIs. Deliverables are a live
prototype or an interactive hi-fi mockup, plus a 60-second pitch covering the problem and the tech
stack. There is no submission form: the live demo at the table is the submission.

Smoke: `uv run pytest -q`

The product that ships is `main`: the last commit that passed the smoke check.

Board: https://github.com/users/atiladeokegab/projects/6

## Deadlines

Your agent checks these every session against the UTC column. GitHub milestones keep only the
date, so this UTC column is the clock, never the milestone.

| Deadline | Event time | UTC |
|---|---|---|
| build start | 2026-09-29T15:35+01:00 | 2026-09-29T14:35Z |
| core | 2026-09-29T15:45+01:00 | 2026-09-29T14:45Z |
| code freeze | 2026-09-29T16:45+01:00 | 2026-09-29T15:45Z |
| submit | 2026-09-29T16:55+01:00 | 2026-09-29T15:55Z |

## Judging criteria

- The brief publishes none. We aim at three: the AI feature really works, the user value is obvious, and the 60-second pitch is clear.

## Team

| Name | GitHub | Role |
|---|---|---|
| Atilade | @atiladeokegab | Lead and designer: core, describe, pitch, submission |
| Matrix | @Atilmatrix | web: the Seen page |

The lead's agents: Zeus plans, reviews, merges and builds the lead's areas. When this page
or a review says "the lead", it may be Zeus acting for the lead.
