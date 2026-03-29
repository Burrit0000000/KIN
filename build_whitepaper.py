import re

css = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>KIN - Technical Whitepaper</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800;900&display=swap" rel="stylesheet">
<style>
* { box-sizing: border-box; }

body {
    font-family: 'Outfit', sans-serif;
    background-color: #030303;
    color: #A3A3A3;
    margin: 0;
    padding: 0;
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
}

/* Hero Section */
.hero {
    position: relative;
    width: 100%;
    min-height: 60vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: #000;
    background-image: url('./assets/vortex_boardroom_cover.png');
    background-size: cover;
    background-position: center;
    overflow: hidden;
}

.hero-overlay {
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: linear-gradient(to bottom, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0.4) 50%, #030303 100%);
    z-index: 1;
}

.hero-nav {
    position: absolute;
    top: 0; left: 0; right: 0;
    padding: 2rem 4rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 10;
}
.hero-nav img { height: 40px; }

.hero-content {
    position: relative;
    z-index: 10;
    text-align: center;
    max-width: 800px;
    padding: 2rem;
    margin-top: 5vh;
}

.hero-title {
    font-size: 6rem;
    font-weight: 900;
    margin: 0;
    line-height: 1;
    letter-spacing: -2px;
    background: linear-gradient(135deg, #00D8FF, #A855F7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 0 40px rgba(168,85,247,0.3);
}

.hero-subtitle {
    font-size: 1.5rem;
    font-weight: 400;
    color: #E5E7EB;
    margin-top: 1rem;
    letter-spacing: 1px;
}

/* Container */
.container {
    max-width: 900px;
    margin: 0 auto;
    padding: 4rem 2rem;
}

/* Typography */
h2 {
    color: #FFFFFF;
    font-size: 2.5rem;
    font-weight: 800;
    letter-spacing: -1px;
    margin-top: 4rem;
    margin-bottom: 1.5rem;
    border-bottom: 1px solid #1A1A1A;
    padding-bottom: 1rem;
}

h3 {
    color: #E5E7EB;
    font-size: 1.5rem;
    font-weight: 600;
    margin-top: 2rem;
    margin-bottom: 1rem;
}

p {
    font-size: 1.125rem;
    font-weight: 300;
    margin-bottom: 1.5rem;
    color: #9CA3AF;
}

ul {
    padding-left: 1.5rem;
    margin-bottom: 2rem;
}

li {
    font-size: 1.125rem;
    font-weight: 300;
    margin-bottom: 0.5rem;
    color: #9CA3AF;
}

strong {
    color: #FFF;
    font-weight: 600;
}

/* Footer */
footer {
    border-top: 1px solid #1A1A1A;
    padding: 4rem 2rem;
    text-align: center;
    background-color: #000;
    margin-top: 4rem;
}
footer p {
    font-size: 0.875rem;
    color: #4B5563;
    margin: 0;
}
</style>
</head>
<body>
<header class="hero">
    <div class="hero-overlay"></div>
    <nav class="hero-nav">
        <img src="./assets/kin-logo-mark.png" alt="KIN Logo">
        <div style="display:flex; gap: 1rem;">
            <a href="index.html" style="color: #FFF; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); padding: 8px 16px; text-decoration: none; border-radius: 20px; font-weight: 600; font-size: 0.9rem; transition: all 0.3s; backdrop-filter: blur(5px);">&larr; Concept</a>
            <a href="pitch_deck.html" style="color: #FFF; background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.3); padding: 8px 16px; text-decoration: none; border-radius: 20px; font-weight: 600; font-size: 0.9rem; transition: all 0.3s; backdrop-filter: blur(5px);">Pitch Deck &rarr;</a>
        </div>
    </nav>
    <div class="hero-content">
        <h1 class="hero-title">WHITEPAPER</h1>
        <div class="hero-subtitle">Technical & Economic Foundation</div>
    </div>
</header>
<main class="container">
"""

def process_markdown():
    with open('/Users/xeniabusigin/.gemini/antigravity/scratch/KR8TIV/text/KIN_Technical_Whitepaper.md', 'r') as f:
        md = f.read()

    html_parts = [css]
    
    # Very simple markdown parser for the whitepaper
    lines = md.split('\\n')
    for line in lines:
        line_str = line.strip()
        if not line_str or line_str == '***' or line_str.startswith('# KIN:'):
            continue
            
        if line_str.startswith('## '):
            html_parts.append(f'<h2>{line_str[3:].replace("**", "")}</h2>')
        elif line_str.startswith('**') and not line_str.startswith('***'):
            # It's an h3 or just strong text. Let's make it an h3 if it starts with a number like **2.1
            html_parts.append(f'<h3>{line_str.replace("**", "")}</h3>')
        elif line_str.startswith('* '):
            # simple bold parsing inside list
            text = line_str[2:]
            text = re.sub(r'\\*\\*(.*?)\\*\\*', r'<strong>\\1</strong>', text)
            html_parts.append(f'<ul><li>{text}</li></ul>')
        elif bool(re.match(r'^\\d+\\.\\s+', line_str)):
            text = line_str
            text = re.sub(r'\\*\\*(.*?)\\*\\*', r'<strong>\\1</strong>', text)
            html_parts.append(f'<ul><li>{text}</li></ul>')
        else:
            text = line_str
            text = re.sub(r'\\*\\*(.*?)\\*\\*', r'<strong>\\1</strong>', text)
            html_parts.append(f'<p>{text}</p>')
                
    html_parts.append("""
</main>
<footer>
    <img src="./assets/kr8tiv-wordmark.png" alt="KR8TIV AI" style="height: 30px; margin-bottom: 1rem; opacity: 0.5;">
    <p>Confidential — Q2 2026. All rights reserved.</p>
</footer>
</body></html>
""")
    
    html_text = '\\n'.join(html_parts)
    html_text = html_text.replace('</ul>\\n<ul>', '\\n')
    
    with open('/Users/xeniabusigin/.gemini/antigravity/scratch/KR8TIV/whitepaper.html', 'w') as f:
        f.write(html_text)

process_markdown()

print("Whitepaper HTML Website Built.")
