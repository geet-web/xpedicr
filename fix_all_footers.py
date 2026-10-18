import re
import glob

NEW_FOOTER = """    <!-- Footer -->
    <footer class="footer bg-dark text-white">
        <div class="container">
            <div class="footer-row">
                <!-- Col 1: Brand + description -->
                <div class="footer-brand-section">
                    <a href="index.html" class="logo footer-logo">
                        <span class="logo-icon text-white"><i class="fa-solid fa-heart-pulse"></i></span>
                        <span class="logo-text text-white">Xpedicr<span class="dot">.</span></span>
                    </a>
                    <p class="footer-description">Building India&apos;s future healthcare infrastructure through technology, partnerships, logistics, and innovation.</p>
                </div>

                <!-- Col 2: Quick links -->
                <div class="footer-links-section">
                    <h5 class="footer-title">Quick Links</h5>
                    <ul class="footer-links">
                        <li><a href="about.html">About Us</a></li>
                        <li><a href="ecosystem-services.html">Ecosystem &amp; Services</a></li>
                        <li><a href="future-partners.html">Future &amp; Partners</a></li>
                        <li><a href="careers.html">Careers</a></li>
                    </ul>
                </div>

                <!-- Col 3: Our Brands -->
                <div class="footer-links-section">
                    <h5 class="footer-title">Our Brands</h5>
                    <ul class="footer-links">
                        <li><a href="ecosystem-services.html#nidhaan">Nidhaan</a></li>
                        <li><a href="ecosystem-services.html#nava">Nava.ai</a></li>
                    </ul>
                </div>

                <!-- Col 4: Contact / social icons -->
                <div class="footer-social-section">
                    <div class="footer-contact mb-4">
                        <div class="contact-item">
                            <i class="fa-solid fa-location-dot"></i>
                            <p>Tech Park, Electronic City, Bengaluru, India</p>
                        </div>
                        <div class="contact-item">
                            <i class="fa-solid fa-envelope"></i>
                            <p>support@xpedicr.in</p>
                        </div>
                        <div class="contact-item">
                            <i class="fa-solid fa-phone"></i>
                            <p>+91 72898 90080</p>
                        </div>
                    </div>
                    
                    <h5 class="footer-title">Connect With Us</h5>
                    <div class="social-links">
                        <a href="#" aria-label="LinkedIn"><i class="fa-brands fa-linkedin-in"></i></a>
                        <a href="#" aria-label="Twitter"><i class="fa-brands fa-twitter"></i></a>
                        <a href="#" aria-label="Instagram"><i class="fa-brands fa-instagram"></i></a>
                    </div>
                </div>
            </div>

            <div class="footer-bottom">
                <p class="mb-0">&copy; 2026 Xpedicr Industry Pvt. Ltd. All rights reserved.</p>
                <div class="footer-legal">
                    <a href="#" class="modal-trigger" data-modal="privacyModal">Privacy Policy</a>
                    <a href="#" class="modal-trigger" data-modal="termsModal">Terms of Service</a>
                </div>
            </div>
        </div>
    </footer>"""

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace the full footer block
    new_content = re.sub(
        r'<!-- Footer -->.*?</footer>',
        NEW_FOOTER,
        content,
        flags=re.DOTALL
    )

    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {file}")
    else:
        print(f"No footer found in: {file}")
