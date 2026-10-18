import os

base_dir = r"c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\xpedicr"
pages = ["about.html", "ecosystem-services.html", "future-partners.html", "careers-news.html", "contact.html"]

for page in pages:
    page_path = os.path.join(base_dir, page)
    if os.path.exists(page_path):
        with open(page_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        content = content.replace("<body>", '<body class="inner-page">')
        
        with open(page_path, "w", encoding="utf-8") as f:
            f.write(content)

print("Added inner-page class to body of all inner HTML pages.")
