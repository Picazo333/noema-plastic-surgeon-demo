# Site Spec

## Goal
Create a premium, credible, responsive static landing concept for a fictional plastic surgeon while demonstrating Noema governance in a consumer repository.

## Audiences
1. Prospective elective-surgery patient comparing physicians.
2. Portfolio reviewer evaluating design/engineering quality.
3. Agent evaluating how Noema routes context and evidence.

## Public information architecture
- `/index.html`: premium patient-facing landing.
- `/business-plan.html`: transparent demo business/growth plan.
- `/noema.html`: public case study and quality trace.

## Landing conversion path
1. Establish calm authority and demo status immediately.
2. Explain philosophy before procedures.
3. Present procedure families without clinical claims.
4. Explain consultation journey and boundaries.
5. Offer a consultation-style CTA that never transmits data.
6. Expose case-study/business-plan surfaces in the footer, not as primary patient CTAs.

## Functional constraints
- Static HTML/CSS/JS only.
- No external JS, analytics, cookies, localStorage or network requests.
- Demo form prevents submission and stores nothing.
- Responsive down to 320 CSS px.
- Works with JavaScript disabled except progressive enhancements.
- Respect `prefers-reduced-motion`.
- Public media are vector/CSS assets committed to the repo.

## Content constraints
- Fictional physician is explicitly disclosed.
- No fabricated certification numbers.
- No before/after results.
- No testimonials presented as real.
- No guaranteed outcomes.
- No personalized medical advice.
