import os
import re

base_dir = r"c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\xpedicr"

new_html = """    <!-- Premium Visual Ecosystem Flow -->
    <section class="premium-flow-section">
        <div class="container" style="position: relative; z-index: 2;">
            <div class="section-title text-center scroll-reveal up">
                <h2 style="font-size: 3rem; font-weight: 800; letter-spacing: -1px; color: #111;">Visual Ecosystem Flow</h2>
                <p style="font-size: 1.1rem; color: #6B7280; max-width: 600px; margin: 0 auto; margin-top: 16px;">How Xpedicr connects the healthcare journey end-to-end.</p>
            </div>
            
            <div class="premium-flow-container scroll-reveal up" style="transition-delay: 0.2s;">
                <div class="flow-line-track">
                    <div class="flow-line-progress"></div>
                </div>
                
                <div class="flow-node">
                    <div class="flow-badge">1</div>
                    <div class="flow-card">
                        <i class="fa-solid fa-mobile-screen flow-card-icon"></i>
                        <h4>User Request</h4>
                        <p>Instant digital booking via app or web platform.</p>
                    </div>
                </div>
                
                <div class="flow-node">
                    <div class="flow-badge">2</div>
                    <div class="flow-card">
                        <i class="fa-solid fa-user-doctor flow-card-icon"></i>
                        <h4>Consultation</h4>
                        <p>AI-assisted triage and verified tele-consultations.</p>
                    </div>
                </div>
                
                <div class="flow-node">
                    <div class="flow-badge">3</div>
                    <div class="flow-card">
                        <i class="fa-solid fa-microscope flow-card-icon"></i>
                        <h4>Diagnostics</h4>
                        <p>Rapid at-home sample collection and digital reports.</p>
                    </div>
                </div>
                
                <div class="flow-node">
                    <div class="flow-badge">4</div>
                    <div class="flow-card">
                        <i class="fa-solid fa-pills flow-card-icon"></i>
                        <h4>Medicine</h4>
                        <p>30-minute hyper-local automated pharmacy delivery.</p>
                    </div>
                </div>
                
                <div class="flow-node">
                    <div class="flow-badge">5</div>
                    <div class="flow-card">
                        <i class="fa-solid fa-truck-medical flow-card-icon"></i>
                        <h4>Emergency</h4>
                        <p>GPS-routed ambulance aggregation and rapid response.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>"""

# Replace in ecosystem-services.html
html_file = os.path.join(base_dir, "ecosystem-services.html")
with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# Using regex to find the old block and replace it
pattern = r'<!-- Visual Ecosystem Flow -->.*?</section>'
content = re.sub(pattern, new_html, content, flags=re.DOTALL)

with open(html_file, "w", encoding="utf-8") as f:
    f.write(content)

# Append CSS
new_css = """
/* ==========================================================================
   PREMIUM VISUAL ECOSYSTEM FLOW
   ========================================================================== */
.premium-flow-section {
    position: relative;
    padding: 120px 0;
    background-color: #FFFFFF;
    overflow: hidden;
}

/* Subtle radial background gradient for modern SaaS look */
.premium-flow-section::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 1000px;
    height: 1000px;
    background: radial-gradient(circle, rgba(37,99,235,0.04) 0%, rgba(255,255,255,0) 70%);
    z-index: 0;
    pointer-events: none;
}

.premium-flow-container {
    position: relative;
    z-index: 2;
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 24px;
    margin-top: 80px;
}

/* The Animated Connector Line */
.flow-line-track {
    position: absolute;
    top: 36px; /* Center of the badges (72px / 2) */
    left: 8%;
    right: 8%;
    height: 2px;
    background: #F3F4F6;
    z-index: 1;
}

.flow-line-progress {
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    width: 0%;
    background: linear-gradient(90deg, #2563EB, #60A5FA);
    box-shadow: 0 0 12px rgba(37,99,235,0.6);
    animation: flowProgress 2.5s cubic-bezier(0.25, 1, 0.5, 1) forwards;
    animation-delay: 0.5s;
}

@keyframes flowProgress {
    0% { width: 0%; }
    100% { width: 100%; }
}

/* Flow Node */
.flow-node {
    position: relative;
    z-index: 2;
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    width: 100%;
}

/* Numbered Badge */
.flow-badge {
    width: 72px;
    height: 72px;
    border-radius: 50%;
    background: #FFFFFF;
    border: 2px solid #E5E7EB;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    font-weight: 800;
    color: #111111;
    box-shadow: 0 4px 15px rgba(0,0,0,0.04);
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    margin-bottom: 32px;
    position: relative;
    font-family: 'Poppins', sans-serif;
}

/* Glowing dot inside badge for extra premium feel */
.flow-badge::after {
    content: '';
    position: absolute;
    width: 100%;
    height: 100%;
    border-radius: 50%;
    box-shadow: 0 0 20px rgba(37,99,235,0);
    transition: all 0.4s ease;
}

.flow-node:hover .flow-badge {
    border-color: #2563EB;
    color: #2563EB;
    transform: scale(1.15);
    background: #FFFFFF;
}

.flow-node:hover .flow-badge::after {
    box-shadow: 0 0 25px rgba(37,99,235,0.25);
}

/* Premium Flow Card */
.flow-card {
    background: #FFFFFF;
    border: 1px solid #F3F4F6;
    border-radius: 24px;
    padding: 36px 24px;
    width: 100%;
    box-shadow: 0 10px 30px rgba(0,0,0,0.03);
    transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
    position: relative;
    overflow: hidden;
}

/* Glassmorphism subtle hover highlight */
.flow-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: transparent;
    transition: all 0.4s ease;
}

.flow-node:hover .flow-card {
    transform: translateY(-10px);
    box-shadow: 0 25px 50px rgba(37,99,235,0.1);
    border-color: rgba(37, 99, 235, 0.2);
}

.flow-node:hover .flow-card::before {
    background: linear-gradient(90deg, #2563EB, #60A5FA);
}

.flow-card-icon {
    font-size: 32px;
    color: #9CA3AF;
    margin-bottom: 24px;
    transition: all 0.4s ease;
}

.flow-node:hover .flow-card-icon {
    color: #2563EB;
    transform: scale(1.1);
}

.flow-card h4 {
    font-size: 20px;
    font-weight: 700;
    color: #111111;
    margin-bottom: 12px;
    font-family: 'Poppins', sans-serif;
    letter-spacing: -0.5px;
}

.flow-card p {
    font-size: 14.5px;
    color: #6B7280;
    margin: 0;
    line-height: 1.6;
}

/* Responsive adjustments */
@media (max-width: 1200px) {
    .flow-card {
        padding: 24px 16px;
    }
    .flow-card h4 {
        font-size: 18px;
    }
}

@media (max-width: 992px) {
    .premium-flow-container {
        flex-wrap: wrap;
        justify-content: center;
        gap: 40px;
    }
    .flow-line-track {
        display: none; /* Hide horizontal line on tablet */
    }
    .flow-node {
        flex: 1 1 40%;
        max-width: 40%;
    }
}

@media (max-width: 768px) {
    .premium-flow-container {
        flex-direction: column;
        align-items: center;
        gap: 48px;
        padding-left: 20px;
    }
    .flow-node {
        flex: 1 1 100%;
        width: 100%;
        max-width: 340px;
        flex-direction: row;
        text-align: left;
        align-items: center;
        gap: 24px;
    }
    .flow-badge {
        margin-bottom: 0;
        flex-shrink: 0;
    }
    .flow-card {
        padding: 24px;
    }
    
    /* Create vertical line for mobile */
    .premium-flow-container::before {
        content: '';
        position: absolute;
        top: 0;
        bottom: 0;
        left: 56px; /* align with badge center: 20px padding + (72px / 2) */
        width: 2px;
        background: #E5E7EB;
        z-index: 1;
    }
}
"""

css_file = os.path.join(base_dir, "style.css")
with open(css_file, "a", encoding="utf-8") as f:
    f.write(new_css)

print("Premium Visual Ecosystem Flow implemented successfully.")
