# Noema Consumer Demo — Edge-Case Validation Report

> **Historical evidence.** This report captures the pre-hardening RC0 consumer run. The six validator gaps documented below were subsequently fixed in Noema, merged, regression-tested, and the consumer workflow was repinned. Current Noema main after hardening/pin: `769a84efa0c1489d24a2b6f9879697d8ecae166a`.

**Consumer:** fictional plastic-surgeon static website  
**Noema pin:** `0.1.0-rc.0` / `730684066573efe3757d0623c7b1a4282e0f1856`  
**Purpose:** validate a small public-facing visual application before selective migration of Skill Foundry and Agency Foundation.

## Result

- **55 edge cases executed**
- **49 PASS**
- **6 Noema hardening gaps**
- **0 remaining demo failures**
- Default build cold-start: **3 files / ~557 heuristic tokens**
- Static JavaScript syntax: **PASS** (`node --check`)
- Python edge harness syntax: **PASS**
- Local static HTTP smoke: **PASS / HTTP 200**

## Findings

### N-01 — Entrypoint path escape can pass reusable CI
**Severity:** critical  
**Observed:** an existing `../outside.md` can satisfy current `noema lint` entrypoint existence check. `audit` would reject it because context resolution uses the safe project-path guard.  
**Impact:** the reusable conformance workflow currently runs `noema lint` only, so the stricter audit guard is not part of the required consumer gate.  
**Recommended patch:** resolve the entrypoint through `safe_project_path()` in lint and require a regular file.

### N-02 — Entrypoint may be a directory
**Severity:** high  
**Observed:** `context.entrypoint: docs` can pass lint because the check is `exists()` rather than `is_file()`.  
**Impact:** CI can claim structural conformance for a context entrypoint that cannot be consumed as a text file.  
**Recommended patch:** require `is_file()` after safe resolution.

### N-03 — Default context mode may be undeclared
**Severity:** medium  
**Observed:** `default_mode: build` may remain while `context.modes.build` is absent. Lint passes and context silently becomes entrypoint-only.  
**Impact:** progressive-context guarantees can degrade without an explicit failure.  
**Recommended patch:** when `modes` exists, require the default mode key or make the fallback behavior explicit in protocol/schema.

### N-04 — Scalar executor registry member can crash validator
**Severity:** high  
**Observed:** adding a string element to `executors:` reaches `.get()` on a non-object and raises `AttributeError`.  
**Impact:** malformed consumer input can produce an internal validator error instead of deterministic FAIL.  
**Recommended patch:** validate registry shape/schema before semantic checks; never call `.get()` on unvalidated entries.

### N-05 — Scalar route registry member can crash validator
**Severity:** high  
**Observed:** adding a string to `routes:` can raise `AttributeError`.  
**Impact:** same fail-open/fail-unclean robustness issue as N-04.  
**Recommended patch:** schema/shape validation first.

### N-06 — Null `prefer` can crash routing registry validation
**Severity:** medium  
**Observed:** `prefer: null` reaches `list(None)` and raises `TypeError`.  
**Impact:** invalid configuration is not reported as deterministic conformance failure.  
**Recommended patch:** require arrays for `prefer`/`fallback` or normalize null to empty list only if protocol explicitly permits it.

## What did *not* break

The consumer passed the intended RC0 semantics for protocol pinning, known project type/traits/quality claims, authority collision detection, broken `repo://` sources, context-reference traversal, missing context files, extension namespace restrictions, duplicate quality claims, invalid project identity, duplicate executor/route IDs, dangling executor references, site integrity, provenance linkage, data-transmission boundaries, accessibility baseline, responsive baseline, reduced motion, medical-claim boundaries, and contrast checks.

## Architecture verdict

**Do not reopen Noema's architecture. Harden RC0 before migration.**

The demo supports the existing model: a small application needed only a concise manifest, an agent entry map, project-local quality gates, evidence, and pinned conformance. Domain-specific medical-content boundaries stayed in the project instead of leaking into Noema. Cold-start remained small.

The six findings are validator/contract-hardening issues. Fixing them should precede selective migration because migration would otherwise replicate a conformance gate that can accept unsafe context entrypoints and can crash on malformed registry inputs.

## Recommended sequence

1. Patch N-01 and N-02 together as the highest-priority context-safety fix.
2. Patch N-04/N-05/N-06 with registry schemas or defensive type validation.
3. Decide N-03 semantics explicitly and encode them in schema/lint/tests.
4. Add regression fixtures for all six cases to Noema.
5. Re-run this consumer demo against the patched Noema commit.
6. Only then begin Skill Foundry selective migration.
