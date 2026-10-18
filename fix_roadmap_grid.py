import os, re

base_dir = r"c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\xpedicr"

# ─── NEW HTML ────────────────────────────────────────────────────────────────
new_html = """    <!-- Premium Staggered Roadmap -->
    <section class="staggered-roadmap-section">
        <div class="container" style="position: relative; z-index: 2;">
            <div class="section-title text-center scroll-reveal up">
                <h2 style="font-size: 3rem; font-weight: 800; letter-spacing: -1px; color: #111;">Infrastructure Roadmap</h2>
                <p style="font-size: 1.1rem; color: #6B7280; max-width: 600px; margin: 0 auto; margin-top: 16px;">A strategic timeline for building the healthcare ecosystem.</p>
            </div>

            <!-- 3-row CSS-Grid roadmap: top-cards / track / bottom-cards -->
            <div class="rm-grid scroll-reveal up delay-1">

                <!-- ROW 1 — TOP CARDS (2026, 2028) -->
                <div class="rm-top-row">
                    <div class="rm-card-wrap col-1">
                        <div class="rm-card">
                            <span class="rm-year">2026</span>
                            <h4>Platform Expansion</h4>
                            <p>Establishing the core technology layer, onboarding primary urban hospitals, and launching unified digital routing protocols.</p>
                        </div>
                        <div class="rm-stem down"></div>
                    </div>
                    <div class="rm-card-wrap col-3">
                        <div class="rm-card">
                            <span class="rm-year">2028</span>
                            <h4>Rural Healthcare</h4>
                            <p>Deploying advanced telemedicine nodes and decentralized diagnostic access points to heavily under-served geographic regions.</p>
                        </div>
                        <div class="rm-stem down"></div>
                    </div>
                </div>

                <!-- ROW 2 — TIMELINE TRACK + NODES -->
                <div class="rm-track-row">
                    <div class="rm-track">
                        <div class="rm-progress"></div>
                    </div>
                    <div class="rm-nodes">
                        <div class="rm-node-wrap col-1"><div class="rm-node"></div></div>
                        <div class="rm-node-wrap col-2"><div class="rm-node"></div></div>
                        <div class="rm-node-wrap col-3"><div class="rm-node"></div></div>
                        <div class="rm-node-wrap col-4"><div class="rm-node"></div></div>
                    </div>
                </div>

                <!-- ROW 3 — BOTTOM CARDS (2027, 2029) -->
                <div class="rm-bottom-row">
                    <div class="rm-card-wrap col-2">
                        <div class="rm-stem up"></div>
                        <div class="rm-card">
                            <span class="rm-year">2027</span>
                            <h4>Ambulance Aggregation</h4>
                            <p>Unifying fragmented emergency response fleets and launching smart GPS dispatch systems to guarantee rapid response times.</p>
                        </div>
                    </div>
                    <div class="rm-card-wrap col-4">
                        <div class="rm-stem up"></div>
                        <div class="rm-card">
                            <span class="rm-year">2029</span>
                            <h4>AI Infrastructure</h4>
                            <p>Full autonomous operational deployment of Nava.ai predictive support across the entire multi-city hospital network.</p>
                        </div>
                    </div>
                </div>

            </div><!-- /.rm-grid -->
        </div>
    </section>"""

# ─── NEW CSS ─────────────────────────────────────────────────────────────────
new_css = """
/* ==========================================================================
   PREMIUM STAGGERED ROADMAP — Grid-Aligned v3
   ========================================================================== */
.staggered-roadmap-section {
    position: relative;
    padding: 100px 0 120px;
    background-color: #FAFAFA;
    overflow: hidden;
}
.staggered-roadmap-section::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at 50% 55%, rgba(37,99,235,0.04) 0%, transparent 60%);
    pointer-events: none;
}

/* ---- Outer grid wrapper ---- */
.rm-grid {
    max-width: 1200px;
    margin: 72px auto 0;
    padding: 0 24px;
    position: relative;
    z-index: 2;
}

/* ---- Shared 4-column spacing system ---- */
/* We use a utility class .col-N to position elements in column N of 4 */
.rm-top-row,
.rm-bottom-row,
.rm-nodes {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 0;
    position: relative;
}

/* ---- ROW 1: Top Cards ---- */
.rm-top-row {
    align-items: flex-end;   /* cards hang down to touch the track */
    margin-bottom: 0;
}

/* ---- ROW 2: Track ---- */
.rm-track-row {
    position: relative;
    height: 48px;            /* vertical height of the track zone */
}

.rm-track {
    position: absolute;
    top: 50%; left: calc(12.5%);   /* start from centre of col-1 */
    right: calc(12.5%);            /* end at centre of col-4      */
    height: 3px;
    background: #E5E7EB;
    transform: translateY(-50%);
    border-radius: 4px;
    z-index: 1;
}

.rm-progress {
    height: 100%; width: 0%;
    background: linear-gradient(90deg, #2563EB, #60A5FA);
    box-shadow: 0 0 14px rgba(37,99,235,0.6);
    animation: rmProgress 4s cubic-bezier(0.25, 1, 0.5, 1) forwards;
    animation-delay: 0.5s;
    border-radius: 4px;
}
@keyframes rmProgress { to { width: 100%; } }

/* Nodes layer sits on top of track */
.rm-nodes {
    position: absolute;
    inset: 0;
    z-index: 2;
}

.rm-node-wrap {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
}

.rm-node {
    width: 20px; height: 20px;
    background: #FFF;
    border: 3px solid #2563EB;
    border-radius: 50%;
    box-shadow: 0 0 0 7px rgba(37,99,235,0.1);
    transition: all 0.4s cubic-bezier(0.16,1,0.3,1);
    position: relative;
    flex-shrink: 0;
}
.rm-node::after {
    content: '';
    position: absolute;
    inset: -11px;
    border-radius: 50%;
    border: 2px solid rgba(37,99,235,0.25);
    animation: rmPulse 2.5s infinite;
}
@keyframes rmPulse {
    0%   { transform: scale(0.8); opacity: 1; }
    100% { transform: scale(1.8); opacity: 0; }
}

/* ---- ROW 3: Bottom Cards ---- */
.rm-bottom-row {
    align-items: flex-start;  /* cards rise up from the track */
    margin-top: 0;
}

/* ---- Column positioning (shared between top/bottom rows) ---- */
.rm-card-wrap {
    display: flex;
    flex-direction: column;
    align-items: center;
}

/* top row: card then stem */
.rm-top-row .rm-card-wrap { flex-direction: column-reverse; }

/* Grid column assignment */
.col-1 { grid-column: 1; }
.col-2 { grid-column: 2; }
.col-3 { grid-column: 3; }
.col-4 { grid-column: 4; }

/* ---- Connecting Stems ---- */
.rm-stem {
    width: 2px; height: 28px;
    flex-shrink: 0;
    border-radius: 2px;
}
.rm-stem.down { background: linear-gradient(180deg, transparent 0%, rgba(37,99,235,0.5) 100%); }
.rm-stem.up   { background: linear-gradient(0deg,   transparent 0%, rgba(37,99,235,0.5) 100%); }

/* ---- The Card ---- */
.rm-card {
    background: #FFFFFF;
    border: 1px solid rgba(229,231,235,0.9);
    border-radius: 16px;
    padding: 24px 24px 22px;
    box-shadow: 0 6px 24px rgba(0,0,0,0.04);
    transition: all 0.45s cubic-bezier(0.16,1,0.3,1);
    width: 100%;
    text-align: left;
    position: relative;
    overflow: hidden;
}
.rm-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; height: 3px;
    background: transparent;
    border-radius: 16px 16px 0 0;
    transition: background 0.4s ease;
}
.rm-card-wrap:hover .rm-card {
    transform: translateY(-6px);
    box-shadow: 0 18px 40px rgba(37,99,235,0.08);
    border-color: rgba(37,99,235,0.28);
}
.rm-card-wrap:hover .rm-card::before {
    background: linear-gradient(90deg, #2563EB, #60A5FA);
}
.rm-card-wrap:hover .rm-node {
    background: #2563EB;
    border-color: #FFF;
    box-shadow: 0 0 20px rgba(37,99,235,0.45);
    transform: scale(1.15);
}
.rm-card-wrap:hover .rm-stem {
    background: #2563EB !important;
}

/* Year badge */
.rm-year {
    display: inline-block;
    background: linear-gradient(135deg, #2563EB, #60A5FA);
    color: #FFF;
    font-size: 12px;
    font-weight: 700;
    padding: 4px 14px;
    border-radius: 30px;
    letter-spacing: 1.5px;
    box-shadow: 0 5px 14px rgba(37,99,235,0.28);
    margin-bottom: 12px;
}
.rm-card h4 {
    font-size: 16px;
    font-weight: 700;
    color: #111;
    margin-bottom: 8px;
    font-family: 'Poppins', sans-serif;
    letter-spacing: -0.2px;
    line-height: 1.3;
}
.rm-card p {
    font-size: 13px;
    color: #6B7280;
    line-height: 1.6;
    margin: 0;
}

/* ── Responsive ─────────────────────────────────────────────────────────── */
/* Tablet: 2-column stagger */
@media (max-width: 1024px) {
    .rm-card h4 { font-size: 15px; }
    .rm-card p  { font-size: 12.5px; }
}

/* Mobile: full vertical stack */
@media (max-width: 768px) {
    .staggered-roadmap-section { padding: 72px 0 88px; }

    .rm-top-row,
    .rm-track-row,
    .rm-bottom-row { display: none; }   /* hide desktop grid */

    /* ---- Mobile-only vertical timeline ---- */
    .rm-grid::after { display: none; }
    .rm-grid {
        display: flex;
        flex-direction: column;
        gap: 0;
        padding-left: 56px;
        position: relative;
    }
    /* vertical track */
    .rm-grid::before {
        content: '';
        position: absolute;
        top: 0; bottom: 0; left: 28px;
        width: 3px;
        background: linear-gradient(180deg, #2563EB, #60A5FA);
        border-radius: 4px;
    }
    /* Show cards in correct order via mobile-specific markup */
    .rm-mobile-card {
        display: flex;
        flex-direction: column;
        padding: 0 0 28px;
        position: relative;
    }
    .rm-mobile-card::before {
        content: '';
        position: absolute;
        top: 22px; left: -42px;
        width: 16px; height: 16px;
        background: #FFF;
        border: 3px solid #2563EB;
        border-radius: 50%;
        box-shadow: 0 0 0 5px rgba(37,99,235,0.12);
        z-index: 3;
    }
}
/* Hide mobile cards on desktop */
.rm-mobile-card { display: none; }
"""

# ─── APPLY TO FILES ────────────────────────────────────────────────────────
def replace_roadmap_html(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    content = re.sub(
        r'<!-- Premium Staggered Roadmap -->.*?</section>',
        new_html, content, flags=re.DOTALL)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  HTML updated: {filepath}")

def replace_roadmap_css(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        css = f.read()
    # Replace the existing staggered-roadmap block (anything between the header comment and next major comment block)
    css = re.sub(
        r'/\* ==+\s*PREMIUM STAGGERED ROADMAP.*?(?=/\* ==|\Z)',
        new_css + "\n", css, flags=re.DOTALL)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(css)
    print(f"  CSS updated:  {filepath}")

fp_html = [
    os.path.join(base_dir, "future-partners.html"),
    os.path.join(base_dir, "index.html"),
]
for f in fp_html:
    replace_roadmap_html(f)

replace_roadmap_css(os.path.join(base_dir, "style.css"))

# Also add mobile cards inside the rm-grid for the mobile fallback
# We inject them as hidden elements that CSS shows only on mobile
mobile_cards = """
                <!-- Mobile fallback (hidden on desktop, shown on mobile) -->
                <div class="rm-mobile-card">
                    <div class="rm-card"><span class="rm-year">2026</span><h4>Platform Expansion</h4><p>Establishing the core technology layer, onboarding primary urban hospitals, and launching unified digital routing protocols.</p></div>
                </div>
                <div class="rm-mobile-card">
                    <div class="rm-card"><span class="rm-year">2027</span><h4>Ambulance Aggregation</h4><p>Unifying fragmented emergency response fleets and launching smart GPS dispatch systems to guarantee rapid response times.</p></div>
                </div>
                <div class="rm-mobile-card">
                    <div class="rm-card"><span class="rm-year">2028</span><h4>Rural Healthcare</h4><p>Deploying advanced telemedicine nodes and decentralized diagnostic access points to heavily under-served geographic regions.</p></div>
                </div>
                <div class="rm-mobile-card">
                    <div class="rm-card"><span class="rm-year">2029</span><h4>AI Infrastructure</h4><p>Full autonomous operational deployment of Nava.ai predictive support across the entire multi-city hospital network.</p></div>
                </div>"""

for fp in fp_html:
    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()
    content = content.replace("</div><!-- /.rm-grid -->", mobile_cards + "\n            </div><!-- /.rm-grid -->")
    with open(fp, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  Mobile fallback injected: {fp}")

print("\nAll done — grid-aligned roadmap deployed successfully.")
