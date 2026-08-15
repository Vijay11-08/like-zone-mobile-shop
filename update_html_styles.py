import os
import re

files = ['mobiles.html', 'accessories.html', 'services.html', 'about.html', 'contact.html']

with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Extract parts from index.html
head_part = index_html.split('<body>')[0] + '<body>\n'
header_match = re.search(r'<header>.*?</header>', index_html, re.DOTALL)
footer_match = re.search(r'<footer.*?</html>', index_html, re.DOTALL)

if not header_match or not footer_match:
    print("Could not find header or footer in index.html")
    exit(1)

header = header_match.group(0)
footer_and_rest = footer_match.group(0)

for file in files:
    if not os.path.exists(file): continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract main content of the file
    main_match = re.search(r'<main>(.*?)</main>', content, re.DOTALL)
    if not main_match:
        print(f'No main in {file}')
        continue
        
    main_content = main_match.group(1)
    
    # Do replacements in main content to match new styles
    main_content = main_content.replace('glass-card', 'custom-card')
    main_content = main_content.replace('reveal-on-scroll', '')
    main_content = main_content.replace('revealed', '')
    
    # Update buttons
    main_content = main_content.replace('btn-primary-gradient', 'custom-btn custom-btn-primary')
    main_content = main_content.replace('btn-outline-glass', 'custom-btn custom-btn-secondary')
    main_content = main_content.replace('btn-whatsapp', 'custom-btn custom-btn-whatsapp')
    main_content = main_content.replace('btn btn-', 'custom-btn custom-btn-')
    main_content = re.sub(r'class="btn\s+', 'class="custom-btn ', main_content)
    
    # Section paddings
    main_content = main_content.replace('py-5', 'section-padding')
    main_content = main_content.replace('py-4', '')
    
    # Specific layout fixes
    if file == 'mobiles.html':
        main_content = main_content.replace('product-icon-wrap', 'product-img-wrap')
        main_content = main_content.replace('class="bi bi-phone-fill"', 'class="bi bi-phone"')
    
    elif file == 'accessories.html':
        main_content = main_content.replace('accessory-card', 'custom-card p-4 text-center')
        main_content = main_content.replace('accessory-icon', 'quick-icon')
    
    elif file == 'services.html':
        main_content = main_content.replace('service-card', 'service-card custom-card')
        main_content = main_content.replace('service-icon-wrap', 'service-icon')
    
    elif file == 'about.html':
        main_content = main_content.replace('team-card', 'team-card custom-card')
        main_content = main_content.replace('team-avatar-img', 'team-avatar')
        main_content = re.sub(r'<div class="float-badge.*?>.*?</div>', '', main_content, flags=re.DOTALL)
        
    elif file == 'contact.html':
        main_content = main_content.replace('location-card custom-card', 'contact-info-card')
        main_content = main_content.replace('location-card glass-card', 'contact-info-card')
        main_content = main_content.replace('contact-card glass-card', 'contact-info-card')
        main_content = main_content.replace('contact-card custom-card', 'contact-info-card')
        main_content = main_content.replace('location-icon', 'contact-icon')
        
    head_original_match = re.search(r'(.*?<body.*?>)', content, re.DOTALL)
    if not head_original_match:
        print(f"Could not find head in {file}")
        continue
    head_original = head_original_match.group(1)
    
    new_html = head_original + '\n' + header + '\n  <main>\n' + main_content + '\n  </main>\n  ' + footer_and_rest
    
    # Remove any old decorations
    new_html = re.sub(r'<div class="bg-decorations".*?>.*?</div>\s*</div>', '', new_html, flags=re.DOTALL)
    new_html = re.sub(r'<div class="bg-decorations".*?>.*?</div>', '', new_html, flags=re.DOTALL)
    new_html = re.sub(r'<!-- Background Decorations -->\s*<div class="bg-decorations" aria-hidden="true">\s*<div class="blob blob-1"></div>\s*<div class="blob blob-2"></div>\s*<div class="blob blob-3"></div>\s*<div class="grid-pattern"></div>\s*<div class="glow-circle glow-1"></div>\s*<div class="glow-circle glow-2"></div>\s*</div>', '', new_html, flags=re.DOTALL)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f'Updated {file}')
