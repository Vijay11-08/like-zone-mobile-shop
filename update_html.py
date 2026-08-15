import glob
import re

print("Updating HTML files...")
for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update logo reference everywhere
    content = re.sub(
        r'images/(?:logo_new\.png|LIKEZONE\s+LOGO\.png|LIKEZONE%20LOGO\.png)',
        r'images/LIKEZONE%20LOGO.png',
        content
    )
    
    # Remove Reviews nav link
    content = re.sub(
        r'<li class="nav-item"><a class="nav-link" href="about\.html#reviews">Reviews</a></li>\s*',
        '',
        content
    )
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done.")
