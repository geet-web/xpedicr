import os
import glob

base_dir = r"c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\xpedicr"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Update wa.me links
    content = content.replace("https://wa.me/918001234567", "https://wa.me/917289890080")
    
    # Update visible phone numbers
    content = content.replace("+91 800 123 4567", "+91 72898 90080")
    
    # Update input placeholders
    content = content.replace("+91 XXXXX XXXXX", "+91 72898 90080")
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Phone numbers updated successfully.")
