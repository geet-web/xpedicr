import os
import glob
import shutil
import re

base_dir = r"c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\xpedicr"

# 1. Update Read More links everywhere
html_files = glob.glob(os.path.join(base_dir, "*.html"))
for file_path in html_files:
    if "news-article.html" in file_path: continue
    if "brochure.html" in file_path: continue
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    content = content.replace('<a href="#" class="news-link">Read More', '<a href="news-article.html" class="news-link">Read More')
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

# 2. Create news-article.html by copying careers-news.html and replacing its body
careers_file = os.path.join(base_dir, "careers-news.html")
news_article_file = os.path.join(base_dir, "news-article.html")

shutil.copy(careers_file, news_article_file)

with open(news_article_file, "r", encoding="utf-8") as f:
    content = f.read()

new_body = """
    <!-- Inner Hero -->
    <div class="inner-hero" style="background: linear-gradient(rgba(5, 28, 51, 0.8), rgba(5, 28, 51, 0.9)), url('https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?auto=format&fit=crop&q=80&w=1920') no-repeat center center; background-size: cover; padding: 120px 0 80px 0;">
        <div class="container fade-in-up text-center">
            <span class="badge mb-3 px-3 py-2" style="background-color: var(--secondary); color: white; border-radius: 50px; font-weight: 600; letter-spacing: 1px;">PRESS RELEASE</span>
            <h1 class="mb-3" style="max-width: 900px; margin: 0 auto; font-size: 3rem; line-height: 1.2;">Xpedicr Secures Series C Funding to Expand Emergency Infrastructure</h1>
            <p style="font-size: 1.1rem; color: #cbd5e1; margin-top: 20px;">Published: September 15, 2026 &nbsp;|&nbsp; Media Contact: press@xpedicr.in</p>
        </div>
    </div>

    <!-- Article Content -->
    <section class="section-padding bg-white">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-lg-8 scroll-reveal up">
                    <p class="lead text-dark mb-4" style="font-size: 1.3rem; font-weight: 600; line-height: 1.8;">BENGALURU, INDIA &mdash; Xpedicr Industry Pvt. Ltd., the parent organization behind Nidhaan and Nava.ai, announced today that it has successfully closed its Series C funding round, securing $45 million to accelerate its nationwide healthcare infrastructure rollout.</p>
                    
                    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--gray); margin-bottom: 25px;">The round was led by Global Health Ventures with participation from existing investors, solidifying Xpedicr's position as a dominant force in India's rapidly evolving HealthTech sector.</p>
                    
                    <h3 class="mt-5 mb-3" style="color: var(--primary); font-family: var(--font-heading);">Accelerating the 10-Minute Emergency Guarantee</h3>
                    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--gray); margin-bottom: 25px;">With this new infusion of capital, Xpedicr plans to drastically scale its flagship "Nidhaan" emergency response network. Currently operating in 15 major metropolitan areas, the company aims to expand its rapid ambulance deployment and AI-routing systems to over 50 Tier-2 and Tier-3 cities by the end of 2027.</p>
                    
                    <div class="bg-light p-4 rounded my-5" style="border-left: 5px solid var(--secondary); box-shadow: 0 5px 15px rgba(0,0,0,0.05);">
                        <h4 class="mb-3" style="color: var(--primary);"><i class="fa-solid fa-quote-left me-2" style="color: var(--secondary);"></i> A Note from Leadership</h4>
                        <p class="mb-0 text-dark" style="font-style: italic; font-size: 1.1rem; line-height: 1.7;">"This funding is not just a financial milestone; it is a validation of our core belief that rapid, technology-driven healthcare is a fundamental right. We are now equipped to push the boundaries of what is possible in emergency medical logistics."</p>
                    </div>
                    
                    <h3 class="mt-5 mb-3" style="color: var(--primary); font-family: var(--font-heading);">Expanding Nava.ai Capabilities</h3>
                    <p style="font-size: 1.1rem; line-height: 1.8; color: var(--gray); margin-bottom: 25px;">In addition to physical infrastructure, a significant portion of the funding will be allocated to R&D for Nava.ai, Xpedicr's deep-learning diagnostic platform. Future updates will focus on integrating real-time wearable data streams with hospital triage software, allowing doctors to begin diagnostic procedures before the patient even arrives at the facility.</p>
                    
                    <hr style="border-color: rgba(0,0,0,0.1); margin: 50px 0;">
                    
                    <h4 style="color: var(--primary); font-family: var(--font-heading);">About Xpedicr</h4>
                    <p style="font-size: 0.95rem; line-height: 1.6; color: var(--gray);">Xpedicr Industry Pvt. Ltd. is a premier HealthTech conglomerate building India's future healthcare infrastructure through technology, partnerships, logistics, and innovation. The ecosystem includes Nidhaan (10-minute emergency services), Nava.ai (deep-learning diagnostics), and Viora (high-end wellness).</p>
                    
                    <div class="mt-5">
                        <a href="careers-news.html" class="btn btn-outline-primary btn-lg"><i class="fa-solid fa-arrow-left me-2"></i> Back to News Hub</a>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

content = re.sub(r'<!-- Inner Hero -->.*<!-- Footer -->', new_body + '\n<!-- Footer -->', content, flags=re.DOTALL)

with open(news_article_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Created news-article.html and updated Read More links globally.")
