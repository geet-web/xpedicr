import os
import glob
import re

base_dir = r"c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\xpedicr"

nav_links = {
    'index.html': 'Home',
    'about.html': 'About',
    'ecosystem-services.html': 'Ecosystem & Services',
    'nava-ai.html': 'Nava.ai',
    'future-partners.html': 'Future & Partners',
    'careers.html': 'Careers',
    'contact.html': 'Contact'
}

for file in glob.glob(os.path.join(base_dir, "*.html")):
    filename = os.path.basename(file)
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # Create the standard nav block
    nav_block = '<nav class="nav-links">\n'
    for link, text in nav_links.items():
        active = ' class="active"' if link == filename else ''
        nav_block += f'                <a href="{link}"{active}>{text}</a>\n'
    nav_block += '            </nav>'

    # Create standard mobile nav block
    mobile_nav_block = '<div class="mobile-nav-links">\n'
    for link, text in nav_links.items():
        active = ' class="active"' if link == filename else ''
        mobile_nav_block += f'            <a href="{link}"{active}>{text}</a>\n'
    mobile_nav_block += '            <a href="#" class="btn btn-accent mt-4 modal-trigger" data-modal="partnerModal">Partner With Us</a>\n        </div>'

    # Replace existing desktop nav-links
    content = re.sub(r'<nav class="nav-links">.*?</nav>', nav_block, content, flags=re.DOTALL)
    
    # Replace existing mobile-nav-links
    content = re.sub(r'<div class="mobile-nav-links">.*?</div>', mobile_nav_block, content, flags=re.DOTALL)

    with open(file, "w", encoding="utf-8") as f:
        f.write(content)

print("Navbar structure perfectly synchronized across all files.")
