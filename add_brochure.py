import os
import glob

base_dir = r"c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\xpedicr"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

# 1. Create the dummy brochure file
brochure_path = os.path.join(base_dir, "Xpedicr_Corporate_Brochure.txt")
brochure_content = """=========================================================
          XPEDICR INDUSTRY PVT. LTD.
         Corporate Brochure - 2026
=========================================================

Welcome to Xpedicr.

We are building India's future healthcare infrastructure 
through technology, partnerships, logistics, and innovation.

--- OUR BRANDS ---
1. Nidhaan - 10-Minute Emergency Medical Services
2. Nava.ai - Deep Learning AI Diagnostic Platform
3. Viora - High-End Wellness & Personalized Care

--- BY THE NUMBERS ---
- 500+ Partner Clinics
- 50+ Cities Expansion Ready
- 8 Service Categories

--- CONTACT US ---
Email: partners@xpedicr.in
Phone: +91 72898 90080
WhatsApp: https://wa.me/917289890080
Headquarters: Tech Park, Electronic City, Bengaluru, India

=========================================================
This is a generated dummy brochure document.
=========================================================
"""
with open(brochure_path, "w", encoding="utf-8") as f:
    f.write(brochure_content)

# 2. Update the links in all HTML files
old_link = '<a href="#" class="btn btn-outline-light btn-sm"><i class="fa-solid fa-download me-2"></i> Download Corporate Brochure</a>'
new_link = '<a href="Xpedicr_Corporate_Brochure.txt" download="Xpedicr_Corporate_Brochure_2026.txt" target="_blank" class="btn btn-outline-light btn-sm"><i class="fa-solid fa-download me-2"></i> Download Corporate Brochure</a>'

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    content = content.replace(old_link, new_link)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Brochure created and links updated globally.")
