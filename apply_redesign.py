import os
import re
import glob

base_dir = r"c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\xpedicr"

def process_html_files():
    files = glob.glob(os.path.join(base_dir, "*.html"))
    for file_path in files:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Update Navbar links
        content = content.replace('href="about.html">About Us</a>', 'href="about.html">About</a>')
        content = content.replace('href="careers.html">Careers</a>', 'href="careers.html">Careers & News</a>')
        
        # Add Nava.ai to Navbar if not present
        if 'href="nava-ai.html">Nava.ai</a>' not in content:
            content = content.replace(
                '<a href="ecosystem-services.html">Ecosystem & Services</a>',
                '<a href="ecosystem-services.html">Ecosystem & Services</a>\n                <a href="nava-ai.html">Nava.ai</a>'
            )

        # Remove glow blobs
        content = re.sub(r'<div class="glow-blob primary"></div>\s*', '', content)
        content = re.sub(r'<div class="glow-blob secondary"></div>\s*', '', content)
        
        # Remove text-gradient and replace with text-primary
        content = content.replace('class="text-gradient"', 'class="text-primary"')

        # Specific index.html changes
        if "index.html" in file_path:
            # 1. Add Trust Bar after Hero Section
            if 'class="trust-bar"' not in content:
                trust_bar = """
    <!-- Trust Bar -->
    <div class="trust-bar section-padding py-4" style="background-color: var(--bg-alt); border-bottom: 1px solid #e5e7eb;">
        <div class="container">
            <div class="row text-center align-items-center" style="display: flex; justify-content: space-between; gap: 20px;">
                <div class="col-md-3"><i class="fa-solid fa-microchip text-primary me-2"></i> <strong>Healthcare Technology</strong></div>
                <div class="col-md-3"><i class="fa-solid fa-handshake text-primary me-2"></i> <strong>Strategic Partnerships</strong></div>
                <div class="col-md-3"><i class="fa-solid fa-laptop-medical text-primary me-2"></i> <strong>Digital Healthcare</strong></div>
                <div class="col-md-3"><i class="fa-solid fa-network-wired text-primary me-2"></i> <strong>Future-Ready Infrastructure</strong></div>
            </div>
        </div>
    </div>
"""
                content = content.replace('</section>\n\n    <!-- About Section -->', '</section>\n' + trust_bar + '\n    <!-- About Section -->')

            # 2. Remove Stats Grid
            content = re.sub(r'<div class="stats-grid mt-4">.*?</div>\s*</div>\s*</div>', r'</div></div>', content, flags=re.DOTALL)

            
            # 3. Founder section layout (Remove bg-dark)
            content = content.replace('class="founder section-padding bg-dark text-white"', 'class="founder section-padding bg-light text-dark"')
            content = content.replace('alt="CEO">', 'alt="Founder" style="filter: grayscale(100%);">')
            content = content.replace('<h4>Founder & CEO</h4>', '<h4 class="text-dark">Founder & CEO</h4>')

            # 4. Add News/Updates section before Contact Preview if not present
            if 'News & Updates' not in content:
                news_section = """
    <!-- News & Updates -->
    <section class="news section-padding bg-light">
        <div class="container">
            <div class="section-title text-center scroll-reveal up">
                <h2>News & Updates</h2>
            </div>
            <div class="row g-4">
                <div class="col-md-4 scroll-reveal up">
                    <div class="card p-0 shadow-sm rounded-lg" style="overflow: hidden; border: none;">
                        <img src="https://images.unsplash.com/photo-1551076805-e1869033e561?auto=format&fit=crop&q=80&w=600" alt="News" style="height: 200px; object-fit: cover; width: 100%;">
                        <div class="p-4">
                            <span class="text-muted small">Announcements</span>
                            <h4 class="mt-2 mb-3">Xpedicr Announces Strategic Hospital Partnerships</h4>
                        </div>
                    </div>
                </div>
                <div class="col-md-4 scroll-reveal up delay-1">
                    <div class="card p-0 shadow-sm rounded-lg" style="overflow: hidden; border: none;">
                        <img src="https://images.unsplash.com/photo-1516549655169-df83a0774514?auto=format&fit=crop&q=80&w=600" alt="News" style="height: 200px; object-fit: cover; width: 100%;">
                        <div class="p-4">
                            <span class="text-muted small">Launches</span>
                            <h4 class="mt-2 mb-3">Nava.ai Pilot Phase Initiated for Diagnostics</h4>
                        </div>
                    </div>
                </div>
                <div class="col-md-4 scroll-reveal up delay-2">
                    <div class="card p-0 shadow-sm rounded-lg" style="overflow: hidden; border: none;">
                        <img src="https://images.unsplash.com/photo-1505751172876-fa1923c5c528?auto=format&fit=crop&q=80&w=600" alt="News" style="height: 200px; object-fit: cover; width: 100%;">
                        <div class="p-4">
                            <span class="text-muted small">Company Updates</span>
                            <h4 class="mt-2 mb-3">Expanding our Digital Telemedicine Reach</h4>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""
                content = content.replace('<!-- Final CTA / Contact Preview -->', news_section + '\n    <!-- Final CTA / Contact Preview -->')

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Processed {file_path}")

def update_css():
    css_path = os.path.join(base_dir, "style.css")
    with open(css_path, "r", encoding="utf-8") as f:
        css = f.read()

    # Force White/Black/Blue system
    css = re.sub(r'--bg-alt:\s*#F8F9FA;', '--bg-alt: #F9FAFB;', css)
    css = re.sub(r'--primary:\s*[^;]+;', '--primary: #000000;', css)
    css = re.sub(r'--accent:\s*[^;]+;', '--accent: #2563EB;', css)
    
    # Remove gradient logic entirely and enforce solid colors
    css = re.sub(r'\.text-gradient\s*\{[^}]*\}', '', css)
    css = css + '''
    /* Modern Redesign Overrides */
    body { background-color: #FFFFFF; color: #111827; }
    h1, h2, h3, h4, h5, h6 { color: #111111; }
    .bg-dark { background-color: #111111 !important; color: #FFFFFF !important; }
    .bg-light { background-color: #F9FAFB !important; color: #111827 !important; }
    .text-primary { color: #2563EB !important; }
    .card { background-color: #FFFFFF; border: 1px solid #E5E7EB; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05); }
    .card:hover { border-color: #2563EB; transform: translateY(-4px); }
    .navbar { background-color: #FFFFFF; border-bottom: 1px solid #E5E7EB; }
    .nav-links a { color: #111111; }
    .nav-links a:hover, .nav-links a.active { color: #2563EB; }
    '''

    with open(css_path, "w", encoding="utf-8") as f:
        f.write(css)
    print("Updated style.css")

def create_nava_page():
    # We will copy ecosystem-services.html to nava-ai.html and modify it
    ecosystem_path = os.path.join(base_dir, "ecosystem-services.html")
    nava_path = os.path.join(base_dir, "nava-ai.html")
    
    with open(ecosystem_path, "r", encoding="utf-8") as f:
        nava_content = f.read()

    nava_content = nava_content.replace('<title>Xpedicr Industry Pvt. Ltd. | Ecosystem & Services</title>', '<title>Xpedicr Industry Pvt. Ltd. | Nava.ai</title>')
    nava_content = re.sub(r'<!-- Hero Section -->.*?<!-- Ecosystem Overview -->', '''
    <!-- Hero Section -->
    <section class="hero inner-hero bg-dark text-white" style="padding: 160px 0 80px; text-align: center;">
        <div class="container">
            <h1 class="fade-in-up text-white">Nava.ai</h1>
            <p class="fade-in-up delay-1 text-light-gray" style="max-width: 600px; margin: 0 auto;">Future healthcare intelligence platform. Empowering operational efficiency through predictive support and automation.</p>
        </div>
    </section>

    <section class="section-padding">
        <div class="container">
            <div class="row align-items-center mb-5">
                <div class="col-md-6 scroll-reveal up">
                    <h2 class="mb-4">Future Healthcare Intelligence</h2>
                    <p class="text-muted mb-4">Nava.ai is our proprietary artificial intelligence platform designed specifically for healthcare operational efficiency. We do not believe in fake dashboards—we believe in backend intelligence that drives real-world outcomes.</p>
                    <p class="text-muted mb-4">By analyzing vast amounts of operational data, Nava.ai predicts demand, automates triage, and optimizes the routing of our emergency and delivery fleets.</p>
                </div>
                <div class="col-md-6 scroll-reveal up delay-1">
                    <img src="https://images.unsplash.com/photo-1555255707-c07966088b7b?auto=format&fit=crop&q=80&w=800" alt="AI Technology" class="rounded-lg shadow-sm" style="border-radius: 8px;">
                </div>
            </div>
            
            <h2 class="text-center mb-5 mt-5 scroll-reveal up">Core Capabilities</h2>
            <div class="row g-4 scroll-reveal up">
                <div class="col-md-4">
                    <div class="card p-4 text-center h-100 shadow-sm" style="border: 1px solid #E5E7EB;">
                        <i class="fa-solid fa-chart-pie text-primary mb-3" style="font-size: 2rem;"></i>
                        <h4 class="text-dark">Predictive Support</h4>
                        <p class="text-muted small">Anticipating medical resource demands regionally.</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card p-4 text-center h-100 shadow-sm" style="border: 1px solid #E5E7EB;">
                        <i class="fa-solid fa-robot text-primary mb-3" style="font-size: 2rem;"></i>
                        <h4 class="text-dark">Smart Patient Assistance</h4>
                        <p class="text-muted small">Automated preliminary triage and routing.</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card p-4 text-center h-100 shadow-sm" style="border: 1px solid #E5E7EB;">
                        <i class="fa-solid fa-gears text-primary mb-3" style="font-size: 2rem;"></i>
                        <h4 class="text-dark">Healthcare Automation</h4>
                        <p class="text-muted small">Reducing administrative burden for partners.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- End Nava -->''', nava_content, flags=re.DOTALL)

    with open(nava_path, "w", encoding="utf-8") as f:
        f.write(nava_content)
    print("Created nava-ai.html")

if __name__ == "__main__":
    process_html_files()
    update_css()
    create_nava_page()
