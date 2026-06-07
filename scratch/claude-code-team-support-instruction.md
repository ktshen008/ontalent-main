# Claude Code task — Add the FLL/FTC Team Support page + wire the funnel

## Before you start (human setup)
Copy this file into the repo as the reference implementation:

- `ontalent-team-building.html` — a complete, working standalone version of the intake (markup + logic), already in OnTalent's violet palette.

This is the third intake on the site, after `group-order-gobilda.html` and `workshop-application.html`. Reuse the same patterns.

## Context
- **Site:** OnTalent — static, multi-page HTML on GitHub Pages. Shared header/nav/footer, one stylesheet, `/assets/`, no framework, no build step.
- **Goal A — new page:** let schools and coaches request help to start or grow an FLL/FTC robotics team. It's an **open, needs-based** intake (they tell us where they are and check what they need) — not tiered packages, not a transaction.
- **Goal B — connect the funnel:** these three flows are one journey (workshop → team → parts). Add cross-links so each stage points to the next.

## Goal A — build the team support page
Create a new page (suggested `team-support.html`) that **reuses the site's real header, nav, footer, CSS, and fonts**. Port the structure and logic from `ontalent-team-building.html`, restyled to the real OnTalent components/tokens.

**Sections / fields**
- **About you:** name (required); role (required select: Teacher/educator · School staff/admin · Parent volunteer coach · Community/club coach · Other); email (required); phone.
- **Your school:** school/organization (required), school type, city (required), board.
- **Where you are:** current stage (new / improving / restarting / exploring); program(s) — multi-select **FLL Explore · FLL Challenge · FTC · Not sure**, at least one required; grades; estimated # students; "Done an OnTalent workshop? (Yes / No / Not yet — interested)" — this is a funnel signal, keep it.
- **Coaching setup:** coach robotics experience; mentors/volunteers lined up; meeting space.
- **What you need most:** a multi-select of support areas — **Registering with FIRST Canada · Funding & grants · Equipment & kits · Coach training · A mentor for our team · Season curriculum & cadence · Competition prep · Fundraising & sustainability** — at least one required; plus an open "tell us more" textarea. This needs-based block is the core of the open framing.
- **Funding & timeline:** funding select; when hoping to start; notes.

**Flow:** validate (≥1 program, ≥1 need, plus required text fields) → "Review request" → "Submit request" → "✓ Request received" confirmation (which, when FTC is selected, mentions the goBILDA group order for parts). Keep "Email instead" / "Copy summary" fallback and the hidden honeypot.

**Config block:** `organizationName`, `organizerEmail`, `submitEndpoint`.

## Submission → the SAME Google Sheet
Reuse the existing endpoint. POST JSON to `CONFIG.submitEndpoint` (same Apps Script URL as the other two forms), `mode: 'no-cors'`, `Content-Type: text/plain`, treat a sent request as success. The key field is **`type: 'team'`** — the updated Apps Script routes on it to a "Team Building" tab. Payload shape:

```json
{
  "type": "team", "submittedAt": "ISO", "org": "OnTalent",
  "name": "", "role": "", "email": "", "phone": "",
  "school": "", "schoolType": "", "city": "", "board": "",
  "stage": "", "programs": "comma-separated", "grades": "", "students": "", "didWorkshop": "",
  "coachExp": "", "mentors": "", "space": "",
  "needs": "comma-separated", "detail": "", "funding": "", "timeline": "", "notes": "",
  "summary": "plain-text summary", "company": "honeypot"
}
```

(The matching script is `ontalent-submission-endpoint.gs`, which now handles order + workshop + team. The human updates the existing deployment with it — see human setup.)

## Goal B — wire the funnel (edit the existing pages)
Add light, native CTAs so the three stages connect. Match the site's existing button/card styling:

1. **Workshop page → team support:** on the workshop confirmation (and/or near the bottom of the page), add a line/CTA like "Ready to start your own team? → Team support" linking to `team-support.html`.
2. **Team support page → group order:** already handled in the confirmation copy (FTC mention); also add a small static link to `group-order-gobilda.html` somewhere sensible on the page ("Already have a team? Order parts through our goBILDA group order").
3. **Robotics pathway page:** make sure all three are discoverable there — workshop application, team support, and the group order — since robotics is the common thread.
4. **Footer / Get Involved:** add "Team support" alongside the existing "goBILDA Group Order" link.

Keep these as plain links/buttons in the site's style — no new dependencies.

## Constraints
- Pure HTML/CSS/JS, no framework/build step. Reuse existing layout/partials and stylesheet. No browser storage.
- Accessible (labels on every field, keyboard-usable, honeypot hidden from assistive tech) and mobile-responsive.
- Don't break other pages or the existing two forms. Work on a branch.

## Steps
1. Create `team-support.html` reusing the real header/footer/CSS; port the form from the reference file and restyle to site tokens; keep the two multi-selects and their required-min validation.
2. Wire submit to `CONFIG.submitEndpoint` with `type: 'team'`; keep email/copy fallback + honeypot.
3. Make the Goal B cross-link edits on the workshop page, robotics pathway page, and footer.
4. Run locally; verify on desktop and a narrow viewport (test: form blocks submit until ≥1 program and ≥1 need are chosen; FTC selection shows the parts-order mention in the confirmation); commit to a branch.

## Acceptance criteria
- Team support page looks native (same header/nav/footer/fonts/violet palette).
- Requires ≥1 program and ≥1 need; "Submit request" posts JSON with `type: 'team'` and shows the confirmation; email/copy fallback works with no endpoint.
- The funnel links exist and point correctly: workshop → team support → group order, and all three are reachable from the robotics page and footer.
- Works on mobile; all fields labeled; no console errors; existing pages and the other two forms unaffected.

## Human setup (out of band, not in the repo)
1. Open the existing Apps Script project (behind the current endpoint).
2. Replace its code with the updated `ontalent-submission-endpoint.gs` (now handles all three types), Save.
3. Deploy → Manage deployments → edit your web app → Version: **New version** → Deploy. (Same URL, no new authorization.)
4. Put that URL in this form's `CONFIG.submitEndpoint`. The "Team Building" tab appears on the first submission; manage it with a Status column (New → Reviewing → Contacted → Scheduled), same as the other tabs.
