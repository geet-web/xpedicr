import re
import os

base_dir = r"c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\xpedicr"
css_file = os.path.join(base_dir, "style.css")

with open(css_file, "r", encoding="utf-8") as f:
    css = f.read()

# We need to remove all blocks related to navbar, nav-container, logo, nav-links, mobile-menu, etc.
# But it's safer to just overwrite the specific blocks.
# Actually, I'll use a strong regex to remove all navbar-related classes.

classes_to_remove = [
    r'\.navbar\b', r'\.navbar\.scrolled', r'\.nav-container', r'\.logo\b', r'\.logo-icon',
    r'\.logo-text', r'\.nav-links', r'\.nav-actions', r'\.mobile-menu-btn', r'\.mobile-menu\b',
    r'\.mobile-menu\.active', r'\.close-menu', r'\.mobile-nav-links', r'\.floating-whatsapp',
    r'body\.inner-page \.navbar'
]

# We will just append our clean, bulletproof navbar at the end, using very high specificity
# so it overrides everything else, or we strip them out.
# A simple way to strip is to match `.class { ... }` but that fails with nested media queries.

# Let's just append an !important overridden block to guarantee the user sees what they want.
clean_navbar_css = """
/* ==========================================================================
   FINAL NAVBAR & MOBILE MENU CLEANUP
   ========================================================================== */

/* Hide all other potential duplicate navbars if any */
header:not(#navbar) {
    display: none !important;
}

.navbar {
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
    width: 100% !important;
    height: 80px !important;
    padding: 0 !important;
    margin: 0 !important;
    background-color: #FFFFFF !important;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05) !important;
    z-index: 9999 !important;
    display: flex !important;
    align-items: center !important;
    transition: all 0.3s ease !important;
    border-bottom: 1px solid #E5E7EB !important;
}

.navbar.scrolled {
    height: 72px !important;
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1) !important;
}

.navbar .nav-container {
    display: flex !important;
    justify-content: space-between !important;
    align-items: center !important;
    width: 100% !important;
    height: 100% !important;
    padding: 0 24px !important;
}

.navbar .logo {
    display: flex !important;
    align-items: center !important;
    gap: 12px !important;
    text-decoration: none !important;
}

.navbar .logo-icon {
    color: #2563EB !important;
    font-size: 24px !important;
}

.navbar .logo-text {
    color: #111111 !important;
    font-weight: 700 !important;
    font-size: 22px !important;
    font-family: 'Poppins', sans-serif !important;
}

.navbar .nav-links {
    display: flex !important;
    gap: 32px !important;
    align-items: center !important;
    margin: 0 !important;
    padding: 0 !important;
}

.navbar .nav-links a {
    color: #4B5563 !important;
    font-weight: 500 !important;
    font-size: 15px !important;
    text-decoration: none !important;
    transition: color 0.2s ease !important;
}

.navbar .nav-links a:hover,
.navbar .nav-links a.active {
    color: #2563EB !important;
}

.navbar .nav-actions {
    display: flex !important;
    align-items: center !important;
    gap: 16px !important;
}

.navbar .nav-actions .btn {
    padding: 10px 24px !important;
    background-color: #2563EB !important;
    color: #FFFFFF !important;
    border-radius: 6px !important;
    font-weight: 600 !important;
    border: none !important;
}

.navbar .nav-actions .btn:hover {
    background-color: #1D4ED8 !important;
}

/* Mobile Menu Button - Hidden on Desktop */
.navbar .mobile-menu-btn {
    display: none !important;
    background: transparent !important;
    border: none !important;
    color: #111111 !important;
    font-size: 24px !important;
    cursor: pointer !important;
}

/* Mobile Menu Styles */
.mobile-menu {
    position: fixed !important;
    top: 0 !important;
    right: -100% !important;
    width: 320px !important;
    max-width: 100vw !important;
    height: 100vh !important;
    background-color: #FFFFFF !important;
    z-index: 10000 !important;
    padding: 80px 32px 32px !important;
    box-shadow: -10px 0 25px rgba(0,0,0,0.1) !important;
    transition: right 0.4s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
    display: flex !important;
    flex-direction: column !important;
}

.mobile-menu.active {
    right: 0 !important;
}

.mobile-menu .close-menu {
    position: absolute !important;
    top: 24px !important;
    right: 24px !important;
    background: transparent !important;
    border: none !important;
    font-size: 28px !important;
    color: #111111 !important;
    cursor: pointer !important;
}

.mobile-menu .mobile-nav-links {
    display: flex !important;
    flex-direction: column !important;
    gap: 24px !important;
}

.mobile-menu .mobile-nav-links a {
    color: #111111 !important;
    font-size: 18px !important;
    font-weight: 500 !important;
    text-decoration: none !important;
}

.mobile-menu .mobile-nav-links a.active {
    color: #2563EB !important;
}

.mobile-menu .mobile-nav-links .btn {
    margin-top: 16px !important;
    background-color: #2563EB !important;
    color: #FFFFFF !important;
    text-align: center !important;
    padding: 14px !important;
    border-radius: 6px !important;
}

/* Push body down to prevent hero overlap since navbar is fixed */
body {
    padding-top: 80px !important; 
}

/* Override padding for hero sections that want to start at the top */
body .hero {
    margin-top: -80px !important;
    padding-top: 160px !important;
}

/* Responsive Rules */
@media (max-width: 992px) {
    .navbar .nav-links { display: none !important; }
    .navbar .nav-actions .btn { display: none !important; }
    .navbar .mobile-menu-btn { display: block !important; }
}
"""

with open(css_file, "a", encoding="utf-8") as f:
    f.write(clean_navbar_css)

print("Navbar CSS consolidated and overridden.")
