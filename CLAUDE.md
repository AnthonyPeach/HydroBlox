# HydroBlox.com — Project Context

This is the consolidated HydroBlox marketing site. It replaces two Wix sites
(hydroblox.com + hydrobloxtech.com) with one static site deployed to Netlify at
**www.hydroblox.com**. This file is the source of truth for a new session — read it first.

## What this is
- A 23-page static HTML site. No framework, no build step required to deploy — Netlify serves the files directly.
- `gen.py` is a Python generator that stamps a consistent SEO `<head>` + shared nav + footer onto pages. Not required at runtime; used when regenerating pages.
- The homepage was migrated out of a single-file SPA into real, indexable pages. Do not reintroduce SPA/JS view-switching — every page must be a real URL for SEO.

## Brand system (do not drift)
- Source of truth: **HydroBlox Brand Guidelines (2026)**. Logo = ribbon drop + "Hydro" (Fraunces 800) + "*Blox*" (Source Serif 4 Italic, Flow Teal) + byline "MOVING WATER RESPONSIBLY" (tracked Inter caps). Never restyle or recolor it.
- Logo on the site: `.logo` lockup in `.nav-template.html` / `.footer-template.html` (drop images `img/hydroblox-drop.png`, `img/hydroblox-drop-reverse.png` for dark backgrounds). Favicon/app icon = drop in a navy tile (`img/favicon-32.png`, `img/apple-touch-icon.png`, `img/icon-512.png`). Share image `img/hydroblox-social.jpg`.
- Fonts: **Fraunces 800** every headline, always upright; the italic payoff (`<em>` in a heading) in **Source Serif 4 Italic**, teal; **Inter** body; **JetBrains Mono** labels.
- Colors (tokens in `css/site.css`): Deep Navy `#0E1F2F` (`--navy`), Flow Teal `#13819B` (`--sky`: "Blox", emphasis, buttons), Water `#2BA9C4` (`--sky2`: accents on navy), Mint `#E3F7F3` (`--mint`: washes), Paper `#F3FBF9` (`--off`: page background). `--teal` `#0E6B80` is the darker hover shade.
- Signature: navy→teal diagonal gradients; alternating white/off "ruled" section bands; the pressure-fed "0.0% grade" mechanism diagram.
- Four cutaway feature icons (Clog-Free, Natural Pressure, 40,000 lbs, 100% Recycled) live on the homepage benefit cards. Light variants on light sections.
- Photos are still missing: `.img-ph` placeholders hold every photo slot. Drop real assets into `/img` and replace placeholders.

## Positioning (the messaging spine)
- Dual-track: **circularity hooks, drainage converts.** "Waste in. Infrastructure out." is the attention line; the spec data closes.
- Unifying idea: a French drain moves water into gravel that clogs; an MRF moves film to landfill. Both relocate the problem. HydroBlox ends it. Recycled content is the *mechanism*, not a virtue.
- Voice: Ed's technical edge + brand authority. Short sentences. Name the villain (gravel, fabric, the MRF). Numbers over adjectives. No exclamation points, no "innovative/seamless/hassle-free."

## CLAIMS — hard rules (legal)
NEVER put these on any page (all were scrubbed; keep them out):
- "Federally Approved" — no such designation exists for a drainage product.
- "NPDES/MS4 certified/compliant" — these regulate the discharger, not the product. Allowed phrasing: "supports NPDES / MS4 permit documentation."
- "Never clogs / never fails / clog-free forever" — use "nothing to clog" (structural fact: no aggregate, no geotextile).
- "World's most advanced" or any unsubstantiated superlative.
- Age claim is **18 years**, everywhere. Never 15+, "over fifteen," or "over ten."
- Do NOT port Hydro Fix solar spacing numbers to HydroBlox without Ed's written sign-off (different entity, different liability).

## Verified specs (safe to use)
40,000 lbs/ft² compression · 14.25 gal/min flow per 40" plank · 0.0% slope · 100% recycled film ·
sold via Home Depot Pro nationwide + regional distributors (US, Canada, Puerto Rico) · phone 724-719-2660.

## OPEN — `[SOURCE NEEDED]` (blocks publish; get from Ed Grieser, HydroBlox Technologies)
Search the tree for `SOURCE NEEDED` to find every flag. They include:
ASTM designations + test results, install count ("thousands" is unverified), tonnage diverted,
load ratings for products, flow rates per product, DOT approvals (roadway), Class I/AREMA (rail),
named reference projects + permission (slope, turf), stormwater-filtering removal efficiencies,
transition-box sizes, warranty terms. Also: replace the gmail contact address with a domain email.

## Structure
```
index.html  about  sustainability  gallery  blog  where-to-buy  contact
products/{hydroplanks,stormwater-system,hydronoodles,transition-boxes}
specs/index + {how-it-works,installation,downloads,roadway-underdrains,railroad,
               slope-stabilization,turf-sports,solar-wind,stormwater-filtering}
legal/{privacy-policy,terms}
css/site.css · _redirects · netlify.toml · robots.txt · sitemap.xml · gen.py
```

## SEO conventions (every page)
Unique title ≤60 chars, unique description ~150-160, canonical to https://www.hydroblox.com/<path>,
OG + Twitter tags, one intent-matched `<h1>`, JSON-LD (Organization on home, Product on product pages,
BreadcrumbList on sub-pages). `_redirects` 301s every hydrobloxtech.com URL to its new home — preserve it.
Canonical host is **www**; bare domain 301s to www.

## Known refinements (not blockers)
1. The 3 product pages currently share the products-view body — give each its own product-only content.
2. Specs sub-pages have real structure but `[SOURCE NEEDED]` placeholders for hard numbers.
3. `/img` is empty — placeholders until real photography lands.
4. Contact form is wired to Netlify Forms (name="contact"); confirm notification routing after deploy.

## Deploy
Netlify, publish directory = repo root. `netlify.toml` forces www + sets security headers.
After first deploy: point hydrobloxtech.com at this site so `_redirects` can 301 it.
