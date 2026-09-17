# Noema Trace

## Why this project exists
This is the first deliberately small, greenfield, customer-facing consumer used after RC0 hardening. It tests whether Noema can govern a sensitive visual project **without turning it into a protocol-heavy repository**.

## Progressive context design
`AGENTS.md` gives an agent the minimal boundary and routing map. The task mode then loads only the relevant source-of-truth documents from `noema.project.yaml`.

Expected cold-start behavior:
- always: `AGENTS.md` + `noema.project.yaml` + user task;
- build: add two focused docs;
- audit: add two different focused docs;
- research: add business/compliance only.

## Quality claims exercised
- contract-conformance
- context-efficiency
- provenance
- security-boundaries
- visual-coherence
- research-groundedness
- delivery-integrity

## Observed learning target
If this project stays understandable, auditable and deployable without agents bulk-reading the repo, progressive context is working as intended.
