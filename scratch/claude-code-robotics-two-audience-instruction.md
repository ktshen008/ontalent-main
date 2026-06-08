# Claude Code task — Robotics: two-audience structure (programs vs team support)

Reference form: `ontalent-team-building.html` (now includes FRC). Same OnTalent site you've been editing — uses `build.py` + `styles.css`, shared header/nav/footer, relative links. Work on a branch.

## The core change
Robotics content currently mixes two audiences. Separate them, and make one distinction explicit everywhere:

> **OnTalent runs FLL and FTC student programs. OnTalent supports FLL, FTC, and FRC teams.**

Do **not** imply OnTalent runs FRC.

- **Students & families** → `pathways-robotics.html` (OnTalent's own FLL & FTC programs)
- **Schools, coaches & teams** → `team-support.html` (support for FLL, FTC & FRC teams)

## 1) `pathways-robotics.html` — families / programs
- Hero: focus on students and families joining OnTalent's robotics programs (build skills, the FLL → FTC ladder, competition prep). One line may note that older students can connect to FRC readiness and regional team support — without claiming OnTalent runs FRC.
- Replace the "ways to take part" area with three cards:
  1. **OnTalent FLL Program** — younger / middle-school; LEGO robotics, coding, teamwork, innovation project.
  2. **OnTalent FTC Program** — advanced; robot design, coding, strategy, documentation, competition.
  3. **Regional Team Support** — for schools, coaches, and community teams (FLL, FTC, FRC) → links to `team-support.html`.
- Buttons: "Register for OnTalent Robotics", "Get Team Support" (→ team-support), "Request a School Workshop" (→ workshop-application).
- Keep current FLL program naming (Explore/Challenge) as-is. *(Future note, not now: FIRST is transitioning FLL naming and hardware starting the 2027-28 season; switch to generic "FIRST LEGO League" naming in a later pass.)*

## 2) `team-support.html` — schools / coaches / teams
- Hero makes the two roles clear, e.g.: "OnTalent supports schools, coaches, and community groups with FIRST robotics teams — FLL, FTC, and FRC — through workshops, mentor connection, equipment planning, coach training, and season prep. (OnTalent also runs its own FLL and FTC student programs.)"
- Port the form's program options as-is — **FLL Challenge, FTC, FRC, Not sure** (FLL Explore was removed as it isn't a focus). Keep FLL Challenge naming for now. Note the form title is now "Start or grow your robotics team" (program-agnostic) — keep it that way.
- Add the **expectations note** near the form (verbatim or close):
  > OnTalent may provide guidance, workshops, mentor connection, parts-planning support, or community coordination depending on capacity. Schools and teams remain responsible for official team registration, student supervision, safety, and competition compliance.

## 3) Trademark footnote (both robotics pages)
Add a small footer note on `pathways-robotics.html` and `team-support.html`:
> FIRST®, FIRST® LEGO® League, FIRST® Tech Challenge, and FIRST® Robotics Competition are trademarks of For Inspiration and Recognition of Science and Technology (FIRST). OnTalent references these programs for educational and team-support purposes.

## Keep (from the prior pass)
- The funnel cross-links: workshop → team support → group order; all three reachable from the robotics page and footer.
- Submission unchanged: the form posts `type: 'team'` to the same Apps Script endpoint → "Team Building" tab. **No backend change is needed for FRC** — it's just another value in the Programs field.

## Constraints
- Static HTML/CSS/JS via the existing design system (`build.py` / `styles.css`); reuse the shared header/nav/footer; relative links; no new dependencies; no browser storage; accessible; mobile-responsive.
- Don't break other pages or the other two forms. Branch + preview before merge.

## Acceptance criteria
- Robotics pathway page reads as families/programs (FLL + FTC) with a clear, separate link to team support; no claim that OnTalent runs FRC.
- Team-support page states the run-vs-support distinction, lists FLL/FTC/FRC support, and includes the FRC form option plus the expectations note.
- Trademark footnote present on both robotics pages.
- Funnel links intact; existing forms and pages unaffected; mobile + accessibility clean.
