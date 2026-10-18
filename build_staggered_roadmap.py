import os
import re

base_dir = r"c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\xpedicr"

new_html = """    <!-- Premium Staggered Roadmap -->
    <section class="staggered-roadmap-section">
        <div class="container" style="position: relative; z-index: 2;">
            <div class="section-title text-center scroll-reveal up">
                <h2 style="font-size: 3rem; font-weight: 800; letter-spacing: -1px; color: #111;">Infrastructure Roadmap</h2>
                <p style="font-size: 1.1rem; color: #6B7280; max-width: 600px; margin: 0 auto; margin-top: 16px;">A strategic timeline for building the healthcare ecosystem.</p>
            </div>
            
            <div class="staggered-roadmap-container scroll-reveal up delay-1">
                <!-- Straight Central Track -->
                <div class="s-roadmap-track">
                    <div class="s-roadmap-progress"></div>
                </div>

                <div class="s-roadmap-flex">
                    <!-- 2026 (UP) -->
                    <div class="s-flex-col up">
                        <div class="s-stem"></div>
                        <div class="s-node-anchor"><div class="s-node"></div></div>
                        <div class="s-roadmap-card">
                            <span class="s-year-badge">2026</span>
                            <h4>Platform Expansion</h4>
                            <p>Establishing the core technology layer, onboarding primary urban hospitals, and launching unified digital routing protocols.</p>
                        </div>
                    </div>

                    <!-- 2027 (DOWN) -->
                    <div class="s-flex-col down" style="animation-delay: 0.1s;">
                        <div class="s-node-anchor"><div class="s-node"></div></div>
                        <div class="s-stem"></div>
                        <div class="s-roadmap-card">
                            <span class="s-year-badge">2027</span>
                            <h4>Ambulance Aggregation</h4>
                            <p>Unifying fragmented emergency response fleets and launching smart GPS dispatch systems to guarantee rapid response times.</p>
                        </div>
                    </div>

                    <!-- 2028 (UP) -->
                    <div class="s-flex-col up" style="animation-delay: 0.2s;">
                        <div class="s-stem"></div>
                        <div class="s-node-anchor"><div class="s-node"></div></div>
                        <div class="s-roadmap-card">
                            <span class="s-year-badge">2028</span>
                            <h4>Rural Healthcare</h4>
                            <p>Deploying advanced telemedicine nodes and decentralized diagnostic access points to heavily under-served geographic regions.</p>
                        </div>
                    </div>

                    <!-- 2029 (DOWN) -->
                    <div class="s-flex-col down" style="animation-delay: 0.3s;">
                        <div class="s-node-anchor"><div class="s-node"></div></div>
                        <div class="s-stem"></div>
                        <div class="s-roadmap-card">
                            <span class="s-year-badge">2029</span>
                            <h4>AI Infrastructure</h4>
                            <p>Full autonomous operational deployment of Nava.ai predictive support across the entire multi-city hospital network.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>"""

def replace_roadmap(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # We replace the previous zigzag-roadmap-section
    pattern = r'<!-- Cinematic Zig-Zag Roadmap -->.*?</section>'
    content = re.sub(pattern, new_html, content, flags=re.DOTALL)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

# Apply to both files
replace_roadmap(os.path.join(base_dir, "future-partners.html"))
replace_roadmap(os.path.join(base_dir, "index.html"))

# Append CSS
new_css = """
/* ==========================================================================
   PREMIUM STAGGERED ROADMAP
   ========================================================================== */
.staggered-roadmap-section {
    position: relative;
    padding: 140px 0;
    background-color: #FAFAFA;
    overflow: hidden;
}

.staggered-roadmap-section::before {
    content: '';
    position: absolute;
    top: 50%; left: 50%; transform: translate(-50%, -50%);
    width: 1200px; height: 1200px;
    background: radial-gradient(circle at center, rgba(37, 99, 235, 0.04) 0%, transparent 60%);
    z-index: 0;
    pointer-events: none;
}

.staggered-roadmap-container {
    position: relative;
    max-width: 1300px;
    margin: 80px auto 0;
    padding: 0 24px;
    z-index: 2;
}

/* The Straight Central Line */
.s-roadmap-track {
    position: absolute;
    top: 50%;
    left: 40px; right: 40px;
    height: 2px;
    background: #E5E7EB;
    z-index: 1;
    transform: translateY(-50%);
}

.s-roadmap-progress {
    position: absolute;
    top: 0; left: 0; height: 100%; width: 0%;
    background: linear-gradient(90deg, #2563EB, #60A5FA);
    box-shadow: 0 0 15px rgba(37,99,235,0.6);
    animation: sTimelineProgress 4s cubic-bezier(0.25, 1, 0.5, 1) forwards;
    animation-delay: 0.5s;
}

@keyframes sTimelineProgress {
    0% { width: 0%; }
    100% { width: 100%; }
}

/* Layout Grid */
.s-roadmap-flex {
    display: flex;
    justify-content: space-between;
    gap: 32px;
    position: relative;
    z-index: 2;
}

.s-flex-col {
    flex: 1;
    height: 650px; /* Provides rigid vertical canvas for staggered positioning */
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative;
}

/* Nodes anchored exactly at 50% */
.s-node-anchor {
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    width: 24px; height: 24px;
    z-index: 4;
}

.s-node {
    width: 100%; height: 100%;
    background: #FFFFFF;
    border: 4px solid #2563EB;
    border-radius: 50%;
    box-shadow: 0 0 0 8px rgba(37, 99, 235, 0.1);
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.s-node::after {
    content: ''; position: absolute;
    top: -12px; left: -12px; right: -12px; bottom: -12px;
    border-radius: 50%;
    border: 2px solid rgba(37, 99, 235, 0.3);
    animation: sNodePulse 2.5s infinite;
}

@keyframes sNodePulse {
    0% { transform: scale(0.8); opacity: 1; }
    100% { transform: scale(1.6); opacity: 0; }
}

.s-flex-col:hover .s-node {
    background: #2563EB;
    box-shadow: 0 0 25px rgba(37, 99, 235, 0.4);
    transform: scale(1.2);
    border-color: #FFFFFF;
}

/* Subtle stems connecting nodes to cards */
.s-stem {
    position: absolute;
    left: 50%;
    width: 2px; height: 40px;
    transform: translateX(-50%);
    z-index: 2;
    transition: all 0.4s ease;
}
.s-flex-col.up .s-stem {
    bottom: 50%;
    background: linear-gradient(0deg, rgba(37, 99, 235, 0.4) 0%, transparent 100%);
}
.s-flex-col.down .s-stem {
    top: 50%;
    background: linear-gradient(180deg, rgba(37, 99, 235, 0.4) 0%, transparent 100%);
}
.s-flex-col:hover .s-stem {
    background: #2563EB;
}

/* Floating Staggered Cards */
.s-roadmap-card {
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(24px);
    border: 1px solid rgba(229, 231, 235, 0.9);
    border-radius: 24px;
    padding: 48px 36px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.03);
    transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
    position: absolute;
    width: 100%;
    text-align: left;
    z-index: 3;
}

/* Position cards above and below line */
.s-flex-col.up .s-roadmap-card { bottom: calc(50% + 40px); }
.s-flex-col.down .s-roadmap-card { top: calc(50% + 40px); }

.s-roadmap-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 25px 50px rgba(37, 99, 235, 0.08);
    border-color: rgba(37, 99, 235, 0.3);
}

/* Minimal Internal Hierarchy */
.s-year-badge {
    display: inline-block;
    background: linear-gradient(135deg, #2563EB, #60A5FA);
    color: #FFFFFF;
    font-size: 16px;
    font-weight: 800;
    padding: 10px 28px;
    border-radius: 40px;
    box-shadow: 0 10px 25px rgba(37, 99, 235, 0.35);
    letter-spacing: 1.5px;
    margin-bottom: 32px;
}

.s-roadmap-card h4 {
    font-size: 24px;
    font-weight: 700;
    color: #111111;
    margin-bottom: 16px;
    font-family: 'Poppins', sans-serif;
    letter-spacing: -0.5px;
}

.s-roadmap-card p {
    font-size: 15.5px;
    color: #6B7280;
    line-height: 1.7;
    margin: 0;
}

/* Responsive adjustments */
@media (max-width: 1200px) {
    .s-roadmap-card { padding: 32px 24px; }
    .s-roadmap-card h4 { font-size: 20px; }
}

@media (max-width: 992px) {
    .staggered-roadmap-container {
        height: auto;
    }
    .s-roadmap-track, .s-node-anchor, .s-stem {
        display: none;
    }
    .s-roadmap-flex {
        flex-direction: column;
        gap: 40px;
        padding-left: 60px;
        margin-top: 60px;
    }
    .s-flex-col {
        height: auto;
    }
    .s-roadmap-card {
        position: relative;
        bottom: auto !important;
        top: auto !important;
    }
    /* Vertical Timeline Track for Mobile */
    .s-roadmap-flex::before {
        content: ''; position: absolute;
        top: 0; bottom: 0; left: 30px;
        width: 3px; background: linear-gradient(180deg, #2563EB, #60A5FA);
        border-radius: 4px;
    }
    /* Vertical Nodes for Mobile */
    .s-flex-col::before {
        content: ''; position: absolute;
        top: 60px; left: -30px;
        transform: translate(-50%, -50%);
        width: 20px; height: 20px;
        background: #FFFFFF;
        border: 4px solid #2563EB;
        border-radius: 50%;
        box-shadow: 0 0 0 6px rgba(37, 99, 235, 0.1);
        z-index: 3;
    }
}
"""

css_file = os.path.join(base_dir, "style.css")
with open(css_file, "a", encoding="utf-8") as f:
    f.write(new_css)

print("Premium Staggered Roadmap implemented successfully.")
