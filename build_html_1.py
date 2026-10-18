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

index_body = """
    <section class="hero">
        <div class="container">
            <div class="hero-split">
                <div class="hero-content reveal">
                    <span class="hero-label">Healthcare Infrastructure & Technology</span>
                    <h1>Building India’s Future Healthcare Infrastructure Through Technology</h1>
                    <p>Xpedicr Industry Pvt. Ltd. is building a connected healthcare ecosystem integrating services, technology, partnerships, and accessibility into one scalable platform.</p>
                    <div class="hero-buttons">
                        <a href="ecosystem-services.html" class="btn btn-primary" style="margin-right: 16px;">Explore Ecosystem</a>
                        <a href="partner-with-us.html" class="btn btn-outline">Partner With Us</a>
                    </div>
                </div>
                <div class="hero-image reveal">
                    <img src="https://images.unsplash.com/photo-1538108149393-cebb47cdf504?auto=format&fit=crop&q=80&w=800" alt="Healthcare Technology" class="hero-img">
                </div>
            </div>
        </div>
    </section>

    <div class="trust-bar reveal">
        <div class="container">
            <div class="trust-grid">
                <div class="trust-item"><i class="fa-solid fa-microchip"></i> Healthcare Technology</div>
                <div class="trust-item"><i class="fa-solid fa-handshake"></i> Strategic Partnerships</div>
                <div class="trust-item"><i class="fa-solid fa-laptop-medical"></i> Digital Healthcare</div>
                <div class="trust-item"><i class="fa-solid fa-network-wired"></i> Future-Ready Infrastructure</div>
            </div>
        </div>
    </div>

    <section class="section-padding bg-light">
        <div class="container">
            <div class="grid-2 align-center">
                <div class="reveal">
                    <img src="https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&q=80&w=800" alt="About Xpedicr" style="border-radius: 8px; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
                </div>
                <div class="reveal">
                    <h2 class="mb-3">Unifying Healthcare Access Across India</h2>
                    <p class="mb-4 text-muted">Xpedicr Industry Pvt. Ltd. operates at the intersection of healthcare and technology. We build scalable infrastructure that connects fragmented medical services—bringing diagnostics, telemedicine, and emergency support into one unified ecosystem.</p>
                    <p class="mb-4 text-muted">Our approach combines deep operational healthcare experience with modern SaaS infrastructure to empower providers and patients alike.</p>
                    <a href="about.html" class="btn btn-primary">Learn More About Us</a>
                </div>
            </div>
        </div>
    </section>

    <section class="section-padding">
        <div class="container">
            <div class="grid-2 align-center reveal">
                <div>
                    <h2 class="mb-4">"Technology is the bridge that turns fragmented healthcare into accessible infrastructure."</h2>
                    <h4 class="mb-1">Dr. Founder Name</h4>
                    <p class="text-muted">Founder & CEO, Xpedicr Industry Pvt. Ltd.</p>
                </div>
                <div>
                    <img src="https://images.unsplash.com/photo-1559839734-2b71ea197ec2?auto=format&fit=crop&q=80&w=600" alt="Founder" style="border-radius: 8px; max-width: 400px; margin: 0 auto; filter: grayscale(100%);">
                </div>
            </div>
        </div>
    </section>

    <section class="section-padding bg-light">
        <div class="container">
            <div class="text-center mb-5 reveal">
                <h2>Our Ecosystem</h2>
                <p class="text-muted mt-2">Comprehensive platforms driving the future of healthcare.</p>
            </div>
            <div class="grid-2">
                <div class="card reveal">
                    <div class="card-icon"><i class="fa-solid fa-kit-medical"></i></div>
                    <h3 class="mb-3">Nidhaan</h3>
                    <p class="text-muted mb-4">Our primary healthcare access platform connecting patients to essential services.</p>
                    <ul style="list-style: none; color: var(--text-muted);">
                        <li class="mb-2"><i class="fa-solid fa-check" style="color: var(--accent); margin-right: 8px;"></i> Medicine Delivery</li>
                        <li class="mb-2"><i class="fa-solid fa-check" style="color: var(--accent); margin-right: 8px;"></i> Diagnostics</li>
                        <li class="mb-2"><i class="fa-solid fa-check" style="color: var(--accent); margin-right: 8px;"></i> Telemedicine</li>
                        <li class="mb-2"><i class="fa-solid fa-check" style="color: var(--accent); margin-right: 8px;"></i> Doctor Consultations</li>
                        <li><i class="fa-solid fa-check" style="color: var(--accent); margin-right: 8px;"></i> Ambulance Support</li>
                    </ul>
                </div>
                <div class="card reveal">
                    <div class="card-icon"><i class="fa-solid fa-brain"></i></div>
                    <h3 class="mb-3">Nava.ai</h3>
                    <p class="text-muted mb-4">Our proprietary AI healthcare intelligence platform streamlining medical operations.</p>
                    <ul style="list-style: none; color: var(--text-muted);">
                        <li class="mb-2"><i class="fa-solid fa-check" style="color: var(--accent); margin-right: 8px;"></i> Predictive Systems</li>
                        <li class="mb-2"><i class="fa-solid fa-check" style="color: var(--accent); margin-right: 8px;"></i> AI Patient Support</li>
                        <li><i class="fa-solid fa-check" style="color: var(--accent); margin-right: 8px;"></i> Smart Healthcare Automation</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <section class="section-padding">
        <div class="container">
            <div class="text-center mb-5 reveal">
                <h2>Core Services</h2>
                <p class="text-muted mt-2">The operational pillars of the Xpedicr infrastructure.</p>
            </div>
            <div class="grid-3">
                <div class="card reveal"><div class="card-icon"><i class="fa-solid fa-pills"></i></div><h4>Medicine Delivery</h4><p class="text-muted mt-2">End-to-end pharmacy fulfillment.</p></div>
                <div class="card reveal"><div class="card-icon"><i class="fa-solid fa-video"></i></div><h4>Telemedicine</h4><p class="text-muted mt-2">Remote clinical consultations.</p></div>
                <div class="card reveal"><div class="card-icon"><i class="fa-solid fa-vial-virus"></i></div><h4>Diagnostics</h4><p class="text-muted mt-2">Integrated lab testing network.</p></div>
                <div class="card reveal"><div class="card-icon"><i class="fa-solid fa-truck-medical"></i></div><h4>Ambulance Booking</h4><p class="text-muted mt-2">Rapid emergency response.</p></div>
                <div class="card reveal"><div class="card-icon"><i class="fa-solid fa-heart-circle-check"></i></div><h4>Wellness Support</h4><p class="text-muted mt-2">Preventative health programs.</p></div>
                <div class="card reveal"><div class="card-icon"><i class="fa-solid fa-user-doctor"></i></div><h4>Doctor Consultation</h4><p class="text-muted mt-2">Access to top specialists.</p></div>
            </div>
        </div>
    </section>

    <section class="section-padding bg-light">
        <div class="container">
            <div class="text-center mb-5 reveal">
                <h2>Future Roadmap</h2>
                <p class="text-muted mt-2">Our strategic vision for the next phase of growth.</p>
            </div>
            <div style="max-width: 800px; margin: 0 auto;">
                <div class="timeline">
                    <div class="timeline-item reveal"><div class="timeline-date">2026</div><h4>Platform Expansion</h4><p class="text-muted">Scaling the Nidhaan core infrastructure across urban centers.</p></div>
                    <div class="timeline-item reveal"><div class="timeline-date">2027</div><h4>Ambulance Aggregation</h4><p class="text-muted">Unifying fragmented emergency response fleets digitally.</p></div>
                    <div class="timeline-item reveal"><div class="timeline-date">2028</div><h4>Rural Healthcare Access</h4><p class="text-muted">Deploying technology nodes to under-served regions.</p></div>
                    <div class="timeline-item reveal"><div class="timeline-date">2029</div><h4>AI Healthcare Systems</h4><p class="text-muted">Full integration of Nava.ai predictive analytics.</p></div>
                </div>
            </div>
        </div>
    </section>

    <section class="section-padding">
        <div class="container">
            <div class="text-center mb-5 reveal">
                <h2>News & Updates</h2>
            </div>
            <div class="grid-3">
                <div class="card reveal" style="padding: 0; overflow: hidden;">
                    <img src="https://images.unsplash.com/photo-1551076805-e1869033e561?auto=format&fit=crop&q=80&w=600" alt="News" style="height: 200px; object-fit: cover;">
                    <div style="padding: 24px;">
                        <span class="text-muted" style="font-size: 13px;">Announcements</span>
                        <h4 class="mt-2 mb-3">Xpedicr Announces Strategic Hospital Partnerships</h4>
                        <a href="#">Read More &rarr;</a>
                    </div>
                </div>
                <div class="card reveal" style="padding: 0; overflow: hidden;">
                    <img src="https://images.unsplash.com/photo-1516549655169-df83a0774514?auto=format&fit=crop&q=80&w=600" alt="News" style="height: 200px; object-fit: cover;">
                    <div style="padding: 24px;">
                        <span class="text-muted" style="font-size: 13px;">Launches</span>
                        <h4 class="mt-2 mb-3">Nava.ai Pilot Phase Initiated for Diagnostics</h4>
                        <a href="#">Read More &rarr;</a>
                    </div>
                </div>
                <div class="card reveal" style="padding: 0; overflow: hidden;">
                    <img src="https://images.unsplash.com/photo-1505751172876-fa1923c5c528?auto=format&fit=crop&q=80&w=600" alt="News" style="height: 200px; object-fit: cover;">
                    <div style="padding: 24px;">
                        <span class="text-muted" style="font-size: 13px;">Company Updates</span>
                        <h4 class="mt-2 mb-3">Expanding our Digital Telemedicine Reach</h4>
                        <a href="#">Read More &rarr;</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="section-padding bg-light text-center">
        <div class="container reveal">
            <h2 class="mb-4">Let’s Build the Future of Healthcare Together</h2>
            <p class="text-muted mb-4 mx-auto" style="max-width: 600px;">Join our mission to create a sustainable, technology-driven healthcare ecosystem that serves everyone.</p>
            <div>
                <a href="contact.html" class="btn btn-primary" style="margin-right: 16px;">Contact Us</a>
                <a href="partner-with-us.html" class="btn btn-outline">Become a Partner</a>
            </div>
        </div>
    </section>
"""

about_body = """
    <div class="inner-hero">
        <div class="container">
            <h1 class="reveal">About Xpedicr</h1>
            <p class="reveal">Understanding our mission, vision, and the core values that drive our ecosystem.</p>
        </div>
    </div>
    <section class="section-padding">
        <div class="container">
            <div class="grid-2 align-center mb-5 reveal">
                <div>
                    <h2 class="mb-4">Company Story</h2>
                    <p class="text-muted mb-3">Xpedicr Industry Pvt. Ltd. was founded with a singular focus: to modernize the fragmented Indian healthcare infrastructure. We recognized that while world-class medical talent exists, the connecting infrastructure—the access layers—are broken.</p>
                    <p class="text-muted">By leveraging scalable technology, we are bridging the gap between healthcare providers, diagnostic centers, pharmacies, and the patients who rely on them.</p>
                </div>
                <div><img src="https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?auto=format&fit=crop&q=80&w=800" alt="Company Story" style="border-radius: 8px;"></div>
            </div>
            
            <div class="grid-2 align-center mt-5 reveal">
                <div><img src="https://images.unsplash.com/photo-1550831107-1553da8c8464?auto=format&fit=crop&q=80&w=800" alt="Challenges" style="border-radius: 8px;"></div>
                <div>
                    <h2 class="mb-4">Healthcare Challenges We Solve</h2>
                    <ul style="list-style: none; color: var(--text-muted);">
                        <li class="mb-3"><strong style="color: var(--black);">Fragmented Data:</strong> Unifying patient records across disparate systems.</li>
                        <li class="mb-3"><strong style="color: var(--black);">Access Inequity:</strong> Bringing premium healthcare services to tier-2 and tier-3 locations.</li>
                        <li class="mb-3"><strong style="color: var(--black);">Emergency Response:</strong> Streamlining ambulance and urgent care coordination.</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>
    
    <section class="section-padding bg-light">
        <div class="container text-center reveal">
            <h2 class="mb-5">Our Core Values</h2>
            <div class="grid-4">
                <div class="card"><div class="card-icon"><i class="fa-solid fa-users"></i></div><h4>Accessibility</h4></div>
                <div class="card"><div class="card-icon"><i class="fa-solid fa-lightbulb"></i></div><h4>Innovation</h4></div>
                <div class="card"><div class="card-icon"><i class="fa-solid fa-shield-halved"></i></div><h4>Trust</h4></div>
                <div class="card"><div class="card-icon"><i class="fa-solid fa-chart-line"></i></div><h4>Scalability</h4></div>
            </div>
        </div>
    </section>
"""

ecosystem_body = """
    <div class="inner-hero">
        <div class="container">
            <h1 class="reveal">Ecosystem & Services</h1>
            <p class="reveal">A unified architecture for holistic healthcare management.</p>
        </div>
    </div>
    <section class="section-padding">
        <div class="container reveal">
            <h2 class="text-center mb-5">Healthcare Ecosystem Overview</h2>
            <div class="grid-2 mb-5">
                <div class="card">
                    <h3 class="mb-3"><i class="fa-solid fa-kit-medical text-accent me-2"></i> Nidhaan Platform</h3>
                    <p class="text-muted">The operational backbone handling consumer-facing services, provider coordination, and logistical fulfillment.</p>
                </div>
                <div class="card">
                    <h3 class="mb-3"><i class="fa-solid fa-brain text-accent me-2"></i> Nava.ai Integration</h3>
                    <p class="text-muted">The intelligence layer providing predictive analytics, workflow automation, and smart clinical support.</p>
                </div>
            </div>
            
            <h2 class="text-center mb-5 mt-5">Service Workflow</h2>
            <div class="grid-4 text-center">
                <div class="card"><div class="card-icon"><i class="fa-solid fa-mobile-screen"></i></div><h4>1. Digital Request</h4><p class="text-muted mt-2 text-sm">Patient initiates request via platform.</p></div>
                <div class="card"><div class="card-icon"><i class="fa-solid fa-network-wired"></i></div><h4>2. Smart Routing</h4><p class="text-muted mt-2 text-sm">Nava.ai routes to optimal provider.</p></div>
                <div class="card"><div class="card-icon"><i class="fa-solid fa-user-doctor"></i></div><h4>3. Fulfillment</h4><p class="text-muted mt-2 text-sm">Service delivered by trusted partner.</p></div>
                <div class="card"><div class="card-icon"><i class="fa-solid fa-laptop-medical"></i></div><h4>4. Data Sync</h4><p class="text-muted mt-2 text-sm">Records unified securely.</p></div>
            </div>
        </div>
    </section>
"""

pages = {
    "index.html": {"title": "Xpedicr | Premium HealthTech Ecosystem", "desc": "Building India's future healthcare infrastructure through technology.", "body": index_body, "active": "active_home"},
    "about.html": {"title": "About Us | Xpedicr", "desc": "Learn about the mission and vision of Xpedicr Industry Pvt. Ltd.", "body": about_body, "active": "active_about"},
    "ecosystem-services.html": {"title": "Ecosystem & Services | Xpedicr", "desc": "Explore our connected healthcare platforms and services.", "body": ecosystem_body, "active": "active_ecosystem"}
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

print("Generated HTML part 1.")
