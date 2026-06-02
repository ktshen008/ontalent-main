#!/usr/bin/env python3
"""Generate the full OnTalent static site (consistent header/footer + per-page bodies)."""
import os

OUT = "/home/claude/site"
os.makedirs(OUT, exist_ok=True)

NAV = [
    ("index.html", "Home"),
    ("pathways.html", "Pathways"),
    ("network.html", "Network"),
    ("experiences.html", "Experiences"),
    ("impact.html", "Impact"),
    ("about.html", "About"),
    ("join.html", "Join"),
]

FORM_ROBOTICS = "https://docs.google.com/forms/d/e/1FAIpQLSfxQlpxTnZw-2ZVWZM3I1Tl_4IvkU4uVsTlw1vT_MTFZv2vtQ/viewform?usp=header"
FORM_CPC = FORM_ROBOTICS
FORM_MEDIQUEST = "https://docs.google.com/forms/d/e/1FAIpQLScIyKoboBvqzk8XNStF0nUsB7bdUqrV_tG7-JDGOCQ5SD9FFA/viewform?usp=header"
FORM_CAMP = "https://docs.google.com/forms/d/e/1FAIpQLSd9bQ65OJWOf3xMD-8XLqNEOj32lUScr90FaneoXWWHrueV1g/viewform?usp=header"
NEWS_ARCHIVE = "https://us14.campaign-archive.com/home/?u=96f01affdb5cc285e50d4a68a&id=27def29310"
NEWS_BASE = "https://ocftd.us14.list-manage.com/subscribe?u=96f01affdb5cc285e50d4a68a&id=27def29310"
LINKEDIN = "https://www.linkedin.com/company/ontalent-stemm"

MARK = ('<svg class="brand__mark" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">'
        '<rect width="32" height="32" rx="9" fill="#2B214A"/>'
        '<circle cx="16" cy="16" r="8.5" stroke="#FF6A4D" stroke-width="2.4"/>'
        '<circle cx="22.2" cy="9.8" r="2.6" fill="#FF6A4D"/></svg>')

def head(title, desc, active, og_title=None):
    og_title = og_title or title
    links = "\n      ".join(
        f'<a class="nav__link{" is-active" if active==href else ""}" href="./{href}">{label}</a>'
        for href, label in NAV
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{desc}">
  <meta property="og:title" content="{og_title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="./social-preview.png">
  <meta property="og:type" content="website">
  <meta name="theme-color" content="#2b214a">
  <link rel="icon" href="./favicon.svg" type="image/svg+xml">
  <link rel="alternate icon" href="./favicon.ico">
  <link rel="apple-touch-icon" href="./favicon.png">
  <link rel="stylesheet" href="./styles.css">
  <script>document.documentElement.classList.add('js');</script>
  <title>{title}</title>
</head>
<body>
<header class="site-header">
  <div class="site-header__inner">
    <a class="brand" href="./index.html" aria-label="OnTalent home">
      {MARK}<span class="brand__word">OnTalent</span>
    </a>
    <button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false" aria-controls="site-nav"><span></span></button>
    <nav class="nav" id="site-nav">
      {links}
      <a class="nav__link nav__cta btn btn--primary btn--sm" href="./join-students-families.html">Register</a>
    </nav>
  </div>
</header>
<main>
"""

FOOTER = f"""</main>
<footer class="site-footer">
  <div class="site-footer__top">
    <div>
      <a class="brand" href="./index.html" aria-label="OnTalent home">{MARK}<span class="brand__word">OnTalent</span></a>
      <p class="site-footer__about">A youth innovation ecosystem — robotics, AI, health science, and leadership at OnTalent Lab | Western STEM Studio.</p>
    </div>
    <div class="fcol">
      <h4>Explore</h4>
      <ul>
        <li><a href="./pathways.html">Pathways</a></li>
        <li><a href="./experiences-summer-camps.html">Summer Camps</a></li>
        <li><a href="./experiences.html">Experiences</a></li>
        <li><a href="./impact.html">Impact &amp; Data</a></li>
      </ul>
    </div>
    <div class="fcol">
      <h4>Network</h4>
      <ul>
        <li><a href="./network-western-stem-studio.html">Western STEM Studio</a></li>
        <li><a href="./network-university-chapters.html">University Involvement</a></li>
        <li><a href="./network-partners-supporters.html">Partners &amp; Supporters</a></li>
      </ul>
    </div>
    <div class="fcol">
      <h4>Get Involved</h4>
      <ul>
        <li><a href="./join-students-families.html">Students &amp; Families</a></li>
        <li><a href="./join.html#mentors-volunteers">Mentors &amp; Volunteers</a></li>
        <li><a href="./join-sponsors-supporters.html">Support Us</a></li>
      </ul>
    </div>
    <div class="fcol">
      <h4>Connect</h4>
      <ul>
        <li><a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a></li>
        <li><a href="{NEWS_ARCHIVE}" target="_blank" rel="noopener">Newsletter</a></li>
        <li><a href="mailto:info@ontalent.org">info@ontalent.org</a></li>
        <li><a href="./about.html">About Us</a></li>
      </ul>
    </div>
  </div>
  <div class="site-footer__legal">
    <p><strong>Ontario Centre for Talent Development</strong> — operating as OnTalent</p>
    <p>OnTalent Lab | Western STEM Studio · Western University Discovery Park · 999 Collip Circle, London, ON N6G 0J3, Canada</p>
    <p>&copy; <span data-year>2026</span> Ontario Centre for Talent Development. All rights reserved.</p>
  </div>
</footer>
<script src="./script.js"></script>
</body>
</html>
"""

def newsletter(label="I'm interested in updates about:", opts=None):
    opts = opts or [("Programs & Registration","Family"),("Volunteer & Mentoring","Mentor"),("Impact & Giving","Donor")]
    btns = "\n        ".join(
        f'<a class="btn btn--on-dark" href="{NEWS_BASE}&MMERGE1={tag}">{txt}</a>' for txt, tag in opts
    )
    return f"""<section class="section section--ink">
  <div class="container center">
    <p class="kicker" data-reveal>Stay connected</p>
    <h2 data-reveal data-delay="1">Updates, stories, and opportunities</h2>
    <p class="newsletter__label mt-1" data-reveal data-delay="1">{label}</p>
    <div class="newsletter__buttons" data-reveal data-delay="2">
        {btns}
    </div>
    <p class="newsletter__alt" data-reveal data-delay="2">Or <a href="{NEWS_ARCHIVE}" target="_blank" rel="noopener">view past newsletters</a>.</p>
  </div>
</section>
"""

def cta_band(title, text, btns):
    b = "\n        ".join(btns)
    return f"""<section class="section section--ink cta-band">
  <div class="container">
    <div class="cta-band__inner center">
      <h2 data-reveal>{title}</h2>
      <p data-reveal data-delay="1">{text}</p>
      <div class="btn-row center" data-reveal data-delay="2">
        {b}
      </div>
    </div>
  </div>
</section>
"""

def page_hero(title, lede, tag=None, cta=None):
    tag_html = f'<span class="page-hero__tag" data-reveal>{tag}</span>' if tag else ''
    cta_html = f'<div class="page-hero__cta btn-row" data-reveal data-delay="2">{cta}</div>' if cta else ''
    return f"""<section class="page-hero">
  <div class="page-hero__inner">
    {tag_html}
    <h1 class="page-hero__title" data-reveal data-delay="1">{title}</h1>
    <p class="page-hero__lede" data-reveal data-delay="1">{lede}</p>
    {cta_html}
  </div>
</section>
"""

def write(name, title, desc, active, body, og=None):
    with open(os.path.join(OUT, name), "w") as f:
        f.write(head(title, desc, active, og) + body + FOOTER)
    print("wrote", name)

# ============================================================ INDEX
index_body = f"""<section class="hero">
  <div class="hero__inner">
    <p class="kicker" data-reveal style="color:#FF6A4D">Youth Innovation Ecosystem</p>
    <h1 class="hero__title" data-reveal data-delay="1">Where young innovators <em>begin, build, and lead.</em></h1>
    <p class="hero__lede" data-reveal data-delay="1">OnTalent helps students explore robotics, coding, health science, and leadership through hands-on, mentor-supported programs at our Western STEM Studio.</p>
    <div class="hero__cta btn-row" data-reveal data-delay="2">
      <a class="btn btn--primary" href="./join-students-families.html">Register for Fall–Winter Programs</a>
      <a class="btn btn--outline-dark" href="./pathways.html">Explore Pathways</a>
    </div>
    <div class="hero__stats" data-reveal data-delay="3">
      <div class="stat"><div class="stat__num" data-count="500" data-suffix="+">500+</div><div class="stat__label">Students served this year</div></div>
      <div class="stat"><div class="stat__num" data-count="92" data-suffix="%">92%</div><div class="stat__label">Continue in STEM study</div></div>
      <div class="stat"><div class="stat__num" data-count="12" data-suffix="+">12+</div><div class="stat__label">University &amp; employer partners</div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section__head" data-reveal>
      <p class="kicker">Why OnTalent</p>
      <h2>Families and partners trust us with what matters most</h2>
    </div>
    <div class="grid grid-4">
      <div class="card feature" data-reveal><span class="feature__icon">📈</span><h3>Student outcomes</h3><p class="card__meta">92% continue in STEM</p><p>Students move from curiosity to real capability through mentorship and projects.</p></div>
      <div class="card feature" data-reveal data-delay="1"><span class="feature__icon">🏢</span><h3>A real studio</h3><p class="card__meta">Western STEM Studio</p><p>A place-based home for building, testing, and presenting work at Western University.</p></div>
      <div class="card feature" data-reveal data-delay="2"><span class="feature__icon">👥</span><h3>Mentor support</h3><p class="card__meta">100+ mentors</p><p>University students and professionals guide every learner with care.</p></div>
      <div class="card feature" data-reveal data-delay="3"><span class="feature__icon">🌱</span><h3>Community impact</h3><p class="card__meta">12+ partners</p><p>Embedded in Ontario's education and innovation ecosystem.</p></div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section__head" data-reveal>
      <p class="kicker">Choose your pathway</p>
      <h2>Start with an interest. Grow toward real capability.</h2>
      <p class="lede mt-1">Students can begin with one pathway and expand into projects, competitions, showcases, mentorship, and leadership over time.</p>
    </div>
    <div class="grid grid-4">
      <a class="pathway pathway--robotics" href="./pathways-robotics.html" data-reveal><div class="pathway__top"><span class="pathway__index">01</span><span class="pathway__icon">🤖</span></div><h3>Robotics &amp; Engineering</h3><p class="pathway__desc">Design, build, code, test, and collaborate through hands-on robotics challenges.</p><span class="pathway__link">Explore pathway →</span></a>
      <a class="pathway pathway--ai" href="./pathways-ai-computing.html" data-reveal data-delay="1"><div class="pathway__top"><span class="pathway__index">02</span><span class="pathway__icon">🧠</span></div><h3>AI &amp; Computing</h3><p class="pathway__desc">Programming, AI projects, computing contests, and responsible technology.</p><span class="pathway__link">Explore pathway →</span></a>
      <a class="pathway pathway--health" href="./pathways-health-medicine.html" data-reveal data-delay="2"><div class="pathway__top"><span class="pathway__index">03</span><span class="pathway__icon">⚕️</span></div><h3>Health &amp; Medicine</h3><p class="pathway__desc">Science enrichment, biomedical curiosity, and early exposure to discovery.</p><span class="pathway__link">Explore pathway →</span></a>
      <a class="pathway pathway--leadership" href="./pathways-leadership-innovation.html" data-reveal data-delay="3"><div class="pathway__top"><span class="pathway__index">04</span><span class="pathway__icon">💡</span></div><h3>Leadership &amp; Innovation</h3><p class="pathway__desc">Teamwork, public speaking, entrepreneurship, and student leadership.</p><span class="pathway__link">Explore pathway →</span></a>
    </div>
    <div class="btn-row center mt-2" data-reveal><a class="btn btn--ghost" href="./pathways.html">View all pathways</a></div>
  </div>
</section>

<section class="section section--ink quote-band">
  <div class="container">
    <div class="quote" data-reveal>
      <p class="quote__text">"I came in curious about robotics. Now I'm mentoring other students and thinking about engineering at McMaster."</p>
      <p class="quote__cite">Sarah<span>Grade 10 · FLL Team Lead</span></p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section__head center" data-reveal><p class="kicker">Get involved</p><h2>Find your role in OnTalent</h2></div>
    <div class="grid grid-4">
      <div class="card role" data-reveal><span class="role__icon">🎓</span><h3>Students &amp; Families</h3><p>Explore camps, programs, and pathways, then register for the season.</p><a class="btn btn--primary btn--sm" href="./join-students-families.html">Register or learn more</a></div>
      <div class="card role" data-reveal data-delay="1"><span class="role__icon">🤝</span><h3>Mentors &amp; Volunteers</h3><p>Guide students, support events, and help grow the network.</p><a class="btn btn--ghost btn--sm" href="./join.html#mentors-volunteers">Get involved</a></div>
      <div class="card role" data-reveal data-delay="2"><span class="role__icon">💛</span><h3>Donors &amp; Sponsors</h3><p>Support innovation through giving, sponsorships, and partnerships.</p><a class="btn btn--ghost btn--sm" href="./join-sponsors-supporters.html">Explore giving</a></div>
      <div class="card role" data-reveal data-delay="3"><span class="role__icon">🌐</span><h3>Partners</h3><p>Collaborate on programs, research, or community outreach.</p><a class="btn btn--ghost btn--sm" href="mailto:info@ontalent.org?subject=Partnership%20Inquiry">Start a conversation</a></div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section__head" data-reveal><p class="kicker">Registration open</p><h2>Fall–Winter 2026–2027 programs</h2><p class="lede mt-1">Three current program pathways at OnTalent Lab | Western STEM Studio. Forms include fees, placement, and next steps.</p></div>
    <div class="grid grid-3">
      <div class="program program--robotics" data-reveal><h3>Robotics FLL / FTC</h3><p class="program__tag">Grades 3–12</p><ul><li>Build, code, test, collaborate</li><li>September 2026 – January 2027</li><li>FLL: Thu 6:30–8:00 PM · Sun 1:30–3:00 PM</li><li>FTC: Thu 7:30–9:00 PM · Sun 2:30–4:00 PM</li></ul><a class="btn btn--primary btn--sm btn--block" href="{FORM_ROBOTICS}" target="_blank" rel="noopener">Register for Robotics</a></div>
      <div class="program program--ai" data-reveal data-delay="1"><h3>CPC Coding Challenge</h3><p class="program__tag">Programming foundations</p><ul><li>Python Junior — Grades 6+</li><li>C++ Intermediate — Grades 7+</li><li>Tuesdays, Sep 22, 2026 – Apr 20, 2027</li><li>Contest-style computing skills</li></ul><a class="btn btn--primary btn--sm btn--block" href="{FORM_CPC}" target="_blank" rel="noopener">Register for CPC</a></div>
      <div class="program program--health" data-reveal data-delay="2"><h3>MediQuest Pre-AP</h3><p class="program__tag">Grades 8–10</p><ul><li>Chemistry — Sat 9:00–10:30 AM</li><li>Biology — Sat 10:30 AM–12:00 PM</li><li>Sep 19, 2026 – Apr 17, 2027</li><li>Stronger science foundations</li></ul><a class="btn btn--primary btn--sm btn--block" href="{FORM_MEDIQUEST}" target="_blank" rel="noopener">Register for MediQuest</a></div>
    </div>
    <p class="note center mt-2" data-reveal>Credits and support may be available: current-family and Western-affiliated credits, sibling/referral credits, and limited needs-based bursaries. Placement and payment are confirmed after registration review.</p>
  </div>
</section>

{newsletter()}"""
write("index.html", "OnTalent | Youth Innovation Ecosystem",
      "OnTalent connects students with robotics, coding, health science, summer camps, mentorship, and hands-on innovation at Western STEM Studio.",
      "index.html", index_body)

# ============================================================ PATHWAYS (hub)
pathways_body = page_hero(
    "Interdisciplinary pathways for <em>future-ready</em> students",
    "Students explore robotics, AI, health science, leadership, and emerging innovation through hands-on projects, mentorship, and progressive challenges.",
    cta='<a class="btn btn--primary" href="./join-students-families.html">Register now</a><a class="btn btn--outline-dark" href="#all">See all pathways</a>'
) + f"""<section class="section">
  <div class="container">
    <div class="section__head" data-reveal><p class="kicker">Learning model</p><h2>Explore → Build → Apply → Lead</h2><p class="lede mt-1">Each pathway helps students explore interests, build practical skills, and connect their work to future study, teamwork, mentorship, and real-world impact.</p></div>
    <div class="steps">
      <div class="step" data-reveal><span class="step__num">01</span><h3>Explore</h3><p>Discover interests through robotics, AI, health science, and leadership.</p></div>
      <div class="step" data-reveal data-delay="1"><span class="step__num">02</span><h3>Build</h3><p>Create projects with mentors, peers, and student leaders.</p></div>
      <div class="step" data-reveal data-delay="2"><span class="step__num">03</span><h3>Apply</h3><p>Present, compete, research, prototype, and solve real challenges.</p></div>
      <div class="step" data-reveal data-delay="3"><span class="step__num">04</span><h3>Lead</h3><p>Mentor younger students, launch initiatives, and grow as leaders.</p></div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section__head" data-reveal><p class="kicker">Family guidance</p><h2>Choosing a starting point</h2><p class="lede mt-1">Families can choose a starting point based on a student's interests, readiness, and goals — then grow toward mentorship, showcases, competitions, and leadership.</p></div>
    <div class="grid grid-3">
      <div class="card feature" data-reveal><h3>Start with interest</h3><p>Begin where curiosity is strongest, then discover connected pathways over time.</p></div>
      <div class="card feature" data-reveal data-delay="1"><h3>Grow through readiness</h3><p>Programs support beginners while giving advanced students deeper challenges.</p></div>
      <div class="card feature" data-reveal data-delay="2"><h3>Build toward leadership</h3><p>Pathways connect learning with showcases, competitions, and mentorship.</p></div>
    </div>
  </div>
</section>

<section class="section" id="all">
  <div class="container">
    <div class="section__head" data-reveal><p class="kicker">The pathways</p><h2>Five ways to grow</h2></div>
    <div class="grid grid-3">
      <a class="pathway pathway--robotics" href="./pathways-robotics.html" data-reveal><div class="pathway__top"><span class="pathway__index">01</span><span class="pathway__tag">Current pathway</span></div><h3>🤖 Robotics &amp; Engineering</h3><p class="pathway__desc">Engineering design, CAD, fabrication, embedded systems, coding, testing, and robotics challenges.</p><span class="pathway__link">Explore pathway →</span></a>
      <a class="pathway pathway--ai" href="./pathways-ai-computing.html" data-reveal data-delay="1"><div class="pathway__top"><span class="pathway__index">02</span><span class="pathway__tag">Current pathway</span></div><h3>🧠 AI &amp; Computing</h3><p class="pathway__desc">Programming, AI projects, data, automation, and responsible emerging technology.</p><span class="pathway__link">Explore pathway →</span></a>
      <a class="pathway pathway--health" href="./pathways-health-medicine.html" data-reveal data-delay="2"><div class="pathway__top"><span class="pathway__index">03</span><span class="pathway__tag">Growing pathway</span></div><h3>⚕️ Health &amp; Medicine</h3><p class="pathway__desc">MediQuest, biomedical innovation, science enrichment, and early exposure to research.</p><span class="pathway__link">Explore pathway →</span></a>
      <a class="pathway pathway--leadership" href="./pathways-leadership-innovation.html" data-reveal><div class="pathway__top"><span class="pathway__index">04</span><span class="pathway__tag">Growing pathway</span></div><h3>💡 Leadership &amp; Innovation</h3><p class="pathway__desc">Public speaking, entrepreneurship, teamwork, peer mentoring, and venture challenges.</p><span class="pathway__link">Explore pathway →</span></a>
      <a class="pathway pathway--emerging" href="./pathways-emerging-innovation.html" data-reveal data-delay="1"><div class="pathway__top"><span class="pathway__index">05</span><span class="pathway__tag">Future direction</span></div><h3>🚀 Emerging Innovation</h3><p class="pathway__desc">Advanced projects, youth fellowships, research, startup learning, and future lab models.</p><span class="pathway__link">Explore pathway →</span></a>
    </div>
  </div>
</section>

{cta_band("Not sure where to begin?", "Our team can help match a student to the right starting point.", ['<a class="btn btn--on-dark" href="./join-students-families.html">Students &amp; Families guide</a>', '<a class="btn btn--outline-dark" href="mailto:info@ontalent.org?subject=Pathway%20Question">Ask a question</a>'])}"""
write("pathways.html", "Pathways | OnTalent",
      "Explore OnTalent's pathways in Robotics & Engineering, AI & Computing, Health & Medicine, Leadership & Innovation, and Emerging Innovation.",
      "pathways.html", pathways_body)

# ---- pathway detail helper
def pathway_detail(name, title, lede, tag, accent_word, strands, programs_html, progression, register_btn):
    strands_html = "\n      ".join(
        f'<div class="card feature" data-reveal data-delay="{i%4}"><span class="feature__icon">{ic}</span><h3>{t}</h3><p>{d}</p></div>'
        for i,(ic,t,d) in enumerate(strands)
    )
    prog_html = "\n      ".join(
        f'<div class="step" data-reveal data-delay="{i%4}"><span class="step__num">0{i+1}</span><h3>{t}</h3><p>{d}</p></div>'
        for i,(t,d) in enumerate(progression)
    )
    return page_hero(title, lede, tag=tag, cta=register_btn) + f"""<section class="section">
  <div class="container">
    <div class="section__head" data-reveal><p class="kicker">What students do</p><h2>Build {accent_word} through real work</h2></div>
    <div class="grid grid-4">
      {strands_html}
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section__head" data-reveal><p class="kicker">Programs</p><h2>Ways to take part</h2></div>
    <div class="grid grid-2">
      {programs_html}
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section__head" data-reveal><p class="kicker">Progression</p><h2>From first project to leadership</h2></div>
    <div class="steps">
      {prog_html}
    </div>
  </div>
</section>

{cta_band("Ready to start " + accent_word + "?", "Registration includes fees, placement, and next steps for families.", [register_btn.replace('btn--primary','btn--on-dark').replace('btn--outline-dark','btn--outline-dark')])}"""

# Robotics
write("pathways-robotics.html", "Robotics & Engineering | OnTalent",
      "Robotics & Engineering at OnTalent: design, build, code, test, and compete in FLL and FTC robotics challenges for Grades 3–12.",
      "pathways.html",
      pathway_detail(
        "robotics","Robotics &amp; <em>Engineering</em>",
        "Students design, build, code, test, and collaborate through hands-on robotics challenges — and prepare for FLL and FTC competition.",
        "Current pathway · Grades 3–12","engineering skill",
        [("✏️","Design &amp; CAD","Sketch, model, and iterate real mechanical designs."),
         ("🔧","Fabrication","Assemble, wire, and refine working robots."),
         ("💻","Coding &amp; control","Program behaviour, sensors, and autonomous routines."),
         ("🏆","Compete &amp; collaborate","Test under pressure and work as a team at events.")],
        f'<div class="program program--robotics" data-reveal><h3>FLL — FIRST LEGO League</h3><p class="program__tag">Younger builders</p><ul><li>Thursdays 6:30–8:00 PM</li><li>Sundays 1:30–3:00 PM</li><li>September 2026 – January 2027</li></ul><a class="btn btn--primary btn--sm btn--block" href="{FORM_ROBOTICS}" target="_blank" rel="noopener">Register for Robotics</a></div>'
        f'<div class="program program--robotics" data-reveal data-delay="1"><h3>FTC — FIRST Tech Challenge</h3><p class="program__tag">Advanced builders</p><ul><li>Thursdays 7:30–9:00 PM</li><li>Sundays 2:30–4:00 PM</li><li>September 2026 – January 2027</li></ul><a class="btn btn--primary btn--sm btn--block" href="{FORM_ROBOTICS}" target="_blank" rel="noopener">Register for Robotics</a></div>',
        [("Explore","Join a team and learn the build–code–test loop."),
         ("Build","Own a subsystem and contribute to a competition robot."),
         ("Apply","Compete regionally and document your engineering."),
         ("Lead","Mentor newer members and lead a team.")],
        f'<a class="btn btn--primary" href="{FORM_ROBOTICS}" target="_blank" rel="noopener">Register for Robotics</a><a class="btn btn--outline-dark" href="./pathways.html">All pathways</a>'
      ))

# AI & Computing
write("pathways-ai-computing.html", "AI & Computing | OnTalent",
      "AI & Computing at OnTalent: programming, AI projects, the CPC coding challenge, automation, and responsible technology.",
      "pathways.html",
      pathway_detail(
        "ai","AI &amp; <em>Computing</em>",
        "Programming, AI projects, computing contests, automation, and responsible technology — for students developing real algorithmic thinking.",
        "Current pathway · Grades 6+","computing skill",
        [("⌨️","Programming","Foundations in Python and C++ with hands-on practice."),
         ("🧠","AI projects","Explore models, data, and responsible AI applications."),
         ("🧩","Problem-solving","Contest-style algorithmic and computational thinking."),
         ("⚙️","Automation","Build tools and systems that do useful work.")],
        f'<div class="program program--ai" data-reveal><h3>CPC — Python Junior</h3><p class="program__tag">Grades 6+</p><ul><li>Programming foundations</li><li>Tuesdays, Sep 22, 2026 – Apr 20, 2027</li><li>Contest-style challenges</li></ul><a class="btn btn--primary btn--sm btn--block" href="{FORM_CPC}" target="_blank" rel="noopener">Register for CPC</a></div>'
        f'<div class="program program--ai" data-reveal data-delay="1"><h3>CPC — C++ Intermediate</h3><p class="program__tag">Grades 7+</p><ul><li>Algorithmic thinking</li><li>Tuesdays, Sep 22, 2026 – Apr 20, 2027</li><li>Competitive computing skills</li></ul><a class="btn btn--primary btn--sm btn--block" href="{FORM_CPC}" target="_blank" rel="noopener">Register for CPC</a></div>',
        [("Explore","Learn to code and think computationally."),
         ("Build","Create AI projects, tools, and contest solutions."),
         ("Apply","Enter computing contests and ship real projects."),
         ("Lead","Mentor peers and explore responsible technology.")],
        f'<a class="btn btn--primary" href="{FORM_CPC}" target="_blank" rel="noopener">Register for CPC</a><a class="btn btn--outline-dark" href="./pathways.html">All pathways</a>'
      ))

# Health & Medicine
write("pathways-health-medicine.html", "Health & Medicine | OnTalent",
      "Health & Medicine at OnTalent: MediQuest science enrichment in Chemistry and Biology for Grades 8–10, plus biomedical curiosity and discovery.",
      "pathways.html",
      pathway_detail(
        "health","Health &amp; <em>Medicine</em>",
        "MediQuest science enrichment, biomedical curiosity, and early exposure to health and medical discovery — building stronger foundations for future study.",
        "Growing pathway · Grades 8–10","scientific foundations",
        [("🧪","Chemistry","Pre-AP enrichment that strengthens core chemistry."),
         ("🧬","Biology","Foundational biology with a biomedical lens."),
         ("🔬","Inquiry","Hands-on investigation and scientific reasoning."),
         ("🩺","Discovery","Early exposure to medicine and health research.")],
        f'<div class="program program--health" data-reveal><h3>MediQuest — Chemistry</h3><p class="program__tag">Grades 8–10 · Pre-AP</p><ul><li>Saturdays 9:00–10:30 AM</li><li>Sep 19, 2026 – Apr 17, 2027</li><li>Stronger chemistry foundations</li></ul><a class="btn btn--primary btn--sm btn--block" href="{FORM_MEDIQUEST}" target="_blank" rel="noopener">Register for MediQuest</a></div>'
        f'<div class="program program--health" data-reveal data-delay="1"><h3>MediQuest — Biology</h3><p class="program__tag">Grades 8–10 · Pre-AP</p><ul><li>Saturdays 10:30 AM–12:00 PM</li><li>Sep 19, 2026 – Apr 17, 2027</li><li>Foundations for biomedical study</li></ul><a class="btn btn--primary btn--sm btn--block" href="{FORM_MEDIQUEST}" target="_blank" rel="noopener">Register for MediQuest</a></div>',
        [("Explore","Build curiosity and stronger science foundations."),
         ("Build","Develop reasoning through hands-on investigation."),
         ("Apply","Connect science to real health and medicine."),
         ("Lead","Pursue advanced study and mentor peers.")],
        f'<a class="btn btn--primary" href="{FORM_MEDIQUEST}" target="_blank" rel="noopener">Register for MediQuest</a><a class="btn btn--outline-dark" href="./pathways.html">All pathways</a>'
      ))

# Leadership & Innovation
write("pathways-leadership-innovation.html", "Leadership & Innovation | OnTalent",
      "Leadership & Innovation at OnTalent: public speaking, entrepreneurship, teamwork, peer mentoring, and venture challenges for students.",
      "pathways.html",
      pathway_detail(
        "leadership","Leadership &amp; <em>Innovation</em>",
        "Public speaking, entrepreneurship, teamwork, peer mentoring, venture challenges, and innovation leadership — turning capability into confidence.",
        "Growing pathway","leadership skill",
        [("🎤","Communication","Public speaking and presenting with confidence."),
         ("🤝","Teamwork","Collaboration, facilitation, and peer mentoring."),
         ("🚀","Entrepreneurship","Venture challenges and turning ideas into action."),
         ("🧭","Leadership","Initiative, ownership, and guiding others.")],
        '<div class="panel" data-reveal><h3>How leadership grows here</h3><p class="card__body">Leadership at OnTalent is earned through practice — students mentor younger learners, lead teams, run showcases, and pitch ideas. Opportunities scale with readiness and interest.</p></div>'
        '<div class="panel" data-reveal data-delay="1"><h3>Where it connects</h3><p class="card__body">Leadership weaves through every pathway. A robotics captain, a coding mentor, or a MediQuest peer leader all build the same durable skills: communication, teamwork, and initiative.</p></div>',
        [("Explore","Try presenting, facilitating, and teamwork."),
         ("Build","Lead a project or mentor a peer."),
         ("Apply","Run an event, pitch a venture, or guide a team."),
         ("Lead","Take on student leadership and launch initiatives.")],
        '<a class="btn btn--primary" href="./join-students-families.html">Get started</a><a class="btn btn--outline-dark" href="./pathways.html">All pathways</a>'
      ))

# Emerging Innovation
write("pathways-emerging-innovation.html", "Emerging Innovation | OnTalent",
      "Emerging Innovation at OnTalent: advanced student projects, youth fellowships, research exploration, startup learning, and future innovation lab models.",
      "pathways.html",
      pathway_detail(
        "emerging","Emerging <em>Innovation</em>",
        "Advanced student projects, youth fellowships, research exploration, startup learning, and future innovation lab models — for students ready for deeper challenges.",
        "Future direction","advanced capability",
        [("🔬","Research","Explore open questions with mentor guidance."),
         ("🛠️","Advanced projects","Tackle ambitious, self-directed builds."),
         ("🎓","Fellowships","Youth fellowship and deeper learning models."),
         ("💡","Startup learning","Prototype, test, and learn venture fundamentals.")],
        '<div class="panel" data-reveal><h3>For students ready to go further</h3><p class="card__body">Emerging Innovation is a future direction for advanced students who have grown through other pathways and want research, fellowship, and startup-style challenges.</p></div>'
        '<div class="panel" data-reveal data-delay="1"><h3>A growing model</h3><p class="card__body">We are developing innovation-lab experiences that connect students with mentors, real problems, and the tools to pursue them. Interested? We would love to hear from you.</p></div>',
        [("Explore","Identify a real problem worth pursuing."),
         ("Build","Prototype with mentorship and feedback."),
         ("Apply","Research, test, and refine toward impact."),
         ("Lead","Help shape OnTalent's future innovation lab.")],
        '<a class="btn btn--primary" href="mailto:info@ontalent.org?subject=Emerging%20Innovation%20Interest">Express interest</a><a class="btn btn--outline-dark" href="./pathways.html">All pathways</a>'
      ))

# ============================================================ NETWORK (hub)
network_body = page_hero(
    "A connected <em>network</em> for youth innovation",
    "OnTalent brings together a real studio, university involvement, and community partners so students can learn, build, and lead with support.",
) + f"""<section class="section">
  <div class="container">
    <div class="grid grid-3">
      <a class="pathway" href="./network-western-stem-studio.html" data-reveal><div class="pathway__top"><span class="pathway__icon">🏢</span></div><h3>Western STEM Studio</h3><p class="pathway__desc">Our flagship, place-based home for learning at Western University Discovery Park.</p><span class="pathway__link">Visit the studio →</span></a>
      <a class="pathway" href="./network-university-chapters.html" data-reveal data-delay="1"><div class="pathway__top"><span class="pathway__icon">🎓</span></div><h3>University Involvement</h3><p class="pathway__desc">University students mentor younger learners and help grow campus-connected involvement.</p><span class="pathway__link">Get involved →</span></a>
      <a class="pathway" href="./network-partners-supporters.html" data-reveal data-delay="2"><div class="pathway__top"><span class="pathway__icon">🤝</span></div><h3>Partners &amp; Supporters</h3><p class="pathway__desc">Universities, employers, and community partners power opportunity for students.</p><span class="pathway__link">Partner with us →</span></a>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="split">
      <div data-reveal>
        <p class="kicker">Why the network matters</p>
        <h2>Learning is stronger when it's connected</h2>
        <p class="lede mt-1">A real studio, mentors who care, and partners invested in youth — together they turn curiosity into capability and capability into leadership.</p>
        <ul class="checklist mt-1">
          <li>A supervised, mentor-supported environment</li>
          <li>University students guiding younger learners</li>
          <li>Employers and institutions opening doors</li>
        </ul>
      </div>
      <div class="panel" data-reveal data-delay="1">
        <h3>Become part of it</h3>
        <p class="card__body">Whether you mentor, partner, or sponsor, there's a place for you in the OnTalent network.</p>
        <div class="btn-row mt-1"><a class="btn btn--primary btn--sm" href="./join.html">Get involved</a><a class="btn btn--ghost btn--sm" href="./join-sponsors-supporters.html">Support us</a></div>
      </div>
    </div>
  </div>
</section>

{cta_band("Help grow the network", "Mentors, partners, and supporters make every program possible.", ['<a class="btn btn--on-dark" href="./join.html">Get involved</a>', '<a class="btn btn--outline-dark" href="./join-sponsors-supporters.html">Support OnTalent</a>'])}"""
write("network.html", "Network | OnTalent",
      "The OnTalent network: Western STEM Studio, university involvement, and community partners supporting youth STEM innovation.",
      "network.html", network_body)

# Western STEM Studio
studio_body = page_hero(
    "OnTalent Lab | <em>Western STEM Studio</em>",
    "Our flagship studio gives OnTalent a real, place-based home for hands-on learning at Western University Discovery Park.",
    cta='<a class="btn btn--primary" href="./join-students-families.html">Register for programs</a><a class="btn btn--outline-dark" href="mailto:info@ontalent.org?subject=Studio%20Visit">Plan a visit</a>'
) + f"""<section class="section">
  <div class="container">
    <div class="split">
      <div data-reveal>
        <p class="kicker">The studio</p>
        <h2>A real place to build, test, and present</h2>
        <p class="lede mt-1">Students learn by doing — assembling robots, writing code, running experiments, and sharing their work with mentors, families, and peers in a supervised, supportive space.</p>
        <ul class="checklist mt-1">
          <li>Hands-on, project-based learning</li>
          <li>Mentor-supported and supervised</li>
          <li>Home base for showcases and team practice</li>
        </ul>
      </div>
      <div class="panel" data-reveal data-delay="1">
        <h3>Find us</h3>
        <p class="card__body">OnTalent Lab | Western STEM Studio<br>Western University Discovery Park<br>999 Collip Circle<br>London, ON N6G 0J3, Canada</p>
        <div class="btn-row mt-1"><a class="btn btn--ghost btn--sm" href="https://maps.google.com/?q=999+Collip+Circle+London+ON+N6G+0J3" target="_blank" rel="noopener">Open in Maps</a></div>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section__head" data-reveal><p class="kicker">What happens here</p><h2>Programs that live in the studio</h2></div>
    <div class="grid grid-3">
      <div class="card feature" data-reveal><span class="feature__icon">🤖</span><h3>Robotics teams</h3><p>FLL and FTC teams build, code, and prepare for competition.</p></div>
      <div class="card feature" data-reveal data-delay="1"><span class="feature__icon">🧠</span><h3>Coding &amp; AI</h3><p>CPC sessions and AI projects develop real computing skill.</p></div>
      <div class="card feature" data-reveal data-delay="2"><span class="feature__icon">⚕️</span><h3>MediQuest science</h3><p>Chemistry and biology enrichment for curious students.</p></div>
    </div>
  </div>
</section>

{cta_band("Come build with us", "Programs run throughout the year at the Western STEM Studio.", ['<a class="btn btn--on-dark" href="./join-students-families.html">Register now</a>', '<a class="btn btn--outline-dark" href="./experiences-summer-camps.html">See summer camps</a>'])}"""
write("network-western-stem-studio.html", "Western STEM Studio | OnTalent",
      "OnTalent Lab | Western STEM Studio at Western University Discovery Park — a real home for hands-on, mentor-supported student learning.",
      "network.html", studio_body)

# University involvement
univ_body = page_hero(
    "University students can <em>mentor, lead, and grow</em> the network",
    "OnTalent gives university students opportunities to mentor younger learners, support youth STEM programs, assist with outreach, and help develop campus-connected involvement.",
    cta='<a class="btn btn--primary" href="mailto:info@ontalent.org?subject=University%20Student%20Involvement%20Interest">Express interest</a>'
) + f"""<section class="section">
  <div class="container">
    <div class="section__head" data-reveal><p class="kicker">Ways to get involved</p><h2>Share your skills with the next generation</h2></div>
    <div class="grid grid-4">
      <div class="card feature" data-reveal><span class="feature__icon">🧑‍🏫</span><h3>Mentor students</h3><p>Guide robotics, coding, and science learners as they build real work.</p></div>
      <div class="card feature" data-reveal data-delay="1"><span class="feature__icon">📣</span><h3>Support outreach</h3><p>Help with events, showcases, and community programs.</p></div>
      <div class="card feature" data-reveal data-delay="2"><span class="feature__icon">🌱</span><h3>Build involvement</h3><p>Help develop campus-connected ways for students to contribute.</p></div>
      <div class="card feature" data-reveal data-delay="3"><span class="feature__icon">🎓</span><h3>Grow as a leader</h3><p>Develop teaching, communication, and leadership experience.</p></div>
    </div>
  </div>
</section>

{cta_band("Interested in mentoring?", "Tell us about your interests and availability — we'd love to connect.", ['<a class="btn btn--on-dark" href="mailto:info@ontalent.org?subject=University%20Student%20Involvement%20Interest">Get in touch</a>', '<a class="btn btn--outline-dark" href="./join.html">More ways to join</a>'])}"""
write("network-university-chapters.html", "University Involvement | OnTalent",
      "University students can mentor younger learners, support outreach, and help grow campus-connected involvement with OnTalent.",
      "network.html", univ_body)

# Partners & supporters
partners_body = page_hero(
    "Partner with us to <em>open doors</em> for students",
    "Universities, employers, and community organizations help OnTalent provide real opportunities — mentorship, equipment, scholarships, and experiences.",
    cta='<a class="btn btn--primary" href="./join-sponsors-supporters.html">Explore sponsorship</a><a class="btn btn--outline-dark" href="mailto:info@ontalent.org?subject=Partnership%20Inquiry">Start a conversation</a>'
) + f"""<section class="section">
  <div class="container">
    <div class="section__head" data-reveal><p class="kicker">Ways to partner</p><h2>Many ways to make an impact</h2></div>
    <div class="grid grid-3">
      <div class="card feature" data-reveal><span class="feature__icon">🎓</span><h3>University partners</h3><p>Provide mentors, host visits, and support career exploration.</p></div>
      <div class="card feature" data-reveal data-delay="1"><span class="feature__icon">🏭</span><h3>Employers &amp; industry</h3><p>Donate expertise, equipment, scholarships, and opportunities.</p></div>
      <div class="card feature" data-reveal data-delay="2"><span class="feature__icon">🤝</span><h3>Community organizations</h3><p>Collaborate on outreach, events, and shared programming.</p></div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container center">
    <div class="section__head center" data-reveal><p class="kicker">Supported by our network</p><h2>Trusted across Ontario's STEM ecosystem</h2></div>
    <div class="logo-wall" data-reveal>
      <div class="logo-chip">Western University</div>
      <div class="logo-chip">McMaster University</div>
      <div class="logo-chip">[CUSTOMIZE: Partner]</div>
      <div class="logo-chip">[CUSTOMIZE: Partner]</div>
      <div class="logo-chip">[CUSTOMIZE: Partner]</div>
    </div>
  </div>
</section>

{cta_band("Let's build something together", "From sponsorship to in-kind support, there's a partnership that fits.", ['<a class="btn btn--on-dark" href="./join-sponsors-supporters.html">Ways to support</a>', '<a class="btn btn--outline-dark" href="mailto:info@ontalent.org?subject=Partnership%20Inquiry">Contact us</a>'])}"""
write("network-partners-supporters.html", "Partners & Supporters | OnTalent",
      "Universities, employers, and community organizations partner with OnTalent to provide mentorship, equipment, scholarships, and opportunities.",
      "network.html", partners_body)

# ============================================================ EXPERIENCES (hub)
exp_body = page_hero(
    "Experiences that turn learning into <em>memories</em>",
    "Beyond weekly programs, OnTalent students join summer camps, hackathons, showcases, and competitions that stretch their skills and confidence.",
    cta='<a class="btn btn--primary" href="./experiences-summer-camps.html">See summer camps</a>'
) + f"""<section class="section">
  <div class="container">
    <div class="grid grid-3">
      <a class="pathway" href="./experiences-summer-camps.html" data-reveal><div class="pathway__top"><span class="pathway__icon">☀️</span></div><h3>Summer Camps</h3><p class="pathway__desc">Week-long camps in AI, robotics, and science for curious young builders.</p><span class="pathway__link">Explore camps →</span></a>
      <a class="pathway" href="./experiences-ai-hackathon.html" data-reveal data-delay="1"><div class="pathway__top"><span class="pathway__icon">⚡</span></div><h3>AI Hackathon</h3><p class="pathway__desc">A fast, collaborative challenge where students build with AI in a day.</p><span class="pathway__link">Learn more →</span></a>
      <div class="pathway" data-reveal data-delay="2"><div class="pathway__top"><span class="pathway__icon">🏆</span></div><h3>Showcases &amp; Competitions</h3><p class="pathway__desc">Students present projects and compete — from FLL/FTC to coding contests.</p><span class="pathway__link note" style="color:var(--muted)">Throughout the year</span></div>
    </div>
  </div>
</section>

{cta_band("Find an experience for your student", "Camps and events fill quickly — register or join a waitlist.", ['<a class="btn btn--on-dark" href="./experiences-summer-camps.html">Summer camps</a>', '<a class="btn btn--outline-dark" href="./join-students-families.html">Students &amp; Families</a>'])}"""
write("experiences.html", "Experiences | OnTalent",
      "OnTalent experiences: summer camps, AI hackathons, showcases, and competitions that stretch students' STEM skills and confidence.",
      "experiences.html", exp_body)

# Summer camps
camps_body = page_hero(
    "Summer at <em>OnTalent</em>",
    "Week-long camps that turn summer curiosity into real building, coding, and discovery — in a supervised, mentor-supported studio.",
    tag="Limited spots remain",
    cta=f'<a class="btn btn--primary" href="{FORM_CAMP}" target="_blank" rel="noopener">Register / Join Waitlist</a>'
) + f"""<section class="section">
  <div class="container">
    <div class="section__head" data-reveal><p class="kicker">This summer</p><h2>Four camps, four adventures</h2><p class="lede mt-1">Camp C: AI Creator Studio and Camp D: MediQuest Junior are still accepting registrations. Camp A and Camp B are currently accepting waitlist registrations.</p></div>
    <div class="grid grid-2">
      <div class="program program--ai" data-reveal><h3>Camp C — AI Creator Studio</h3><p class="program__tag">Registrations open</p><ul><li>Create with AI tools and computing</li><li>Hands-on, project-based days</li><li>Mentor-supported</li></ul><a class="btn btn--primary btn--sm btn--block" href="{FORM_CAMP}" target="_blank" rel="noopener">Register for Camp C</a></div>
      <div class="program program--health" data-reveal data-delay="1"><h3>Camp D — MediQuest Junior</h3><p class="program__tag">Registrations open</p><ul><li>Hands-on science and discovery</li><li>Biomedical curiosity for younger students</li><li>Mentor-supported</li></ul><a class="btn btn--primary btn--sm btn--block" href="{FORM_CAMP}" target="_blank" rel="noopener">Register for Camp D</a></div>
      <div class="program" data-reveal data-delay="2"><h3>Camp A</h3><p class="program__tag">Waitlist</p><ul><li>[CUSTOMIZE: short description]</li><li>Accepting waitlist registrations</li></ul><a class="btn btn--ghost btn--sm btn--block" href="{FORM_CAMP}" target="_blank" rel="noopener">Join Camp A waitlist</a></div>
      <div class="program" data-reveal data-delay="3"><h3>Camp B</h3><p class="program__tag">Waitlist</p><ul><li>[CUSTOMIZE: short description]</li><li>Accepting waitlist registrations</li></ul><a class="btn btn--ghost btn--sm btn--block" href="{FORM_CAMP}" target="_blank" rel="noopener">Join Camp B waitlist</a></div>
    </div>
  </div>
</section>

{cta_band("Don't miss out", "Camps C and D are still open; A and B are taking waitlist sign-ups.", [f'<a class="btn btn--on-dark" href="{FORM_CAMP}" target="_blank" rel="noopener">Register / Join Waitlist</a>', '<a class="btn btn--outline-dark" href="./experiences.html">All experiences</a>'])}"""
write("experiences-summer-camps.html", "Summer Camps | OnTalent",
      "OnTalent summer camps: AI Creator Studio, MediQuest Junior, and more — hands-on, mentor-supported weeks for young innovators.",
      "experiences.html", camps_body)

# AI hackathon
hack_body = page_hero(
    "AI Hackathon: build something <em>in a day</em>",
    "A fast, collaborative challenge where students team up, learn with AI tools, and ship a real project — supported by mentors throughout.",
    cta='<a class="btn btn--primary" href="mailto:info@ontalent.org?subject=AI%20Hackathon%20Interest">Express interest</a>'
) + f"""<section class="section">
  <div class="container">
    <div class="section__head" data-reveal><p class="kicker">What it's like</p><h2>Learn fast, build together</h2></div>
    <div class="grid grid-3">
      <div class="card feature" data-reveal><span class="feature__icon">👥</span><h3>Team up</h3><p>Students form teams and tackle a shared challenge.</p></div>
      <div class="card feature" data-reveal data-delay="1"><span class="feature__icon">🤖</span><h3>Build with AI</h3><p>Use modern AI tools responsibly to create something real.</p></div>
      <div class="card feature" data-reveal data-delay="2"><span class="feature__icon">🎤</span><h3>Present &amp; celebrate</h3><p>Demo your project and celebrate what you made.</p></div>
    </div>
    <div class="panel mt-2" data-reveal>
      <h3>Details</h3>
      <p class="card__body">[CUSTOMIZE: dates, eligible grades, location, and cost. Add a registration link or form when available — for now, students and families can express interest by email and we'll follow up.]</p>
    </div>
  </div>
</section>

{cta_band("Want in on the next hackathon?", "Tell us you're interested and we'll share dates and details.", ['<a class="btn btn--on-dark" href="mailto:info@ontalent.org?subject=AI%20Hackathon%20Interest">Express interest</a>', '<a class="btn btn--outline-dark" href="./experiences.html">All experiences</a>'])}"""
write("experiences-ai-hackathon.html", "AI Hackathon | OnTalent",
      "The OnTalent AI Hackathon: a fast, collaborative, mentor-supported challenge where students build a real project with AI in a day.",
      "experiences.html", hack_body)

# ============================================================ IMPACT
impact_body = page_hero(
    "Our <em>impact</em>",
    "Measurable outcomes in student achievement, pathways, and community growth. (Figures shown are placeholders — confirm with current OnTalent data before publishing.)",
    cta='<a class="btn btn--primary" href="./impact-report.html">Read the impact report</a><a class="btn btn--outline-dark" href="./join-sponsors-supporters.html">Support us</a>'
) + f"""<section class="section">
  <div class="container">
    <div class="section__head" data-reveal><p class="kicker">At a glance</p><h2>This year's impact</h2></div>
    <div class="grid grid-4">
      <div class="metric" data-reveal><div class="metric__num">500+</div><div class="metric__label">Students served</div><p>Across robotics, AI, health science, and leadership.</p></div>
      <div class="metric" data-reveal data-delay="1"><div class="metric__num">92%</div><div class="metric__label">Continue in STEM</div><p>Pathway graduates pursuing further STEM study or careers.</p></div>
      <div class="metric" data-reveal data-delay="2"><div class="metric__num">100+</div><div class="metric__label">Mentors engaged</div><p>University students, professionals, and volunteers.</p></div>
      <div class="metric" data-reveal data-delay="3"><div class="metric__num">12+</div><div class="metric__label">Institutional partners</div><p>Universities, schools, employers, and community groups.</p></div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section__head" data-reveal><p class="kicker">Three-year trend</p><h2>Growing, year over year</h2></div>
    <div class="trend">
      <div data-reveal><div class="trend__year">2023–2024</div><div class="trend__stat">280 students</div><div class="trend__bar" style="width:56%"></div><p class="trend__note">Foundation year · 3 core pathways</p></div>
      <div data-reveal data-delay="1"><div class="trend__year">2024–2025</div><div class="trend__stat">410 students</div><div class="trend__bar" style="width:82%"></div><p class="trend__note">Expanded summer camps</p></div>
      <div data-reveal data-delay="2"><div class="trend__year">2025–2026</div><div class="trend__stat">500+ students</div><div class="trend__bar" style="width:100%"></div><p class="trend__note">New partnerships · 4+ pathways</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section__head" data-reveal><p class="kicker">Student stories</p><h2>From curiosity to capability</h2></div>
    <div class="grid grid-3">
      <article class="card story" data-reveal><div class="story__media" style="background:linear-gradient(135deg,var(--brand),var(--health))"></div><div class="story__pad"><h3>Sarah — curious to competitive</h3><p class="story__meta">Grade 10 · Robotics</p><p class="story__quote">"I started with zero experience. Now I lead my FTC team and mentor younger students."</p><p class="story__outcome"><strong>Outcome:</strong> Provincial championships; eyeing engineering at McMaster.</p></div></article>
      <article class="card story" data-reveal data-delay="1"><div class="story__media" style="background:linear-gradient(135deg,var(--ai),var(--health))"></div><div class="story__pad"><h3>Priya — discovering medicine</h3><p class="story__meta">Grade 9 · MediQuest</p><p class="story__quote">"MediQuest showed me the real science behind diagnosis and treatment."</p><p class="story__outcome"><strong>Outcome:</strong> Pre-AP chemistry &amp; biology; planning pre-med.</p></div></article>
      <article class="card story" data-reveal data-delay="2"><div class="story__media" style="background:linear-gradient(135deg,var(--robotics),var(--leadership))"></div><div class="story__pad"><h3>Marcus — student to leader</h3><p class="story__meta">Grade 11 · Multi-pathway</p><p class="story__quote">"I tried robotics, then AI. Now I mentor both teams and help others get started."</p><p class="story__outcome"><strong>Outcome:</strong> Student ambassador; leadership scholarships.</p></div></article>
    </div>
    <p class="note center mt-2" data-reveal>Stories are illustrative examples — replace with real, consented student stories and photos before publishing.</p>
  </div>
</section>

{cta_band("Help us scale this impact", "Every gift helps us reach more students and build bigger opportunities.", ['<a class="btn btn--on-dark" href="./join-sponsors-supporters.html">Explore ways to support</a>', '<a class="btn btn--outline-dark" href="./impact-report.html">Read the report</a>'])}"""
write("impact.html", "Impact | OnTalent",
      "OnTalent's impact: students served, STEM continuation, mentors engaged, partnerships, and student success stories.",
      "impact.html", impact_body)

# Impact report (long form)
report_body = page_hero(
    "Impact Report",
    "A closer look at how OnTalent turns curiosity into capability — and how every contribution is put to work. (Placeholder figures; confirm before publishing.)",
    tag="Annual overview",
    cta='<a class="btn btn--primary" href="#" >[CUSTOMIZE: Download PDF]</a><a class="btn btn--outline-dark" href="./join-sponsors-supporters.html">Support us</a>'
) + f"""<section class="section">
  <div class="container-narrow">
    <div data-reveal>
      <p class="kicker">From the team</p>
      <h2>A year of growth</h2>
      <p class="lede mt-1">This year, OnTalent welcomed more students than ever into hands-on robotics, computing, and science — supported by mentors who believe in their potential and partners who open doors. [CUSTOMIZE: add a short letter from your Executive Director.]</p>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section__head" data-reveal><p class="kicker">By the numbers</p><h2>What we achieved</h2></div>
    <div class="grid grid-4">
      <div class="metric" data-reveal><div class="metric__num">500+</div><div class="metric__label">Students served</div></div>
      <div class="metric" data-reveal data-delay="1"><div class="metric__num">92%</div><div class="metric__label">Continue in STEM</div></div>
      <div class="metric" data-reveal data-delay="2"><div class="metric__num">100+</div><div class="metric__label">Mentors</div></div>
      <div class="metric" data-reveal data-delay="3"><div class="metric__num">12+</div><div class="metric__label">Partners</div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section__head" data-reveal><p class="kicker">Program highlights</p><h2>Where the impact happened</h2></div>
    <div class="grid grid-3">
      <div class="card feature" data-reveal><span class="feature__icon">🤖</span><h3>Robotics</h3><p>FLL and FTC teams built, competed, and grew leaders. [CUSTOMIZE]</p></div>
      <div class="card feature" data-reveal data-delay="1"><span class="feature__icon">🧠</span><h3>AI &amp; Computing</h3><p>CPC students developed real algorithmic skill. [CUSTOMIZE]</p></div>
      <div class="card feature" data-reveal data-delay="2"><span class="feature__icon">⚕️</span><h3>MediQuest</h3><p>Students strengthened science foundations. [CUSTOMIZE]</p></div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="split">
      <div data-reveal>
        <p class="kicker">Financial stewardship</p>
        <h2>Where funding goes</h2>
        <p class="lede mt-1">We are committed to transparency. The breakdown below is an example — replace with audited figures.</p>
      </div>
      <div class="spend" data-reveal data-delay="1">
        <div class="spend__row"><div class="spend__label">65% — Program delivery</div><div class="spend__bar" style="width:65%;background:var(--health)"></div></div>
        <div class="spend__row"><div class="spend__label">20% — Studio &amp; operations</div><div class="spend__bar" style="width:20%;background:var(--brand)"></div></div>
        <div class="spend__row"><div class="spend__label">15% — Development &amp; fundraising</div><div class="spend__bar" style="width:15%;background:var(--leadership)"></div></div>
      </div>
    </div>
  </div>
</section>

{cta_band("Be part of next year's story", "Your support helps more students begin, build, and lead.", ['<a class="btn btn--on-dark" href="./join-sponsors-supporters.html">Ways to support</a>', '<a class="btn btn--outline-dark" href="./impact.html">Back to impact</a>'])}"""
write("impact-report.html", "Impact Report | OnTalent",
      "OnTalent's impact report: program highlights, outcomes, and financial stewardship for the year.",
      "impact.html", report_body)

# ============================================================ ABOUT
about_body = page_hero(
    "About <em>OnTalent</em>",
    "Our mission, leadership, and commitment to youth innovation across Ontario.",
) + f"""<section class="section">
  <div class="container">
    <div class="section__head" data-reveal><p class="kicker">Our foundation</p><h2>What drives us</h2></div>
    <div class="grid grid-3">
      <div class="card" data-reveal><h3>Mission</h3><p class="card__body">To empower Ontario youth to discover their potential in STEM, build real capabilities through hands-on learning, and grow into confident leaders and innovators.</p></div>
      <div class="card" data-reveal data-delay="1"><h3>Vision</h3><p class="card__body">A generation of young innovators, equipped with STEM skills and the confidence to shape the future.</p></div>
      <div class="card" data-reveal data-delay="2"><h3>Values</h3><ul class="card__body"><li><strong>Student-centered</strong> — outcomes first</li><li><strong>Hands-on</strong> — learning by building</li><li><strong>Inclusive</strong> — removing barriers</li><li><strong>Community</strong> — powered by mentors &amp; partners</li></ul></div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section__head" data-reveal><p class="kicker">Our team</p><h2>The people behind OnTalent</h2></div>
    <div class="grid grid-3">
      <div class="card member" data-reveal><div class="member__avatar"></div><h3>[CUSTOMIZE: Name]</h3><p class="role-title">Executive Director</p><p>[CUSTOMIZE: short bio on background and passion for youth STEM.]</p></div>
      <div class="card member" data-reveal data-delay="1"><div class="member__avatar"></div><h3>[CUSTOMIZE: Name]</h3><p class="role-title">Program Director</p><p>[CUSTOMIZE: background and role in student programs.]</p></div>
      <div class="card member" data-reveal data-delay="2"><div class="member__avatar"></div><h3>[CUSTOMIZE: Name]</h3><p class="role-title">Community &amp; Partnerships</p><p>[CUSTOMIZE: background and partnerships role.]</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section__head" data-reveal><p class="kicker">Governance</p><h2>Board of Directors</h2><p class="lede mt-1">OnTalent is governed by dedicated leaders from education, industry, and community.</p></div>
    <div class="board-grid">
      <div class="board-item" data-reveal><strong>[CUSTOMIZE: Name]</strong><span>[Title · Organization]</span></div>
      <div class="board-item" data-reveal><strong>[CUSTOMIZE: Name]</strong><span>[Title · Organization]</span></div>
      <div class="board-item" data-reveal><strong>[CUSTOMIZE: Name]</strong><span>[Title · Organization]</span></div>
      <div class="board-item" data-reveal><strong>[CUSTOMIZE: Name]</strong><span>[Title · Organization]</span></div>
      <div class="board-item" data-reveal><strong>[CUSTOMIZE: Name]</strong><span>[Title · Organization]</span></div>
      <div class="board-item" data-reveal><strong>[CUSTOMIZE: Name]</strong><span>[Title · Organization]</span></div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section__head" data-reveal><p class="kicker">Legal &amp; registration</p><h2>Transparency you can verify</h2></div>
    <div class="grid grid-3">
      <div class="card" data-reveal><h3>CRA charity</h3><p class="card__body"><strong>Charity #:</strong> [CUSTOMIZE]<br><strong>Status:</strong> Registered charitable organization<br><strong>Receipts:</strong> Available for all donations</p><a href="https://www.canada.ca/en/revenue-agency/services/charities-giving/charities.html" target="_blank" rel="noopener">Verify with CRA →</a></div>
      <div class="card" data-reveal data-delay="1"><h3>Location</h3><p class="card__body">OnTalent Lab | Western STEM Studio<br>Western University Discovery Park<br>999 Collip Circle<br>London, ON N6G 0J3, Canada</p></div>
      <div class="card" data-reveal data-delay="2"><h3>Contact</h3><p class="card__body"><strong>Email:</strong> <a href="mailto:info@ontalent.org">info@ontalent.org</a><br><strong>Phone:</strong> [CUSTOMIZE]</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="split">
      <div data-reveal>
        <p class="kicker">Financial transparency</p>
        <h2>Where your donation goes</h2>
        <p class="lede mt-1">We're committed to using every gift well. The split below is an example — replace with audited figures and link your reports.</p>
        <div class="grid grid-3 mt-1">
          <a class="doc-link" href="#" data-reveal><span class="doc-icon">📄</span><span class="doc-title">[Annual Report]</span></a>
          <a class="doc-link" href="#" data-reveal data-delay="1"><span class="doc-icon">📊</span><span class="doc-title">[Audited Financials]</span></a>
          <a class="doc-link" href="#" data-reveal data-delay="2"><span class="doc-icon">📋</span><span class="doc-title">[T1236 / CRA]</span></a>
        </div>
      </div>
      <div class="spend" data-reveal data-delay="1">
        <div class="spend__row"><div class="spend__label">65% — Direct program delivery</div><div class="spend__bar" style="width:65%;background:var(--health)"></div><p class="spend__note">Instruction, mentorship, materials</p></div>
        <div class="spend__row"><div class="spend__label">20% — Studio &amp; operations</div><div class="spend__bar" style="width:20%;background:var(--brand)"></div><p class="spend__note">Space, equipment, technology</p></div>
        <div class="spend__row"><div class="spend__label">15% — Development &amp; fundraising</div><div class="spend__bar" style="width:15%;background:var(--leadership)"></div><p class="spend__note">Grants, donor relations, partnerships</p></div>
      </div>
    </div>
  </div>
</section>

{newsletter("I'm interested in:", [("Impact & Mission","Impact"),("Giving & Sponsorship","Donor")])}"""
write("about.html", "About | OnTalent",
      "Learn about OnTalent's mission, vision, values, leadership, governance, and financial transparency.",
      "about.html", about_body)

# ============================================================ JOIN (hub)
join_body = page_hero(
    "Find your place in the <em>OnTalent network</em>",
    "Student, parent, university mentor, volunteer, educator, sponsor, or community partner — there's a clear way for you to get involved.",
    cta='<a class="btn btn--primary" href="./join-students-families.html">Register for programs</a><a class="btn btn--outline-dark" href="mailto:info@ontalent.org?subject=OnTalent%20Program%20Question">Ask a question</a>'
) + f"""<section class="section">
  <div class="container">
    <div class="section__head" data-reveal><p class="kicker">Choose your path</p><h2>Ways to get involved</h2></div>
    <div class="grid grid-4">
      <div class="card role" data-reveal><span class="role__icon">🎓</span><h3>Students &amp; Families</h3><p>Explore camps, programs, pathways, age ranges, and next steps.</p><a class="btn btn--primary btn--sm" href="./join-students-families.html">Start here</a></div>
      <div class="card role" data-reveal data-delay="1"><span class="role__icon">🤝</span><h3>Mentors &amp; Volunteers</h3><p>Support workshops, events, camps, teams, and showcases.</p><a class="btn btn--ghost btn--sm" href="#mentors-volunteers">Get involved</a></div>
      <div class="card role" data-reveal data-delay="2"><span class="role__icon">🎓</span><h3>University Students</h3><p>Mentor younger learners and help grow campus involvement.</p><a class="btn btn--ghost btn--sm" href="./network-university-chapters.html">Explore</a></div>
      <div class="card role" data-reveal data-delay="3"><span class="role__icon">💛</span><h3>Partners &amp; Supporters</h3><p>Start a sponsorship, grant, or collaboration conversation.</p><a class="btn btn--ghost btn--sm" href="./join-sponsors-supporters.html">Support us</a></div>
    </div>
  </div>
</section>

<section class="section section--alt" id="mentors-volunteers">
  <div class="container">
    <div class="section__head" data-reveal><p class="kicker">Mentors &amp; volunteers</p><h2>Help students build confidence, skills, and leadership</h2><p class="lede mt-1">Mentors and volunteers support OnTalent through workshops, events, camps, robotics teams, showcases, and leadership development.</p></div>
    <div class="grid grid-4">
      <div class="card feature" data-reveal><span class="feature__icon">🧑‍🏫</span><h3>Mentor projects</h3><p>Guide students as they build, test, and present real work.</p></div>
      <div class="card feature" data-reveal data-delay="1"><span class="feature__icon">🎟️</span><h3>Support events</h3><p>Help students share learning at showcases and community events.</p></div>
      <div class="card feature" data-reveal data-delay="2"><span class="feature__icon">🧰</span><h3>Volunteer with programs</h3><p>Support camps, workshops, and project-based learning.</p></div>
      <div class="card feature" data-reveal data-delay="3"><span class="feature__icon">🌟</span><h3>Grow young leaders</h3><p>Encourage teamwork, confidence, and peer mentorship.</p></div>
    </div>
    <div class="btn-row mt-2" data-reveal><a class="btn btn--primary" href="mailto:info@ontalent.org?subject=Mentor%20%2F%20Volunteer%20Interest">Volunteer with us</a></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section__head" data-reveal><p class="kicker">How joining works</p><h2>Role → Connect → Path → Grow</h2></div>
    <div class="steps">
      <div class="step" data-reveal><span class="step__num">01</span><h3>Choose your role</h3><p>Find the right entry point for your interests and experience.</p></div>
      <div class="step" data-reveal data-delay="1"><span class="step__num">02</span><h3>Connect with us</h3><p>Share goals, availability, questions, or partnership ideas.</p></div>
      <div class="step" data-reveal data-delay="2"><span class="step__num">03</span><h3>Join the right path</h3><p>Enter a program, volunteer role, or support conversation.</p></div>
      <div class="step" data-reveal data-delay="3"><span class="step__num">04</span><h3>Grow with the network</h3><p>Build confidence, mentor, contribute, and expand opportunity.</p></div>
    </div>
  </div>
</section>

{newsletter("Not ready to join yet? Stay connected:", [("Programs & Registration","Family"),("Volunteer & Mentoring","Mentor"),("Impact & Giving","Donor")])}"""
write("join.html", "Join | OnTalent",
      "Find your place in the OnTalent network — as a student, family, mentor, volunteer, university student, sponsor, or partner.",
      "join.html", join_body)

# Join — students & families
families_body = page_hero(
    "Students &amp; Families",
    "Everything you need to choose a program, understand fees and placement, and take the next step — written for parents.",
    cta='<a class="btn btn--primary" href="#programs">See current programs</a>'
) + f"""<section class="section">
  <div class="container">
    <div class="section__head" data-reveal><p class="kicker">How it works</p><h2>Explore → Choose → Register → Grow</h2></div>
    <div class="steps">
      <div class="step" data-reveal><span class="step__num">01</span><h3>Review programs</h3><p>Explore camps, fall–winter options, and pathway entry points.</p></div>
      <div class="step" data-reveal data-delay="1"><span class="step__num">02</span><h3>Choose a fit</h3><p>Compare age ranges, interests, schedules, and readiness.</p></div>
      <div class="step" data-reveal data-delay="2"><span class="step__num">03</span><h3>Register</h3><p>Complete the form; placement and payment follow review.</p></div>
      <div class="step" data-reveal data-delay="3"><span class="step__num">04</span><h3>Keep growing</h3><p>Move toward projects, mentorship, showcases, and leadership.</p></div>
    </div>
  </div>
</section>

<section class="section section--alt" id="programs">
  <div class="container">
    <div class="section__head" data-reveal><p class="kicker">Current programs</p><h2>Fall–Winter 2026–2027</h2></div>
    <div class="grid grid-3">
      <div class="program program--robotics" data-reveal><h3>Robotics FLL / FTC</h3><p class="program__tag">Grades 3–12</p><ul><li>Sep 2026 – Jan 2027</li><li>FLL: Thu 6:30–8:00 PM · Sun 1:30–3:00 PM</li><li>FTC: Thu 7:30–9:00 PM · Sun 2:30–4:00 PM</li></ul><a class="btn btn--primary btn--sm btn--block" href="{FORM_ROBOTICS}" target="_blank" rel="noopener">Register</a></div>
      <div class="program program--ai" data-reveal data-delay="1"><h3>CPC Coding</h3><p class="program__tag">Grades 6+ / 7+</p><ul><li>Python Junior (6+), C++ Intermediate (7+)</li><li>Tuesdays, Sep 22 – Apr 20, 2027</li></ul><a class="btn btn--primary btn--sm btn--block" href="{FORM_CPC}" target="_blank" rel="noopener">Register</a></div>
      <div class="program program--health" data-reveal data-delay="2"><h3>MediQuest</h3><p class="program__tag">Grades 8–10</p><ul><li>Chemistry: Sat 9:00–10:30 AM</li><li>Biology: Sat 10:30 AM–12:00 PM</li><li>Sep 19 – Apr 17, 2027</li></ul><a class="btn btn--primary btn--sm btn--block" href="{FORM_MEDIQUEST}" target="_blank" rel="noopener">Register</a></div>
    </div>
    <div class="panel mt-2" data-reveal>
      <h3>Summer camps</h3>
      <p class="card__body">Camp C (AI Creator Studio) and Camp D (MediQuest Junior) are accepting registrations; Camps A and B are taking waitlist sign-ups.</p>
      <div class="btn-row mt-1"><a class="btn btn--ghost btn--sm" href="./experiences-summer-camps.html">See camp details</a><a class="btn btn--ghost btn--sm" href="{FORM_CAMP}" target="_blank" rel="noopener">Register / waitlist</a></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="split">
      <div data-reveal>
        <p class="kicker">Fees &amp; support</p>
        <h2>Credits and bursaries</h2>
        <p class="lede mt-1">We work to keep programs accessible.</p>
        <ul class="checklist mt-1">
          <li>Current-family and Western-affiliated credits</li>
          <li>Sibling and referral credits</li>
          <li>Limited needs-based bursaries</li>
          <li>Placement &amp; payment confirmed after review</li>
        </ul>
      </div>
      <div class="panel" data-reveal data-delay="1">
        <h3>Questions before you register?</h3>
        <p class="card__body">We're happy to help you find the right fit for your child.</p>
        <div class="btn-row mt-1"><a class="btn btn--primary btn--sm" href="mailto:info@ontalent.org?subject=Program%20Question">Ask a question</a></div>
      </div>
    </div>
  </div>
</section>

{cta_band("Ready to register?", "Choose a program above, or reach out and we'll guide you.", [f'<a class="btn btn--on-dark" href="{FORM_ROBOTICS}" target="_blank" rel="noopener">Register now</a>', '<a class="btn btn--outline-dark" href="./pathways.html">Explore pathways</a>'])}"""
write("join-students-families.html", "Students & Families | OnTalent",
      "A parent-friendly guide to OnTalent programs: camps, fall–winter options, age ranges, fees, credits, and registration next steps.",
      "join.html", families_body)

# Join — sponsors & supporters
spon_body = page_hero(
    "Support the next generation of <em>innovators</em>",
    "Your support gives Ontario youth real studio space, mentorship, and pathways into STEM. (Tiers and figures are examples — confirm before publishing.)",
    cta='<a class="btn btn--primary" href="#tiers">Ways to give</a><a class="btn btn--outline-dark" href="mailto:info@ontalent.org?subject=Sponsorship%20Inquiry">Talk to us</a>'
) + f"""<section class="section">
  <div class="container">
    <div class="section__head" data-reveal><p class="kicker">Why support us</p><h2>Your gift goes further here</h2></div>
    <div class="grid grid-4">
      <div class="card feature" data-reveal><span class="feature__icon">🎯</span><h3>Direct impact</h3><p>65% of funds go straight to programs and mentorship.</p></div>
      <div class="card feature" data-reveal data-delay="1"><span class="feature__icon">📊</span><h3>Measurable outcomes</h3><p>92% continue in STEM, with transparent reporting.</p></div>
      <div class="card feature" data-reveal data-delay="2"><span class="feature__icon">🤝</span><h3>Trusted network</h3><p>Supported by universities and leading employers.</p></div>
      <div class="card feature" data-reveal data-delay="3"><span class="feature__icon">💡</span><h3>Innovation hub</h3><p>A real studio where students build, test, and lead.</p></div>
    </div>
  </div>
</section>

<section class="section section--alt" id="tiers">
  <div class="container">
    <div class="section__head" data-reveal><p class="kicker">Ways to give</p><h2>Choose a level</h2><p class="lede mt-1">Every gift is tax-receiptable.</p></div>
    <div class="grid grid-4">
      <div class="tier tier--ai" data-reveal><h3 class="tier__name">Friend</h3><p class="tier__range">$100–$500</p><ul class="tier__list"><li>Full tax receipt</li><li>Annual supporters list</li><li>Quarterly impact updates</li></ul><a class="btn btn--ghost btn--sm btn--block" href="#">[Donate link]</a></div>
      <div class="tier tier--featured" data-reveal data-delay="1"><span class="tier__tag">Popular</span><h3 class="tier__name">Program Builder</h3><p class="tier__range">$501–$2,500</p><ul class="tier__list"><li>Tax receipt</li><li>Annual showcase invite</li><li>Pathway impact report</li><li>Listing in annual report</li></ul><a class="btn btn--primary btn--sm btn--block" href="#">[Donate link]</a></div>
      <div class="tier tier--health" data-reveal data-delay="2"><h3 class="tier__name">Innovation Partner</h3><p class="tier__range">$2,501–$10,000</p><ul class="tier__list"><li>All prior benefits</li><li>VIP event invitations</li><li>Website &amp; program recognition</li><li>Impact briefings 2×/year</li></ul><a class="btn btn--ghost btn--sm btn--block" href="#">[Donate link]</a></div>
      <div class="tier tier--leadership" data-reveal data-delay="3"><h3 class="tier__name">Founding Visionary</h3><p class="tier__range">$10,000+</p><ul class="tier__list"><li>All prior benefits</li><li>Naming opportunity</li><li>Leadership circle</li><li>Dedicated contact</li></ul><a class="btn btn--ghost btn--sm btn--block" href="mailto:info@ontalent.org?subject=Founding%20Visionary">Contact us</a></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section__head" data-reveal><p class="kicker">Corporate &amp; institutional</p><h2>Sponsorship that builds your brand</h2></div>
    <div class="grid grid-3">
      <div class="card" data-reveal><h3>Program Sponsor</h3><p class="card__meta">$5,000–$15,000 / yr</p><ul class="card__body"><li>Logo on materials, site, signage</li><li>Branded team gear</li><li>Showcase recognition</li><li>Employee volunteering</li></ul></div>
      <div class="card" data-reveal data-delay="1"><h3>Pathway Partner</h3><p class="card__meta">$15,000–$40,000 / yr</p><ul class="card__body"><li>All Program Sponsor benefits</li><li>Named scholarship</li><li>Quarterly briefings</li><li>Featured in report &amp; media</li></ul></div>
      <div class="card" data-reveal data-delay="2"><h3>Founding Partner</h3><p class="card__meta">$40,000+ / yr</p><ul class="card__body"><li>All Pathway Partner benefits</li><li>Naming rights</li><li>Advisory involvement</li><li>Joint PR campaigns</li></ul></div>
    </div>
    <div class="btn-row center mt-2" data-reveal><a class="btn btn--primary" href="mailto:info@ontalent.org?subject=Corporate%20Sponsorship">Start a sponsorship conversation</a></div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="section__head center" data-reveal><p class="kicker">In-kind &amp; alternative</p><h2>More ways to help</h2></div>
    <div class="grid grid-4">
      <div class="card feature" data-reveal><span class="feature__icon">🤝</span><h3>Mentorship</h3><p>Mentor a team, lead a workshop, or judge a showcase.</p><a href="mailto:info@ontalent.org?subject=Mentorship">Get involved →</a></div>
      <div class="card feature" data-reveal data-delay="1"><span class="feature__icon">🛠️</span><h3>Equipment</h3><p>Donate kits, computers, software, or tools.</p><a href="mailto:info@ontalent.org?subject=Equipment%20Donation">Discuss →</a></div>
      <div class="card feature" data-reveal data-delay="2"><span class="feature__icon">🏢</span><h3>Space</h3><p>Host workshops, field trips, or events.</p><a href="mailto:info@ontalent.org?subject=Facility%20Partnership">Explore →</a></div>
      <div class="card feature" data-reveal data-delay="3"><span class="feature__icon">📚</span><h3>Expertise</h3><p>Teach a class or run a career panel.</p><a href="mailto:info@ontalent.org?subject=Expertise%20Offer">Share →</a></div>
    </div>
  </div>
</section>

{cta_band("Ready to make an impact?", "From a one-time gift to a founding partnership, your support changes lives.", ['<a class="btn btn--on-dark" href="mailto:info@ontalent.org?subject=I%20want%20to%20support%20OnTalent">Talk to our team</a>', '<a class="btn btn--outline-dark" href="./impact.html">See our impact</a>'])}"""
write("join-sponsors-supporters.html", "Support OnTalent | Sponsorship & Giving",
      "Support OnTalent through donations, corporate sponsorships, and in-kind giving. 65% of funds go directly to student programs.",
      "join.html", spon_body)

# ============================================================ 404
notfound = """<section class="page-hero" style="min-height:70vh;display:flex;align-items:center">
  <div class="page-hero__inner center" style="margin-inline:auto">
    <h1 class="page-hero__title" style="font-size:clamp(4rem,12vw,7rem);margin-inline:auto">404</h1>
    <p class="page-hero__lede" style="margin-inline:auto">The page you're looking for doesn't exist or has moved. Let's get you back on track.</p>
    <div class="btn-row center mt-2">
      <a class="btn btn--primary" href="./index.html">Return home</a>
      <a class="btn btn--outline-dark" href="./pathways.html">Explore pathways</a>
    </div>
  </div>
</section>"""
with open(os.path.join(OUT, "404.html"), "w") as f:
    f.write(head("Page Not Found | OnTalent", "Page not found.", None) + notfound + FOOTER)
print("wrote 404.html")

print("DONE")
