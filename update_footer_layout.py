import os
import glob
import re

def update_footer():
    html_files = glob.glob('*.html')
    
    new_footer_row = """            <div class="row">
                <div class="col-lg-6 col-md-6 mb-4">
                    <a href="index.html" class="logo footer-logo mb-3 d-inline-block">
                        <span class="logo-icon text-white"><i class="fa-solid fa-heart-pulse"></i></span>
                        <span class="logo-text text-white">Xpedicr<span class="dot">.</span></span>
                    </a>
                    <p class="text-light-gray mb-3">Building India's future healthcare infrastructure through technology, partnerships, logistics, and innovation.</p>
                    <div class="footer-contact text-light-gray">
                        <p class="text-sm mb-2"><i class="fa-solid fa-location-dot me-2"></i> Tech Park, Electronic City, Bengaluru, India</p>
                        <p class="text-sm mb-2"><i class="fa-solid fa-envelope me-2"></i> support@xpedicr.in</p>
                        <p class="text-sm mb-0"><i class="fa-solid fa-phone me-2"></i> +91 72898 90080</p>
                    </div>
                </div>
                
                <div class="col-lg-3 col-md-6 mb-4">
                    <h5 class="footer-title">Quick Links</h5>
                    <ul class="footer-links">
                        <li><a href="about.html">About Us</a></li>
                        <li><a href="ecosystem-services.html">Ecosystem & Services</a></li>
                        <li><a href="#" class="modal-trigger" data-modal="partnerModal">Future & Partners</a></li>
                        <li><a href="careers.html">Careers</a></li>
                    </ul>
                </div>
                
                <div class="col-lg-3 col-md-6 mb-4">
                    <h5 class="footer-title">Connect With Us</h5>
                    <div class="social-links mt-3">
                        <a href="#"><i class="fa-brands fa-linkedin-in"></i></a>
                        <a href="#"><i class="fa-brands fa-twitter"></i></a>
                        <a href="#"><i class="fa-brands fa-instagram"></i></a>
                    </div>
                </div>
            </div>"""

    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        pattern = re.compile(r'<div class="row">.*?</div>\s*<div class="footer-bottom', re.DOTALL)
        content = pattern.sub(new_footer_row + '\n            \n            <div class="footer-bottom', content)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

update_footer()
