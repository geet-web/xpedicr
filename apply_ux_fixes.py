import os
import re
import glob

base_dir = r"c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\xpedicr"

def update_file(filename, replacements):
    filepath = os.path.join(base_dir, filename)
    if not os.path.exists(filepath):
        return
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    for old, new in replacements:
        content = re.sub(old, new, content, flags=re.IGNORECASE | re.DOTALL)
        
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

# A & F: Fix unverified stats and misleading hub claims across files
global_replacements = [
    (r'nationwide transformation', 'healthcare infrastructure transformation'),
    (r'Nationwide Vision', 'Ecosystem Vision'),
    (r'nationwide healthcare dominance', 'enabling healthcare connectivity'),
    (r'India’s largest', 'Building healthcare infrastructure'),
    (r'leading healthcare hub', 'Developing healthcare ecosystem'),
    (r'<h3 class="stat-number">500\+</h3>', '<h3>Extensive Network</h3>'),
    (r'<h3 class="stat-number">50\+</h3>', '<h3>Growing Reach</h3>'),
    (r'<div class="stats-container">.*?</div>\s*</div>\s*</div>', '<div class="stats-container"><div class="stat-item"><h2>Ecosystem Infrastructure</h2><p>Connecting patients, clinics, and labs.</p></div></div>')
]

for file in glob.glob(os.path.join(base_dir, "*.html")):
    update_file(os.path.basename(file), global_replacements)

# B: Add Partner Logos to index.html
partner_section = """
    <!-- Pilot Collaborations -->
    <section class="partners section-padding py-5 border-top border-bottom" style="background-color: var(--white);">
        <div class="container text-center">
            <span class="subtitle text-muted small text-uppercase" style="letter-spacing: 2px;">Pilot Collaborations & Ecosystem Partners</span>
            <div class="d-flex justify-content-center align-items-center flex-wrap mt-4" style="gap: 40px; opacity: 0.6; filter: grayscale(100%);">
                <!-- Grayscale placeholder partner logos -->
                <div style="font-weight: 700; font-size: 1.2rem; color: #111;"><i class="fa-solid fa-hospital me-2"></i> CityCare Hospitals</div>
                <div style="font-weight: 700; font-size: 1.2rem; color: #111;"><i class="fa-solid fa-flask me-2"></i> Prime Diagnostics</div>
                <div style="font-weight: 700; font-size: 1.2rem; color: #111;"><i class="fa-solid fa-truck-medical me-2"></i> RapidResponse</div>
                <div style="font-weight: 700; font-size: 1.2rem; color: #111;"><i class="fa-solid fa-pills me-2"></i> PharmaConnect</div>
            </div>
        </div>
    </section>
"""
index_path = os.path.join(base_dir, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    idx_content = f.read()
if "Pilot Collaborations & Ecosystem Partners" not in idx_content:
    idx_content = idx_content.replace('<!-- About Section -->', partner_section + '\n    <!-- About Section -->')
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(idx_content)

# C: Expand Ecosystem Page
ecosystem_flow = """
    <!-- Visual Ecosystem Flow -->
    <section class="section-padding bg-light">
        <div class="container">
            <div class="section-title text-center scroll-reveal up">
                <h2>Visual Ecosystem Flow</h2>
                <p>How Xpedicr connects the healthcare journey end-to-end.</p>
            </div>
            
            <div class="d-flex flex-column flex-md-row justify-content-between align-items-center text-center mt-5 scroll-reveal up" style="gap: 20px;">
                <div class="card p-4 shadow-sm" style="flex: 1;"><i class="fa-solid fa-user fa-2x text-primary mb-3"></i><h5>1. User Request</h5></div>
                <i class="fa-solid fa-arrow-right text-muted d-none d-md-block"></i>
                <div class="card p-4 shadow-sm" style="flex: 1;"><i class="fa-solid fa-user-doctor fa-2x text-primary mb-3"></i><h5>2. Consultation</h5></div>
                <i class="fa-solid fa-arrow-right text-muted d-none d-md-block"></i>
                <div class="card p-4 shadow-sm" style="flex: 1;"><i class="fa-solid fa-microscope fa-2x text-primary mb-3"></i><h5>3. Diagnostics</h5></div>
                <i class="fa-solid fa-arrow-right text-muted d-none d-md-block"></i>
                <div class="card p-4 shadow-sm" style="flex: 1;"><i class="fa-solid fa-pills fa-2x text-primary mb-3"></i><h5>4. Medicine</h5></div>
                <i class="fa-solid fa-arrow-right text-muted d-none d-md-block"></i>
                <div class="card p-4 shadow-sm" style="flex: 1;"><i class="fa-solid fa-truck-medical fa-2x text-primary mb-3"></i><h5>5. Emergency</h5></div>
            </div>
        </div>
    </section>
"""
update_file("ecosystem-services.html", [(r'<!-- Services Section -->', ecosystem_flow + '\n    <!-- Services Section -->')])

# D & E: Expand Future & Partners Page, add Roadmap
future_expansion = """
    <!-- Detailed Expansion Strategy -->
    <section class="section-padding">
        <div class="container">
            <div class="section-title text-center scroll-reveal up mb-5">
                <h2>Our Expansion Strategy</h2>
                <p>Why partnerships matter and how we operationalize our healthcare network.</p>
            </div>
            <div class="row g-4 scroll-reveal up">
                <div class="col-md-6">
                    <div class="card p-4 h-100 shadow-sm border-0 bg-light">
                        <h4 class="text-primary mb-3"><i class="fa-solid fa-network-wired me-2"></i> Technology Infrastructure</h4>
                        <p>We are deploying scalable nodes connecting pharmacies, labs, and clinics into a unified platform. This reduces administrative overhead and enables real-time data sharing.</p>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="card p-4 h-100 shadow-sm border-0 bg-light">
                        <h4 class="text-primary mb-3"><i class="fa-solid fa-truck-medical me-2"></i> Ambulance Aggregation</h4>
                        <p>Fragmented emergency response times cost lives. We are digitally unifying ambulance fleets to ensure rapid, GPS-routed dispatch.</p>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="card p-4 h-100 shadow-sm border-0 bg-light">
                        <h4 class="text-primary mb-3"><i class="fa-solid fa-map-location-dot me-2"></i> Rural Healthcare Access</h4>
                        <p>Tier 2 and Tier 3 cities lack specialized care. By expanding telemedicine and localized diagnostic hubs, we bridge the geographical divide.</p>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="card p-4 h-100 shadow-sm border-0 bg-light">
                        <h4 class="text-primary mb-3"><i class="fa-solid fa-brain me-2"></i> AI Healthcare Integration</h4>
                        <p>Nava.ai will serve as the intelligent routing layer, predicting demand spikes and automating triage to optimize provider workflows.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Professional Timeline -->
    <section class="section-padding bg-light">
        <div class="container">
            <div class="section-title text-center scroll-reveal up mb-5">
                <h2>Infrastructure Roadmap</h2>
                <p>A strategic timeline for building the healthcare ecosystem.</p>
            </div>
            <div class="timeline-wrapper scroll-reveal up" style="max-width: 800px; margin: 0 auto; padding-left: 20px; border-left: 2px solid #2563EB;">
                <div style="position: relative; margin-bottom: 30px; padding-left: 30px;">
                    <div style="position: absolute; left: -37px; top: 0; width: 12px; height: 12px; background: #2563EB; border-radius: 50%; border: 2px solid white; box-shadow: 0 0 0 4px #2563EB;"></div>
                    <h5 class="text-primary fw-bold">2026 &rarr; Platform Expansion</h5>
                    <p class="text-muted">Establishing the core technology layer and aggregating primary urban partners.</p>
                </div>
                <div style="position: relative; margin-bottom: 30px; padding-left: 30px;">
                    <div style="position: absolute; left: -37px; top: 0; width: 12px; height: 12px; background: #2563EB; border-radius: 50%; border: 2px solid white; box-shadow: 0 0 0 4px #2563EB;"></div>
                    <h5 class="text-primary fw-bold">2027 &rarr; Ambulance Aggregation</h5>
                    <p class="text-muted">Unifying emergency response fleets and launching smart GPS dispatch systems.</p>
                </div>
                <div style="position: relative; margin-bottom: 30px; padding-left: 30px;">
                    <div style="position: absolute; left: -37px; top: 0; width: 12px; height: 12px; background: #2563EB; border-radius: 50%; border: 2px solid white; box-shadow: 0 0 0 4px #2563EB;"></div>
                    <h5 class="text-primary fw-bold">2028 &rarr; Rural Healthcare Network</h5>
                    <p class="text-muted">Deploying telemedicine nodes and diagnostic access points to under-served regions.</p>
                </div>
                <div style="position: relative; margin-bottom: 30px; padding-left: 30px;">
                    <div style="position: absolute; left: -37px; top: 0; width: 12px; height: 12px; background: #2563EB; border-radius: 50%; border: 2px solid white; box-shadow: 0 0 0 4px #2563EB;"></div>
                    <h5 class="text-primary fw-bold">2029 &rarr; AI Healthcare Infrastructure</h5>
                    <p class="text-muted">Full autonomous operational deployment of Nava.ai predictive support.</p>
                </div>
            </div>
        </div>
    </section>
"""
# Insert into future-partners.html
update_file("future-partners.html", [(r'<!-- Vision Section -->', future_expansion + '\n    <!-- Vision Section -->')])

# G: Scroll-to-Top CSS and JS
scroll_css = """
/* Scroll to Top */
.scroll-top-btn {
    position: fixed;
    bottom: 30px;
    right: 30px;
    width: 48px;
    height: 48px;
    background-color: #111111;
    color: #FFFFFF;
    border: none;
    border-radius: 50%;
    font-size: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
    opacity: 0;
    visibility: hidden;
    transform: translateY(20px);
    transition: all 0.3s ease;
    z-index: 9999;
}
.scroll-top-btn:hover {
    background-color: #2563EB;
    transform: translateY(15px);
}
.scroll-top-btn.visible {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
}
"""
css_path = os.path.join(base_dir, "style.css")
with open(css_path, "a", encoding="utf-8") as f:
    f.write(scroll_css)

scroll_js = """
    // Scroll to Top Logic
    const scrollTopBtn = document.createElement('button');
    scrollTopBtn.className = 'scroll-top-btn';
    scrollTopBtn.innerHTML = '<i class="fa-solid fa-arrow-up"></i>';
    document.body.appendChild(scrollTopBtn);

    window.addEventListener('scroll', () => {
        if (window.scrollY > 400) {
            scrollTopBtn.classList.add('visible');
        } else {
            scrollTopBtn.classList.remove('visible');
        }
    });

    scrollTopBtn.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
"""
js_path = os.path.join(base_dir, "script.js")
with open(js_path, "a", encoding="utf-8") as f:
    f.write(scroll_js)

print("UX fixes applied.")
