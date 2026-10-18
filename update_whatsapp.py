import os
import glob

base_dir = r"c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\xpedicr"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

whatsapp_link = 'href="https://wa.me/918001234567" target="_blank"'

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace floating whatsapp
    content = content.replace('<a href="#" class="floating-whatsapp"', f'<a {whatsapp_link} class="floating-whatsapp"')
    
    # Replace contact page chat now
    content = content.replace('<a href="#" class="btn btn-light btn-lg w-100"><i class="fa-brands fa-whatsapp text-success me-2"></i> Chat Now</a>', f'<a {whatsapp_link} class="btn btn-light btn-lg w-100"><i class="fa-brands fa-whatsapp text-success me-2"></i> Chat Now</a>')
    
    # Replace index page chat on whatsapp
    content = content.replace('<a href="#" class="btn btn-light whatsapp-btn"><i class="fa-brands fa-whatsapp text-success"></i> Chat on WhatsApp</a>', f'<a {whatsapp_link} class="btn btn-light whatsapp-btn"><i class="fa-brands fa-whatsapp text-success"></i> Chat on WhatsApp</a>')

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("WhatsApp links updated successfully across all HTML files.")
