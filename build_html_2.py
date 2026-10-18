import os

base_dir = r"c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\xpedicr"

header_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header class="navbar">
        <div class="container">
            <a href="index.html" class="logo">
                <i class="fa-solid fa-heart-pulse"></i> Xpedicr
            </a>
            <nav class="nav-links">
                <a href="index.html" class="{active_home}">Home</a>
                <a href="about.html" class="{active_about}">About</a>
                <a href="ecosystem-services.html" class="{active_ecosystem}">Ecosystem & Services</a>
                <a href="nava-ai.html" class="{active_nava}">Nava.ai</a>
                <a href="future-partners.html" class="{active_future}">Future & Partners</a>
                <a href="careers.html" class="{active_careers}">Careers & News</a>
                <a href="contact.html" class="{active_contact}">Contact</a>
            </nav>
            <div class="nav-right">
                <a href="partner-with-us.html" class="btn btn-primary">Partner With Us</a>
                <button class="hamburger"><i class="fa-solid fa-bars"></i></button>
            </div>
        </div>
    </header>

    <div class="mobile-menu">
        <button class="close-menu"><i class="fa-solid fa-xmark"></i></button>
        <div class="mobile-nav-links">
            <a href="index.html">Home</a>
            <a href="about.html">About</a>
            <a href="ecosystem-services.html">Ecosystem & Services</a>
            <a href="nava-ai.html">Nava.ai</a>
            <a href="future-partners.html">Future & Partners</a>
            <a href="careers.html">Careers & News</a>
            <a href="contact.html">Contact</a>
            <a href="partner-with-us.html" class="btn btn-primary mt-4" style="color: white; text-align: center;">Partner With Us</a>
        </div>
    </div>
"""

footer_template = """
    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-col">
                    <a href="index.html" class="logo footer-logo">
                        <i class="fa-solid fa-heart-pulse"></i> Xpedicr
                    </a>
                    <p class="mt-4">Building India's future healthcare infrastructure through technology, partnerships, and scalable ecosystems.</p>
                </div>
                <div class="footer-col">
                    <h4>Quick Links</h4>
                    <ul class="footer-links">
                        <li><a href="about.html">About Us</a></li>
                        <li><a href="future-partners.html">Future & Partners</a></li>
                        <li><a href="careers.html">Careers & News</a></li>
                        <li><a href="contact.html">Contact Support</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Ecosystem</h4>
                    <ul class="footer-links">
                        <li><a href="ecosystem-services.html">Nidhaan</a></li>
                        <li><a href="nava-ai.html">Nava.ai</a></li>
                        <li><a href="partner-with-us.html">Partner Network</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Newsletter</h4>
                    <p class="mb-3">Get the latest updates on our healthcare ecosystem.</p>
                    <div class="form-group mb-0">
                        <input type="email" class="form-control" placeholder="Email address" style="background: transparent; color: white; border-color: #333;">
                        <button class="btn btn-primary mt-2" style="width: 100%;">Subscribe</button>
                    </div>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 Xpedicr Industry Pvt. Ltd. All rights reserved.</p>
                <div class="social-icons">
                    <a href="#"><i class="fa-brands fa-linkedin-in"></i></a>
                    <a href="#"><i class="fa-brands fa-twitter"></i></a>
                </div>
                <div class="footer-legal">
                    <a href="#">Privacy Policy</a>
                    <span style="margin: 0 10px;">|</span>
                    <a href="#">Terms of Service</a>
                </div>
            </div>
        </div>
    </footer>
    <button class="scroll-top"><i class="fa-solid fa-arrow-up"></i></button>
    <script src="script.js"></script>
</body>
</html>
"""

nava_body = """
    <div class="inner-hero" style="background: var(--black); color: var(--white);">
        <div class="container">
            <h1 class="reveal text-white">Nava.ai</h1>
            <p class="reveal" style="color: #A1A1AA;">The intelligent core of our healthcare infrastructure.</p>
        </div>
    </div>
    <section class="section-padding">
        <div class="container">
            <div class="grid-2 align-center reveal mb-5">
                <div>
                    <h2 class="mb-4">Future Healthcare Intelligence</h2>
                    <p class="text-muted mb-4">Nava.ai is our proprietary artificial intelligence platform designed specifically for healthcare operational efficiency. We do not believe in fake dashboards—we believe in backend intelligence that drives real-world outcomes.</p>
                    <p class="text-muted mb-4">By analyzing vast amounts of operational data, Nava.ai predicts demand, automates triage, and optimizes the routing of our emergency and delivery fleets.</p>
                </div>
                <div><img src="https://images.unsplash.com/photo-1555255707-c07966088b7b?auto=format&fit=crop&q=80&w=800" alt="AI Technology" style="border-radius: 8px;"></div>
            </div>
            
            <h2 class="text-center mb-5 mt-5 reveal">Core Capabilities</h2>
            <div class="grid-3 reveal">
                <div class="card"><div class="card-icon"><i class="fa-solid fa-chart-pie"></i></div><h4>Predictive Support</h4><p class="text-muted mt-2">Anticipating medical resource demands regionally.</p></div>
                <div class="card"><div class="card-icon"><i class="fa-solid fa-robot"></i></div><h4>Smart Patient Assistance</h4><p class="text-muted mt-2">Automated preliminary triage and routing.</p></div>
                <div class="card"><div class="card-icon"><i class="fa-solid fa-gears"></i></div><h4>Healthcare Automation</h4><p class="text-muted mt-2">Reducing administrative burden for partners.</p></div>
            </div>
        </div>
    </section>
"""

future_body = """
    <div class="inner-hero">
        <div class="container">
            <h1 class="reveal">Future & Partners</h1>
            <p class="reveal">Our expansion vision and roadmap for healthcare equity.</p>
        </div>
    </div>
    <section class="section-padding">
        <div class="container">
            <div class="grid-2 align-center reveal mb-5">
                <div><img src="https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?auto=format&fit=crop&q=80&w=800" alt="Expansion Vision" style="border-radius: 8px;"></div>
                <div>
                    <h2 class="mb-4">Expansion Vision</h2>
                    <p class="text-muted mb-4">Xpedicr is not just building a product; we are building an ecosystem. Over the next five years, our primary objective is deep market penetration across underserved regions.</p>
                    <ul style="list-style: none; color: var(--text-muted);">
                        <li class="mb-2"><i class="fa-solid fa-building text-accent me-2"></i> Tier 2/3 City Focus</li>
                        <li class="mb-2"><i class="fa-solid fa-truck-medical text-accent me-2"></i> Emergency Infrastructure Scale</li>
                        <li><i class="fa-solid fa-handshake text-accent me-2"></i> Private-Public Collaboration Models</li>
                    </ul>
                </div>
            </div>
            
            <h2 class="text-center mb-5 mt-5 reveal">Growth Roadmap</h2>
            <div style="max-width: 800px; margin: 0 auto;">
                <div class="timeline">
                    <div class="timeline-item reveal"><div class="timeline-date">Phase 1: Present</div><h4>Urban Consolidation</h4><p class="text-muted">Establishing the core technology layer.</p></div>
                    <div class="timeline-item reveal"><div class="timeline-date">Phase 2: 2027</div><h4>Rural Healthcare Plans</h4><p class="text-muted">Extending access points to semi-urban and rural districts.</p></div>
                    <div class="timeline-item reveal"><div class="timeline-date">Phase 3: 2028+</div><h4>AI Healthcare Future</h4><p class="text-muted">Full autonomous operational deployment.</p></div>
                </div>
            </div>
        </div>
    </section>
"""

partner_body = """
    <section class="hero" style="min-height: 60vh; padding: 150px 0 80px; background: linear-gradient(rgba(17,17,17,0.8), rgba(17,17,17,0.9)), url('https://images.unsplash.com/photo-1538108149393-cebb47cdf504?auto=format&fit=crop&q=80&w=1600') center/cover; color: white;">
        <div class="container text-center reveal">
            <span class="hero-label">Partnerships & Growth</span>
            <h1 class="text-white mb-4">Partner With Xpedicr to Transform Healthcare Together</h1>
            <p class="mx-auto" style="color: #A1A1AA; max-width: 700px; font-size: 18px;">Join a growing healthcare ecosystem connecting healthcare providers, technology, and infrastructure across India.</p>
        </div>
    </section>
    
    <section class="section-padding bg-light">
        <div class="container reveal">
            <h2 class="text-center mb-5">Who Can Partner</h2>
            <div class="grid-4 text-center">
                <div class="card"><h4>Pharmacies</h4></div>
                <div class="card"><h4>Labs</h4></div>
                <div class="card"><h4>Doctors</h4></div>
                <div class="card"><h4>Hospitals</h4></div>
                <div class="card"><h4>Clinics</h4></div>
                <div class="card"><h4>Wellness Brands</h4></div>
                <div class="card"><h4>Medical Suppliers</h4></div>
                <div class="card"><h4>Healthcare Distributors</h4></div>
            </div>
        </div>
    </section>

    <section class="section-padding">
        <div class="container reveal">
            <div class="grid-2 align-center">
                <div>
                    <h2 class="mb-4">Submit Partnership Request</h2>
                    <p class="text-muted mb-4">Fill out the form to initiate the technical and operational evaluation process.</p>
                </div>
                <div class="card" style="padding: 40px;">
                    <form>
                        <div class="grid-2" style="gap: 20px;">
                            <div class="form-group mb-0"><label class="form-label">Full Name</label><input type="text" class="form-control"></div>
                            <div class="form-group mb-0"><label class="form-label">Company Name</label><input type="text" class="form-control"></div>
                            <div class="form-group mb-0"><label class="form-label">Email</label><input type="email" class="form-control"></div>
                            <div class="form-group mb-0"><label class="form-label">Phone</label><input type="tel" class="form-control"></div>
                            <div class="form-group mb-0"><label class="form-label">Business Category</label>
                                <select class="form-control">
                                    <option>Pharmacy</option><option>Diagnostic Lab</option><option>Hospital</option><option>Other</option>
                                </select>
                            </div>
                            <div class="form-group mb-0"><label class="form-label">License / GST Number</label><input type="text" class="form-control"></div>
                        </div>
                        <div class="form-group mt-4">
                            <label class="form-label">Upload Documents (PDF, DOCX)</label>
                            <input type="file" class="form-control" accept=".pdf,.doc,.docx">
                        </div>
                        <button class="btn btn-primary mt-4 w-100" style="width: 100%;">Submit Partnership Request</button>
                    </form>
                </div>
            </div>
        </div>
    </section>
"""

careers_body = """
    <div class="inner-hero">
        <div class="container">
            <h1 class="reveal">Careers</h1>
            <p class="reveal">Join the team building India's digital healthcare backbone.</p>
        </div>
    </div>
    <section class="section-padding">
        <div class="container reveal">
            <div class="text-center mb-5">
                <h2>Open Roles</h2>
                <p class="text-muted mt-2">Explore opportunities to make a real-world impact.</p>
            </div>
            
            <div style="max-width: 800px; margin: 0 auto;">
                <div class="card mb-4" style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 20px;">
                    <div>
                        <h3 class="mb-2">Senior Full Stack Engineer</h3>
                        <p class="text-muted mb-0"><i class="fa-solid fa-location-dot me-2"></i> Bengaluru, India (Hybrid) • Engineering</p>
                    </div>
                    <button class="btn btn-outline">Apply Now</button>
                </div>
                
                <div class="card mb-4" style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 20px;">
                    <div>
                        <h3 class="mb-2">Healthcare Operations Manager</h3>
                        <p class="text-muted mb-0"><i class="fa-solid fa-location-dot me-2"></i> Mumbai, India • Operations</p>
                    </div>
                    <button class="btn btn-outline">Apply Now</button>
                </div>
            </div>
        </div>
    </section>
"""

contact_body = """
    <div class="inner-hero">
        <div class="container">
            <h1 class="reveal">Contact Us</h1>
            <p class="reveal">Get in touch with our support, sales, and partnership teams.</p>
        </div>
    </div>
    <section class="section-padding">
        <div class="container reveal">
            <div class="grid-2">
                <div>
                    <h2 class="mb-4">Contact Information</h2>
                    <div class="card mb-4">
                        <div style="display: flex; gap: 16px; margin-bottom: 24px;">
                            <i class="fa-solid fa-location-dot text-accent" style="font-size: 24px;"></i>
                            <div><h4>Headquarters</h4><p class="text-muted">Tech Park, Electronic City, Bengaluru, India</p></div>
                        </div>
                        <div style="display: flex; gap: 16px; margin-bottom: 24px;">
                            <i class="fa-solid fa-envelope text-accent" style="font-size: 24px;"></i>
                            <div><h4>Email</h4><p class="text-muted">support@xpedicr.in</p></div>
                        </div>
                        <div style="display: flex; gap: 16px; margin-bottom: 24px;">
                            <i class="fa-solid fa-phone text-accent" style="font-size: 24px;"></i>
                            <div><h4>Phone</h4><p class="text-muted">+91 72898 90080</p></div>
                        </div>
                        <div style="display: flex; gap: 16px;">
                            <i class="fa-brands fa-whatsapp text-success" style="font-size: 24px;"></i>
                            <div><h4>WhatsApp</h4><a href="https://wa.me/917289890080" class="text-muted">Chat with Support</a></div>
                        </div>
                    </div>
                </div>
                
                <div class="card">
                    <h3 class="mb-4">Send a Message</h3>
                    <form>
                        <div class="form-group"><label class="form-label">Name</label><input type="text" class="form-control"></div>
                        <div class="form-group"><label class="form-label">Email</label><input type="email" class="form-control"></div>
                        <div class="form-group"><label class="form-label">Inquiry Type</label>
                            <select class="form-control"><option>General Inquiry</option><option>Business Inquiry</option><option>Career Inquiry</option></select>
                        </div>
                        <div class="form-group"><label class="form-label">Message</label><textarea class="form-control" rows="4"></textarea></div>
                        <button class="btn btn-primary w-100" style="width: 100%;">Submit Message</button>
                    </form>
                </div>
            </div>
        </div>
    </section>
"""

pages = {
    "nava-ai.html": {"title": "Nava.ai | Xpedicr", "desc": "Future healthcare intelligence platform.", "body": nava_body, "active": "active_nava"},
    "future-partners.html": {"title": "Future & Partners | Xpedicr", "desc": "Our expansion vision.", "body": future_body, "active": "active_future"},
    "partner-with-us.html": {"title": "Partner With Us | Xpedicr", "desc": "Join our ecosystem.", "body": partner_body, "active": "active_contact"}, # active_contact because CTA is isolated, or none
    "careers.html": {"title": "Careers | Xpedicr", "desc": "Join the team.", "body": careers_body, "active": "active_careers"},
    "contact.html": {"title": "Contact Us | Xpedicr", "desc": "Get in touch.", "body": contact_body, "active": "active_contact"}
}

for filename, data in pages.items():
    page_content = header_template.format(
        title=data["title"], 
        desc=data["desc"],
        active_home="active" if data["active"] == "active_home" else "",
        active_about="active" if data["active"] == "active_about" else "",
        active_ecosystem="active" if data["active"] == "active_ecosystem" else "",
        active_nava="active" if data["active"] == "active_nava" else "",
        active_future="active" if data["active"] == "active_future" else "",
        active_careers="active" if data["active"] == "active_careers" else "",
        active_contact="active" if data["active"] == "active_contact" else ""
    ) + data["body"] + footer_template
    
    with open(os.path.join(base_dir, filename), "w", encoding="utf-8") as f:
        f.write(page_content)

print("Generated HTML part 2.")
