import os
import re

base_dir = r"c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\xpedicr"

new_html = """    <!-- Cinematic Zig-Zag Roadmap -->
    <section class="zigzag-roadmap-section">
        <div class="container" style="position: relative; z-index: 2;">
            <div class="section-title text-center scroll-reveal up">
                <h2 style="font-size: 3rem; font-weight: 800; letter-spacing: -1px; color: #111;">Infrastructure Roadmap</h2>
                <p style="font-size: 1.1rem; color: #6B7280; max-width: 600px; margin: 0 auto; margin-top: 16px;">A strategic timeline for building the healthcare ecosystem.</p>
            </div>
            
            <div class="z-roadmap-container scroll-reveal up delay-1">
                <!-- SVG Wave Track -->
                <div class="svg-wave-track">
                    <svg viewBox="0 0 1000 1000" preserveAspectRatio="none">
                        <path d="M -50 500 C 37.5 500, 37.5 750, 125 750 C 250 750, 250 250, 375 250 C 500 250, 500 750, 625 750 C 750 750, 750 250, 875 250 C 962.5 250, 962.5 500, 1050 500" 
                              fill="none" stroke="rgba(229, 231, 235, 0.8)" stroke-width="4" stroke-linecap="round"/>
                        <path class="svg-wave-progress" d="M -50 500 C 37.5 500, 37.5 750, 125 750 C 250 750, 250 250, 375 250 C 500 250, 500 750, 625 750 C 750 750, 750 250, 875 250 C 962.5 250, 962.5 500, 1050 500" 
                              fill="none" stroke="#2563EB" stroke-width="6" stroke-linecap="round" />
                    </svg>
                </div>

                <!-- Floating Cards -->
                <div class="wave-card pos-1">
                    <div class="wave-node"></div>
                    <div class="h-card-header">
                        <span class="h-year-badge">2026</span>
                        <div class="h-card-icon-wrap"><i class="fa-solid fa-server"></i></div>
                    </div>
                    <h4>Platform Expansion</h4>
                    <p>Establishing the core technology layer, onboarding primary urban hospitals, and launching unified digital routing protocols.</p>
                </div>

                <div class="wave-card pos-2">
                    <div class="wave-node"></div>
                    <div class="h-card-header">
                        <span class="h-year-badge">2027</span>
                        <div class="h-card-icon-wrap"><i class="fa-solid fa-truck-medical"></i></div>
                    </div>
                    <h4>Ambulance Aggregation</h4>
                    <p>Unifying fragmented emergency response fleets and launching smart GPS dispatch systems to guarantee 10-minute response times.</p>
                </div>

                <div class="wave-card pos-3">
                    <div class="wave-node"></div>
                    <div class="h-card-header">
                        <span class="h-year-badge">2028</span>
                        <div class="h-card-icon-wrap"><i class="fa-solid fa-tower-cell"></i></div>
                    </div>
                    <h4>Rural Healthcare Network</h4>
                    <p>Deploying advanced telemedicine nodes and decentralized diagnostic access points to heavily under-served geographic regions.</p>
                </div>

                <div class="wave-card pos-4">
                    <div class="wave-node"></div>
                    <div class="h-card-header">
                        <span class="h-year-badge">2029</span>
                        <div class="h-card-icon-wrap"><i class="fa-solid fa-brain"></i></div>
                    </div>
                    <h4>AI Infrastructure</h4>
                    <p>Full autonomous operational deployment of Nava.ai predictive support across the entire multi-city hospital network.</p>
                </div>
            </div>
        </div>
    </section>"""

def replace_roadmap(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # We replace the previous horizontal-roadmap-section
    pattern = r'<!-- Horizontal Infrastructure Roadmap -->.*?</section>'
    content = re.sub(pattern, new_html, content, flags=re.DOTALL)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

# Apply to both files
replace_roadmap(os.path.join(base_dir, "future-partners.html"))
replace_roadmap(os.path.join(base_dir, "index.html"))

# Append CSS
new_css = """
/* ==========================================================================
   CINEMATIC ZIG-ZAG ROADMAP
   ========================================================================== */
.zigzag-roadmap-section {
    position: relative;
    padding: 140px 0;
    background-color: #FFFFFF;
    overflow: hidden;
}

.zigzag-roadmap-section::before {
    content: '';
    position: absolute;
    top: 50%; left: 50%; transform: translate(-50%, -50%);
    width: 1200px; height: 1200px;
    background: radial-gradient(circle at center, rgba(37, 99, 235, 0.04) 0%, transparent 60%);
    z-index: 0;
    pointer-events: none;
}

.z-roadmap-container {
    position: relative;
    width: 100%;
    max-width: 1300px;
    height: 700px; /* Provides vertical canvas for the wave */
    margin: 80px auto 0;
}

/* SVG Wavy Track */
.svg-wave-track {
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    z-index: 1;
}

.svg-wave-track svg {
    width: 100%; height: 100%;
    overflow: visible;
}

.svg-wave-progress {
    stroke-dasharray: 4000;
    stroke-dashoffset: 4000;
    animation: drawWave 5s cubic-bezier(0.25, 1, 0.5, 1) forwards;
    animation-delay: 0.5s;
    filter: drop-shadow(0 0 15px rgba(37, 99, 235, 0.6));
}

@keyframes drawWave {
    to { stroke-dashoffset: 0; }
}

/* Floating Milestone Cards */
.wave-card {
    position: absolute;
    width: 22%;
    transform: translate(-50%, -50%); /* Center directly over the SVG node point */
    z-index: 2;
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(24px);
    border: 1px solid rgba(229, 231, 235, 0.9);
    border-radius: 28px;
    padding: 40px 32px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.04);
    transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
    text-align: left;
}

/* The Zig-Zag Mathematics (Matching SVG percentages perfectly) */
.pos-1 { left: 12.5%; top: 75%; }
.pos-2 { left: 37.5%; top: 25%; }
.pos-3 { left: 62.5%; top: 75%; }
.pos-4 { left: 87.5%; top: 25%; }

/* Card Hover Interactions */
.wave-card:hover {
    transform: translate(-50%, -55%); /* Slight upward floating lift */
    box-shadow: 0 30px 60px rgba(37, 99, 235, 0.1);
    border-color: rgba(37, 99, 235, 0.4);
    background: #FFFFFF;
}

/* Card Header Redesign */
.h-card-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 32px;
    position: relative;
    z-index: 2;
}

.h-year-badge {
    background: linear-gradient(135deg, #2563EB, #60A5FA);
    color: #FFFFFF;
    font-size: 16px;
    font-weight: 800;
    padding: 10px 24px;
    border-radius: 30px;
    box-shadow: 0 10px 25px rgba(37, 99, 235, 0.4);
    letter-spacing: 1px;
    transform: translateY(-8px); /* High-end floating effect */
}

/* Softer Minimal Icon */
.h-card-icon-wrap {
    width: 48px; height: 48px;
    background: #F9FAFB;
    border: 1px solid #E5E7EB;
    border-radius: 14px;
    display: flex; align-items: center; justify-content: center;
    font-size: 20px;
    color: #9CA3AF; /* Minimal grey-blue */
    transition: all 0.4s ease;
}

.wave-card:hover .h-card-icon-wrap {
    color: #2563EB;
    background: rgba(37, 99, 235, 0.05);
    border-color: rgba(37, 99, 235, 0.2);
    transform: scale(1.08);
}

.wave-card h4 {
    font-size: 24px;
    font-weight: 700;
    color: #111111;
    margin-bottom: 14px;
    font-family: 'Poppins', sans-serif;
    letter-spacing: -0.5px;
    position: relative;
    z-index: 2;
}

.wave-card p {
    font-size: 15px;
    color: #6B7280;
    line-height: 1.7;
    margin: 0;
    position: relative;
    z-index: 2;
}

/* Glowing central node (anchored behind the card) */
.wave-node {
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    width: 28px; height: 28px;
    background: #FFFFFF;
    border: 5px solid #2563EB;
    border-radius: 50%;
    box-shadow: 0 0 0 8px rgba(37, 99, 235, 0.1);
    z-index: 0;
    pointer-events: none;
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.wave-node::after {
    content: ''; position: absolute;
    top: -12px; left: -12px; right: -12px; bottom: -12px;
    border-radius: 50%;
    border: 2px solid rgba(37, 99, 235, 0.3);
    animation: hNodePulse 2.5s infinite;
}

.wave-card:hover .wave-node {
    border-color: #FFFFFF;
    background: #2563EB;
    box-shadow: 0 0 25px rgba(37, 99, 235, 0.5);
    transform: translate(-50%, -50%) scale(1.2);
}

/* Responsive adjustments */
@media (max-width: 1200px) {
    .wave-card { width: 23.5%; padding: 32px 20px; }
    .wave-card h4 { font-size: 20px; }
}

@media (max-width: 992px) {
    .z-roadmap-container {
        height: auto;
        display: flex;
        flex-direction: column;
        gap: 40px;
        padding-left: 60px;
        margin-top: 60px;
    }
    .svg-wave-track { display: none; } /* Hide horizontal wave on tablet */
    
    .wave-card {
        position: relative;
        width: 100%;
        left: 0 !important; top: 0 !important;
        transform: none !important;
    }
    .wave-card:hover {
        transform: translateY(-8px) !important;
    }
    
    /* Re-create vertical line for tablet/mobile */
    .z-roadmap-container::before {
        content: ''; position: absolute;
        top: 0; bottom: 0; left: 30px;
        width: 4px; background: linear-gradient(180deg, #2563EB, #60A5FA);
        border-radius: 4px;
    }
    
    .wave-node {
        left: -30px;
    }
}
"""

css_file = os.path.join(base_dir, "style.css")
with open(css_file, "a", encoding="utf-8") as f:
    f.write(new_css)

print("Cinematic Zig-Zag Roadmap implemented successfully.")
