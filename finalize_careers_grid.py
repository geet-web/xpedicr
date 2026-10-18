import re

path = r"c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\xpedicr\careers.html"
css_path = r"c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\xpedicr\style.css"

with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# Remove the orphaned old section: everything from the leftover <div style="max-width: 900px"...>
# down to and including the closing </section> that matches the old open-positions section clone
old_block = re.search(
    r'\s*<div style="max-width: 900px.*?</section>',
    html, re.DOTALL)
if old_block:
    html = html[:old_block.start()] + "\n" + html[old_block.end():]
    print("Old cards block removed.")
else:
    # Fallback: remove all job-item divs that are outside the new grid
    html = re.sub(r'\s*<!-- Job Card \d+ -->\s*<div class="job-item.*?</div>\s*</div>\s*', 
                  '', html, flags=re.DOTALL)
    # Remove the leftover wrapper close tags
    html = re.sub(r'\s*</div>\s*</div>\s*</section>\s*\n\s*<!-- 4\.',
                  '\n    <!-- 4.', html, flags=re.DOTALL)
    print("Fallback cleanup done.")

with open(path, "w", encoding="utf-8") as f:
    f.write(html)
print("HTML cleaned.")

# ─── CSS ────────────────────────────────────────────────────────────────────
new_css = """
/* ==========================================================================
   CAREERS — Modern Job Card Grid
   ========================================================================== */
.careers-openings-section {
    background: #F9FAFB;
    padding: 100px 0;
}

/* 3-column responsive grid */
.jobs-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
    max-width: 1200px;
    margin: 0 auto;
}

/* ── Job Card ── */
.jc-card {
    background: #FFFFFF;
    border: 1px solid rgba(229, 231, 235, 0.9);
    border-radius: 16px;
    padding: 28px 26px 24px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.03);
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    cursor: pointer;
    display: flex;
    flex-direction: column;
    position: relative;
    overflow: hidden;
}
.jc-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; height: 3px;
    background: transparent;
    border-radius: 16px 16px 0 0;
    transition: background 0.35s ease;
}
.jc-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 20px 40px rgba(37, 99, 235, 0.08);
    border-color: rgba(37, 99, 235, 0.25);
}
.jc-card:hover::before {
    background: linear-gradient(90deg, #2563EB, #60A5FA);
}

/* Card Top Row */
.jc-top {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    margin-bottom: 16px;
}
.jc-type-badge {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
    color: #2563EB;
    background: rgba(37, 99, 235, 0.08);
    border: 1px solid rgba(37, 99, 235, 0.15);
    padding: 4px 12px;
    border-radius: 20px;
    text-transform: uppercase;
}

/* Title */
.jc-title {
    font-size: 17px;
    font-weight: 700;
    color: #111111;
    line-height: 1.35;
    margin-bottom: 12px;
    font-family: 'Poppins', sans-serif;
    letter-spacing: -0.2px;
}

/* Meta row: location + exp */
.jc-meta {
    display: flex;
    gap: 16px;
    flex-wrap: wrap;
    font-size: 12.5px;
    color: #6B7280;
    margin-bottom: 14px;
}
.jc-meta i {
    color: #2563EB;
    margin-right: 4px;
}

/* Summary */
.jc-summary {
    font-size: 13.5px;
    color: #6B7280;
    line-height: 1.65;
    margin-bottom: 18px;
    flex-grow: 1;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

/* Skill Tags */
.jc-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 7px;
    margin-bottom: 20px;
}
.jc-tags span {
    font-size: 11.5px;
    font-weight: 500;
    color: #374151;
    background: #F3F4F6;
    border: 1px solid #E5E7EB;
    padding: 4px 11px;
    border-radius: 20px;
    transition: all 0.2s ease;
}
.jc-card:hover .jc-tags span {
    background: rgba(37, 99, 235, 0.05);
    border-color: rgba(37, 99, 235, 0.2);
    color: #2563EB;
}

/* Card Footer */
.jc-footer {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-top: 16px;
    border-top: 1px solid #F3F4F6;
    margin-top: auto;
}
.jc-details-link {
    font-size: 13px;
    font-weight: 600;
    color: #2563EB;
    display: flex;
    align-items: center;
    gap: 6px;
    transition: gap 0.2s ease;
}
.jc-card:hover .jc-details-link {
    gap: 10px;
}
.jc-apply-btn {
    font-size: 12.5px;
    font-weight: 700;
    color: #FFFFFF;
    background: #2563EB;
    padding: 8px 20px;
    border-radius: 20px;
    text-decoration: none;
    transition: all 0.3s ease;
    letter-spacing: 0.3px;
    box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25);
}
.jc-apply-btn:hover {
    background: #1D4ED8;
    box-shadow: 0 6px 18px rgba(37, 99, 235, 0.35);
    color: #FFFFFF;
    transform: translateY(-1px);
}

/* ── Job Detail Modal ── */
.jm-overlay {
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.5);
    backdrop-filter: blur(6px);
    z-index: 9999;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 24px;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.3s ease;
}
.jm-overlay.active {
    opacity: 1;
    pointer-events: all;
}
.jm-box {
    background: #FFFFFF;
    border-radius: 24px;
    max-width: 680px;
    width: 100%;
    max-height: 85vh;
    display: flex;
    flex-direction: column;
    box-shadow: 0 40px 80px rgba(0, 0, 0, 0.18);
    transform: translateY(20px) scale(0.98);
    transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
    position: relative;
}
.jm-overlay.active .jm-box {
    transform: translateY(0) scale(1);
}
.jm-close {
    position: absolute;
    top: 20px; right: 20px;
    width: 36px; height: 36px;
    border-radius: 50%;
    border: 1px solid #E5E7EB;
    background: #F9FAFB;
    color: #374151;
    font-size: 20px;
    line-height: 1;
    cursor: pointer;
    display: flex; align-items: center; justify-content: center;
    transition: all 0.2s ease;
    z-index: 2;
}
.jm-close:hover { background: #F3F4F6; border-color: #D1D5DB; }

.jm-body {
    overflow-y: auto;
    padding: 40px 40px 8px;
    flex: 1;
}
.jm-header { margin-bottom: 24px; }
.jm-badge {
    display: inline-block;
    font-size: 11px; font-weight: 700; letter-spacing: 1px;
    color: #2563EB;
    background: rgba(37, 99, 235, 0.08);
    border: 1px solid rgba(37, 99, 235, 0.15);
    padding: 4px 12px; border-radius: 20px;
    text-transform: uppercase; margin-bottom: 14px;
}
.jm-header h2 {
    font-size: 22px; font-weight: 700; color: #111;
    font-family: 'Poppins', sans-serif; letter-spacing: -0.4px;
    margin-bottom: 12px; line-height: 1.3;
}
.jm-meta-row {
    display: flex; gap: 20px; flex-wrap: wrap;
    font-size: 13px; color: #6B7280;
}
.jm-meta-row i { color: #2563EB; margin-right: 5px; }
.jm-summary {
    font-size: 14px; color: #4B5563; line-height: 1.7;
    margin-bottom: 24px;
    padding-bottom: 24px;
    border-bottom: 1px solid #F3F4F6;
}
.jm-section { margin-bottom: 22px; }
.jm-section h5 {
    font-size: 13px; font-weight: 700; color: #111;
    text-transform: uppercase; letter-spacing: 0.8px;
    margin-bottom: 10px;
}
.jm-section ul {
    padding-left: 18px; margin: 0;
}
.jm-section ul li {
    font-size: 13.5px; color: #4B5563;
    line-height: 1.65; margin-bottom: 6px;
}
.jm-footer {
    padding: 20px 40px 28px;
    border-top: 1px solid #F3F4F6;
    display: flex; justify-content: flex-end;
}
.jm-apply-btn {
    background: #2563EB; color: #FFF;
    padding: 12px 32px; border-radius: 24px;
    text-decoration: none; font-weight: 700; font-size: 14px;
    box-shadow: 0 6px 18px rgba(37, 99, 235, 0.3);
    transition: all 0.3s ease;
}
.jm-apply-btn:hover {
    background: #1D4ED8; color: #FFF;
    box-shadow: 0 8px 24px rgba(37, 99, 235, 0.4);
    transform: translateY(-1px);
}

/* ── Responsive ── */
@media (max-width: 1024px) {
    .jobs-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 640px) {
    .jobs-grid { grid-template-columns: 1fr; gap: 16px; }
    .jm-body  { padding: 28px 24px 8px; }
    .jm-footer { padding: 16px 24px 24px; }
}
"""

with open(css_path, "a", encoding="utf-8") as f:
    f.write(new_css)
print("CSS appended successfully.")
