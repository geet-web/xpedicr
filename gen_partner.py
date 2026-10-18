html = open("about.html","r",encoding="utf-8").read()

# Extract navbar block (lines up to mobile menu end) and footer+scripts block
nav_end = html.index("<!-- Inner Hero -->")
footer_start = html.index("<!-- Footer -->")

navbar_block = html[:nav_end]
# Fix active link
navbar_block = navbar_block.replace('href="about.html" class="active"','href="about.html"')
navbar_block = navbar_block.replace('href="contact.html" class="btn btn-outline-primary">Partner With Us','href="partner-with-us.html" class="btn btn-outline-primary active">Partner With Us')

footer_block = html[footer_start:]

body = """
    <!-- Inner Hero -->
    <div class="inner-hero partner-hero" style="background:linear-gradient(rgba(0,0,0,0.75),rgba(17,17,17,0.9)),url('https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&q=80&w=1920') center/cover no-repeat;padding:160px 0 100px;">
        <div class="container" style="position:relative;z-index:1;">
            <p style="color:rgba(255,255,255,0.5);font-size:.85rem;margin-bottom:1rem;"><a href="index.html" style="color:rgba(255,255,255,0.5);text-decoration:none;">Home</a> / Partner With Us</p>
            <span class="badge fade-in-up" style="background:rgba(255,255,255,0.1);color:#fff;border:1px solid rgba(255,255,255,0.2);">Partnerships &amp; Growth</span>
            <h1 class="fade-in-up delay-1" style="color:#fff;font-size:clamp(2rem,4vw,3.5rem);max-width:800px;margin:24px 0;">Partner With Xpedicr to <span style="opacity:.7;">Transform Healthcare</span> Together</h1>
            <p class="fade-in-up delay-2" style="color:rgba(255,255,255,0.7);font-size:1.15rem;max-width:620px;line-height:1.7;margin-bottom:2rem;">Join a growing healthcare ecosystem connecting providers, services, and technology to create faster, smarter, and more accessible healthcare across India.</p>
            <a href="#partner-form" class="btn btn-primary btn-lg fade-in-up delay-3">Become a Partner <i class="fa-solid fa-arrow-right ms-2"></i></a>
        </div>
    </div>

    <!-- 2. Introduction -->
    <section class="section-padding bg-white">
        <div class="container">
            <div class="row align-items-center g-5">
                <div class="col-lg-6 scroll-reveal left">
                    <span class="subtitle">About the Initiative</span>
                    <h2 style="font-size:2.5rem;margin:16px 0 24px;">Building a Stronger Healthcare Ecosystem</h2>
                    <p style="font-size:1.1rem;line-height:1.8;color:#555;margin-bottom:1.2rem;">Xpedicr Industry Pvt. Ltd. is developing a unified healthcare platform that connects service providers, businesses, and infrastructure into one seamless network.</p>
                    <p style="font-size:1.1rem;line-height:1.8;color:#555;">Our goal is to simplify healthcare access, improve service delivery, and create scalable growth opportunities for every partner involved — from independent clinics to large hospital chains.</p>
                </div>
                <div class="col-lg-6 scroll-reveal right">
                    <img src="https://images.unsplash.com/photo-1631217868264-e5b90bb7e133?auto=format&fit=crop&q=80&w=800" alt="Healthcare Partnership" style="width:100%;border-radius:16px;box-shadow:0 20px 50px rgba(0,0,0,0.12);">
                </div>
            </div>
        </div>
    </section>

    <!-- 3. Ecosystem Overview -->
    <section class="section-padding" style="background:#f9fafb;">
        <div class="container">
            <div class="section-title text-center scroll-reveal up" style="margin-bottom:60px;">
                <span class="subtitle">Our Network</span>
                <h2>We Connect the Entire Healthcare Chain</h2>
                <p class="section-desc">Every stakeholder in healthcare — under one intelligent platform.</p>
            </div>
            <div class="row g-4" style="justify-content:center;">
                ''' + "".join([f'''
                <div class="col-6 col-md-4 col-lg-3 scroll-reveal up">
                    <div class="feature-card text-center" style="padding:28px 20px;">
                        <div class="feature-icon" style="font-size:2rem;margin-bottom:12px;"><i class="{ic}"></i></div>
                        <h5 style="font-weight:600;font-size:.95rem;margin:0;">{name}</h5>
                    </div>
                </div>''' for ic,name in [
                    ("fa-solid fa-hospital","Hospitals &amp; Clinics"),
                    ("fa-solid fa-stethoscope","Doctors &amp; Specialists"),
                    ("fa-solid fa-pills","Pharmacies"),
                    ("fa-solid fa-flask","Diagnostic Labs"),
                    ("fa-solid fa-shield-halved","Insurance Providers"),
                    ("fa-solid fa-truck-medical","Emergency Services"),
                    ("fa-solid fa-spa","Wellness Brands"),
                    ("fa-solid fa-box","Medical Suppliers"),
                    ("fa-solid fa-network-wired","Healthcare Distributors"),
                ]]) + '''
            </div>
        </div>
    </section>

    <!-- 4. Why Partner -->
    <section class="section-padding bg-white">
        <div class="container">
            <div class="section-title text-center scroll-reveal up" style="margin-bottom:60px;">
                <span class="subtitle">Why Choose Us</span>
                <h2>Why Partner With Xpedicr</h2>
            </div>
            <div class="features-grid">
                ''' + "".join([f'''
                <div class="feature-card scroll-reveal up">
                    <div class="feature-icon"><i class="{ic}"></i></div>
                    <h4>{title}</h4>
                    <p>{desc}</p>
                </div>''' for ic,title,desc in [
                    ("fa-solid fa-globe","Expand Your Reach","Access patients and partners across 50+ cities and growing pan-India network."),
                    ("fa-solid fa-users","Increase Patient Access","Connect with thousands of patients seeking quality, verified healthcare services."),
                    ("fa-solid fa-microchip","Technology Operations","Leverage AI-driven tools, dashboards and integrations that streamline daily operations."),
                    ("fa-solid fa-bolt","Faster Integration","Go live quickly with our dedicated onboarding team and pre-built integration stack."),
                    ("fa-solid fa-star","Brand Credibility","Be listed under a trusted, growing healthcare brand recognized across India."),
                    ("fa-solid fa-chart-line","Scalable Growth","Grow at your own pace with tiered partnership models built for long-term success."),
                ]]) + '''
            </div>
        </div>
    </section>

    <!-- 5. Benefits -->
    <section class="section-padding" style="background:#111;color:#fff;">
        <div class="container">
            <div class="section-title text-center scroll-reveal up" style="margin-bottom:60px;">
                <span class="subtitle" style="color:rgba(255,255,255,0.5);">What You Gain</span>
                <h2 style="color:#fff;">Partnership Benefits</h2>
            </div>
            <div class="row g-4">
                ''' + "".join([f'''
                <div class="col-md-6 col-lg-4 scroll-reveal up">
                    <div style="padding:32px;background:rgba(255,255,255,0.05);border:1px solid rgba(255,255,255,0.1);border-radius:16px;height:100%;">
                        <div style="width:48px;height:48px;background:rgba(255,255,255,0.1);border-radius:12px;display:flex;align-items:center;justify-content:center;margin-bottom:20px;font-size:1.4rem;"><i class="{ic}" style="color:#fff;"></i></div>
                        <h4 style="color:#fff;margin-bottom:12px;">{title}</h4>
                        <p style="color:rgba(255,255,255,0.6);margin:0;line-height:1.7;">{desc}</p>
                    </div>
                </div>''' for ic,title,desc in [
                    ("fa-solid fa-chart-network","Rapidly Growing Network","Tap into a network that is actively expanding to new cities and healthcare categories every quarter."),
                    ("fa-solid fa-eye","Increased Visibility","Your business gets listed and promoted across the Xpedicr platform and partner channels."),
                    ("fa-solid fa-gears","Streamlined Operations","Technology tools that reduce admin burden, automate processes, and improve patient experience."),
                    ("fa-solid fa-seedling","Sustainable Growth","Build long-term recurring revenue streams through our tiered referral and collaboration models."),
                    ("fa-solid fa-lightbulb","Innovation Access","Be first to integrate with future healthcare innovations — AI diagnostics, telemedicine, logistics AI."),
                    ("fa-solid fa-handshake","Dedicated Support","A dedicated partner success manager guides your onboarding and ongoing collaboration journey."),
                ]]) + '''
            </div>
        </div>
    </section>

    <!-- 6. Who Can Partner -->
    <section class="section-padding" style="background:#f9fafb;">
        <div class="container">
            <div class="section-title text-center scroll-reveal up" style="margin-bottom:60px;">
                <span class="subtitle">Eligibility</span>
                <h2>Who Can Partner With Us</h2>
                <p class="section-desc">We welcome all serious healthcare businesses and professionals.</p>
            </div>
            <div class="row g-3" style="justify-content:center;">
                ''' + "".join([f'<div class="col-6 col-md-4 col-lg-3 scroll-reveal up"><div class="partner-badge" style="display:block;text-align:center;padding:18px 12px;background:#fff;border:1px solid #e5e7eb;border-radius:12px;font-weight:600;font-size:.9rem;color:#111;box-shadow:0 2px 8px rgba(0,0,0,0.05);">{n}</div></div>' for n in ["Pharmacies","Diagnostic Labs","Doctors","Hospitals","Clinics","Cosmetic Companies","Supplement Companies","Insurance Companies","Wellness Brands","Medical Device Suppliers","Healthcare Distributors","Emergency Service Providers"]]) + '''
            </div>
        </div>
    </section>

    <!-- 7. Form -->
    <section id="partner-form" class="section-padding bg-white">
        <div class="container">
            <div class="section-title text-center scroll-reveal up" style="margin-bottom:60px;">
                <span class="subtitle">Apply Now</span>
                <h2>Partnership Registration</h2>
                <p class="section-desc">Fill out the form below and our team will reach out within 48 hours.</p>
            </div>
            <div style="max-width:860px;margin:0 auto;background:#f9fafb;border:1px solid #e5e7eb;border-radius:20px;padding:48px 40px;" class="scroll-reveal up">
                <form id="partnerForm">
                    <h4 style="color:#111;border-bottom:2px solid #111;padding-bottom:12px;margin-bottom:28px;">Basic Information</h4>
                    <div class="row g-4 mb-4">
                        <div class="col-md-6"><label class="form-label">Full Name *</label><input class="form-control" type="text" placeholder="Your full name" required></div>
                        <div class="col-md-6"><label class="form-label">Company / Business Name *</label><input class="form-control" type="text" placeholder="Your business name" required></div>
                        <div class="col-md-6"><label class="form-label">Designation *</label><input class="form-control" type="text" placeholder="e.g. CEO, Director, Owner"></div>
                        <div class="col-md-6"><label class="form-label">Business Category *</label>
                            <select class="form-control" required>
                                <option value="">Select category</option>
                                <option>Pharmacy</option><option>Diagnostic Lab</option><option>Hospital</option>
                                <option>Clinic</option><option>Doctor / Specialist</option><option>Cosmetic / Wellness Brand</option>
                                <option>Insurance Provider</option><option>Medical Supplier</option><option>Healthcare Distributor</option>
                                <option>Emergency Services</option><option>Other</option>
                            </select>
                        </div>
                    </div>

                    <h4 style="color:#111;border-bottom:2px solid #111;padding-bottom:12px;margin:36px 0 28px;">Professional Details</h4>
                    <div class="row g-4 mb-4">
                        <div class="col-md-6"><label class="form-label">Specialization / Services Offered</label><input class="form-control" type="text" placeholder="e.g. Cardiology, General Medicine"></div>
                        <div class="col-md-6"><label class="form-label">Registration / License Number *</label><input class="form-control" type="text" placeholder="License number" required></div>
                        <div class="col-md-6"><label class="form-label">GST Number (optional)</label><input class="form-control" type="text" placeholder="GST number if applicable"></div>
                        <div class="col-md-3"><label class="form-label">Years in Business</label><input class="form-control" type="number" min="0" placeholder="e.g. 5"></div>
                        <div class="col-md-3"><label class="form-label">No. of Branches</label><input class="form-control" type="number" min="1" placeholder="e.g. 3"></div>
                        <div class="col-md-6"><label class="form-label">Monthly Business Volume (optional)</label><input class="form-control" type="text" placeholder="Approximate monthly volume"></div>
                    </div>

                    <h4 style="color:#111;border-bottom:2px solid #111;padding-bottom:12px;margin:36px 0 28px;">Contact Details</h4>
                    <div class="row g-4 mb-4">
                        <div class="col-md-6"><label class="form-label">Email Address *</label><input class="form-control" type="email" placeholder="your@email.com" required></div>
                        <div class="col-md-6"><label class="form-label">Mobile Number *</label><input class="form-control" type="tel" placeholder="+91 XXXXX XXXXX" required></div>
                        <div class="col-md-6"><label class="form-label">WhatsApp Number</label><input class="form-control" type="tel" placeholder="+91 XXXXX XXXXX"></div>
                        <div class="col-md-6"><label class="form-label">City / Location *</label><input class="form-control" type="text" placeholder="City, State" required></div>
                        <div class="col-md-12"><label class="form-label">Full Address</label><input class="form-control" type="text" placeholder="Full business address"></div>
                        <div class="col-md-12"><label class="form-label">Website / Social Media (optional)</label><input class="form-control" type="text" placeholder="https://"></div>
                    </div>

                    <h4 style="color:#111;border-bottom:2px solid #111;padding-bottom:12px;margin:36px 0 28px;">Partnership Requirements</h4>
                    <div class="row g-4 mb-4">
                        <div class="col-md-6"><label class="form-label">Partnership Type *</label>
                            <select class="form-control" required>
                                <option value="">Select type</option>
                                <option>Service Integration Partner</option><option>Referral Partner</option>
                                <option>Technology Partner</option><option>Supply Chain Partner</option>
                                <option>Co-branding Partner</option><option>Other</option>
                            </select>
                        </div>
                        <div class="col-md-6"><label class="form-label">Expected Collaboration Details</label><input class="form-control" type="text" placeholder="Brief expectation"></div>
                        <div class="col-md-12"><label class="form-label">Brief Company Profile</label><textarea class="form-control" rows="3" placeholder="Describe your business and services..."></textarea></div>
                        <div class="col-md-12"><label class="form-label">Additional Message</label><textarea class="form-control" rows="3" placeholder="Any additional notes or queries..."></textarea></div>
                    </div>

                    <h4 style="color:#111;border-bottom:2px solid #111;padding-bottom:12px;margin:36px 0 28px;">Upload Documents</h4>
                    <div class="row g-4 mb-4">
                        <div class="col-md-6"><label class="form-label">Company Profile / Brochure</label><input class="form-control" type="file" accept=".pdf,.doc,.docx"></div>
                        <div class="col-md-6"><label class="form-label">License Certificate *</label><input class="form-control" type="file" accept=".pdf,.jpg,.png" required></div>
                        <div class="col-md-6"><label class="form-label">GST Certificate (optional)</label><input class="form-control" type="file" accept=".pdf,.jpg,.png"></div>
                        <div class="col-md-6"><label class="form-label">Visiting Card</label><input class="form-control" type="file" accept=".pdf,.jpg,.png"></div>
                        <div class="col-md-6"><label class="form-label">Product Catalogue (optional)</label><input class="form-control" type="file" accept=".pdf"></div>
                    </div>

                    <div style="text-align:center;margin-top:40px;">
                        <button type="submit" class="btn btn-primary btn-lg" style="min-width:300px;padding:18px 40px;font-size:1.1rem;">Submit Partnership Request <i class="fa-solid fa-paper-plane ms-2"></i></button>
                    </div>
                </form>
            </div>
        </div>
    </section>

    <!-- 8. Trust Section -->
    <section class="section-padding" style="background:#f9fafb;">
        <div class="container">
            <div class="section-title text-center scroll-reveal up" style="margin-bottom:50px;">
                <span class="subtitle">Our Commitment</span>
                <h2>You Can Trust Xpedicr</h2>
            </div>
            <div class="row g-4 justify-content-center">
                ''' + "".join([f'''
                <div class="col-md-6 col-lg-3 scroll-reveal up">
                    <div class="text-center" style="padding:36px 24px;background:#fff;border-radius:16px;box-shadow:0 4px 20px rgba(0,0,0,0.06);">
                        <div style="width:64px;height:64px;background:#111;border-radius:16px;display:flex;align-items:center;justify-content:center;font-size:1.6rem;color:#fff;margin:0 auto 20px;"><i class="{ic}"></i></div>
                        <h5 style="font-weight:700;margin-bottom:10px;">{title}</h5>
                        <p style="color:#666;font-size:.9rem;margin:0;">{desc}</p>
                    </div>
                </div>''' for ic,title,desc in [
                    ("fa-solid fa-lock","Secure Data Handling","All data is encrypted and stored securely on ISO-compliant infrastructure."),
                    ("fa-solid fa-badge-check","Verified Partner Network","Every partner goes through a strict vetting and verification process."),
                    ("fa-solid fa-user-tie","Professional Onboarding","Dedicated team ensures smooth, fast onboarding with zero disruption to operations."),
                    ("fa-solid fa-headset","Fast Response Support","24/7 partner support ensures your queries are resolved within hours, not days."),
                ]]) + '''
            </div>
        </div>
    </section>

    <!-- 9. Final CTA -->
    <section class="section-padding" style="background:#111;color:#fff;text-align:center;">
        <div class="container scroll-reveal up">
            <h2 style="color:#fff;font-size:clamp(1.8rem,3.5vw,3rem);max-width:750px;margin:0 auto 20px;line-height:1.3;">Together with Xpedicr, Let's Build India's Future Healthcare Infrastructure</h2>
            <p style="color:rgba(255,255,255,0.6);font-size:1.1rem;max-width:560px;margin:0 auto 40px;">Join hundreds of healthcare professionals who are already part of the ecosystem.</p>
            <div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap;">
                <a href="#partner-form" class="btn btn-primary btn-lg">Submit Request</a>
                <a href="contact.html" class="btn btn-outline-primary btn-lg" style="border-color:rgba(255,255,255,0.4);color:#fff;">Contact Team</a>
            </div>
        </div>
    </section>
'''

page = navbar_block.replace('<title>Xpedicr Industry Pvt. Ltd. | Future Healthcare Infrastructure</title>',
    '<title>Partner With Us | Xpedicr Industry Pvt. Ltd.</title>')
page = page.replace('href="contact.html" class="btn btn-outline-primary active">Partner With Us',
    'href="partner-with-us.html" class="btn btn-outline-primary active">Partner With Us')

# Fix active nav
page = page.replace('href="about.html" class="active"', 'href="about.html"')

page += body + footer_block

# Add form label style
page = page.replace('</style>','') # no inline style block in about.html base
extra_style = (
    "<style>"
    ".form-label{display:block;font-weight:600;font-size:0.85rem;margin-bottom:6px;color:#333;}"
    ".form-control{width:100%;padding:12px 16px;border:1.5px solid #e5e7eb;border-radius:10px;font-family:inherit;font-size:0.95rem;background:#fff;color:#111;transition:border 0.2s;}"
    ".form-control:focus{outline:none;border-color:#111;box-shadow:0 0 0 3px rgba(0,0,0,0.08);}"
    "</style>"
)
page = page.replace('</head>', extra_style + '</head>')

open("partner-with-us.html","w",encoding="utf-8").write(page)
print("Done")
