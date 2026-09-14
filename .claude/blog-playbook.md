# HydroBlox Blog Playbook

This is the single source of truth for writing and publishing one blog post. A new
post must be **indistinguishable in markup** from the 55 existing posts in `/blog`.
Follow this file exactly. Also obey `../CLAUDE.md` (brand voice + legal claim rules) —
those rules are non-negotiable and this playbook does not override them.

The site is **static HTML, no build step**. It is git-linked to Netlify: a push to
`main` auto-deploys. There is no framework, no bundler, no dependencies. Never add any.

---

## 1. Audience & voice (specifics, not adjectives)

**Who reads this:** the people who specify or buy subsurface drainage — homeowners with
wet yards and failed French drains; commercial property managers and HOAs; municipal
public-works and stormwater engineers; golf course superintendents; sports-turf and
grounds managers; civil/site engineers and architects; farmers and growers; solar
developers. Most arrive from a search like "how to fix a yard that won't drain" or
"French drain alternative" or "athletic field drainage." They want the problem solved
permanently, and they are comparing HydroBlox against gravel-and-pipe systems.

**Voice (copy the cadence of real posts):**
- Short declarative sentences. Numbers over adjectives. No exclamation points.
- Name the villain: gravel that clogs, geotextile fabric that blinds, the 1% slope a
  gravity system needs, the crushed perforated pipe, the every-few-years re-dig.
- HydroBlox is **pressure-fed** drainage: water moves plank-to-plank by hydrostatic
  pressure, so it works on **0.0% slope / level ground**. There is **nothing to clog**
  (no aggregate, no fabric). Recycled content is the *mechanism*, not a virtue.
- Banned words (from CLAUDE.md): "innovative," "seamless," "hassle-free," "world's most
  advanced," any unsubstantiated superlative. Banned claims: "never clogs / never fails"
  (use "nothing to clog"), "federally approved," "NPDES/MS4 certified/compliant" (use
  "supports NPDES / MS4 permit documentation"). Age is **18 years**, always. Do not
  invent DOT/rail approvals, TSS-removal numbers, named projects, or solar spacing —
  those are `[SOURCE NEEDED]` and blocked until Ed signs off.
- **Verified specs you may use:** 40,000 lbs/ft² compression · 14.25 gal/min flow per 40"
  plank · 0.0% slope · 100% recycled film · 25+ year life expectancy · sold via Home
  Depot Pro nationwide + regional distributors (US, Canada, Puerto Rico) · 724-719-2660.

**Length & shape:** 700–1,100 words. One `<h1>` (the title). 4–7 `<h2>` sections. Short
paragraphs. Use `<ul><li>` for comparisons/lists and one `<blockquote>` for the money
line, exactly as existing posts do. National-generic — never tie claims to one state or
region (say "heavy clay soils," "wet climates," "on level sites," not a specific metro).

---

## 2. The exact post template

Copy the structure of a real post **byte-for-byte** and change only the marked fields.
The canonical reference is [`blog/hydroblox-vs-french-drains.html`](../blog/hydroblox-vs-french-drains.html).

**Rules that keep markup identical:**
- The `<nav class="site-nav">` + `<div class="mob-nav">` block, the `<footer>` block, and
  the closing `<script>` block are **copied verbatim from any existing `/blog/*.html`
  post** (they all match). Do **not** hand-write or "improve" them. Copy, don't compose.
- All asset/link paths from a post use the `../` prefix (posts live one level deep in
  `/blog`). Sibling blog posts are linked with a bare filename (no `../`), e.g.
  `href="tee-box-drainage.html"`.
- If existing posts ever gain an analytics/pixel/tracking block in `<head>` or before
  `</body>`, copy it **verbatim** too. (As of now there is none — do not add one.)

### 2a. `<head>` — fill the `{{FIELDS}}`, keep everything else identical

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{TITLE_TAG}}</title>
<meta name="description" content="{{META_DESCRIPTION}}">
<link rel="canonical" href="https://www.hydroblox.com/blog/{{SLUG}}">
<meta name="robots" content="index, follow">
<meta property="og:type" content="article">
<meta property="og:title" content="{{TITLE_TAG}}">
<meta property="og:description" content="{{META_DESCRIPTION}}">
<meta property="og:url" content="https://www.hydroblox.com/blog/{{SLUG}}">
<meta property="og:image" content="https://www.hydroblox.com/img/hydroblox-social.jpg">
<meta property="og:site_name" content="HydroBlox">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{{TITLE_TAG}}">
<meta name="twitter:description" content="{{META_DESCRIPTION}}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../css/site.css">
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "BlogPosting", "headline": "{{HEADLINE}}", "description": "{{META_DESCRIPTION}}", "datePublished": "{{ISO_DATE}}", "dateModified": "{{ISO_DATE}}", "author": {"@type": "Organization", "name": "HydroBlox", "url": "https://www.hydroblox.com/"}, "publisher": {"@type": "Organization", "name": "HydroBlox", "url": "https://www.hydroblox.com/"}, "mainEntityOfPage": {"@type": "WebPage", "@id": "https://www.hydroblox.com/blog/{{SLUG}}"}}</script>
<script type="application/ld+json">{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.hydroblox.com/"}, {"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://www.hydroblox.com/blog"}, {"@type": "ListItem", "position": 3, "name": "{{HEADLINE}}", "item": "https://www.hydroblox.com/blog/{{SLUG}}"}]}</script>
</head>
```

`{{HEADLINE}}` = the article title WITHOUT the ` | HydroBlox` suffix. `{{TITLE_TAG}}` =
`{{HEADLINE}} | HydroBlox`. `{{ISO_DATE}}` = today, `YYYY-MM-DD`.

### 2b. `<body>` skeleton (between the verbatim nav and the verbatim footer)

```html
<body>
<!-- >>> paste the verbatim <nav class="site-nav"> ... </nav> and <div class="mob-nav"> ... </div> here <<< -->
<div class="post-header"><div class="post-header-inner">
 <a href="../blog.html" class="post-back">← All articles</a>
 <p class="label">{{CATEGORY}}</p>
 <h1>{{HEADLINE}}</h1>
 <div class="post-meta"><span>{{DISPLAY_DATE}}</span><span>{{N}} min read</span></div>
</div></div>
<div class="post-body">
<p>{{Opening — name the problem in the reader's words.}}</p>
<h2>{{Section}}</h2>
<p>...</p>
<ul><li><strong>...:</strong> ...</li> ... </ul>
<blockquote><p>{{The single sharpest line of the piece.}}</p></blockquote>
</div>
<div class="post-cta">
 <h3>Have a wet site to solve?</h3>
 <p>Send us the site and the problem. We'll tell you whether HydroBlox is the right fit and get you the data your drawing set needs.</p>
 <div class="btn-sky-lg" style="cursor:pointer;display:inline-block" onclick="location.href='../contact.html'">Get in Touch</div>
</div>
<section class="related-posts"><div class="related-inner"><p class="label">Keep Reading</p><h2>Related <em>articles.</em></h2><div class="blog-grid">{{THREE_RELATED_CARDS}}</div></div></section>
<!-- >>> paste the verbatim <footer> ... </footer> and the closing <script> ... </script> here <<< -->
</body>
</html>
```

- `{{DISPLAY_DATE}}` = today as `Month D, YYYY` (e.g. `September 14, 2026`).
- `{{N}} min read` = round(words ÷ 200), typically 6–9.
- Each related card (pick 3, prefer same/adjacent category, real posts that exist):
  `<a href="{{sibling-slug}}.html" class="blog-card"><div class="blog-card-img">{{EMOJI}}</div><div class="blog-card-body"><p class="blog-card-tag">{{CATEGORY}}</p><h3>{{Their title}}</h3><span class="blog-card-date">{{Their date}}</span></div></a>`

### 2c. Category → emoji (use one of these; match the topic)

| Category | Emoji | Category | Emoji |
|---|---|---|---|
| Residential | 🏡 | Sustainability | ♻️ |
| Commercial | 🏢 | Engineering | 🔬 |
| Municipal | 🏛️ | Agriculture | 🌾 |
| Golf | ⛳ | Solar | ☀️ |
| Sports | 🏟️ | Design | 📐 |
| Guide | 📘 | Comparison | ⚖️ |

Pick the single best-fit category. Do not invent new category/emoji pairs.

---

## 3. File naming + URL pattern

- Slug: lowercase kebab-case, words from the topic, no dates, no stop-word padding,
  `.html` extension. Example: `pickleball-tennis-court-drainage.html`.
- File path: `blog/{{slug}}.html`. Canonical/OG URL: `https://www.hydroblox.com/blog/{{slug}}`
  (no `.html` — Netlify serves the pretty URL).
- The slug must be unique. Check `blog/` first; if a near-duplicate exists, pick the next
  undone topic instead.

---

## 4. Ordered checklist — files to edit per post (exactly these, nothing else)

1. **Create** `blog/{{slug}}.html` from the template above (verbatim nav/footer/script).
2. **`blog.html`** — prepend ONE card as the FIRST child of the main grid
   `<div class="blog-grid reveal" ...>` inside `<div class="mpage" id="page-blog">`
   (newest first). Card format (note the extra `<p>` teaser that index cards have and
   related cards don't):
   `<a href="blog/{{slug}}.html" class="blog-card"><div class="blog-card-img">{{EMOJI}}</div><div class="blog-card-body"><p class="blog-card-tag">{{CATEGORY}}</p><h3>{{HEADLINE}}</h3><p>{{1-sentence teaser, ~110 chars, may end with …}}</p><span class="blog-card-date">{{DISPLAY_DATE}}</span></div></a>`
   Do **not** edit the `<span data-guide-count>` number — it is computed by JavaScript
   from the cards at runtime (see `/*guidecount*/` in blog.html). Touch nothing else on
   this page.
3. **`sitemap.xml`** — add one line among the existing `/blog/` entries (right after the
   `<loc>.../blog</loc>` line is fine):
   `  <url><loc>https://www.hydroblox.com/blog/{{slug}}</loc><changefreq>monthly</changefreq><priority>0.6</priority></url>`
4. **`.claude/blog-topics.md`** — mark the topic you used with a `[done] ` prefix, and
   refill the queue if needed (see §7).

Do not create or edit any other file. There is no RSS feed and no posts JSON manifest —
do not invent one.

---

## 5. SEO rules (every post)

- `<title>` ≤ 60 characters, including ` | HydroBlox`. Front-load the primary keyword.
- Meta description 150–160 characters, unique, benefit-led, matches the search intent.
  Reuse it verbatim in og:description and twitter:description (as existing posts do).
- Exactly one `<h1>` (the headline). Section headers are `<h2>`.
- **2–4 inline internal links in the body prose**, to named money/service pages, with
  anchor text that matches the destination. Valid targets and correct relative paths:
  `../contact.html`, `../where-to-buy.html`, `../products/hydroplanks.html`,
  `../products/stormwater-system.html`, `../products/corners-junctions.html`,
  `../products/transition-boxes.html`, `../specs/how-it-works.html`,
  `../specs/installation.html`, `../specs/index.html`, and the application spec pages
  (`../specs/turf-sports.html`, `../specs/roadway-underdrains.html`,
  `../specs/slope-stabilization.html`, `../specs/solar-wind.html`,
  `../specs/stormwater-filtering.html`, `../specs/railroad.html`),
  `../sustainability.html`. When you reference another blog post in prose, link to that
  post's real file (`../blog/{{that-slug}}.html`) — **never** point mismatched anchor text
  at `contact.html`.
- Both JSON-LD blocks present and valid (BlogPosting + BreadcrumbList), dates = today.
- Canonical points to the www pretty URL. Never `noindex` a normal post.

---

## 6. Deploy (how this site actually ships)

Git-linked: **push to `main` → Netlify auto-deploys** (publish dir = repo root, no build
command). The automated pipeline commits to a branch, opens a PR, and auto-merges it to
`main`; the merge triggers the deploy. There is no manual Netlify step and no CLI token.
Do not run `netlify`, do not touch `netlify.toml`, `_redirects`, or `.netlify/`.

---

## 7. Topic queue

`.claude/blog-topics.md` is a plain list, one topic per line. A run takes the **top line
without a `[done]` prefix**, writes that post, then prepends `[done] ` to that line.
**Refill:** after writing, if fewer than 8 undone topics remain, append ~12 fresh topics —
on-brand, national-generic, legally safe (no DOT/rail/TSS/named-project claims), and
**deduped** against both the existing lines and every title in `blog/`. One topic per line,
no `[done]` prefix on the new ones.

---

## 8. Hard DO-NOT list

- ❌ Never modify the shared nav, `mob-nav`, footer, or the closing `<script>` block
  markup (copy them verbatim; never edit the originals on other pages).
- ❌ Never touch analytics/pixel/tracking tags (copy verbatim if present; never add/alter).
- ❌ Never edit existing posts in `/blog`, or any page outside the blog flow
  (products, specs, legal, about, sustainability, gallery, contact, where-to-buy, css).
  The ONLY non-post files you may edit are `blog.html` (prepend one card) and
  `sitemap.xml` (add one url) and `.claude/blog-topics.md`.
- ❌ Never hardcode or edit an on-page count (e.g. the guides count) — it is JS-computed.
- ❌ No dependencies, no `package.json`, no build tools, no new CSS files, no files
  outside this repo, no images (the site is image-free by design; `img/hydroblox-social.jpg`
  is a referenced-but-absent OG image handled at go-live — do not create local images).
- ❌ Never violate a `../CLAUDE.md` legal claim rule, even if a topic seems to invite it.
