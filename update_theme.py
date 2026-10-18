import os
import glob
import re

base_dir = r"c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\xpedicr"

# 1. Update style.css
style_path = os.path.join(base_dir, "style.css")
with open(style_path, "r", encoding="utf-8") as f:
    css = f.read()

new_root = """:root {
    /* Color Palette */
    --primary: #000000;       /* Black */
    --primary-light: #222222;
    --secondary: #000000;     /* Black */
    --secondary-dark: #111111;
    --accent: #F4F4F5;        /* Subtle secondary */
    
    /* Neutrals */
    --dark: #000000;
    --dark-gray: #333333;
    --gray: #666666;
    --light-gray: #A0A0A0;
    --light: #F9FAFB;
    --white: #FFFFFF;
"""
css = re.sub(r':root\s*\{.*?(?=/\* Typography \*/)', new_root + "    ", css, flags=re.DOTALL)

# Update founder gradient
css = css.replace("linear-gradient(rgba(5, 28, 51, 0.85), rgba(10, 61, 107, 0.9))", "linear-gradient(rgba(0, 0, 0, 0.8), rgba(17, 17, 17, 0.95))")

# Update orbs to white/grey
css = css.replace("background: var(--secondary);\n    filter: blur(120px);", "background: #ffffff;\n    filter: blur(120px);")
css = css.replace("background: #00e5ff;", "background: #f4f4f5;")

# Replace shadow-glow
css = css.replace("--shadow-glow: 0 0 25px rgba(0, 180, 125, 0.3);", "--shadow-glow: 0 0 25px rgba(0, 0, 0, 0.15);")

with open(style_path, "w", encoding="utf-8") as f:
    f.write(css)

# 2. Update HTML images
html_files = glob.glob(os.path.join(base_dir, "*.html"))
for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Hero image -> realistic hospital corridor or technology
    content = content.replace("images/hero_healthtech_1777033621396.png", "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?auto=format&fit=crop&q=80&w=1920")
    
    # About image -> realistic doctors / medical team
    content = content.replace("images/ecosystem_illustration_1777033648527.png", "https://images.unsplash.com/photo-1579684385127-1ef15d508118?auto=format&fit=crop&q=80&w=800")
    
    # Founder image -> realistic professional
    content = content.replace("https://images.unsplash.com/photo-1560250097-0b93528c311a?auto=format&fit=crop&q=80&w=256&h=256", "https://images.unsplash.com/photo-1559839734-2b71ea197ec2?auto=format&fit=crop&q=80&w=256&h=256")
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Theme and images updated.")
