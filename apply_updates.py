import os
import re

files = {
    'index.html': 'Home',
    'mobiles.html': 'Mobile Phones',
    'accessories.html': 'Mobile Accessories',
    'services.html': 'Mobile Services',
    'about.html': 'About Us & Team',
    'contact.html': 'Contact Us'
}

map_link = 'https://www.google.com/maps/search/?api=1&query=Like+Zone+Mobile+Shop,+6WG6%2BWCC,+Tramba,+Rajkot,+Gujarat+360020'
old_address_pattern = re.compile(r'Kasturba Dham, Tramba, Rajkot, Gujarat [–-] 360020')
new_address = 'Like Zone Mobile Shop, 6WG6+WCC, Tramba, Rajkot, Gujarat 360020'
footer_address = f'<a href="{map_link}" target="_blank" rel="noopener noreferrer" style="color: inherit;">{new_address}</a>'

for filename, page_name in files.items():
    if not os.path.exists(filename): continue
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update Address
    content = old_address_pattern.sub(new_address, content)
    
    # Make the footer address clickable for directions
    content = content.replace(f'<span>{new_address}</span>', f'<span>{footer_address}</span>')
    content = content.replace(f'</i>\n            {new_address}', f'</i>\n            {footer_address}')
    
    if filename == 'contact.html':
        content = content.replace('Get Directions', f'<a href="{map_link}" target="_blank" class="custom-btn custom-btn-secondary custom-btn-sm mt-2">Get Directions</a>')
    
    # 2. Update SEO
    # Update title
    title_pattern = re.compile(r'<title>.*?</title>')
    new_title = f'<title>{page_name} | Like Zone Mobile Shop | Tramba, Rajkot</title>'
    content = title_pattern.sub(new_title, content)
    
    # Update description based on page
    desc_pattern = re.compile(r'<meta name="description"\s*content=".*?"\s*/>', re.DOTALL)
    new_desc = f'<meta name="description" content="Explore {page_name.lower()} at Like Zone Mobile Shop in Tramba, Rajkot. Best prices and premium service." />'
    if filename == 'index.html':
        new_desc = '<meta name="description" content="Like Zone Mobile Shop in Tramba, Rajkot. Explore smartphones, accessories, covers, chargers, and mobile-related services." />'
    content = desc_pattern.sub(new_desc, content)
    
    # 3. Add animation classes
    content = content.replace('class="custom-card', 'class="custom-card reveal-on-scroll')
    if 'hero-title' in content:
        content = content.replace('class="hero-title"', 'class="hero-title reveal-on-scroll"')
        content = content.replace('class="hero-desc"', 'class="hero-desc reveal-on-scroll"')
        content = content.replace('class="hero-visual text-center"', 'class="hero-visual text-center reveal-on-scroll"')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated all HTML files with SEO, Maps link, and Animation classes.")
