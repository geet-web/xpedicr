import os

base_dir = r"c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\xpedicr"

css_content = """
/* Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Poppins:wght@500;600;700&display=swap');

:root {
    --white: #FFFFFF;
    --black: #111111;
    --charcoal: #1A1A1A;
    --accent: #2563EB;
    --accent-hover: #1D4ED8;
    --bg-light: #F9FAFB;
    --border-color: #E5E7EB;
    --text-muted: #6B7280;
    
    --font-heading: 'Poppins', sans-serif;
    --font-body: 'Inter', sans-serif;
    
    --transition: all 0.3s ease;
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    font-family: var(--font-body);
    color: var(--charcoal);
    background-color: var(--white);
    line-height: 1.6;
    overflow-x: hidden;
}

h1, h2, h3, h4, h5, h6 {
    font-family: var(--font-heading);
    color: var(--black);
    font-weight: 600;
    line-height: 1.2;
}

a { text-decoration: none; color: var(--accent); transition: var(--transition); }
a:hover { color: var(--accent-hover); }

img { max-width: 100%; height: auto; display: block; }

/* Utilities */
.container { width: 100%; max-width: 1200px; margin: 0 auto; padding: 0 24px; }
.section-padding { padding: 100px 0; }
.bg-light { background-color: var(--bg-light); }
.text-center { text-align: center; }
.text-muted { color: var(--text-muted); }
.mb-1 { margin-bottom: 8px; }
.mb-2 { margin-bottom: 16px; }
.mb-3 { margin-bottom: 24px; }
.mb-4 { margin-bottom: 32px; }
.mb-5 { margin-bottom: 48px; }
.mt-4 { margin-top: 32px; }

/* Buttons */
.btn {
    display: inline-block;
    padding: 12px 28px;
    font-family: var(--font-heading);
    font-weight: 500;
    font-size: 15px;
    border-radius: 6px;
    cursor: pointer;
    transition: var(--transition);
    border: 1px solid transparent;
}
.btn-primary {
    background-color: var(--accent);
    color: var(--white);
}
.btn-primary:hover {
    background-color: var(--accent-hover);
    color: var(--white);
}
.btn-outline {
    background-color: transparent;
    border-color: var(--charcoal);
    color: var(--charcoal);
}
.btn-outline:hover {
    background-color: var(--charcoal);
    color: var(--white);
}

/* Navbar */
.navbar {
    position: fixed;
    top: 0; left: 0; width: 100%;
    background-color: var(--white);
    border-bottom: 1px solid var(--border-color);
    z-index: 1000;
    transition: var(--transition);
}
.navbar .container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 80px;
}
.logo {
    display: flex;
    align-items: center;
    gap: 8px;
    font-family: var(--font-heading);
    font-size: 24px;
    font-weight: 700;
    color: var(--black);
}
.logo i { color: var(--accent); }
.nav-links {
    display: flex;
    gap: 32px;
}
.nav-links a {
    color: var(--charcoal);
    font-weight: 500;
    font-size: 15px;
}
.nav-links a:hover, .nav-links a.active {
    color: var(--accent);
}
.nav-right { display: flex; align-items: center; gap: 20px; }
.hamburger { display: none; font-size: 24px; cursor: pointer; color: var(--black); border: none; background: transparent; }

/* Mobile Menu */
.mobile-menu {
    position: fixed; top: 0; right: -100%; width: 300px; height: 100vh;
    background: var(--white); z-index: 2000; padding: 40px 24px;
    box-shadow: -5px 0 15px rgba(0,0,0,0.05); transition: right 0.3s ease;
}
.mobile-menu.active { right: 0; }
.close-menu { position: absolute; top: 24px; right: 24px; font-size: 24px; cursor: pointer; background: none; border: none; }
.mobile-nav-links { display: flex; flex-direction: column; gap: 24px; margin-top: 40px; }
.mobile-nav-links a { color: var(--charcoal); font-weight: 500; font-size: 18px; }

/* Scroll to top */
.scroll-top {
    position: fixed; bottom: 30px; right: 30px;
    background: var(--accent); color: var(--white);
    width: 45px; height: 45px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    cursor: pointer; opacity: 0; pointer-events: none; transition: var(--transition); z-index: 999; border: none;
}
.scroll-top.visible { opacity: 1; pointer-events: all; }
.scroll-top:hover { background: var(--black); }

/* Hero Section */
.hero {
    padding: 180px 0 100px;
    min-height: 90vh;
    display: flex; align-items: center;
}
.hero-split {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 60px;
    align-items: center;
}
.hero-label {
    display: inline-block;
    padding: 6px 12px;
    background: var(--bg-light);
    color: var(--accent);
    font-size: 13px;
    font-weight: 600;
    border-radius: 4px;
    margin-bottom: 24px;
    text-transform: uppercase;
    letter-spacing: 1px;
}
.hero h1 { font-size: 48px; margin-bottom: 24px; }
.hero p { font-size: 18px; color: var(--text-muted); margin-bottom: 40px; max-width: 500px; }
.hero-img { width: 100%; border-radius: 12px; object-fit: cover; box-shadow: 0 20px 40px rgba(0,0,0,0.08); }

/* Inner Hero */
.inner-hero {
    padding: 160px 0 80px;
    background: var(--bg-light);
    text-align: center;
    border-bottom: 1px solid var(--border-color);
}
.inner-hero h1 { font-size: 42px; margin-bottom: 16px; }
.inner-hero p { font-size: 18px; color: var(--text-muted); max-width: 600px; margin: 0 auto; }

/* Grid Layouts */
.grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; }
.grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px; }
.grid-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; }

/* Cards */
.card {
    background: var(--white);
    border: 1px solid var(--border-color);
    padding: 32px;
    border-radius: 8px;
    transition: var(--transition);
}
.card:hover {
    box-shadow: 0 10px 30px rgba(0,0,0,0.04);
    transform: translateY(-4px);
    border-color: var(--accent);
}
.card-icon {
    font-size: 32px;
    color: var(--accent);
    margin-bottom: 24px;
}

/* Trust Bar */
.trust-bar {
    padding: 40px 0;
    border-bottom: 1px solid var(--border-color);
    background: var(--white);
}
.trust-grid {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 20px;
}
.trust-item {
    display: flex;
    align-items: center;
    gap: 12px;
    color: var(--charcoal);
    font-weight: 500;
}
.trust-item i { color: var(--accent); font-size: 20px; }

/* Footer */
.footer {
    background: var(--black);
    color: var(--white);
    padding: 80px 0 24px;
}
.footer-grid {
    display: grid;
    grid-template-columns: 2fr 1fr 1fr 1fr;
    gap: 40px;
    margin-bottom: 60px;
}
.footer-logo { color: var(--white); margin-bottom: 20px; display: inline-flex; }
.footer p { color: #A1A1AA; font-size: 14px; }
.footer h4 { color: var(--white); font-size: 18px; margin-bottom: 24px; }
.footer-links { list-style: none; }
.footer-links li { margin-bottom: 12px; }
.footer-links a { color: #A1A1AA; font-size: 15px; }
.footer-links a:hover { color: var(--white); }
.footer-bottom {
    border-top: 1px solid rgba(255,255,255,0.1);
    padding-top: 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 14px;
    color: #A1A1AA;
}
.social-icons { display: flex; gap: 16px; }
.social-icons a { color: #A1A1AA; font-size: 18px; }
.social-icons a:hover { color: var(--white); }

/* Forms */
.form-group { margin-bottom: 24px; }
.form-label { display: block; font-weight: 500; margin-bottom: 8px; font-size: 14px; }
.form-control {
    width: 100%;
    padding: 12px 16px;
    border: 1px solid var(--border-color);
    border-radius: 6px;
    font-family: var(--font-body);
    font-size: 15px;
    transition: var(--transition);
}
.form-control:focus {
    outline: none;
    border-color: var(--accent);
    box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

/* Timeline */
.timeline { position: relative; padding-left: 30px; }
.timeline::before {
    content: ''; position: absolute; left: 0; top: 0; height: 100%; width: 2px; background: var(--border-color);
}
.timeline-item { position: relative; margin-bottom: 40px; }
.timeline-item::before {
    content: ''; position: absolute; left: -35px; top: 5px; width: 12px; height: 12px;
    background: var(--accent); border-radius: 50%; border: 3px solid var(--white);
}
.timeline-date { font-weight: 700; color: var(--accent); margin-bottom: 8px; }

/* Responsive */
@media (max-width: 992px) {
    .nav-links, .nav-right .btn { display: none; }
    .hamburger { display: block; }
    .hero-split { grid-template-columns: 1fr; text-align: center; }
    .hero p { margin: 0 auto 40px; }
    .footer-grid { grid-template-columns: 1fr 1fr; }
}
@media (max-width: 768px) {
    .grid-2, .grid-3, .grid-4 { grid-template-columns: 1fr; }
    .footer-grid { grid-template-columns: 1fr; }
    .footer-bottom { flex-direction: column; gap: 16px; text-align: center; }
}

/* Animations */
.reveal { opacity: 0; transform: translateY(30px); transition: all 0.8s ease; }
.reveal.active { opacity: 1; transform: translateY(0); }
"""

js_content = """
document.addEventListener('DOMContentLoaded', () => {
    // Mobile Menu
    const hamburger = document.querySelector('.hamburger');
    const mobileMenu = document.querySelector('.mobile-menu');
    const closeMenu = document.querySelector('.close-menu');

    if(hamburger) {
        hamburger.addEventListener('click', () => {
            mobileMenu.classList.add('active');
        });
    }
    if(closeMenu) {
        closeMenu.addEventListener('click', () => {
            mobileMenu.classList.remove('active');
        });
    }

    // Scroll Reveal
    const reveals = document.querySelectorAll('.reveal');
    const revealOnScroll = () => {
        const windowHeight = window.innerHeight;
        const elementVisible = 100;
        reveals.forEach(reveal => {
            const elementTop = reveal.getBoundingClientRect().top;
            if (elementTop < windowHeight - elementVisible) {
                reveal.classList.add('active');
            }
        });
    };
    window.addEventListener('scroll', revealOnScroll);
    revealOnScroll(); // Trigger on load

    // Scroll to Top
    const scrollTopBtn = document.querySelector('.scroll-top');
    if(scrollTopBtn) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 300) {
                scrollTopBtn.classList.add('visible');
            } else {
                scrollTopBtn.classList.remove('visible');
            }
        });
        scrollTopBtn.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }
});
"""

with open(os.path.join(base_dir, "style.css"), "w", encoding="utf-8") as f:
    f.write(css_content)

with open(os.path.join(base_dir, "script.js"), "w", encoding="utf-8") as f:
    f.write(js_content)

print("CSS and JS generated.")
