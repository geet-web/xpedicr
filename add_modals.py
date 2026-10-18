import os
import glob

base_dir = r"c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\xpedicr"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

modal_html = """
    <!-- Privacy Policy Modal -->
    <div class="modal-overlay" id="privacyModal">
        <div class="modal-content">
            <div class="modal-header">
                <h3>Privacy Policy</h3>
                <button class="modal-close" data-close="privacyModal"><i class="fa-solid fa-xmark"></i></button>
            </div>
            <div class="modal-body">
                <p><strong>Effective Date:</strong> January 1, 2026</p>
                <p>At Xpedicr Industry Pvt. Ltd., we take your privacy seriously. This Privacy Policy explains how we collect, use, disclose, and safeguard your information when you visit our website or use our healthcare services.</p>
                <h4>1. Information We Collect</h4>
                <p>We may collect personal identification information, including but not limited to your name, email address, phone number, and medical history when you register for an account, book a service, or consult with our partners.</p>
                <h4>2. How We Use Your Information</h4>
                <p>Your data is primarily used to provide you with rapid emergency responses, accurate AI-assisted diagnostics via Nava.ai, and seamless telemedicine consultations. We also use aggregated data to improve our service logistics.</p>
                <h4>3. Data Security</h4>
                <p>We implement state-of-the-art encryption and robust secure server architecture to protect your personal health information. However, no electronic transmission over the internet can be guaranteed to be 100% secure.</p>
                <h4>4. Third-Party Sharing</h4>
                <p>We only share necessary information with verified partner clinics, hospitals, and pharmacies directly involved in your care. We do not sell your personal data to advertisers.</p>
            </div>
        </div>
    </div>

    <!-- Terms of Service Modal -->
    <div class="modal-overlay" id="termsModal">
        <div class="modal-content">
            <div class="modal-header">
                <h3>Terms of Service</h3>
                <button class="modal-close" data-close="termsModal"><i class="fa-solid fa-xmark"></i></button>
            </div>
            <div class="modal-body">
                <p><strong>Last Updated:</strong> January 1, 2026</p>
                <p>Welcome to Xpedicr. By accessing or using our platform, ecosystem subsidiaries (Nidhaan, Nava.ai), and services, you agree to be bound by these Terms of Service.</p>
                <h4>1. Acceptance of Terms</h4>
                <p>By registering for an account or utilizing our healthcare aggregator platform, you acknowledge that you have read, understood, and agree to comply with all rules and conditions stated herein.</p>
                <h4>2. Medical Disclaimer</h4>
                <p>While Nava.ai provides advanced AI-assisted insights and triage support, it does not replace professional medical advice, diagnosis, or treatment. Always seek the advice of your physician regarding a medical condition.</p>
                <h4>3. Service Availability</h4>
                <p>Our 10-minute emergency response times are subject to geographic location, traffic conditions, and partner availability. We continually strive to expand our high-speed network across Tier 1, 2, and 3 cities.</p>
                <h4>4. User Responsibilities</h4>
                <p>You agree to provide accurate and complete health information. Providing false information may lead to incorrect medical assistance, for which Xpedicr Industry Pvt. Ltd. cannot be held liable.</p>
            </div>
        </div>
    </div>

"""

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace links
    content = content.replace('<a href="#">Privacy Policy</a>', '<a href="#" class="modal-trigger" data-modal="privacyModal">Privacy Policy</a>')
    content = content.replace('<a href="#">Terms of Service</a>', '<a href="#" class="modal-trigger" data-modal="termsModal">Terms of Service</a>')
    
    # Inject modal HTML if not present
    if 'id="privacyModal"' not in content:
        if '<!-- Scripts -->' in content:
            content = content.replace('<!-- Scripts -->', modal_html + '    <!-- Scripts -->')
        else:
            content = content.replace('</body>', modal_html + '\n</body>')
            
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Modals added to all HTML files successfully.")
