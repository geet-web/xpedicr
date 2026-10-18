import os

base_dir = r"c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\xpedicr"
index_path = os.path.join(base_dir, "index.html")

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Define markers
header_end = content.find("<!-- Hero Section -->")
footer_start = content.find("<!-- Footer -->")

header = content[:header_end]
footer = content[footer_start:]

# Extract sections
# 1. About (About + Vision + Founder)
about_start = content.find("<!-- About Section -->")
ecosystem_start = content.find("<!-- Ecosystem Section -->")
about_section = content[about_start:ecosystem_start]

# 2. Ecosystem & Services
services_end = content.find("<!-- Future Expansion Plans & Partners Section -->")
ecosystem_section = content[ecosystem_start:services_end]

# 3. Future & Partners
careers_start = content.find("<!-- Careers & News Section -->")
future_section = content[services_end:careers_start]

# 4. Careers & News
contact_start = content.find("<!-- Contact Section -->")
careers_section = content[careers_start:contact_start]

# 5. Contact
contact_section = content[contact_start:footer_start]

def build_page(page_name, page_content, active_link):
    # Fix the navbar links
    new_header = header.replace('href="#home"', 'href="index.html"')
    new_header = new_header.replace('href="#about"', 'href="about.html"')
    new_header = new_header.replace('href="#ecosystem"', 'href="ecosystem-services.html"')
    new_header = new_header.replace('href="#future-partners"', 'href="future-partners.html"')
    new_header = new_header.replace('href="#careers-news"', 'href="careers-news.html"')
    new_header = new_header.replace('href="#contact"', 'href="contact.html"')
    
    # Add active class to main nav links and mobile nav links
    old_link = f'href="{active_link}"'
    new_link = f'href="{active_link}" class="active"'
    new_header = new_header.replace(old_link, new_link)
    
    # Fix the footer links
    new_footer = footer.replace('href="#about"', 'href="about.html"')
    new_footer = new_footer.replace('href="#ecosystem"', 'href="ecosystem-services.html"')
    new_footer = new_footer.replace('href="#future-partners"', 'href="future-partners.html"')
    new_footer = new_footer.replace('href="#careers-news"', 'href="careers-news.html"')
    new_footer = new_footer.replace('href="#contact"', 'href="contact.html"')
    
    # Add extra padding for first section on inner pages if not index
    if page_name != "index.html":
        # we can inject a div to push content down
        page_content = '<div style="height: 80px; background: var(--dark);"></div>\n' + page_content
        
    page = new_header + page_content + new_footer
    with open(os.path.join(base_dir, page_name), "w", encoding="utf-8") as f:
        f.write(page)

# Create Pages
build_page("about.html", about_section, "about.html")
build_page("ecosystem-services.html", ecosystem_section, "ecosystem-services.html")
build_page("future-partners.html", future_section, "future-partners.html")
build_page("careers-news.html", careers_section, "careers-news.html")
build_page("contact.html", contact_section, "contact.html")

# Update index.html
index_hero = content[header_end:about_start]
build_page("index.html", index_hero + about_section + ecosystem_section + future_section + careers_section + contact_section, "index.html")

print("All pages generated successfully.")
