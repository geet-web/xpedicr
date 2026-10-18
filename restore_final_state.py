import os
import re

base_dir = r"c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\xpedicr"

# 1. Fix script.js
js_path = os.path.join(base_dir, "script.js")
with open(js_path, "r", encoding="utf-8") as f:
    js_content = f.read()

# Remove all scroll-to-top logic
js_content = re.sub(r'// Scroll to Top Logic.*?\}\);\s*\}\);', '', js_content, flags=re.DOTALL)
js_content = re.sub(r'// Scroll to Top Logic.*', '', js_content, flags=re.DOTALL)

clean_js = """
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
});
"""
# Make sure we don't duplicate the final }); if it was stripped
if not js_content.strip().endswith('});'):
    js_content += "\n});"

# Actually, the original script ended with });
# Let's just remove the scroll top logic entirely, and inject it right before the final });
js_content = js_content.replace('});\n});', '});')
if js_content.endswith('});'):
    js_content = js_content[:-3] + clean_js

with open(js_path, "w", encoding="utf-8") as f:
    f.write(js_content)


# 2. Fix ecosystem-services.html
ecosystem_path = os.path.join(base_dir, "ecosystem-services.html")
with open(ecosystem_path, "r", encoding="utf-8") as f:
    eco_content = f.read()

if "Visual Ecosystem Flow" not in eco_content:
    flow = """
    <!-- Visual Ecosystem Flow -->
    <section class="section-padding">
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
    eco_content = eco_content.replace('<!-- Footer -->', flow + '\n<!-- Footer -->')
    with open(ecosystem_path, "w", encoding="utf-8") as f:
        f.write(eco_content)


# 3. Fix future-partners.html
future_path = os.path.join(base_dir, "future-partners.html")
with open(future_path, "r", encoding="utf-8") as f:
    fut_content = f.read()

if "Our Expansion Strategy" not in fut_content:
    expansion = """
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
    fut_content = fut_content.replace('<!-- Footer -->', expansion + '\n<!-- Footer -->')
    with open(future_path, "w", encoding="utf-8") as f:
        f.write(fut_content)

print("Restored JS and missing HTML content.")
