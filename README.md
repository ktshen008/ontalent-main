# OnTalent — Full Website (Rebuilt)

A complete, redesigned static site for **OnTalent** (Ontario Centre for Talent Development), ready to drop into your GitHub Pages repo. Every page shares one design system, uses **relative links** (so it works under any repo name or a custom domain), and is built for accessibility and mobile.

---

## What's included (26 files)

**21 pages**
```
index.html
pathways.html
pathways-robotics.html
pathways-ai-computing.html
pathways-health-medicine.html
pathways-leadership-innovation.html
pathways-emerging-innovation.html
network.html
network-western-stem-studio.html
network-university-chapters.html
network-partners-supporters.html
experiences.html
experiences-summer-camps.html
experiences-ai-hackathon.html
impact.html
impact-report.html
about.html              ← new
join.html
join-students-families.html
join-sponsors-supporters.html
404.html                ← new
```

**Assets**
```
styles.css        full design system (one file, CSS variables)
script.js         mobile nav, scroll reveal, stat count-up (degrades without JS)
favicon.svg       brand mark
favicon.png       180×180 apple-touch icon
favicon.ico       multi-size icon for older browsers
```

---

## Deploy

These files **replace your current ones at the repo root** (same level as the existing HTML). The one file I did **not** include is your existing `social-preview.png` — keep it (every page references `./social-preview.png`). Your existing `assets/` folder can stay too; nothing here depends on it, so you can keep or remove it.

```bash
git checkout -b redesign-v2          # work on a branch first
# copy all files from this package into the repo root, overwriting
git add -A
git commit -m "Full site rebuild: unified design system, About + 404 pages, relative links, favicons"
git push origin redesign-v2
```

Open the branch's GitHub Pages preview, click through every page, then merge to `main`.

> **Tip:** this also fixes the old hardcoded `ktshen008.github.io/...` links — everything is relative now, so it keeps working even if you rename the repo or move to `ontalent.ca`/`.org`.

---

## ⚠️ Before you publish: replace placeholder content

Search the project for **`[CUSTOMIZE`** to find everything that needs real content:

- **about.html** — team names, photos, and bios; board members; **CRA charity number**; phone number; links to your annual report / audited financials.
- **impact.html & impact-report.html** — confirm or replace every number; add a real ED letter; swap gradient blocks for student photos.
- **join-sponsors-supporters.html** — add real donation links (e.g. CanadaHelps) on each tier; confirm tier amounts and benefits.
- **network-partners-supporters.html** — real partner names/logos.
- **experiences-summer-camps.html** — Camp A & B descriptions.
- **experiences-ai-hackathon.html** — dates, grades, location, cost, registration link.

### Numbers are placeholders — do not publish as-is
The stats throughout (500+ students, 92% continue in STEM, 100+ mentors, 12+ partners, the 3-year trend, and the 65/20/15 spending split) are **illustrative examples I inserted to show structure**. Confirm every figure with your team — and ideally cite a source or date — before this goes live. Same for the student stories on the impact page: replace with real, consented stories and photos.

The real program details *are* accurate as given to me: Robotics FLL/FTC schedules, CPC (Python Junior 6+, C++ Intermediate 7+, Tuesdays), MediQuest (Chemistry/Biology Saturdays, Grades 8–10), the camp statuses, and all the Google Form / Mailchimp / LinkedIn links. Double-check them anyway in case anything changed.

---

## Design notes

- **Type:** Fraunces (display) + Hanken Grotesk (body), loaded from Google Fonts.
- **Palette:** warm paper `#FBF7F0`, brand ink-violet `#2b214a`, coral accent `#FF6A4D`, plus per-pathway accent colors. All defined as CSS variables at the top of `styles.css` — change them in one place.
- **Motion:** subtle staggered reveals on scroll and a hero stat count-up. Fully disabled for users with "reduce motion" on, and content stays visible if JavaScript is off.
- **Accessibility:** semantic headings, labelled nav toggle, focus-friendly markup, strong contrast. Still worth a final pass with Lighthouse or WAVE once your real content and images are in.

---

## Still recommended (optional, after launch)

- Real photography of students at the studio.
- A custom domain (`ontalent.ca` / `.org`); once live, change every `og:image` to the absolute URL (`https://yourdomain/social-preview.png`) so link previews render on social platforms.
- An AODA/Lighthouse accessibility review with the final content.
- If you'd like to edit pages in place, preview, and commit directly to the repo, that workflow is smoother in **Claude Code in the desktop app** than handing files back and forth in chat.

---

*Generated as a complete handoff package. The page generator (`build.py`) and stylesheet are included in case you want to regenerate or extend pages.*

https://ktshen008.github.io/ontalent-main/
