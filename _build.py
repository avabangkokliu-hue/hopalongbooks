import os, json, datetime
ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://avabangkokliu-hue.github.io/hopalongbooks"
PUB = "Hop Along Books"
TODAY = "2026-10-08"

BOOKS = [
 dict(slug="trucks-trains-rockets", key="book1", color="#1F75FE",
      title="Trucks, Trains, Rockets & Things That Go",
      short="Things That Go",
      sub="Color by Number for Kids Ages 3-5",
      amazon="https://www.amazon.com/s?k=Trucks+Trains+Rockets+Things+That+Go+Hop+Along+Books",
      isbn="", status="Published October 2026",
      blurb="45 big, friendly vehicles: cars, fire trucks, diggers, school buses, trains, boats, planes and rockets, plus busy scenes like the airport and the construction site.",
      inside="cars, trucks, diggers, trains, rockets, boats, planes, buses, space and construction scenes",
      levels=["Car", "Steam Train", "Construction Site"], sample="Fire Truck", fact="a read-aloud vehicle fact"),
 dict(slug="cute-animals", key="book2", color="#1CAC78",
      title="Cute Animals Color by Number for Kids Ages 3-5",
      short="Cute Animals",
      sub="Pets, Farm, Zoo & Dinosaurs",
      amazon="https://www.amazon.com/s?k=Cute+Animals+Color+by+Number+Hop+Along+Books",
      isbn="9798160782225", status="Published October 2026",
      blurb="45 big, friendly animals: cats, dogs, ducks, lions, elephants, penguins, dolphins, dinosaurs and busy scenes like the farm, the jungle and under the sea.",
      inside="pets, farm animals, zoo animals, sea creatures, dinosaurs and big scenes",
      levels=["Cat", "Lion", "Farm"], sample="Elephant", fact="a read-aloud animal fact"),
 dict(slug="dinosaurs", key="book3", color="#6A4BB0",
      title="Dinosaurs Color by Number for Kids Ages 3-5",
      short="Dinosaurs",
      sub="A Day in the Life of Silly Dinos",
      amazon="https://www.amazon.com/s?k=Dinosaurs+Color+by+Number+Silly+Dinos+Hop+Along+Books",
      isbn="", status="Coming October 2026",
      blurb="45 pictures starring 8 dino friends - T-Rex, Triceratops, Stegosaurus, Brachiosaurus, Ankylosaurus, Parasaurolophus, Pteranodon and Baby Dino - brushing their teeth, baking cakes, driving trucks and flying rockets.",
      inside="8 recurring dinosaur characters in everyday life, jobs, vehicles and big scenes",
      levels=["T-Rex Eats an Apple", "Brachiosaurus Pulls a Carrot", "A Dinosaur Birthday Party"], sample="T-Rex Brushes His Teeth", fact="a read-aloud dinosaur fact"),
]

CSS = """
:root{--ink:#1D3557;--mut:#5b6472;--bg:#fff;--card:#f4f6fa;--line:#e3e7ee;--acc:#FFD166}
*{box-sizing:border-box}body{margin:0;font-family:-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;color:#222;background:var(--bg);line-height:1.55}
a{color:var(--ink)}.wrap{max-width:960px;margin:0 auto;padding:0 20px}
header{border-bottom:1px solid var(--line)}header .wrap{display:flex;align-items:center;justify-content:space-between;height:64px}
.brand{font-weight:800;font-size:20px;color:var(--ink);text-decoration:none}.brand span{background:var(--acc);border-radius:6px;padding:2px 8px;margin-right:6px}
nav a{margin-left:18px;text-decoration:none;color:var(--mut);font-weight:600}
h1{font-size:34px;line-height:1.2;color:var(--ink);margin:36px 0 10px}h2{color:var(--ink);margin-top:36px}
.lead{font-size:19px;color:#333;max-width:700px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:22px;margin:28px 0}
.card{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:16px}.card img{width:100%;border-radius:10px;display:block}
.card h3{margin:12px 0 4px;font-size:18px}.card p{margin:4px 0;color:var(--mut);font-size:15px}
.btn{display:inline-block;background:var(--ink);color:#fff;text-decoration:none;padding:10px 18px;border-radius:10px;font-weight:700;margin-top:10px}
.btn.alt{background:#fff;color:var(--ink);border:2px solid var(--ink)}
.spec{width:100%;border-collapse:collapse;margin:16px 0}.spec th,.spec td{text-align:left;padding:8px 10px;border-bottom:1px solid var(--line);vertical-align:top}.spec th{width:34%;color:var(--mut);font-weight:600}
.three{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.three img{width:100%;border-radius:10px;border:1px solid var(--line)}.three figcaption{font-size:14px;color:var(--mut);margin-top:6px}
.faq h3{margin-bottom:4px}.faq p{margin-top:0;color:#333}
footer{border-top:1px solid var(--line);margin-top:60px;padding:28px 0;color:var(--mut);font-size:14px}
.post{max-width:720px}.post p,.post li{font-size:17px}.post h2{font-size:24px}
@media(max-width:600px){.three{grid-template-columns:1fr 1fr}h1{font-size:28px}nav a{margin-left:12px;font-size:14px}}
"""

def page(title, desc, body, path, jsonld=None, canonical=None):
    can = canonical or f"{SITE}/{path}"
    ld = f'<script type="application/ld+json">{json.dumps(jsonld)}</script>' if jsonld else ""
    html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><link rel="canonical" href="{can}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website"><meta property="og:url" content="{can}">
<style>{CSS}</style>{ld}</head><body>
<header><div class="wrap"><a class="brand" href="{SITE}/"><span>HA</span>Hop Along Books</a><nav><a href="{SITE}/#books">Books</a><a href="{SITE}/blog/">Guides</a><a href="{SITE}/about.html">About</a></nav></div></header>
<main class="wrap">{body}</main>
<footer><div class="wrap">&copy; 2026 Hop Along Books. Color by number books for ages 3-5. Available on Amazon. &middot; <a href="{SITE}/about.html">About</a> &middot; <a href="{SITE}/blog/">Guides for parents</a></div></footer>
</body></html>"""
    full = os.path.join(ROOT, path); os.makedirs(os.path.dirname(full), exist_ok=True); open(full, "w").write(html)

def book_card(b):
    return f"""<div class="card"><a href="{SITE}/books/{b['slug']}.html"><img src="{SITE}/img/{b['key']}_cover.jpg" alt="{b['title']} - cover"></a>
<h3><a href="{SITE}/books/{b['slug']}.html" style="text-decoration:none">{b['short']}</a></h3><p>{b['sub']}</p><p>{b['status']}</p>
<a class="btn" href="{b['amazon']}" rel="nofollow">See on Amazon</a></div>"""

# ---------- home ----------
home_body = f"""
<h1>Color by number books a 3-year-old can actually finish</h1>
<p class="lead">Big shapes. Color names written on every key. One picture per page, with a fun activity page behind it. Every Hop Along book is made for ages 3-5 and checked page by page so small hands can stay inside the lines.</p>
<h2 id="books">The books</h2>
<div class="grid">{''.join(book_card(b) for b in BOOKS)}</div>
<h2>What makes a Hop Along book different</h2>
<div class="grid">
<div class="card"><h3>A color key kids can read</h3><p>Every page shows the number, a color swatch <b>and the color name written out</b> - Red, Blue, Green, Brown. No guessing what a dot means, and no odd shades you don't own.</p></div>
<div class="card"><h3>Really made for ages 3-5</h3><p>5 levels, easy to harder. Level 1 has 3 colors and spaces about an inch wide. Even the busiest Level 5 scenes keep every space about half an inch wide or bigger. We measure every page.</p></div>
<div class="card"><h3>One picture per page</h3><p>Pictures are printed on one side only, so markers can't ruin the next picture. Behind each one: a read-aloud fact, a color test strip, a "How did you feel?" face and a box to draw your own.</p></div>
<div class="card"><h3>102 pages, 8.5 x 11 in</h3><p>45 pictures, 45 activity pages and full answer pictures at the back. Big pages for little hands.</p></div>
</div>
<h2>Guides for parents</h2>
<ul>
<li><a href="{SITE}/blog/how-to-choose-a-color-by-number-book-for-a-3-year-old.html">How to choose a color by number book for a 3-year-old</a></li>
<li><a href="{SITE}/blog/why-color-names-matter-more-than-color-dots.html">Why color names matter more than color dots</a></li>
<li><a href="{SITE}/blog/markers-vs-crayons-for-toddler-coloring-books.html">Markers vs crayons for toddler coloring books</a></li>
</ul>
"""
page("Hop Along Books - Color by Number for Kids Ages 3-5", "Color by number books made for ages 3-5: big shapes, color names on every key, one picture per page, a fun activity page behind each. Trucks, animals and dinosaurs. On Amazon.", home_body, "index.html",
     jsonld={"@context":"https://schema.org","@type":"Organization","name":PUB,"url":SITE+"/","description":"Publisher of color by number books for children ages 3-5."}, canonical=SITE+"/")

# ---------- book pages ----------
for b in BOOKS:
    k = b["key"]
    ld = {"@context":"https://schema.org","@type":"Book","name":b["title"],"alternativeHeadline":b["sub"],"author":{"@type":"Organization","name":PUB},"publisher":{"@type":"Organization","name":PUB},
          "bookFormat":"https://schema.org/Paperback","numberOfPages":102,"inLanguage":"en","typicalAgeRange":"3-5","genre":"Children's activity book, color by number",
          "image":f"{SITE}/img/{k}_cover.jpg","url":f"{SITE}/books/{b['slug']}.html","offers":{"@type":"Offer","url":b["amazon"],"priceCurrency":"USD","price":"10.99","availability":"https://schema.org/InStock"}}
    if b["isbn"]: ld["isbn"] = b["isbn"]
    body = f"""
<div class="grid" style="grid-template-columns:1fr 1.4fr;align-items:start">
<div><img src="{SITE}/img/{k}_cover.jpg" alt="{b['title']} cover" style="width:100%;border-radius:14px;border:1px solid var(--line)"></div>
<div><h1 style="margin-top:0">{b['title']}</h1><p class="lead">{b['sub']}</p><p>{b['blurb']}</p>
<a class="btn" href="{b['amazon']}" rel="nofollow">See on Amazon</a> <span style="color:var(--mut);margin-left:8px">{b['status']} &middot; $10.99</span></div>
</div>
<h2>At a glance</h2>
<table class="spec">
<tr><th>Age</th><td>3-5 (preschool and kindergarten)</td></tr>
<tr><th>Pictures</th><td>45, in 5 levels from easy to harder</td></tr>
<tr><th>Colors per picture</th><td>Level 1: 3 &middot; Level 2: 4 &middot; Level 3: 5 &middot; Level 4: 6 &middot; Level 5: 8</td></tr>
<tr><th>Smallest coloring space</th><td>Level 1 about 1 inch (25 mm) wide; Level 5 about half an inch (12 mm) wide. Every page is measured.</td></tr>
<tr><th>Color key</th><td>Number + color swatch + color name written out. Everyday colors only (Red, Blue, Yellow, Green, Orange, Brown, Violet, Gray, Pink, Sky Blue = any light blue).</td></tr>
<tr><th>Printing</th><td>One picture per page, printed on one side. Behind each picture: {b['fact']}, a color test strip, a "How did you feel?" face to circle and a box to draw your own.</td></tr>
<tr><th>Pages / size</th><td>102 pages &middot; 8.5 x 11 in &middot; paperback, matte cover</td></tr>
<tr><th>What's inside</th><td>{b['inside']}; answer pictures at the back</td></tr>
<tr><th>Best with</th><td>Crayons or colored pencils. Markers work too - the back of each picture is an activity page, not another picture.</td></tr>
{f'<tr><th>ISBN</th><td>{b["isbn"]}</td></tr>' if b['isbn'] else ''}
</table>
<h2>Easy to harder</h2>
<div class="three">
<figure><img src="{SITE}/img/{k}_A1_level.jpg" alt="Level 1 example"><figcaption>Level 1 &middot; 3 colors</figcaption></figure>
<figure><img src="{SITE}/img/{k}_A2_level.jpg" alt="Level 3 example"><figcaption>Level 3 &middot; 5 colors</figcaption></figure>
<figure><img src="{SITE}/img/{k}_A3_level.jpg" alt="Level 5 example"><figcaption>Level 5 &middot; 8 colors</figcaption></figure>
</div>
<h2>More than a coloring page</h2>
<div class="three">
<figure><img src="{SITE}/img/{k}_B1_page.jpg" alt="A numbered coloring page"><figcaption>One picture per page</figcaption></figure>
<figure><img src="{SITE}/img/{k}_B2_back.jpg" alt="The activity page behind each picture"><figcaption>Flip the page: fact, color test, feelings</figcaption></figure>
<figure><img src="{SITE}/img/{k}_B3_key.jpg" alt="Color key with color names"><figcaption>A color key kids can read</figcaption></figure>
</div>
<h2>More from Hop Along Books</h2>
<div class="grid">{''.join(book_card(o) for o in BOOKS if o['key']!=k)}</div>
"""
    page(f"{b['title']} | Hop Along Books", f"{b['sub']}. 45 pictures in 5 levels for ages 3-5, color names on every key, one picture per page. 102 pages, 8.5 x 11 in.", body, f"books/{b['slug']}.html", jsonld=ld)

# ---------- blog ----------
POSTS = [
 ("how-to-choose-a-color-by-number-book-for-a-3-year-old", "How to choose a color by number book for a 3-year-old",
  "Five things to check before you buy a color by number book for a toddler or preschooler - and the one mistake most books make.",
  f"""
<p>Most color by number books say "for kids" on the cover. Very few are made for a 3-year-old. Here is what to look at before you buy, based on what parents complain about most in Amazon reviews.</p>
<h2>1. How big are the spaces?</h2>
<p>This is the whole game. A 3-year-old holds a crayon in a fist and colors in big scribbles. If the spaces are the size of a fingernail, the picture will look like a mess and your child will give up. Look for spaces at least <b>half an inch wide</b>, and for the first pages, closer to <b>an inch</b>. If the listing doesn't say, zoom in on the sample pages.</p>
<h2>2. How many colors per picture?</h2>
<p>Three or four is right for a first book. Eight colors is a lot of switching for a small child. The best books start with 3 colors and build up, so the same book still works at 5.</p>
<h2>3. Does the color key have words, or just dots?</h2>
<p>Many books show only colored dots next to the numbers. A child who can't tell light blue from blue, or a parent who is color blind, gets stuck. Look for the <b>color name written out</b> next to each number: "1 - Red", "2 - Blue". <a href="{SITE}/blog/why-color-names-matter-more-than-color-dots.html">More on why this matters</a>.</p>
<h2>4. Are the colors ones you actually own?</h2>
<p>"Tan", "Apricot" and "Cerulean" are real crayon colors, but not in every box. Books that stick to Red, Blue, Yellow, Green, Orange, Brown and a few more work with any crayons in the house.</p>
<h2>5. What is on the back of each page?</h2>
<p>If pictures are printed on both sides, a marker will bleed through and ruin the picture behind it. One-sided printing fixes that. The best books put something useful on the back - a fact to read aloud, a place to test colors, a box to draw.</p>
<h2>The mistake most books make</h2>
<p>They print the age range on the cover without ever measuring the pages. "Ages 3-8" usually means "fine for 6, frustrating for 3." A book really made for 3-5 will tell you the number of colors per level and how big the spaces are.</p>
<p>That is how we make <a href="{SITE}/">Hop Along Books</a>: 5 levels from 3 to 8 colors, spaces measured on every page, color names on every key, one picture per page. <a href="{SITE}/#books">See the books</a>.</p>
"""),
 ("why-color-names-matter-more-than-color-dots", "Why color names matter more than color dots",
  "Color by number keys that show only colored dots leave young children and color-blind parents guessing. Here's why written color names work better.",
  f"""
<p>Open most color by number books and the key looks like this: a number, then a small colored dot. Simple enough for an adult. For a 3-year-old, it often isn't.</p>
<h2>Dots are hard to match</h2>
<p>A printed dot is tiny, flat and lit by whatever lamp is on. A crayon is waxy, thicker and a slightly different shade. Asking a child to hold a crayon up to a dot and decide "is this the same?" is a real task. Light blue vs blue, orange vs red-orange, brown vs dark orange - these trip up small children constantly.</p>
<h2>Words remove the guessing</h2>
<p>When the key says <b>"2 - Blue"</b>, a child who knows the word blue (most 3-year-olds do) can pick the blue crayon, and a parent can say "find the blue one" without pointing. The crayon's own label says Blue too. Everything matches.</p>
<h2>It also helps color-blind parents</h2>
<p>About 1 in 12 men has some form of color blindness. A key with dots only is useless to them when their child asks for help. A key with names works for everyone.</p>
<h2>And it teaches color words</h2>
<p>Every page becomes a little lesson: the number, the swatch and the word, side by side. Children who color this way learn color names faster, because they read and use the word every time.</p>
<h2>What to look for</h2>
<p>A key that shows <b>number + swatch + name</b>, and uses everyday color names that match the crayons you own. If a book uses an unusual shade, it should tell you what to use instead ("Sky Blue - any light blue crayon").</p>
<p>Every <a href="{SITE}/">Hop Along</a> book is made this way. <a href="{SITE}/#books">See the books</a>.</p>
"""),
 ("markers-vs-crayons-for-toddler-coloring-books", "Markers vs crayons for toddler coloring books",
  "Markers bleed through thin paper and ruin the next page. Here's what works best for ages 3-5 and how to choose a book that survives markers.",
  f"""
<p>The most common one-star review of children's coloring books is some version of "the marker bled through and ruined the next picture." Here's what is going on and what to do about it.</p>
<h2>Why it happens</h2>
<p>Print-on-demand paperbacks (which is most coloring books on Amazon now) use fairly thin paper. Markers, especially washable kids' markers, soak through. Crayons and colored pencils sit on top of the paper and don't.</p>
<h2>Crayons: the best choice for 3-5</h2>
<p>Thick crayons are easiest for small hands to grip, they don't bleed, and a 3-year-old can press hard without tearing the page. For a first color by number book, crayons win.</p>
<h2>Colored pencils: good for 4-5</h2>
<p>Finer control, no bleed, but they need a bit more hand strength. Nice for the harder levels.</p>
<h2>Markers: fun, but check the book first</h2>
<p>Kids love markers. If yours insists, pick a book where <b>pictures are printed on one side only</b>, so bleed-through lands on a blank or activity page instead of the next picture. Slip a sheet of scrap paper behind the page as well.</p>
<h2>What to look for in a book</h2>
<ul><li>One picture per page, one-sided printing</li><li>Something useful on the back of each picture (so the page isn't wasted)</li><li>Thick, clear outlines that are easy to see even if a marker spreads a little</li></ul>
<p><a href="{SITE}/">Hop Along</a> books are printed one picture per page; the back of each picture is an activity page with a fact, a color test strip and a drawing box. <a href="{SITE}/#books">See the books</a>.</p>
"""),
]
idx = "<h1>Guides for parents</h1><p class='lead'>Short, practical guides on choosing and using coloring books with 3-5 year olds.</p><ul>"
for slug, title, desc, body in POSTS:
    ld = {"@context":"https://schema.org","@type":"Article","headline":title,"description":desc,"author":{"@type":"Organization","name":PUB},"publisher":{"@type":"Organization","name":PUB},"datePublished":TODAY,"url":f"{SITE}/blog/{slug}.html"}
    page(f"{title} | Hop Along Books", desc, f"<article class='post'><h1>{title}</h1><p style='color:var(--mut)'>Hop Along Books &middot; {TODAY}</p>{body}</article>", f"blog/{slug}.html", jsonld=ld)
    idx += f"<li><a href='{SITE}/blog/{slug}.html'>{title}</a><br><span style='color:var(--mut)'>{desc}</span></li>"
idx += "</ul>"
page("Guides for parents | Hop Along Books", "Practical guides on choosing and using color by number books with children ages 3-5.", idx, "blog/index.html")

# ---------- about ----------
page("About Hop Along Books", "Hop Along Books makes color by number books for ages 3-5, measured page by page so small hands can finish them.", f"""
<h1>About Hop Along Books</h1>
<p class="lead">We make color by number books for children ages 3-5 - and we measure every page.</p>
<p>Most coloring books put an age range on the cover and hope. We started Hop Along Books because the books we found for 3-year-olds had spaces too small, too many colors, and keys that showed only dots.</p>
<p>So every Hop Along book follows the same rules:</p>
<ul>
<li><b>5 levels, easy to harder</b> - from 3 colors and inch-wide shapes up to 8-color scenes.</li>
<li><b>Every space is measured.</b> Level 1 spaces are about an inch wide; even Level 5 keeps every space about half an inch or bigger.</li>
<li><b>Color names on every key</b>, in everyday colors you already own.</li>
<li><b>One picture per page</b>, with a fact, a color test strip, a feelings face and a drawing box on the back.</li>
<li><b>Answer pictures at the back</b>, and a small color example on every page.</li>
</ul>
<p>The books are published through Amazon KDP and printed on demand. Line art and text are produced with AI tools and checked by hand, page by page.</p>
<p>Questions? Write to <a href="mailto:hello@hopalongbooks.com">hello@hopalongbooks.com</a>.</p>
<h2>The books</h2><div class="grid">{''.join(book_card(b) for b in BOOKS)}</div>
""", "about.html")

# sitemap + robots
urls = [SITE+"/", SITE+"/about.html", SITE+"/blog/"] + [f"{SITE}/books/{b['slug']}.html" for b in BOOKS] + [f"{SITE}/blog/{p[0]}.html" for p in POSTS]
open(os.path.join(ROOT,"sitemap.xml"),"w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+"".join(f"<url><loc>{u}</loc><lastmod>{TODAY}</lastmod></url>" for u in urls)+"</urlset>")
open(os.path.join(ROOT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
open(os.path.join(ROOT,".nojekyll"),"w").write("")
print("built", len(urls), "pages")
