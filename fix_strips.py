import re

html = open('index.html', encoding='utf-8').read()
css  = open('style.css',  encoding='utf-8').read()

# ── 1. Pilot section replace ─────────────────────────────────────────────────
new_pilot = """    <!-- Pilot Collaborations -->
    <section class="pilot-section">
        <div class="pilot-inner">
            <span class="pilot-label">Pilot Collaborations &amp; Ecosystem Partners</span>
            <div class="pilot-strip">
                <div class="pilot-badge"><i class="fa-solid fa-hospital"></i> CityCare Hospitals</div>
                <div class="pilot-sep"></div>
                <div class="pilot-badge"><i class="fa-solid fa-flask"></i> Prime Diagnostics</div>
                <div class="pilot-sep"></div>
                <div class="pilot-badge"><i class="fa-solid fa-truck-medical"></i> RapidResponse</div>
                <div class="pilot-sep"></div>
                <div class="pilot-badge"><i class="fa-solid fa-pills"></i> PharmaConnect</div>
            </div>
        </div>
    </section>"""

html = re.sub(
    r'<!-- Pilot Collaborations -->.*?</section>',
    new_pilot, html, flags=re.DOTALL)
print("Pilot HTML:", "pilot-section" in html)

open('index.html', 'w', encoding='utf-8').write(html)

# ── 2. Fix feat-strip CSS (remove overflow:hidden, add outer wrapper) ────────
old_strip = """.feat-strip {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0;
    max-width: 900px;
    margin: 0 auto;
    background: #FFFFFF;
    border: 1px solid rgba(229, 231, 235, 0.9);
    border-radius: 20px;
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.04);
    padding: 8px 16px;
    overflow: hidden;
}"""

new_strip = """.feat-strip-outer {
    max-width: 960px;
    margin: 0 auto;
    padding: 0 32px;
}

.feat-strip {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0;
    background: #FFFFFF;
    border: 1px solid rgba(229, 231, 235, 0.9);
    border-radius: 20px;
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.04);
    padding: 8px 24px;
}"""

if old_strip in css:
    css = css.replace(old_strip, new_strip)
    print("feat-strip CSS: fixed")
else:
    print("feat-strip CSS: not found, appending outer wrapper rule only")
    css += "\n.feat-strip-outer { max-width: 960px; margin: 0 auto; padding: 0 32px; }\n"
    css = css.replace("overflow: hidden;\n}", "/* overflow removed */\n}")

# ── 3. Append pilot CSS ──────────────────────────────────────────────────────
pilot_css = """
/* ==========================================================================
   PILOT COLLABORATIONS STRIP
   ========================================================================== */
.pilot-section {
    background: #FFFFFF;
    border-top: 1px solid #E5E7EB;
    border-bottom: 1px solid #E5E7EB;
    padding: 32px 24px;
}
.pilot-inner {
    max-width: 860px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 20px;
}
.pilot-label {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #9CA3AF;
}
.pilot-strip {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
    gap: 0;
    background: #FAFAFA;
    border: 1px solid #E5E7EB;
    border-radius: 16px;
    padding: 6px 12px;
}
.pilot-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 10px 20px;
    font-size: 13.5px;
    font-weight: 600;
    color: #374151;
    border-radius: 12px;
    transition: all 0.3s ease;
    cursor: default;
    white-space: nowrap;
}
.pilot-badge i {
    color: #6B7280;
    font-size: 14px;
    transition: color 0.3s ease;
}
.pilot-badge:hover { background: rgba(37,99,235,0.05); color: #2563EB; }
.pilot-badge:hover i { color: #2563EB; }
.pilot-sep { width: 1px; height: 28px; background: #E5E7EB; flex-shrink: 0; }
"""

open('style.css', 'w', encoding='utf-8').write(css + pilot_css)
print("CSS written.")
print("Done.")
