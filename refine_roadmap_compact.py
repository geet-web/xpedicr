import os
import re

base_dir = r"c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\xpedicr"
css_file = os.path.join(base_dir, "style.css")

with open(css_file, "r", encoding="utf-8") as f:
    css = f.read()

# Replace the Premium Staggered Roadmap block with a compact version
old_block_pattern = r'/\* ==+\s*PREMIUM STAGGERED ROADMAP\s*==+.*?(?=/\* ==|\Z)'
new_block = """/* ==========================================================================
   PREMIUM STAGGERED ROADMAP — Compact Refined
   ========================================================================== */
.staggered-roadmap-section {
    position: relative;
    padding: 100px 0;
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
    margin: 70px auto 0;
    padding: 0 24px;
    z-index: 2;
}

/* Straight Glowing Central Track */
.s-roadmap-track {
    position: absolute;
    top: 50%;
    left: 40px; right: 40px;
    height: 3px;
    background: #E5E7EB;
    z-index: 1;
    transform: translateY(-50%);
    border-radius: 4px;
}

.s-roadmap-progress {
    position: absolute;
    top: 0; left: 0; height: 100%; width: 0%;
    background: linear-gradient(90deg, #2563EB, #60A5FA);
    box-shadow: 0 0 18px rgba(37, 99, 235, 0.65);
    animation: sTimelineProgress 4s cubic-bezier(0.25, 1, 0.5, 1) forwards;
    animation-delay: 0.5s;
    border-radius: 4px;
}

@keyframes sTimelineProgress {
    0%   { width: 0%; }
    100% { width: 100%; }
}

/* Layout */
.s-roadmap-flex {
    display: flex;
    justify-content: space-between;
    gap: 24px;
    position: relative;
    z-index: 2;
}

/* Each column is the vertical canvas — reduced height */
.s-flex-col {
    flex: 1;
    height: 380px;          /* Key reduction from 650px */
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative;
}

/* Node pinned at the midpoint (50%) of the column */
.s-node-anchor {
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    width: 20px; height: 20px;
    z-index: 4;
}

.s-node {
    width: 100%; height: 100%;
    background: #FFFFFF;
    border: 3px solid #2563EB;
    border-radius: 50%;
    box-shadow: 0 0 0 7px rgba(37, 99, 235, 0.1);
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

.s-node::after {
    content: '';
    position: absolute;
    top: -11px; left: -11px; right: -11px; bottom: -11px;
    border-radius: 50%;
    border: 2px solid rgba(37, 99, 235, 0.25);
    animation: sNodePulse 2.5s infinite;
}

@keyframes sNodePulse {
    0%   { transform: scale(0.8); opacity: 1; }
    100% { transform: scale(1.6); opacity: 0; }
}

.s-flex-col:hover .s-node {
    background: #2563EB;
    box-shadow: 0 0 22px rgba(37, 99, 235, 0.45);
    transform: scale(1.15);
    border-color: #FFFFFF;
}

/* Connecting stem from node to card */
.s-stem {
    position: absolute;
    left: 50%;
    width: 2px; height: 28px;
    transform: translateX(-50%);
    z-index: 2;
    transition: background 0.4s ease;
}
.s-flex-col.up   .s-stem { bottom: 50%; background: linear-gradient(0deg,   rgba(37,99,235,0.45) 0%, transparent 100%); }
.s-flex-col.down .s-stem { top:    50%; background: linear-gradient(180deg, rgba(37,99,235,0.45) 0%, transparent 100%); }
.s-flex-col:hover .s-stem { background: #2563EB !important; }

/* -------- The Compact Card -------- */
.s-roadmap-card {
    background: #FFFFFF;
    border: 1px solid rgba(229, 231, 235, 0.9);
    border-radius: 16px;
    padding: 24px 28px;
    box-shadow: 0 6px 24px rgba(0, 0, 0, 0.04);
    transition: all 0.45s cubic-bezier(0.16, 1, 0.3, 1);
    position: absolute;
    width: 100%;
    text-align: left;
    z-index: 3;
}

/* Stagger positions — snug to the node */
.s-flex-col.up   .s-roadmap-card { bottom: calc(50% + 28px); }
.s-flex-col.down .s-roadmap-card { top:    calc(50% + 28px); }

.s-roadmap-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 18px 40px rgba(37, 99, 235, 0.08);
    border-color: rgba(37, 99, 235, 0.3);
}

/* Top-border glow on hover */
.s-roadmap-card::after {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; height: 3px;
    background: transparent;
    border-radius: 16px 16px 0 0;
    transition: background 0.4s ease;
}
.s-roadmap-card:hover::after {
    background: linear-gradient(90deg, #2563EB, #60A5FA);
}

/* Year badge — compact pill */
.s-year-badge {
    display: inline-block;
    background: linear-gradient(135deg, #2563EB, #60A5FA);
    color: #FFFFFF;
    font-size: 13px;
    font-weight: 700;
    padding: 5px 16px;
    border-radius: 30px;
    box-shadow: 0 6px 16px rgba(37, 99, 235, 0.3);
    letter-spacing: 1.5px;
    margin-bottom: 14px;
}

.s-roadmap-card h4 {
    font-size: 18px;
    font-weight: 700;
    color: #111111;
    margin-bottom: 8px;
    font-family: 'Poppins', sans-serif;
    letter-spacing: -0.3px;
    line-height: 1.3;
}

.s-roadmap-card p {
    font-size: 13.5px;
    color: #6B7280;
    line-height: 1.6;
    margin: 0;
}

/* ---- Responsive ---- */
@media (max-width: 1200px) {
    .s-flex-col    { height: 360px; }
    .s-roadmap-card { padding: 20px 20px; }
    .s-roadmap-card h4 { font-size: 16px; }
}

@media (max-width: 992px) {
    .staggered-roadmap-container { padding: 0 16px; }
    .s-roadmap-track, .s-node-anchor, .s-stem { display: none; }

    .s-roadmap-flex {
        flex-direction: column;
        gap: 24px;
        padding-left: 52px;
        margin-top: 48px;
        position: relative;
    }
    .s-flex-col { height: auto; }

    .s-roadmap-card {
        position: relative;
        bottom: auto !important;
        top:    auto !important;
    }

    /* Vertical glowing track */
    .s-roadmap-flex::before {
        content: ''; position: absolute;
        top: 0; bottom: 0; left: 26px;
        width: 3px;
        background: linear-gradient(180deg, #2563EB, #60A5FA);
        border-radius: 4px;
    }

    /* Vertical nodes */
    .s-flex-col::before {
        content: ''; position: absolute;
        top: 30px; left: -26px;
        transform: translate(-50%, 0);
        width: 16px; height: 16px;
        background: #FFFFFF;
        border: 3px solid #2563EB;
        border-radius: 50%;
        box-shadow: 0 0 0 5px rgba(37, 99, 235, 0.12);
        z-index: 3;
    }
}

@media (max-width: 768px) {
    .staggered-roadmap-section { padding: 72px 0; }
    .s-roadmap-card p { font-size: 13px; }
}

"""

css = re.sub(old_block_pattern, new_block, css, flags=re.DOTALL)

with open(css_file, "w", encoding="utf-8") as f:
    f.write(css)

print("Compact staggered roadmap CSS applied.")
