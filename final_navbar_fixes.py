import os
import glob
import re

base_dir = r"c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\xpedicr"

# 1. Update text in all HTML files securely
for file in glob.glob(os.path.join(base_dir, "*.html")):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace the text
    content = content.replace("Careers &amp; News", "Careers")
    content = content.replace("Careers & News", "Careers")

    with open(file, "w", encoding="utf-8") as f:
        f.write(content)

# 2. Append CSS fixes for exact visual match to screenshot
css_append = """
/* Screenshot Match Overrides */
.navbar .logo-icon {
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    width: 40px !important;
    height: 40px !important;
    background: #111111 !important; /* Dark square */
    color: #2563EB !important; /* Blue heartbeat */
    border-radius: 10px !important;
    font-size: 20px !important;
}

.navbar .nav-links a {
    position: relative !important;
    padding-bottom: 6px !important;
}

.navbar .nav-links a.active::after {
    content: '' !important;
    position: absolute !important;
    bottom: 0 !important;
    left: 0 !important;
    width: 100% !important;
    height: 2px !important;
    background-color: #2563EB !important;
    border-radius: 2px !important;
}

/* Ensure mobile menu active state is visible but without absolute underline overlapping */
.mobile-menu .mobile-nav-links a.active::after {
    display: none !important;
}
"""

css_file = os.path.join(base_dir, "style.css")
with open(css_file, "a", encoding="utf-8") as f:
    f.write(css_append)

print("Final navbar text and visual fixes applied.")
