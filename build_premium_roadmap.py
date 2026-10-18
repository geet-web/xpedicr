import os
import re

base_dir = r"c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\xpedicr"

new_html = """    <!-- Premium Infrastructure Roadmap -->
    <section class="premium-roadmap-section">
        <div class="container" style="position: relative; z-index: 2;">
            <div class="section-title text-center scroll-reveal up">
                <h2 style="font-size: 3rem; font-weight: 800; letter-spacing: -1px; color: #111;">Infrastructure Roadmap</h2>
                <p style="font-size: 1.1rem; color: #6B7280; max-width: 600px; margin: 0 auto; margin-top: 16px;">A strategic timeline for building the healthcare ecosystem.</p>
            </div>
            
            <div class="roadmap-container scroll-reveal up delay-1">
                <div class="roadmap-line-progress"></div>
                
                <!-- 2026 -->
                <div class="roadmap-item">
                    <div class="roadmap-node"></div>
                    <div class="roadmap-content">
                        <i class="fa-solid fa-server roadmap-icon"></i>
                        <span class="roadmap-year">2026</span>
                        <h4>Platform Expansion</h4>
                        <p>Establishing the core technology layer, onboarding primary urban hospitals, and launching unified digital routing protocols.</p>
                    </div>
                </div>

                <!-- 2027 -->
                <div class="roadmap-item" style="transition-delay: 0.2s;">
                    <div class="roadmap-node"></div>
                    <div class="roadmap-content">
                        <i class="fa-solid fa-truck-medical roadmap-icon"></i>
                        <span class="roadmap-year">2027</span>
                        <h4>Ambulance Aggregation</h4>
                        <p>Unifying fragmented emergency response fleets and launching smart GPS dispatch systems to guarantee 10-minute response times.</p>
                    </div>
                </div>

                <!-- 2028 -->
                <div class="roadmap-item" style="transition-delay: 0.4s;">
                    <div class="roadmap-node"></div>
                    <div class="roadmap-content">
                        <i class="fa-solid fa-tower-cell roadmap-icon"></i>
                        <span class="roadmap-year">2028</span>
                        <h4>Rural Healthcare Network</h4>
                        <p>Deploying advanced telemedicine nodes and decentralized diagnostic access points to heavily under-served geographic regions.</p>
                    </div>
                </div>

                <!-- 2029 -->
                <div class="roadmap-item" style="transition-delay: 0.6s;">
                    <div class="roadmap-node"></div>
                    <div class="roadmap-content">
                        <i class="fa-solid fa-brain roadmap-icon"></i>
                        <span class="roadmap-year">2029</span>
                        <h4>AI Healthcare Infrastructure</h4>
                        <p>Full autonomous operational deployment of Nava.ai predictive support across the entire multi-city hospital network.</p>
                    </div>
                </div>

            </div>
        </div>
    </section>"""

html_file = os.path.join(base_dir, "future-partners.html")
with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

pattern = r'<!-- Professional Timeline -->.*?</section>'
content = re.sub(pattern, new_html, content, flags=re.DOTALL)

with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)

# Append CSS
new_css = """
/* ==========================================================================
   PREMIUM INFRASTRUCTURE ROADMAP
   ========================================================================== */
.premium-roadmap-section {
    position: relative;
    padding: 140px 0;
    background-color: #FAFAFA;
    overflow: hidden;
    z-index: 1;
}

/* Subtle background styling */
.premium-roadmap-section::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background-image: 
        radial-gradient(circle at 15% 50%, rgba(37, 99, 235, 0.04) 0%, transparent 50%),
        radial-gradient(circle at 85% 30%, rgba(96, 165, 250, 0.04) 0%, transparent 50%);
    z-index: -1;
    pointer-events: none;
}

.roadmap-container {
    position: relative;
    max-width: 1000px;
    margin: 80px auto 0;
    padding: 0 20px;
}

/* The Central Glowing Line */
.roadmap-container::before {
    content: '';
    position: absolute;
    top: 0;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 2px;
    background: rgba(229, 231, 235, 0.8);
    z-index: 1;
}

.roadmap-line-progress {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 2px;
    background: linear-gradient(180deg, #2563EB 0%, #60A5FA 80%, transparent 100%);
    box-shadow: 0 0 15px rgba(37,99,235,0.6);
    z-index: 2;
    height: 0%;
    animation: timelineProgress 4s cubic-bezier(0.25, 1, 0.5, 1) forwards;
    animation-delay: 0.5s;
}

@keyframes timelineProgress {
    0% { height: 0%; }
    100% { height: 100%; }
}

/* Milestone Wrapper */
.roadmap-item {
    position: relative;
    z-index: 3;
    margin-bottom: 80px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
}

.roadmap-item:last-child {
    margin-bottom: 0;
}

/* Alternating layout logic */
.roadmap-item:nth-child(even) {
    flex-direction: row-reverse;
}

/* The Central Node */
.roadmap-node {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    width: 24px;
    height: 24px;
    background: #FFFFFF;
    border: 4px solid #2563EB;
    border-radius: 50%;
    box-shadow: 0 0 0 6px rgba(37, 99, 235, 0.1);
    z-index: 4;
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

/* Pulse animation for nodes */
.roadmap-node::after {
    content: '';
    position: absolute;
    top: -10px; left: -10px; right: -10px; bottom: -10px;
    border-radius: 50%;
    border: 2px solid rgba(37, 99, 235, 0.3);
    animation: nodePulse 2s infinite;
}

@keyframes nodePulse {
    0% { transform: scale(0.8); opacity: 1; }
    100% { transform: scale(1.6); opacity: 0; }
}

.roadmap-item:hover .roadmap-node {
    background: #2563EB;
    box-shadow: 0 0 20px rgba(37, 99, 235, 0.4);
    transform: translate(-50%, -50%) scale(1.2);
    border-color: #FFFFFF;
}

/* The Content Card */
.roadmap-content {
    width: 45%;
    background: #FFFFFF;
    border-radius: 24px;
    padding: 40px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.03);
    border: 1px solid rgba(229, 231, 235, 0.8);
    position: relative;
    transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
}

.roadmap-item:nth-child(odd) .roadmap-content {
    text-align: right;
}

.roadmap-item:nth-child(even) .roadmap-content {
    text-align: left;
}

.roadmap-item:hover .roadmap-content {
    transform: translateY(-8px);
    box-shadow: 0 25px 50px rgba(37, 99, 235, 0.08);
    border-color: rgba(37, 99, 235, 0.3);
}

/* Glassmorphism subtle hover highlight */
.roadmap-content::after {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; height: 4px;
    background: transparent;
    transition: all 0.4s ease;
    border-radius: 24px 24px 0 0;
}

.roadmap-item:hover .roadmap-content::after {
    background: linear-gradient(90deg, #2563EB, #60A5FA);
}

/* Connecting Arrow/Line to Card */
.roadmap-content::before {
    content: '';
    position: absolute;
    top: 50%;
    width: 0;
    height: 0;
    border-top: 12px solid transparent;
    border-bottom: 12px solid transparent;
    transition: all 0.4s ease;
}

/* Arrows pointing to the center line */
.roadmap-item:nth-child(odd) .roadmap-content::before {
    right: -12px;
    border-left: 12px solid #FFFFFF;
    transform: translateY(-50%);
    filter: drop-shadow(2px 0px 1px rgba(229, 231, 235, 0.8));
}

.roadmap-item:nth-child(even) .roadmap-content::before {
    left: -12px;
    border-right: 12px solid #FFFFFF;
    transform: translateY(-50%);
    filter: drop-shadow(-2px 0px 1px rgba(229, 231, 235, 0.8));
}

.roadmap-item:hover .roadmap-content::before {
    filter: drop-shadow(0px 0px 0px transparent);
}

/* Year Badge */
.roadmap-year {
    display: inline-block;
    background: linear-gradient(135deg, #2563EB, #1D4ED8);
    color: #FFFFFF;
    font-size: 15px;
    font-weight: 700;
    padding: 6px 20px;
    border-radius: 30px;
    margin-bottom: 20px;
    box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
    letter-spacing: 1px;
}

.roadmap-icon {
    position: absolute;
    top: 40px;
    right: 40px;
    font-size: 40px;
    color: rgba(37, 99, 235, 0.08);
    transition: all 0.5s ease;
}

.roadmap-item:nth-child(even) .roadmap-icon {
    right: auto;
    left: 40px;
}

.roadmap-item:hover .roadmap-icon {
    color: rgba(37, 99, 235, 0.6);
    transform: scale(1.15);
}

.roadmap-content h4 {
    font-size: 24px;
    font-weight: 700;
    color: #111111;
    margin-bottom: 12px;
    font-family: 'Poppins', sans-serif;
    letter-spacing: -0.5px;
}

.roadmap-content p {
    font-size: 15.5px;
    color: #6B7280;
    margin: 0;
    line-height: 1.6;
}

/* Responsive adjustments */
@media (max-width: 992px) {
    .roadmap-container::before,
    .roadmap-line-progress {
        left: 40px;
    }
    .roadmap-node {
        left: 40px;
    }
    .roadmap-item,
    .roadmap-item:nth-child(even) {
        flex-direction: column;
        align-items: flex-end;
    }
    .roadmap-content {
        width: calc(100% - 90px);
    }
    .roadmap-item:nth-child(odd) .roadmap-content,
    .roadmap-item:nth-child(even) .roadmap-content {
        text-align: left;
    }
    .roadmap-item:nth-child(odd) .roadmap-content::before,
    .roadmap-item:nth-child(even) .roadmap-content::before {
        left: -12px;
        right: auto;
        border-right: 12px solid #FFFFFF;
        border-left: none;
        filter: drop-shadow(-2px 0px 1px rgba(229, 231, 235, 0.8));
    }
    .roadmap-icon,
    .roadmap-item:nth-child(even) .roadmap-icon {
        right: 32px;
        left: auto;
    }
}

@media (max-width: 768px) {
    .premium-roadmap-section {
        padding: 80px 0;
    }
    .roadmap-container::before,
    .roadmap-line-progress,
    .roadmap-node {
        left: 20px;
    }
    .roadmap-content {
        width: calc(100% - 50px);
        padding: 32px 24px;
    }
    .roadmap-item {
        margin-bottom: 48px;
    }
    .roadmap-icon,
    .roadmap-item:nth-child(even) .roadmap-icon {
        display: none; /* Hide huge background icon on mobile to save space */
    }
}
"""

css_file = os.path.join(base_dir, "style.css")
with open(css_file, "a", encoding="utf-8") as f:
    f.write(new_css)

print("Premium Roadmap implemented successfully.")
