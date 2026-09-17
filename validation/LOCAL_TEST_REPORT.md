# Local Test Report — Professional Demo

**Date:** 2026-09-17  
**Scope:** static site + Noema consumer structure before remote publication.

## Result

**PASS locally.** Exact Noema conformance and GitHub Pages deployment remain remote gates and will run once the repository exists on GitHub.

| Gate | Result | Evidence |
|---|---|---|
| Public pages present | PASS | landing, business plan, Noema case study |
| Internal links + anchors | PASS | deterministic parser |
| Demo disclosure | PASS | all three public primary pages |
| Form outbound endpoint | PASS | none |
| Network APIs | PASS | none in public JS |
| Browser persistence APIs | PASS | none |
| Prohibited guarantee/superlative patterns | PASS | static scan |
| JS syntax | PASS | `node --check site/app.js` |
| Agent entrypoint budget | PASS | 142 words (~189-token heuristic) |
| Noema context refs | PASS | no missing `repo://` paths |
| Noema source locators | PASS | no missing source-of-truth paths |
| External runtime assets | PASS | 0 |
| Static public payload | PASS | ~35 KB before compression |
| Main text contrast | PASS | Ink/Paper 17.0:1 |
| Accent contrast | PASS | Oxblood/Paper 10.3:1 |
| CTA contrast | PASS | White/Oxblood 10.9:1 |
| Reduced motion path | PASS | CSS `prefers-reduced-motion` |
| GitHub Pages workflow pattern | PASS | aligned to current official GitHub Pages action versions |
| Noema reusable workflow | READY | pinned to immutable Noema main commit containing hardened consumer workflow |

## Edge case found during this build
The first prohibited-claims check flagged a negative sentence containing the words “resultados garantizados.” The copy was rewritten to “Sin promesas de resultado,” preventing a false positive without weakening the safety boundary.

## Visual QA
Desktop preview renders show:
- editorial hierarchy remains legible;
- the custom profile illustration is coherent with the brand territory;
- business-plan and Noema case-study pages use the same system;
- no external image/font dependency is required.

The repository ships responsive CSS down to 320 px. Browser-level responsive verification will be repeated in GitHub/real browser after publication.

## Remote exit criteria
1. Noema conformance workflow PASS.
2. Static quality workflow PASS.
3. GitHub Pages deployment PASS.
4. Live desktop/mobile smoke review PASS.
5. Record final live URL + workflow runs in this report.
