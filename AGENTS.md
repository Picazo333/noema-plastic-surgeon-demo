# Agent entrypoint

This repository is a **fictional, privacy-safe professional demo** for a plastic-surgery practice.

1. Read `noema.project.yaml` and identify the current task mode.
2. Load only the files required by that mode; do **not** recursively read `docs/` or `validation/` by default.
3. Preserve these non-negotiables:
   - never invent real medical credentials, certifications, outcomes or testimonials;
   - never add medical advice or guaranteed-result language;
   - never transmit, persist or track patient/user data in this demo;
   - keep the public site deployable as static files under `site/`;
   - keep the visual language editorial, restrained and high-trust.
4. Before finishing a code/content change, run `python tests/test_static.py` and inspect the relevant Noema quality claims.

Task routing:
- **patch** → `docs/SITE_SPEC.md`
- **build** → `docs/SITE_SPEC.md`, `docs/BRAND_SYSTEM.md`
- **research** → `docs/BUSINESS_PLAN.md`, `docs/COMPLIANCE.md`
- **audit** → `validation/QUALITY_GATE.md`, `docs/COMPLIANCE.md`
- **architect** → `docs/ARCHITECTURE.md`, `docs/SITE_SPEC.md`
- **recover** → `README.md`, `validation/NOEMA_TRACE.md`
