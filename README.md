# VÉRTICE — Noema Professional Demo

A production-shaped demonstration of a premium plastic-surgery landing page governed by **Noema RC0**.

> **Fictional demo.** The physician, practice, credentials, metrics and financial assumptions shown here are invented for portfolio/testing purposes. Nothing on the site is medical advice or a real commercial offer.

## What this repo demonstrates

- A polished static GitHub Pages deliverable.
- Noema progressive context with a deliberately small agent entrypoint.
- Clear ownership / non-ownership boundaries for a sensitive medical-domain project.
- A demo business plan and editable funnel economics model.
- Privacy-by-default behavior: no tracking, cookies, storage or form transmission.
- Deterministic static checks plus Noema conformance in GitHub Actions.
- A public case-study page explaining the process without exposing unnecessary internal context.

## Public surfaces

- `site/index.html` — patient-facing landing concept.
- `site/business-plan.html` — demo growth/business plan + editable economics calculator.
- `site/noema.html` — public case study of the Noema process.

## Agent start

Read **`AGENTS.md` first**, then `noema.project.yaml`, then only the context required by the task mode. Do not bulk-read the repository.

## Local preview

```bash
python -m http.server 8000 --directory site
```

Then open `http://localhost:8000`.

## Validation

```bash
python tests/test_static.py
```

Remote CI additionally runs Noema's pinned reusable conformance workflow.
