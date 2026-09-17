# Edge-case Results

Cases: **55** · GAP: **6** · PASS: **49**

## Material findings

- **GAP / critical — entrypoint traversal outside repo**: RC0 lint passes an existing ../ entrypoint outside project root; audit safe-path logic would reject it.
- **GAP / high — entrypoint points to directory**: RC0 lint checks exists(), not is_file(); reusable CI can pass a directory entrypoint.
- **GAP / medium — default context mode has no declaration**: Schema/lint allow default_mode with no matching context.modes entry; cold start silently degrades to entrypoint-only.
- **GAP / high — executor registry contains scalar entry**: Malformed executor list entry can raise AttributeError instead of deterministic FAIL.
- **GAP / high — routing registry contains scalar entry**: Malformed route list entry can crash validator instead of deterministic FAIL.
- **GAP / medium — routing prefer is null**: Null route preference can raise TypeError in list(None).

## Full matrix

| # | Family | Case | Result | Detail |
|---:|---|---|---|---|
| 1 | noema | baseline consumer conformance | PASS | [] |
| 2 | noema | protocol pin mismatch | PASS | observed=FAIL; expected=FAIL; issues=['NOEMA-VERSION-001'] |
| 3 | noema | unknown project type | PASS | observed=FAIL; expected=FAIL; issues=['NOEMA-COMP-001'] |
| 4 | noema | unknown trait | PASS | observed=FAIL; expected=FAIL; issues=['NOEMA-COMP-002'] |
| 5 | noema | unknown quality claim | PASS | observed=FAIL; expected=FAIL; issues=['NOEMA-QLT-002'] |
| 6 | noema | authority overlap | PASS | observed=FAIL; expected=FAIL; issues=['NOEMA-AUTH-001'] |
| 7 | noema | missing context entrypoint | PASS | observed=FAIL; expected=FAIL; issues=['NOEMA-CTX-001'] |
| 8 | noema | broken repo source of truth | PASS | observed=FAIL; expected=FAIL; issues=['NOEMA-REF-001'] |
| 9 | noema | source of truth traversal escape | PASS | observed=FAIL; expected=FAIL; issues=['NOEMA-REF-001'] |
| 10 | noema | missing required context ref | PASS | observed=FAIL; expected=FAIL; issues=['NOEMA-CTX-002'] |
| 11 | noema | required context traversal escape | PASS | observed=FAIL; expected=FAIL; issues=['NOEMA-CTX-002'] |
| 12 | noema | invalid extension namespace | PASS | observed=FAIL; expected=FAIL; issues=['extension-key'] |
| 13 | noema | duplicate quality claim | PASS | observed=FAIL; expected=FAIL; issues=['quality-claims'] |
| 14 | noema | invalid uppercase project id | PASS | observed=FAIL; expected=FAIL; issues=['project-id'] |
| 15 | noema | unknown top-level field | PASS | observed=FAIL; expected=FAIL; issues=['extra-top'] |
| 16 | noema | default mode undeclared | PASS | observed=PASS; expected=PASS; issues=[] |
| 17 | noema | duplicate executor ids | PASS | observed=FAIL; expected=FAIL; issues=['NOEMA-STACK-001'] |
| 18 | noema | invalid executor status | PASS | observed=FAIL; expected=FAIL; issues=['NOEMA-STACK-001'] |
| 19 | noema | duplicate route ids | PASS | observed=FAIL; expected=FAIL; issues=['NOEMA-ROUTE-REG-001'] |
| 20 | noema | route references unknown executor | PASS | observed=FAIL; expected=FAIL; issues=['NOEMA-ROUTE-REG-001'] |
| 21 | noema | entrypoint traversal outside repo | GAP | RC0 lint passes an existing ../ entrypoint outside project root; audit safe-path logic would reject it. |
| 22 | noema | entrypoint points to directory | GAP | RC0 lint checks exists(), not is_file(); reusable CI can pass a directory entrypoint. |
| 23 | noema | default context mode has no declaration | GAP | Schema/lint allow default_mode with no matching context.modes entry; cold start silently degrades to entrypoint-only. |
| 24 | noema | executor registry contains scalar entry | GAP | Malformed executor list entry can raise AttributeError instead of deterministic FAIL. |
| 25 | noema | routing registry contains scalar entry | GAP | Malformed route list entry can crash validator instead of deterministic FAIL. |
| 26 | noema | routing prefer is null | GAP | Null route preference can raise TypeError in list(None). |
| 27 | site | viewport metadata | PASS |  |
| 28 | site | single h1 | PASS | h1=1 |
| 29 | site | main landmark | PASS |  |
| 30 | site | skip link target exists | PASS |  |
| 31 | site | dialog has accessible label | PASS |  |
| 32 | site | mobile menu exposes aria state | PASS |  |
| 33 | site | all form controls wrapped by labels | PASS | controls=3 labels=3 |
| 34 | site | demo disclosure visible | PASS |  |
| 35 | site | fictional identity disclosure | PASS |  |
| 36 | site | no remote scripts/styles | PASS |  |
| 37 | site | no data transmission APIs | PASS |  |
| 38 | site | no browser persistence | PASS |  |
| 39 | site | no dynamic code execution | PASS |  |
| 40 | site | submit is prevented | PASS |  |
| 41 | site | form reset after simulation | PASS |  |
| 42 | site | no external form action | PASS |  |
| 43 | site | no prohibited marketing/medical claims | PASS |  |
| 44 | site | risk disclosure present | PASS |  |
| 45 | site | reduced-motion CSS | PASS |  |
| 46 | site | mobile breakpoint present | PASS |  |
| 47 | site | contrast body text | PASS | 15.74:1 |
| 48 | site | contrast wine text | PASS | 9.74:1 |
| 49 | site | contrast primary CTA | PASS | 11.28:1 |
| 50 | site | contrast muted copy | PASS | 4.94:1 |
| 51 | artifact | artifact required fields | PASS | [] |
| 52 | artifact | artifact project linkage | PASS | noema-plastic-surgeon-demo |
| 53 | artifact | artifact integrity hash matches | PASS | artifact hash |
| 54 | artifact | artifact evidence refs exist | PASS | evidence paths |
| 55 | context | default cold-start context budget | PASS | 3 files, ~557 heuristic tokens |
