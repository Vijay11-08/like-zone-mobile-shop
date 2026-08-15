import glob
import re

print("Removing footer ratings...")
for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Match the footer-rating div block
    # We use a more careful regex to avoid over-matching
    content = re.sub(
        r'<div class="footer-rating[^>]*>.*?(?:Google Reviews</span>\s*</div>|</span></div>)',
        '',
        content,
        flags=re.DOTALL
    )
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done.")
