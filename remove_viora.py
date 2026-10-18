import os
import glob

def remove_viora():
    html_files = glob.glob('*.html')
    
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Common text replacements
        content = content.replace('<li><a href="ecosystem-services.html">Viora</a></li>\n', '')
        content = content.replace('<li><a href="ecosystem-services.html">Viora</a></li>', '')
        content = content.replace('(Nidhaan, Nava.ai, Viora)', '(Nidhaan, Nava.ai)')
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

remove_viora()
