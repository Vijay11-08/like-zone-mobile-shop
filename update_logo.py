import glob
import re
import os

print("Updating logo across all HTML files...")
for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace header logo
    content = re.sub(
        r'<div class="logo-icon"[^>]*>\s*<i class="bi bi-phone-fill"></i>\s*</div>',
        '<img src="images/logo_new.png" class="logo-img" alt="Like Zone Logo" style="height: 42px; width: auto; border-radius: 8px; box-shadow: 0 4px 15px rgba(59,130,246,0.4);" />',
        content
    )
    # Replace footer logo
    content = re.sub(
        r'<div class="logo-icon small-logo"[^>]*>\s*<i class="bi bi-phone-fill"></i>\s*</div>',
        '<img src="images/logo_new.png" class="logo-img-small" alt="Like Zone Logo" style="height: 36px; width: auto; border-radius: 6px;" />',
        content
    )
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done.")
