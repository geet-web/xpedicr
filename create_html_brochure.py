import os
import glob

base_dir = r"c:\Users\This pc\.gemini\antigravity\playground\baryonic-shuttle\xpedicr"

brochure_html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Xpedicr - Corporate Brochure 2026</title>
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
    <!-- Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --primary: #0A3D6B; /* Deep Blue */
            --secondary: #00B47D; /* Emerald Green */
            --dark: #051C33;
            --white: #FFFFFF;
            --light: #F8F9FA;
            --gray: #6C757D;
        }
        body {
            background-color: #e9ecef;
            font-family: 'Inter', sans-serif;
            margin: 0;
            padding: 40px 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 40px;
        }
        .page {
            width: 21cm;
            height: 29.7cm; /* A4 aspect ratio */
            background: var(--white);
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            position: relative;
            overflow: hidden;
            box-sizing: border-box;
            display: flex;
            flex-direction: column;
        }
        .page-cover {
            background: linear-gradient(135deg, var(--dark), var(--primary));
            color: var(--white);
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 40px;
        }
        .cover-logo {
            font-size: 5rem;
            color: var(--secondary);
            margin-bottom: 20px;
        }
        .cover-title {
            font-family: 'Poppins', sans-serif;
            font-size: 3.5rem;
            font-weight: 700;
            margin: 0;
            line-height: 1.2;
        }
        .cover-subtitle {
            font-size: 1.5rem;
            font-weight: 300;
            margin-top: 20px;
            color: rgba(255,255,255,0.8);
        }
        .cover-year {
            position: absolute;
            bottom: 40px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 1rem;
            letter-spacing: 2px;
            text-transform: uppercase;
            color: var(--secondary);
            font-weight: 600;
        }
        
        .page-content {
            padding: 60px 80px;
        }
        .page-header {
            border-bottom: 2px solid var(--primary);
            padding-bottom: 20px;
            margin-bottom: 40px;
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
        }
        .page-header h2 {
            font-family: 'Poppins', sans-serif;
            color: var(--primary);
            font-size: 2rem;
            margin: 0;
        }
        .header-logo {
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--dark);
        }
        .header-logo i {
            color: var(--secondary);
        }
        
        h3 {
            font-family: 'Poppins', sans-serif;
            color: var(--dark);
            font-size: 1.5rem;
            margin-bottom: 15px;
        }
        p {
            font-size: 1.1rem;
            line-height: 1.7;
            color: var(--gray);
            margin-bottom: 20px;
        }
        
        .grid-2 {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin-top: 30px;
        }
        .brand-box {
            background: var(--light);
            padding: 25px;
            border-radius: 10px;
            border-left: 4px solid var(--secondary);
        }
        .brand-box h4 {
            color: var(--primary);
            font-size: 1.25rem;
            margin: 0 0 10px 0;
        }
        .brand-box p {
            font-size: 0.95rem;
            margin: 0;
        }
        
        .stats-container {
            display: flex;
            justify-content: space-between;
            margin-top: 50px;
            background: var(--primary);
            color: white;
            padding: 40px;
            border-radius: 10px;
            text-align: center;
        }
        .stat-item h2 {
            font-size: 3rem;
            color: var(--secondary);
            margin: 0;
        }
        .stat-item p {
            color: rgba(255,255,255,0.8);
            margin: 0;
            font-weight: 600;
            text-transform: uppercase;
            font-size: 0.8rem;
        }
        
        .contact-footer {
            margin-top: auto;
            background: var(--dark);
            color: white;
            padding: 40px;
            border-radius: 10px;
        }
        .contact-footer h3 {
            color: white;
            margin-top: 0;
        }
        .contact-info {
            display: flex;
            justify-content: space-between;
        }
        .contact-item {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .contact-item i {
            color: var(--secondary);
            font-size: 1.2rem;
        }
        
        .watermark {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) rotate(-45deg);
            font-size: 15rem;
            color: rgba(0,0,0,0.02);
            z-index: 0;
            pointer-events: none;
        }
        
        @media print {
            body { background: white; padding: 0; gap: 0; }
            .page { box-shadow: none; margin: 0; width: 100%; height: 100vh; page-break-after: always; }
        }
        
        /* Floating print button */
        .print-btn {
            position: fixed;
            bottom: 30px;
            right: 30px;
            background: var(--secondary);
            color: white;
            border: none;
            padding: 15px 25px;
            border-radius: 30px;
            font-family: 'Inter', sans-serif;
            font-weight: 600;
            font-size: 1rem;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(0, 180, 125, 0.4);
            display: flex;
            align-items: center;
            gap: 10px;
            transition: all 0.3s ease;
            z-index: 100;
        }
        .print-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(0, 180, 125, 0.5);
        }
        @media print {
            .print-btn { display: none; }
        }
    </style>
</head>
<body>

    <button class="print-btn" onclick="window.print()"><i class="fa-solid fa-print"></i> Print / Save as PDF</button>

    <!-- PAGE 1: Cover -->
    <div class="page page-cover">
        <i class="fa-solid fa-heart-pulse watermark"></i>
        <div class="cover-logo"><i class="fa-solid fa-heart-pulse"></i></div>
        <h1 class="cover-title">Corporate<br>Brochure</h1>
        <p class="cover-subtitle">Building India's Future Healthcare Infrastructure</p>
        <div class="cover-year">2026 Edition</div>
    </div>

    <!-- PAGE 2: Content -->
    <div class="page">
        <i class="fa-solid fa-heart-pulse watermark"></i>
        <div class="page-content">
            <div class="page-header">
                <h2>Our Ecosystem</h2>
                <div class="header-logo"><i class="fa-solid fa-heart-pulse"></i> Xpedicr.</div>
            </div>
            
            <h3>The Vision</h3>
            <p>Xpedicr Industry Pvt. Ltd. is integrating fragmented medical services into a unified, technology-driven platform. We ensure accessibility, affordability, and rapid response for every citizen across India by combining AI-driven logistics, premium telemedicine, and a vast physical network.</p>
            
            <div class="grid-2">
                <div class="brand-box">
                    <h4>Nidhaan</h4>
                    <p>India's fastest growing 10-minute emergency medical services network, optimizing ambulance routing through predictive AI.</p>
                </div>
                <div class="brand-box">
                    <h4>Nava.ai</h4>
                    <p>Advanced deep-learning diagnostic platform assisting doctors in rapid, accurate triaging and patient data analysis.</p>
                </div>
                <div class="brand-box">
                    
                <div class="brand-box">
                    <h4>Partner Network</h4>
                    <p>An elite alliance of hospitals, clinics, and diagnostic centers fully integrated into the Xpedicr infrastructure.</p>
                </div>
            </div>
            
            <div class="stats-container">
                <div class="stat-item">
                    <h2>500+</h2>
                    <p>Partner Clinics</p>
                </div>
                <div class="stat-item">
                    <h2>50+</h2>
                    <p>Cities Ready</p>
                </div>
                <div class="stat-item">
                    <h2>10m</h2>
                    <p>Response Time</p>
                </div>
            </div>
            
            <div class="contact-footer" style="margin-top: 60px;">
                <h3>Get in Touch</h3>
                <div class="contact-info">
                    <div class="contact-item">
                        <i class="fa-solid fa-envelope"></i>
                        <span>partners@xpedicr.in</span>
                    </div>
                    <div class="contact-item">
                        <i class="fa-solid fa-phone"></i>
                        <span>+91 72898 90080</span>
                    </div>
                    <div class="contact-item">
                        <i class="fa-solid fa-location-dot"></i>
                        <span>Bengaluru, India</span>
                    </div>
                </div>
            </div>
            
        </div>
    </div>

</body>
</html>"""

brochure_html_path = os.path.join(base_dir, "brochure.html")
with open(brochure_html_path, "w", encoding="utf-8") as f:
    f.write(brochure_html_content)

html_files = glob.glob(os.path.join(base_dir, "*.html"))
html_files = [f for f in html_files if "brochure.html" not in f]

old_link = '<a href="Xpedicr_Corporate_Brochure.txt" download="Xpedicr_Corporate_Brochure_2026.txt" target="_blank" class="btn btn-outline-light btn-sm"><i class="fa-solid fa-download me-2"></i> Download Corporate Brochure</a>'
new_link = '<a href="brochure.html" target="_blank" class="btn btn-outline-light btn-sm"><i class="fa-solid fa-book-open me-2"></i> View Corporate Brochure</a>'

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    content = content.replace(old_link, new_link)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

# Clean up the old txt file
txt_path = os.path.join(base_dir, "Xpedicr_Corporate_Brochure.txt")
if os.path.exists(txt_path):
    os.remove(txt_path)

print("Beautiful HTML brochure created and links updated.")
