import re

new_footer = """
    <!-- Footer -->
    <footer class="footer bg-dark text-white">
        <div class="container">
            <div class="row">
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
            </div>
            
            <div class="footer-bottom mt-4 pt-4 border-top border-secondary text-light-gray text-sm d-flex justify-content-between align-items-center flex-wrap" style="padding-bottom: 20px;">
                <p class="mb-0">&copy; 2026 Xpedicr Industry Pvt. Ltd. All rights reserved.</p>
                <div class="footer-legal mt-0">
                    <a href="#" class="modal-trigger" data-modal="privacyModal">Privacy Policy</a>
                    <a href="#" class="modal-trigger" data-modal="termsModal">Terms of Service</a>
                </div>
            </div>
        </div>
    </footer>
"""

contact_row = """
                <div class="row m-0">
                    <div class="col-md-7 contact-form-wrapper p-5">
                        <h2 class="mb-4">Get in Touch</h2>
                        <form id="contactForm" class="contact-form">
                            <div class="row">
                                <div class="col-md-6 form-group">
                                    <label>Name</label>
                                    <input type="text" class="form-control" placeholder="John Doe" required>
                                </div>
                                <div class="col-md-6 form-group">
                                    <label>Phone</label>
                                    <input type="tel" class="form-control" placeholder="+91 XXXXX XXXXX" required>
                                </div>
                            </div>
                            <div class="form-group">
                                <label>Email</label>
                                <input type="email" class="form-control" placeholder="john@company.com" required>
                            </div>
                            <div class="form-group">
                                <label>Inquiry Type</label>
                                <select class="form-control text-gray">
                                    <option>Partnership Inquiry</option>
                                    <option>Careers</option>
                                    <option>Customer Support</option>
                                    <option>Media & Press</option>
                                </select>
                            </div>
                            <div class="form-group mt-3">
                                <label>Message</label>
                                <textarea class="form-control" rows="4" placeholder="How can we help you?" required></textarea>
                            </div>
                            <button type="submit" class="btn btn-primary btn-lg w-100 mt-2">Send Message</button>
                        </form>
                    </div>
                    
                    <div class="col-md-5 contact-info-wrapper p-5 bg-primary text-white d-flex align-items-center justify-content-center flex-column text-center">
                        <div class="brand-detail-icon bg-white text-primary mb-4 shadow-lg"><i class="fa-brands fa-whatsapp"></i></div>
                        <h3 class="text-white mb-3">Instant Support</h3>
                        <p class="text-light-gray mb-4">Need immediate assistance? Connect with our dedicated support team on WhatsApp for instant resolutions.</p>
                        <a href="https://wa.me/917289890080" target="_blank" class="btn btn-light btn-lg w-100"><i class="fa-brands fa-whatsapp text-success me-2"></i> Chat Now</a>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace from <div class="row m-0"> down to <!-- WhatsApp
content = re.sub(r'<div class="row m-0">.*?<!-- WhatsApp', contact_row + new_footer + '\n    <!-- WhatsApp', content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
