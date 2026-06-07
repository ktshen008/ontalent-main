# Claude Code task — Add the Workshop Application page to the OnTalent site

## Before you start (human setup)
Copy this file into the repo as the reference implementation:

- `ontalent-workshop-application.html` — a complete, working standalone version of the form (markup + logic), already in OnTalent's violet palette.

(Drop it in `scratch/`; it doesn't have to stay in the final site.)

This builds on the same site you just added `group-order-gobilda.html` to. Reuse the same patterns.

## Context
- **Site:** OnTalent — a static, multi-page HTML site deployed via GitHub Pages. Shared header/nav/footer markup, a single stylesheet, assets under `/assets/`, no framework, no build step.
- **Brand:** deep violet (`#2b214a`); the reference file is already violet, so this is mostly about swapping in the *real* site header, footer, fonts, and design tokens so the page is identical in chrome to every other page.
- **Goal:** let educators and student leaders apply to host a hands-on OnTalent workshop at their school, across all four pathways (robotics-focused). It's an application that lands in the team's review pipeline — not a transaction. No payment, no totals.

## What to build
Create a new page (suggested `workshop-application.html`) that **reuses the site's existing header, nav, footer, CSS, and fonts** so it looks native. Port the form's structure and logic from `ontalent-workshop-application.html`, restyled to the real OnTalent components and tokens.

**Sections / fields**
- **About you:** full name (required), role (required select: Educator/staff · University student leader · High-school student leader · Other), email (required), phone.
- **School sponsor (conditional, critical):** shown and **required whenever the role is not "Educator/staff"** — i.e., for both student-leader types and "Other." Collects sponsor name, role, and school email. For high-school applicants the wording makes clear this is the responsible adult and that OnTalent coordinates with them, not the student. Keep this gating exactly as in the reference file — the form must not submit a non-educator application without a sponsor.
- **Your school:** school/organization name (required), school type, city (required), board/district.
- **The workshop:** pathway(s) — a **multi-select of all four** (Robotics & Engineering, AI & Computing, Health & Medicine, Leadership & Innovation), robotics listed first, at least one required; grade level(s); estimated # of students; format; where it would run; preferred timeframe; space & equipment (textarea).
- **Goals & support:** goals (textarea); funding (select); notes (textarea).

**Flow:** validate (including the conditional sponsor requirement and ≥1 pathway) → "Review application" (clean summary) → "Submit application" → "✓ Application received" confirmation (which acknowledges the sponsor for student-led requests). Keep "Email instead" / "Copy summary" as a fallback. Include the hidden honeypot field.

**Config block** (top of the script): `organizationName`, `organizerEmail`, `submitEndpoint`.

## Submission → the SAME Google Sheet
This reuses the existing order endpoint. On submit, POST JSON to `CONFIG.submitEndpoint` (the same Apps Script web app URL the group-order form already uses) with `mode: 'no-cors'` and `Content-Type: text/plain`, and treat a sent request as success:

```js
fetch(CONFIG.submitEndpoint, {
  method: 'POST', mode: 'no-cors',
  headers: { 'Content-Type': 'text/plain;charset=utf-8' },
  body: JSON.stringify(payload)   // payload.type === 'workshop'
});
```

The key field is **`type: 'workshop'`** — the updated Apps Script routes on it and writes to a "Workshop Applications" tab (the order form sends no type and is unaffected). Payload shape:

```json
{
  "type": "workshop", "submittedAt": "ISO", "org": "OnTalent",
  "name": "", "role": "", "email": "", "phone": "",
  "sponsorName": "", "sponsorRole": "", "sponsorEmail": "",
  "school": "", "schoolType": "", "city": "", "board": "",
  "pathways": "comma-separated", "grades": "", "students": "",
  "format": "", "location": "", "timeframe": "", "space": "",
  "goals": "", "funding": "", "notes": "",
  "summary": "plain-text summary", "company": "honeypot"
}
```

(The matching Apps Script is `ontalent-submission-endpoint.gs` — the human updates the existing deployment with it; it's not deployed from the repo.)

## Constraints
- Pure HTML/CSS/JS, no framework or build step. Reuse the existing layout/partials and stylesheet — don't fork the design. No browser storage.
- Accessible (labels on every field, keyboard-usable, honeypot hidden from assistive tech) and mobile-responsive.
- **Preserve the sponsor gating logic exactly** — it's a safeguarding requirement, not cosmetic.
- Don't modify or break other pages. Work on a branch.

## Linking
Add links following site conventions — sensible spots: the "Get Involved" / "Join" area, the Pathways page or each pathway page (especially robotics), and the footer. Match existing nav/footer markup.

## Steps
1. Inspect the repo: confirm how header/nav/footer/CSS/fonts are shared (you did this for the order page — reuse that knowledge).
2. Create `workshop-application.html` reusing the real header/footer/CSS.
3. Port the form markup + JS from the reference file; swap the reference's inline styles for the site's tokens/components; keep the conditional sponsor logic and the multi-select pathways intact.
4. Wire submit to `CONFIG.submitEndpoint` (same URL as the order form) per the contract above; keep email/copy fallback + honeypot.
5. Add the link(s).
6. Run locally, verify on desktop and a narrow viewport (test: choosing a student-leader role reveals and requires the sponsor block; choosing Educator hides it), and commit to a branch.

## Acceptance criteria
- Looks like part of the OnTalent site (same header/nav/footer/fonts/violet palette).
- Selecting "Educator/staff" hides the sponsor block; selecting either student-leader role (or Other) shows it and blocks submission until sponsor name + valid email are filled.
- Pathways multi-select requires at least one; robotics appears first.
- "Review application" shows an accurate summary; "Submit application" posts the JSON with `type: 'workshop'` and shows the confirmation; email/copy fallback works with no endpoint.
- Works on mobile; all fields labeled; no console errors; other pages and the existing order form are unaffected.

## Human setup (out of band, not in the repo)
1. Open the existing Apps Script project (the one behind the group-order endpoint).
2. Replace its code with `ontalent-submission-endpoint.gs`, Save.
3. Deploy → Manage deployments → edit your web app → Version: **New version** → Deploy. (Same URL, no new authorization.)
4. Put that URL in this form's `CONFIG.submitEndpoint`. The "Workshop Applications" tab appears automatically on the first submission; add a Status column workflow (New → Reviewing → Contacted → Scheduled) as you like.
