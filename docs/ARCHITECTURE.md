# Architecture

## Deployment
Static files in `site/` deploy to GitHub Pages through a dedicated Actions workflow.

## Runtime
There is no application backend. `site/app.js` provides only progressive UI behavior:
- mobile navigation;
- non-transmitting demo consultation confirmation;
- business-funnel calculator;
- case-study disclosure interactions.

## Data boundary
No persistent data stores exist. No browser storage APIs or network requests are permitted.

## Noema boundary
`noema.project.yaml` is the machine-readable project contract. `AGENTS.md` is the small human/agent entrypoint. Context modes route agents to only the documents needed for the task.

## CI
1. Static project checks (`tests/test_static.py`).
2. Reusable Noema conformance pinned to an immutable Noema commit.
3. GitHub Pages deployment from `site/` after push to main.
