import os
import re

base_dir = r"c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\xpedicr"

new_html = """    <!-- Horizontal Infrastructure Roadmap -->
    <section class="horizontal-roadmap-section">
        <div class="container" style="position: relative; z-index: 2;">
            <div class="section-title text-center scroll-reveal up">
                <h2 style="font-size: 3rem; font-weight: 800; letter-spacing: -1px; color: #111;">Infrastructure Roadmap</h2>
                <p style="font-size: 1.1rem; color: #6B7280; max-width: 600px; margin: 0 auto; margin-top: 16px;">A strategic timeline for building the healthcare ecosystem.</p>
            </div>
            
            <div class="h-roadmap-container scroll-reveal up delay-1">
                <div class="h-roadmap-track">
                    <div class="h-roadmap-progress"></div>
                </div>
                
                <div class="h-roadmap-grid">
                    <!-- 2026 -->
                    <div class="h-roadmap-item">
                        <div class="h-roadmap-node"></div>
                        <div class="h-roadmap-card">
                            <span class="h-year-badge">2026</span>
                            <i class="fa-solid fa-server h-card-icon d-block"></i>
                            <h4>Platform Expansion</h4>
                            <p>Establishing the core technology layer, onboarding primary urban hospitals, and launching unified digital routing protocols.</p>
                        </div>
                    </div>

                    <!-- 2027 -->
                    <div class="h-roadmap-item" style="transition-delay: 0.2s;">
                        <div class="h-roadmap-node"></div>
                        <div class="h-roadmap-card">
                            <span class="h-year-badge">2027</span>
                            <i class="fa-solid fa-truck-medical h-card-icon d-block"></i>
                            <h4>Ambulance Aggregation</h4>
                            <p>Unifying fragmented emergency response fleets and launching smart GPS dispatch systems to guarantee 10-minute response times.</p>
                        </div>
                    </div>

                    <!-- 2028 -->
                    <div class="h-roadmap-item" style="transition-delay: 0.4s;">
                        <div class="h-roadmap-node"></div>
                        <div class="h-roadmap-card">
                            <span class="h-year-badge">2028</span>
                            <i class="fa-solid fa-tower-cell h-card-icon d-block"></i>
                            <h4>Rural Healthcare Network</h4>
                            <p>Deploying advanced telemedicine nodes and decentralized diagnostic access points to heavily under-served regions.</p>
                        </div>
                    </div>

                    <!-- 2029 -->
                    <div class="h-roadmap-item" style="transition-delay: 0.6s;">
                        <div class="h-roadmap-node"></div>
                        <div class="h-roadmap-card">
                            <span class="h-year-badge">2029</span>
                            <i class="fa-solid fa-brain h-card-icon d-block"></i>
                            <h4>AI Infrastructure</h4>
                            <p>Full autonomous operational deployment of Nava.ai predictive support across the entire multi-city hospital network.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>"""

# Replace in future-partners.html
future_file = os.path.join(base_dir, "future-partners.html")
with open(future_file, "r", encoding="utf-8") as f:
    f_content = f.read()

pattern = r'<!-- Premium Infrastructure Roadmap -->.*?</section>'
f_content = re.sub(pattern, new_html, f_content, flags=re.DOTALL)

with open(future_file, "w", encoding="utf-8") as f:
    f.write(f_content)

# Add to index.html right above the Footer
index_file = os.path.join(base_dir, "index.html")
with open(index_file, "r", encoding="utf-8") as f:
    i_content = f.read()

if "Horizontal Infrastructure Roadmap" not in i_content:
    i_content = i_content.replace("<!-- Footer -->", new_html + "\n\n<!-- Footer -->")
    with open(index_file, "w", encoding="utf-8") as f:
        f.write(i_content)

# Append CSS
new_css = """
/* ==========================================================================
   HORIZONTAL PREMIUM ROADMAP
   ========================================================================== */
.horizontal-roadmap-section {
    position: relative;
    padding: 120px 0;
    background-color: #FFFFFF;
    overflow: hidden;
}

.horizontal-roadmap-section::before {
    content: '';
    position: absolute;
    top: 50%; left: 50%; transform: translate(-50%, -50%);
    width: 100%; height: 100%;
    background: radial-gradient(circle at center, rgba(37, 99, 235, 0.03) 0%, transparent 70%);
    z-index: 0;
    pointer-events: none;
}

.h-roadmap-container {
    position: relative;
    max-width: 1300px;
    margin: 80px auto 0;
    padding: 0 24px;
    z-index: 2;
}

/* The Horizontal Line */
.h-roadmap-track {
    position: absolute;
    top: 24px; /* Center of the 48px nodes */
    left: 12%; /* Starts a bit in */
    right: 12%;
    height: 3px;
    background: #E5E7EB;
    z-index: 1;
}

.h-roadmap-progress {
    position: absolute;
    top: 0; left: 0; height: 100%; width: 0%;
    background: linear-gradient(90deg, #2563EB, #60A5FA);
    box-shadow: 0 0 12px rgba(37,99,235,0.6);
    animation: hTimelineProgress 3s cubic-bezier(0.25, 1, 0.5, 1) forwards;
    animation-delay: 0.5s;
}

@keyframes hTimelineProgress {
    0% { width: 0%; }
    100% { width: 100%; }
}

.h-roadmap-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 32px;
    position: relative;
    z-index: 2;
}

.h-roadmap-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
}

.h-roadmap-node {
    width: 48px;
    height: 48px;
    background: #FFFFFF;
    border: 4px solid #2563EB;
    border-radius: 50%;
    box-shadow: 0 0 0 8px rgba(37, 99, 235, 0.1);
    z-index: 4;
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    margin-bottom: 40px;
    position: relative;
}

.h-roadmap-node::after {
    content: '';
    position: absolute;
    top: -12px; left: -12px; right: -12px; bottom: -12px;
    border-radius: 50%;
    border: 2px solid rgba(37, 99, 235, 0.3);
    animation: hNodePulse 2.5s infinite;
}

@keyframes hNodePulse {
    0% { transform: scale(0.8); opacity: 1; }
    100% { transform: scale(1.4); opacity: 0; }
}

.h-roadmap-item:hover .h-roadmap-node {
    background: #2563EB;
    box-shadow: 0 0 25px rgba(37, 99, 235, 0.4);
    transform: scale(1.15);
    border-color: #FFFFFF;
}

/* Premium Card */
.h-roadmap-card {
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(229, 231, 235, 0.8);
    border-radius: 24px;
    padding: 32px 24px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.03);
    transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
    position: relative;
    overflow: hidden;
    width: 100%;
}

.h-roadmap-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; height: 4px;
    background: transparent;
    transition: all 0.4s ease;
}

.h-roadmap-item:hover .h-roadmap-card {
    transform: translateY(-8px);
    box-shadow: 0 20px 40px rgba(37, 99, 235, 0.08);
    border-color: rgba(37, 99, 235, 0.3);
    background: #FFFFFF;
}

.h-roadmap-item:hover .h-roadmap-card::before {
    background: linear-gradient(90deg, #2563EB, #60A5FA);
}

.h-year-badge {
    display: inline-block;
    background: linear-gradient(135deg, #2563EB, #1D4ED8);
    color: #FFFFFF;
    font-size: 15px;
    font-weight: 700;
    padding: 6px 16px;
    border-radius: 20px;
    margin-bottom: 20px;
    box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
    letter-spacing: 1px;
}

.h-card-icon {
    font-size: 32px;
    color: #9CA3AF;
    margin-bottom: 20px;
    transition: all 0.4s ease;
}

.h-roadmap-item:hover .h-card-icon {
    color: #2563EB;
    transform: scale(1.1);
}

.h-roadmap-card h4 {
    font-size: 20px;
    font-weight: 700;
    color: #111111;
    margin-bottom: 12px;
    font-family: 'Poppins', sans-serif;
    letter-spacing: -0.5px;
}

.h-roadmap-card p {
    font-size: 14.5px;
    color: #6B7280;
    margin: 0;
    line-height: 1.6;
}

/* Responsive */
@media (max-width: 1200px) {
    .h-roadmap-card { padding: 24px 16px; }
    .h-roadmap-card h4 { font-size: 18px; }
}

@media (max-width: 992px) {
    .h-roadmap-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 64px 32px;
    }
    .h-roadmap-track {
        display: none; /* Hide continuous track on tablet wrapping */
    }
}

@media (max-width: 768px) {
    .h-roadmap-grid {
        grid-template-columns: 1fr;
        gap: 32px;
    }
    .h-roadmap-item {
        flex-direction: row;
        align-items: center;
        text-align: left;
        gap: 24px;
    }
    .h-roadmap-node {
        margin-bottom: 0;
        flex-shrink: 0;
    }
    /* Recreate vertical line for mobile */
    .h-roadmap-container::before {
        content: '';
        position: absolute;
        top: 0; bottom: 0;
        left: 48px; /* 24px padding + 24px half node */
        width: 2px;
        background: #E5E7EB;
        z-index: 1;
    }
}
"""

css_file = os.path.join(base_dir, "style.css")
with open(css_file, "a", encoding="utf-8") as f:
    f.write(new_css)

print("Horizontal Roadmap implemented successfully.")
