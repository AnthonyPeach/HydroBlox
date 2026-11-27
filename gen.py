#!/usr/bin/env python3
"""Full migration generator: SPA views -> real multi-page site with SEO + corrected claims."""
import re, html, os

DOMAIN="https://www.hydroblox.com"
SOCIAL_IMG=DOMAIN+"/img/hydroblox-social.jpg"

# path(route) -> (h1, schema)  ; title/desc parsed from SEO map
H1 = {
 "index":("Gravel clogs. Fabric clogs. HydroBlox has neither.","Organization"),
 "about":("18 years proving the gravel was the problem.","AboutPage"),
 "sustainability":("Made from what nobody else will take.","WebPage"),
 "gallery":("In the ground.","CollectionPage"),
 "blog":("Field notes.","Blog"),
 "where-to-buy":("Find a supplier.","WebPage"),
 "contact":("Tell us what's wet.","ContactPage"),
 "products/hydroplanks":("HydroPlanks.","Product"),
 "products/stormwater-system":("Stormwater Retention Box.","Product"),
 "products/hydronoodles":("HydroNoodles.","Product"),
 "products/transition-boxes":("Transition Boxes.","Product"),
 "specs/index":("Everything you need to put HydroBlox in a drawing set.","CollectionPage"),
 "specs/how-it-works":("No pump. No pitch. Works flat.","WebPage"),
 "specs/installation":("Trench. Place. Backfill. Done.","HowTo"),
 "specs/downloads":("Downloads.","WebPage"),
 "specs/roadway-underdrains":("The underdrain that outlives the road.","WebPage"),
 "specs/railroad":("Ballast fouls. Track settles. Water is why.","WebPage"),
 "specs/slope-stabilization":("Slopes fail wet.","WebPage"),
 "specs/turf-sports":("Play the day after.","WebPage"),
 "specs/solar-wind":("Drainage that lets you tighten the array.","WebPage"),
 "specs/stormwater-filtering":("It moves water. It also cleans it.","WebPage"),
 "legal/privacy-policy":("Privacy Policy","WebPage"),
 "legal/terms":("Terms of Use","WebPage"),
}
# route key -> url path
URL = {k:("/" if k=="index" else "/"+k.replace("/index","")) for k in H1}

# ---- parse titles/descriptions from SEO map ----
TITLE={}; DESC={}
HERE=os.path.dirname(os.path.abspath(__file__))
def _read(*names):
    """Return the contents of the first readable file among names (script-relative), else ''."""
    for n in names:
        p=n if os.path.isabs(n) else os.path.join(HERE,n)
        if os.path.exists(p):
            return open(p,encoding='utf-8').read()
    return ''
# SEO map is optional: if absent, TITLE/DESC stay empty and head() falls back to defaults.
md=_read('hydroblox-seo-map.md','_seo/hydroblox-seo-map.md')

def _skip_href(body):
    """True for links that must NOT be re-prefixed: protocol (tel:/mailto:/http:), //, or #anchors."""
    return bool(re.match(r'(?:[a-z][a-z0-9+.\-]*:|//|#)', body, re.I))
# map md headers to our route keys
route_by_url={
 "/":"index","/about":"about","/sustainability":"sustainability","/gallery":"gallery","/blog":"blog",
 "/where-to-buy":"where-to-buy","/contact":"contact",
 "/products/hydroplanks":"products/hydroplanks","/products/stormwater-system":"products/stormwater-system",
 "/products/hydronoodles":"products/hydronoodles","/products/transition-boxes":"products/transition-boxes",
 "/specs":"specs/index","/specs/how-it-works":"specs/how-it-works","/specs/installation":"specs/installation",
 "/specs/downloads":"specs/downloads","/specs/roadway-underdrains":"specs/roadway-underdrains",
 "/specs/railroad":"specs/railroad","/specs/slope-stabilization":"specs/slope-stabilization",
 "/specs/turf-sports":"specs/turf-sports","/specs/solar-wind":"specs/solar-wind",
 "/specs/stormwater-filtering":"specs/stormwater-filtering",
 "/legal/privacy-policy":"legal/privacy-policy","/legal/terms":"legal/terms",
}
blocks=re.split(r'\n\*\*', md)
for b in blocks:
    hm=re.match(r'([^\*]+)\*\*', b)
    if not hm: continue
    header=hm.group(1).strip()
    urlm=re.match(r'(/[A-Za-z0-9/-]*|/)', header)
    if not urlm: continue
    url=urlm.group(1).rstrip('/') or "/"
    if url not in route_by_url: continue
    t=re.search(r'Title:\s*`([^`]+)`', b); d=re.search(r'Desc:\s*`([^`]+)`', b)
    if t and d:
        k=route_by_url[url]
        TITLE[k]=t.group(1).replace('²','2'); DESC[k]=d.group(1).replace('²','2').replace('—','-')

NAV=_read('.nav-template.html','_nav.html')
FOOT=_read('.footer-template.html','_footer.html')

def prefix(route):
    d=route.count("/")
    # index.html at specs/ counts as depth1
    if route.endswith("/index"): d=route.count("/")
    return "../"*d if d else ""

def nav(route):
    px=prefix(route)
    n=NAV
    # the extracted nav was generated with '../' (specs depth). Re-point all href="../X" and href="X" to this page's prefix.
    # Normalise: strip any leading ../ sequences then re-add px.
    n=re.sub(r'href="(?:\.\./)*([^"]*)"', lambda m: m.group(0) if _skip_href(m.group(1)) else f'href="{px}{m.group(1)}"', n)
    n=re.sub(r"location\.href='(?:\.\./)*([^']*)'", lambda m: m.group(0) if _skip_href(m.group(1)) else f"location.href='{px}{m.group(1)}'", n)
    # active state
    n=re.sub(r'\s?class="active"','',n); n=re.sub(r'ndrop active','ndrop',n)
    seg=route.split('/')[0]
    if route.startswith('specs'): n=n.replace('class="ndrop">Specs','class="ndrop active">Specs')
    elif route.startswith('products'): n=n.replace('class="ndrop">Products','class="ndrop active">Products')
    else:
        top=route
        n=re.sub(rf'href="{re.escape(px)}{top}\.html"', f'href="{px}{top}.html" class="active"', n, count=1)
    return n

def footer(route):
    px=prefix(route); f=FOOT
    f=re.sub(r'href="(?:\.\./)*([^"]*)"', lambda m: m.group(0) if _skip_href(m.group(1)) else f'href="{px}{m.group(1)}"', f)
    return f

def head(route):
    t=TITLE.get(route,"HydroBlox"); d=DESC.get(route,"")
    h1,schema=H1[route]; url=URL[route]
    canon=DOMAIN+(url if url!="/" else "/")
    px=prefix(route)
    org=""
    if schema=="Organization":
        org=f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Organization","name":"HydroBlox","url":"{DOMAIN}/","telephone":"+1-724-719-2660"}}</script>'
    elif schema=="Product":
        org=f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Product","name":"{html.escape(h1.rstrip("."))}","brand":{{"@type":"Brand","name":"HydroBlox"}},"description":"{html.escape(d)}"}}</script>'
    crumb=""
    if url!="/" and "/" in url.strip("/"):
        parts=url.strip("/").split("/"); items=[f'{{"@type":"ListItem","position":1,"name":"Home","item":"{DOMAIN}/"}}']; acc=DOMAIN
        for i,p in enumerate(parts,2):
            acc+="/"+p; items.append(f'{{"@type":"ListItem","position":{i},"name":"{p.replace("-"," ").title()}","item":"{acc}"}}')
        crumb=f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{",".join(items)}]}}</script>'
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(t)}</title>
<meta name="description" content="{html.escape(d)}">
<link rel="canonical" href="{canon}">
<meta name="robots" content="index, follow">
<meta property="og:type" content="website">
<meta property="og:title" content="{html.escape(t)}">
<meta property="og:description" content="{html.escape(d)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SOCIAL_IMG}">
<meta property="og:site_name" content="HydroBlox">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(t)}">
<meta name="twitter:description" content="{html.escape(d)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,800&family=Source+Serif+4:ital,opsz,wght@1,8..60,600;1,8..60,700&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{px}css/site.css">
<link rel="icon" type="image/png" sizes="32x32" href="{px}img/favicon-32.png">
<link rel="apple-touch-icon" sizes="180x180" href="{px}img/apple-touch-icon.png">
{org}
{crumb}
</head>'''

if __name__=="__main__":
    print("routes:",len(H1),"| titles parsed:",len(TITLE),"| descs parsed:",len(DESC))
    miss=[k for k in H1 if k not in TITLE]
    print("missing title/desc:",miss if miss else "none")
