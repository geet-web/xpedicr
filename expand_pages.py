import os
import re

base_dir = r"c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\xpedicr"
index_path = os.path.join(base_dir, "index.html")

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# Extract header and footer
# The header goes from <!DOCTYPE html> until the end of <!-- Mobile Menu --> div.
# We can find <!-- Hero Section --> and split there.
header_end = content.find("<!-- Hero Section -->")
footer_start = content.find("<!-- Footer -->")

header = content[:header_end]
footer = content[footer_start:]

# Remove the spacer from header if it exists (I didn't put it in index.html before, so it shouldn't be there, but just in case)
header = header.replace('<div style="height: 80px; background: var(--dark);"></div>\n', '')

def build_page(page_name, page_content, active_link):
    # Set the active link properly
    # Remove active class from all nav links first just to be safe
    new_header = re.sub(r'class="active"', '', header)
    # Then add it back to the specific one
    old_link = f'href="{active_link}"'
    new_link = f'href="{active_link}" class="active"'
    new_header = new_header.replace(old_link, new_link)
    
    page = new_header + page_content + footer
    with open(os.path.join(base_dir, page_name), "w", encoding="utf-8") as f:
        f.write(page)

# --- ABOUT PAGE CONTENT ---
about_content = """
    <!-- Inner Hero -->
    <div class="inner-hero">
        <div class="container fade-in-up">
            <h1>About Xpedicr</h1>
            <p>Building India’s future healthcare infrastructure through innovation, compassion, and technology.</p>
        </div>
    </div>

    <!-- Company Story -->
    <section class="section-padding">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-md-6 scroll-reveal left">
                    <img src="images/realistic_healthcare_tech_story_1777566250841.png" alt="Xpedicr Ecosystem" class="rounded-image shadow-lg" style="width: 100%; height: auto; border-radius: 16px; object-fit: cover;">
                </div>
                <div class="col-md-6 scroll-reveal right">
                    <div class="content-block">
                        <span class="subtitle">Our Story</span>
                        <h3>Why Xpedicr Was Founded</h3>
                        <p>India’s healthcare system, while immense and growing, suffers from deep fragmentation. Patients often struggle to find immediate emergency support, reliable diagnostics, and accessible specialists all under one roof.</p>
                        <p>Xpedicr was born out of a profound realization: technology is the only scalable bridge capable of uniting these fragmented pieces. By combining rapid logistics, verified medical professionals, and advanced AI platforms, we aim to solve the accessibility and affordability crisis.</p>
                        <p class="mt-4" style="color: var(--dark); font-style: italic; font-weight: 600; font-size: 1.1rem;">Our philosophy is simple: Geography and infrastructure should never stand in the way of saving a life.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Core Values -->
    <section class="section-padding bg-light">
        <div class="container">
            <div class="section-title text-center scroll-reveal up">
                <span class="subtitle">Our Principles</span>
                <h2>Core Values</h2>
            </div>
            <div class="features-grid mt-5">
                <div class="value-card scroll-reveal up">
                    <i class="fa-solid fa-lightbulb"></i>
                    <h4>Innovation</h4>
                    <p>Continuously pushing the boundaries of what health-tech can achieve.</p>
                </div>
                <div class="value-card scroll-reveal up delay-1">
                    <i class="fa-solid fa-shield-halved"></i>
                    <h4>Trust</h4>
                    <p>Maintaining the highest standards of data security and clinical reliability.</p>
                </div>
                <div class="value-card scroll-reveal up delay-2">
                    <i class="fa-solid fa-globe"></i>
                    <h4>Accessibility</h4>
                    <p>Democratizing top-tier healthcare for both urban and rural populations.</p>
                </div>
                <div class="value-card scroll-reveal up">
                    <i class="fa-solid fa-bolt"></i>
                    <h4>Speed</h4>
                    <p>Optimizing logistics for the fastest emergency and delivery responses.</p>
                </div>
                <div class="value-card scroll-reveal up delay-1">
                    <i class="fa-solid fa-heart"></i>
                    <h4>Compassion</h4>
                    <p>Putting the patient's well-being at the absolute center of our universe.</p>
                </div>
                <div class="value-card scroll-reveal up delay-2">
                    <i class="fa-solid fa-handshake"></i>
                    <h4>Integrity</h4>
                    <p>Operating with transparent, ethical practices in every partnership and patient interaction.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Founder Message -->
    <section class="founder section-padding bg-dark text-white">
        <div class="container">
            <div class="founder-wrapper scroll-reveal up">
                <div class="quote-icon"><i class="fa-solid fa-quote-left"></i></div>
                <blockquote class="founder-quote">
                    "We are not just building services, we are building India’s future healthcare infrastructure."
                </blockquote>
                <div class="founder-info">
                    <div class="founder-avatar">
                        <img src="https://images.unsplash.com/photo-1560250097-0b93528c311a?auto=format&fit=crop&q=80&w=256&h=256" alt="CEO">
                    </div>
                    <div class="founder-details">
                        <h4>Founder & CEO</h4>
                        <p>Xpedicr Industry Pvt. Ltd.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Call to Action -->
    <section class="section-padding bg-white text-center">
        <div class="container scroll-reveal up">
            <h2 class="mb-4">Ready to Transform Healthcare?</h2>
            <p class="section-desc mb-5" style="margin-left: auto; margin-right: auto; max-width: 600px;">Whether you're a healthcare provider looking to scale, or an innovator wanting to make an impact, we want you on our side.</p>
            <div class="mt-4" style="display: flex; justify-content: center; gap: 20px;">
                <a href="#" class="btn btn-primary btn-lg modal-trigger" data-modal="partnerModal">Partner With Us</a>
                <a href="careers.html" class="btn btn-outline-dark btn-lg">Explore Careers</a>
            </div>
        </div>
    </section>
"""

# --- ECOSYSTEM & SERVICES PAGE CONTENT ---
ecosystem_content = """
    <!-- Inner Hero -->
    <div class="inner-hero">
        <div class="container fade-in-up">
            <h1>Ecosystem & Services</h1>
            <p>A unified network of specialized brands and comprehensive healthcare solutions working together seamlessly.</p>
        </div>
    </div>

    <!-- Detailed Brands -->
    <section class="section-padding bg-light">
        <div class="container">
            <div class="section-title text-center scroll-reveal up">
                <span class="subtitle">Innovation Brands</span>
                <h2>Our Specialized Subsidiaries</h2>
                <p class="section-desc">How all brands work together under one powerful ecosystem.</p>
            </div>

            <div class="brand-detail-card scroll-reveal up mt-5">
                <div class="brand-detail-icon"><i class="fa-solid fa-suitcase-medical"></i></div>
                <div class="brand-detail-content">
                    <span class="subtitle glow-text">Access Platform</span>
                    <h3>Nidhaan</h3>
                    <p>Nidhaan serves as the core operational platform helping families with end-to-end healthcare logistics. From routing ambulances to fulfilling pharmacy orders within 30 minutes, it is the backbone of our physical service network.</p>
                    <ul>
                        <li><i class="fa-solid fa-check"></i> Fast medicine delivery</li>
                        <li><i class="fa-solid fa-check"></i> Verified doctor consultations</li>
                        <li><i class="fa-solid fa-check"></i> Telemedicine convenience</li>
                        <li><i class="fa-solid fa-check"></i> Ambulance booking during emergencies</li>
                        <li><i class="fa-solid fa-check"></i> Diagnostics from trusted NABL labs</li>
                        <li><i class="fa-solid fa-check"></i> Preventive wellness support</li>
                    </ul>
                </div>
            </div>

            <div class="brand-detail-card scroll-reveal up">
                <div class="brand-detail-icon"><i class="fa-solid fa-brain"></i></div>
                <div class="brand-detail-content">
                    <span class="subtitle glow-text">Intelligence Engine</span>
                    <h3>Nava.ai</h3>
                    <p>Nava.ai represents the future of AI-driven healthcare. It ingests data from patient interactions to predict health risks, automate triaging, and provide clinical decision support to our partner doctors.</p>
                    <ul>
                        <li><i class="fa-solid fa-check"></i> Smart patient support assistant</li>
                        <li><i class="fa-solid fa-check"></i> Symptom guidance system</li>
                        <li><i class="fa-solid fa-check"></i> Healthcare workflow automation</li>
                        <li><i class="fa-solid fa-check"></i> Predictive care systems</li>
                        <li><i class="fa-solid fa-check"></i> AI-based health engagement</li>
                        <li><i class="fa-solid fa-check"></i> Automated diagnostic analysis</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>
"""

# --- FUTURE & PARTNERS PAGE CONTENT ---
future_content = """
    <!-- Inner Hero -->
    <div class="inner-hero">
        <div class="container fade-in-up">
            <h1>Future Expansion & Partners</h1>
            <p>Scaling our operations to build India's strongest healthcare alliance.</p>
        </div>
    </div>

    <!-- Expansion Vision -->
    <section class="section-padding">
        <div class="container">
            <div class="row align-items-center mb-5">
                <div class="col-md-6 scroll-reveal left">
                    <div class="content-block">
                        <span class="subtitle">Growth Roadmap</span>
                        <h3>Our Nationwide Vision</h3>
                        <p>We are executing an aggressive roadmap to ensure our ecosystem reaches every corner of the country. This involves not just digital scale, but deep physical infrastructure partnerships.</p>
                        <p>Our goal is to build a <strong>10-minute emergency healthcare response model</strong> in top urban areas while simultaneously expanding robust telemedicine and mobile clinic access to Tier 2, Tier 3, and rural India.</p>
                    </div>
                </div>
                <div class="col-md-6 scroll-reveal right">
                    <div class="about-image-wrapper">
                        <img src="https://images.unsplash.com/photo-1576091160550-2173dba999ef?auto=format&fit=crop&q=80&w=800" alt="Healthcare Expansion" class="rounded-image shadow-lg">
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Partner Benefits -->
    <section class="section-padding bg-light">
        <div class="container">
            <div class="section-title text-center scroll-reveal up">
                <span class="subtitle">Partnerships</span>
                <h2>Why Partner With Us</h2>
                <p class="section-desc">We bring volume, efficiency, and technology to your practice.</p>
            </div>

            <div class="features-grid grid-2 mt-5">
                <div class="partner-benefit-card scroll-reveal up">
                    <h4><i class="fa-solid fa-hospital text-primary me-2"></i> Hospitals</h4>
                    <p>Integrate our ambulance aggregator for faster inbound emergency routing and digitize your OPD flow with our AI triage.</p>
                </div>
                <div class="partner-benefit-card scroll-reveal up delay-1">
                    <h4><i class="fa-solid fa-stethoscope text-primary me-2"></i> Clinics & Doctors</h4>
                    <p>Gain access to thousands of telemedicine patients, automated appointment scheduling, and AI-assisted clinical data.</p>
                </div>
                <div class="partner-benefit-card scroll-reveal up delay-2">
                    <h4><i class="fa-solid fa-microscope text-primary me-2"></i> Diagnostic Labs</h4>
                    <p>Expand your reach with our home sample collection logistics fleet and deliver digital reports instantly.</p>
                </div>
                <div class="partner-benefit-card scroll-reveal up">
                    <h4><i class="fa-solid fa-pills text-primary me-2"></i> Pharmacies</h4>
                    <p>Turn your local store into a micro-fulfillment center serving 30-minute delivery orders generated by our app.</p>
                </div>
            </div>

            <div class="text-center mt-5 pt-4 scroll-reveal up">
                <a href="contact.html" class="btn btn-primary btn-lg">Become a Growth Partner</a>
            </div>
        </div>
    </section>
"""

# --- CONTACT PAGE CONTENT ---
contact_content = """
    <!-- Inner Hero -->
    <div class="inner-hero">
        <div class="container fade-in-up">
            <h1>Contact Us</h1>
            <p>We're here to help and answer any question you might have.</p>
        </div>
    </div>

    <!-- Contact Form & Info -->
    <section class="section-padding">
        <div class="container">
            <div class="contact-wrapper shadow-lg scroll-reveal up">
                <div class="row">
                    <div class="col-md-7 contact-form-wrapper p-5">
                        <h3 class="mb-4">Send a Message</h3>
                        <form class="contact-form">
                            <div class="row">
                                <div class="col-md-6 form-group">
                                    <label>Full Name</label>
                                    <input type="text" class="form-control" placeholder="John Doe" required>
                                </div>
                                <div class="col-md-6 form-group">
                                    <label>Email</label>
                                    <input type="email" class="form-control" placeholder="john@company.com" required>
                                </div>
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
                        <a href="#" class="btn btn-light btn-lg w-100"><i class="fa-brands fa-whatsapp text-success me-2"></i> Chat Now</a>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

# Build all pages
build_page("about.html", about_content, "about.html")
build_page("ecosystem-services.html", ecosystem_content, "ecosystem-services.html")
build_page("future-partners.html", future_content, "future-partners.html")
build_page("contact.html", contact_content, "contact.html")

print("Expanded pages successfully generated!")
