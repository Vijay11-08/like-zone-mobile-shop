import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract parts
header_match = re.search(r'(<!DOCTYPE html>.*?</header>)', content, re.DOTALL)
footer_match = re.search(r'(<!-- FOOTER -->.*</html>)', content, re.DOTALL)

if not header_match or not footer_match:
    print("Could not find header or footer")
    exit(1)

header = header_match.group(1)
footer = footer_match.group(1)

# Extract sections
hero = re.search(r'(<!-- ============================================================\s*HERO SECTION.*?)(?=<!-- ============================================================|\Z)', content, re.DOTALL).group(1)
quick = re.search(r'(<!-- ============================================================\s*QUICK ACTION CARDS.*?)(?=<!-- ============================================================|\Z)', content, re.DOTALL).group(1)
about = re.search(r'(<!-- ============================================================\s*ABOUT SECTION.*?)(?=<!-- ============================================================|\Z)', content, re.DOTALL).group(1)
mobiles = re.search(r'(<!-- ============================================================\s*MOBILE PHONES SECTION.*?)(?=<!-- ============================================================|\Z)', content, re.DOTALL).group(1)
accessories = re.search(r'(<!-- ============================================================\s*ACCESSORIES SECTION.*?)(?=<!-- SERVICES SECTION -->|\Z)', content, re.DOTALL).group(1)
services = re.search(r'(<!-- SERVICES SECTION -->.*?)(?=<!-- WHY CHOOSE US -->|\Z)', content, re.DOTALL).group(1)
why_us = re.search(r'(<!-- WHY CHOOSE US -->.*?)(?=<!-- TEAM SECTION -->|\Z)', content, re.DOTALL).group(1)
team = re.search(r'(<!-- TEAM SECTION -->.*?)(?=<!-- REVIEWS SECTION -->|\Z)', content, re.DOTALL).group(1)
reviews = re.search(r'(<!-- REVIEWS SECTION -->.*?)(?=<!-- LOCATION SECTION -->|\Z)', content, re.DOTALL).group(1)
location = re.search(r'(<!-- LOCATION SECTION -->.*?)(?=<!-- CONTACT SECTION -->|\Z)', content, re.DOTALL).group(1)
contact = re.search(r'(<!-- CONTACT SECTION -->.*?)(?=<!-- WHATSAPP CTA -->|\Z)', content, re.DOTALL).group(1)
cta = re.search(r'(<!-- WHATSAPP CTA -->.*?)(?=</main>|\Z)', content, re.DOTALL).group(1)

# Modify header links for multi-page
def update_nav(nav_html, active_page):
    nav_html = nav_html.replace('href="#home"', 'href="index.html"')
    nav_html = nav_html.replace('href="#mobiles"', 'href="mobiles.html"')
    nav_html = nav_html.replace('href="#accessories"', 'href="accessories.html"')
    nav_html = nav_html.replace('href="#services"', 'href="services.html"')
    nav_html = nav_html.replace('href="#team"', 'href="about.html"')
    nav_html = nav_html.replace('href="#reviews"', 'href="about.html#reviews"')
    nav_html = nav_html.replace('href="#contact"', 'href="contact.html"')
    
    # Reset active class
    nav_html = re.sub(r'class="nav-link active"', 'class="nav-link"', nav_html)
    # Set active class for the specific page
    if active_page == 'home':
        nav_html = nav_html.replace('href="index.html"', 'href="index.html" class="nav-link active"')
    elif active_page == 'mobiles':
        nav_html = nav_html.replace('href="mobiles.html"', 'href="mobiles.html" class="nav-link active"')
    elif active_page == 'accessories':
        nav_html = nav_html.replace('href="accessories.html"', 'href="accessories.html" class="nav-link active"')
    elif active_page == 'services':
        nav_html = nav_html.replace('href="services.html"', 'href="services.html" class="nav-link active"')
    elif active_page == 'about':
        nav_html = nav_html.replace('href="about.html"', 'href="about.html" class="nav-link active"')
    elif active_page == 'contact':
        nav_html = nav_html.replace('href="contact.html"', 'href="contact.html" class="nav-link active"')
    return nav_html

def update_footer(footer_html):
    footer_html = footer_html.replace('href="#home"', 'href="index.html"')
    footer_html = footer_html.replace('href="#mobiles"', 'href="mobiles.html"')
    footer_html = footer_html.replace('href="#accessories"', 'href="accessories.html"')
    footer_html = footer_html.replace('href="#services"', 'href="services.html"')
    footer_html = footer_html.replace('href="#team"', 'href="about.html"')
    footer_html = footer_html.replace('href="#contact"', 'href="contact.html"')
    return footer_html

# Page creations
pages = {
    'index.html': {
        'active': 'home',
        'content': f"\n  <main>\n{hero}{quick}{cta}\n  </main>\n"
    },
    'mobiles.html': {
        'active': 'mobiles',
        'content': f"\n  <main>\n{mobiles}\n  </main>\n"
    },
    'accessories.html': {
        'active': 'accessories',
        'content': f"\n  <main>\n{accessories}\n  </main>\n"
    },
    'services.html': {
        'active': 'services',
        'content': f"\n  <main>\n{services}\n  </main>\n"
    },
    'about.html': {
        'active': 'about',
        'content': f"\n  <main>\n{about}{why_us}{team}{reviews}\n  </main>\n"
    },
    'contact.html': {
        'active': 'contact',
        'content': f"\n  <main>\n{location}{contact}\n  </main>\n"
    }
}

for page_name, data in pages.items():
    page_header = update_nav(header, data['active'])
    page_footer = update_footer(footer)
    # Quick fix for script references if nested, but they are root
    full_html = page_header + data['content'] + page_footer
    with open(page_name, 'w', encoding='utf-8') as f:
        f.write(full_html)
        
print("Pages generated successfully.")
