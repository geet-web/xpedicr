import os
import glob
import re

def remove_viora_everywhere():
    # 1. Update all HTML files
    html_files = glob.glob('*.html')
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Remove the Viora card section from ecosystem-services.html or any other file
        viora_card_pattern = r'<div class="brand-detail-card scroll-reveal up">\s*<div class="brand-detail-icon"><i class="fa-solid fa-heart-pulse"></i></div>\s*<div class="brand-detail-content">\s*<span class="subtitle glow-text">Connected Devices</span>\s*<h3>Viora</h3>.*?</div>\s*</div>'
        content = re.sub(viora_card_pattern, '', content, flags=re.DOTALL)
        
        # General text replacements
        content = content.replace(' (Nidhaan, Nava.ai, Viora)', ' (Nidhaan, Nava.ai)')
        content = content.replace('Nidhaan, Nava.ai, and Viora', 'Nidhaan and Nava.ai')
        content = content.replace('Nidhaan, Nava.ai, Viora', 'Nidhaan, Nava.ai')
        content = content.replace('<li><a href="ecosystem-services.html">Viora</a></li>\n', '')
        content = content.replace('<li><a href="ecosystem-services.html">Viora</a></li>', '')
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")

    # 2. Update Python scripts that might re-add it
    py_files = ['add_modals.py', 'add_news_article.py', 'create_html_brochure.py']
    for file in py_files:
        if os.path.exists(file):
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            content = content.replace(' (Nidhaan, Nava.ai, Viora)', ' (Nidhaan, Nava.ai)')
            content = content.replace('Nidhaan, Nava.ai, and Viora', 'Nidhaan and Nava.ai')
            content = content.replace('Nidhaan, Nava.ai, Viora', 'Nidhaan, Nava.ai')
            
            # Remove Viora list items in create_html_brochure.py
            if file == 'create_html_brochure.py':
                content = re.sub(r'<h4>Viora</h4>.*?</div>', '', content, flags=re.DOTALL)

            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {file}")

if __name__ == "__main__":
    remove_viora_everywhere()
