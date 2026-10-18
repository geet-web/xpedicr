import os
import re

base_dir = r"c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\xpedicr"

new_html = """    <!-- Premium Expansion Strategy -->
    <section class="premium-strategy-section">
        <div class="container">
            <div class="section-title text-center scroll-reveal up">
                <h2 style="font-size: 3rem; font-weight: 800; letter-spacing: -1px; color: #111;">Our Expansion Strategy</h2>
                <p style="font-size: 1.1rem; color: #6B7280; max-width: 600px; margin: 0 auto; margin-top: 16px;">Why partnerships matter and how we operationalize our healthcare network.</p>
            </div>
            
            <div class="strategy-grid scroll-reveal up delay-1">
                <!-- Card 1 -->
                <div class="strategy-card">
                    <div class="strategy-card-header">
                        <div class="strategy-icon-wrap">
                            <i class="fa-solid fa-network-wired"></i>
                        </div>
                        <h4>Technology Infrastructure</h4>
                    </div>
                    <p>We are deploying scalable nodes connecting pharmacies, labs, and clinics into a unified platform. This reduces administrative overhead and enables real-time data sharing.</p>
                </div>
                
                <!-- Card 2 -->
                <div class="strategy-card" style="transition-delay: 0.1s;">
                    <div class="strategy-card-header">
                        <div class="strategy-icon-wrap">
                            <i class="fa-solid fa-truck-medical"></i>
                        </div>
                        <h4>Ambulance Aggregation</h4>
                    </div>
                    <p>Fragmented emergency response times cost lives. We are digitally unifying ambulance fleets to ensure rapid, GPS-routed dispatch.</p>
                </div>

                <!-- Card 3 -->
                <div class="strategy-card" style="transition-delay: 0.2s;">
                    <div class="strategy-card-header">
                        <div class="strategy-icon-wrap">
                            <i class="fa-solid fa-map-location-dot"></i>
                        </div>
                        <h4>Rural Healthcare Access</h4>
                    </div>
                    <p>Tier 2 and Tier 3 cities lack specialized care. By expanding telemedicine and localized diagnostic hubs, we bridge the geographical divide.</p>
                </div>

                <!-- Card 4 -->
                <div class="strategy-card" style="transition-delay: 0.3s;">
                    <div class="strategy-card-header">
                        <div class="strategy-icon-wrap">
                            <i class="fa-solid fa-brain"></i>
                        </div>
                        <h4>AI Healthcare Integration</h4>
                    </div>
                    <p>Nava.ai will serve as the intelligent routing layer, predicting demand spikes and automating triage to optimize provider workflows.</p>
                </div>
            </div>
        </div>
    </section>"""

# Replace in future-partners.html
html_file = os.path.join(base_dir, "future-partners.html")
with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

pattern = r'<!-- Detailed Expansion Strategy -->.*?</section>'
content = re.sub(pattern, new_html, content, flags=re.DOTALL)

with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)

# Append CSS
new_css = """
/* ==========================================================================
   PREMIUM EXPANSION STRATEGY
   ========================================================================== */
.premium-strategy-section {
    position: relative;
    padding: 120px 0;
    background-color: #FFFFFF;
    overflow: hidden;
    z-index: 1;
}

/* Faint grid texture & glow */
.premium-strategy-section::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background-image: 
        linear-gradient(rgba(37, 99, 235, 0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(37, 99, 235, 0.03) 1px, transparent 1px);
    background-size: 40px 40px;
    z-index: -2;
}

.premium-strategy-section::after {
    content: '';
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    width: 1000px;
    height: 1000px;
    background: radial-gradient(circle, rgba(37, 99, 235, 0.05) 0%, rgba(255, 255, 255, 0) 70%);
    z-index: -1;
    pointer-events: none;
}

/* Premium Card Grid */
.strategy-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 32px;
    margin-top: 64px;
    position: relative;
    z-index: 2;
}

.strategy-card {
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(229, 231, 235, 0.9);
    border-radius: 24px;
    padding: 40px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.02);
    transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
}

/* Corner Glow Effect */
.strategy-card::before {
    content: '';
    position: absolute;
    top: -50px;
    right: -50px;
    width: 150px;
    height: 150px;
    background: radial-gradient(circle, rgba(37, 99, 235, 0.12) 0%, rgba(255, 255, 255, 0) 70%);
    border-radius: 50%;
    opacity: 0;
    transition: all 0.5s ease;
    pointer-events: none;
}

.strategy-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 25px 60px rgba(37, 99, 235, 0.08);
    border-color: rgba(37, 99, 235, 0.3);
    background: #FFFFFF;
}

.strategy-card:hover::before {
    opacity: 1;
    transform: scale(1.5);
}

/* Card Header (Icon + Title) */
.strategy-card-header {
    display: flex;
    align-items: center;
    gap: 20px;
    margin-bottom: 24px;
}

.strategy-icon-wrap {
    width: 64px;
    height: 64px;
    border-radius: 16px;
    background: linear-gradient(135deg, rgba(37, 99, 235, 0.05), rgba(96, 165, 250, 0.1));
    border: 1px solid rgba(37, 99, 235, 0.15);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 26px;
    color: #2563EB;
    flex-shrink: 0;
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.strategy-card:hover .strategy-icon-wrap {
    background: linear-gradient(135deg, #2563EB, #60A5FA);
    color: #FFFFFF;
    box-shadow: 0 10px 25px rgba(37, 99, 235, 0.3);
    transform: scale(1.1);
    border-color: transparent;
}

.strategy-card h4 {
    font-size: 22px;
    font-weight: 700;
    color: #111111;
    margin: 0;
    font-family: 'Poppins', sans-serif;
    letter-spacing: -0.5px;
    transition: color 0.3s ease;
}

.strategy-card p {
    font-size: 15.5px;
    color: #6B7280;
    margin: 0;
    line-height: 1.7;
}

@media (max-width: 992px) {
    .strategy-grid {
        grid-template-columns: 1fr;
        gap: 24px;
    }
    .strategy-card {
        padding: 32px 24px;
    }
}
"""

css_file = os.path.join(base_dir, "style.css")
with open(css_file, "a", encoding="utf-8") as f:
    f.write(new_css)

print("Premium Expansion Strategy implemented successfully.")
