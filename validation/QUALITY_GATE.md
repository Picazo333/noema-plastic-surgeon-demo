# Quality Gate

A change is releasable only when all applicable gates pass.

## Deterministic
- All public HTML files exist and internal navigation targets resolve.
- No remote network calls or browser persistence APIs in public JS.
- Demo form has no action endpoint and is intercepted locally.
- Every public page carries fictional-demo disclosure.
- No prohibited medical marketing terms in public copy.
- Noema project manifest exists and uses a declared default context mode.
- Agent entrypoint remains intentionally small.

## Human/model review
- Visual hierarchy remains calm and premium rather than promotional.
- Mobile view has no horizontal overflow.
- CTA hierarchy is clear without urgency manipulation.
- Business-plan numbers remain labeled as assumptions.
- Noema case-study accurately distinguishes governance from domain authority.

## Release gate
- `python tests/test_static.py` PASS.
- Noema reusable conformance PASS.
- GitHub Pages deployment PASS.
