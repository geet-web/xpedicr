import os
import glob

base_dir = r"c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\xpedicr"

# 1. Update index.html hero section
index_file = os.path.join(base_dir, "index.html")
with open(index_file, "r", encoding="utf-8") as f:
    content = f.read()
content = content.replace('<a href="#future-partners" class="btn btn-outline-dark btn-lg">Partner With Us</a>', '<a href="future-partners.html" class="btn btn-outline-dark btn-lg">Partner With Us</a>')
with open(index_file, "w", encoding="utf-8") as f:
    f.write(content)

# 2. Update navbar across all HTML
html_files = glob.glob(os.path.join(base_dir, "*.html"))
html_files = [f for f in html_files if "brochure.html" not in f]

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Desktop Navbar
    content = content.replace('<a href="future-partners.html" class="btn btn-outline-primary">Partner With Us</a>', '<a href="contact.html" class="btn btn-outline-primary">Partner With Us</a>')
    
    content = content.replace('<a href="future-partners.html" class="btn btn-outline-primary active">Partner With Us</a>', '<a href="contact.html" class="btn btn-outline-primary">Partner With Us</a>')
    
    # Mobile Navbar
    content = content.replace('<a href="future-partners.html" class="btn btn-primary mt-4">Partner With Us</a>', '<a href="contact.html" class="btn btn-primary mt-4">Partner With Us</a>')
    
    content = content.replace('<a href="future-partners.html" class="btn btn-primary mt-4 active">Partner With Us</a>', '<a href="contact.html" class="btn btn-primary mt-4">Partner With Us</a>')

    # Re-apply active class for contact.html ONLY
    if os.path.basename(file_path) == "contact.html":
        content = content.replace('<a href="contact.html" class="btn btn-outline-primary">Partner With Us</a>', '<a href="contact.html" class="btn btn-outline-primary active">Partner With Us</a>')
        content = content.replace('<a href="contact.html" class="btn btn-primary mt-4">Partner With Us</a>', '<a href="contact.html" class="btn btn-primary mt-4 active">Partner With Us</a>')

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Navbar links updated.")
