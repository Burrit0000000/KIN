import re

css = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>KIN - Meet Your Companion</title>
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
    min-height: 100vh;
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
    background: linear-gradient(to bottom, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0.2) 50%, #030303 100%);
    z-index: 1;
}

.hero-nav {
    position: absolute;
    top: 0; left: 0; right: 0;
    padding: 2rem 4rem;
    display: flex;
    justify-content: space-between;
    z-index: 10;
}
.hero-nav img { height: 40px; }

.hero-content {
    position: relative;
    z-index: 10;
    text-align: center;
    max-width: 800px;
    padding: 2rem;
    margin-top: 10vh;
}

.hero-title {
    font-size: 8rem;
    font-weight: 900;
    margin: 0;
    line-height: 1;
    letter-spacing: -4px;
    background: linear-gradient(135deg, #FFF, #888);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 0 40px rgba(255,255,255,0.1);
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
    max-width: 1200px;
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

blockquote {
    border-left: 4px solid #A855F7;
    background: rgba(168, 85, 247, 0.05);
    margin: 3rem 0;
    padding: 2rem;
    border-radius: 0 16px 16px 0;
}

blockquote p {
    font-style: italic;
    font-size: 1.5rem;
    color: #E5E7EB;
    margin: 0;
    line-height: 1.4;
}

/* Tables */
.table-wrapper {
    overflow-x: auto;
    margin: 3rem 0;
}

table {
    width: 100%;
    border-collapse: collapse;
    background: #0A0A0A;
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid #1A1A1A;
}

th, td {
    padding: 1.25rem 1.5rem;
    text-align: left;
    border-bottom: 1px solid #1A1A1A;
}

th {
    background-color: #111111;
    color: #FFF;
    font-weight: 600;
    font-size: 1rem;
    text-transform: uppercase;
    letter-spacing: 1px;
}

td {
    color: #9CA3AF;
    font-size: 1rem;
}

tr:hover td {
    background-color: rgba(255,255,255,0.02);
}

/* Genesis Grid Layout */
.genesis-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 2.5rem;
    margin: 4rem 0;
}

.genesis-card {
    background: #0A0A0A;
    border-radius: 20px;
    border: 1px solid #1A1A1A;
    overflow: hidden;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    display: flex;
    flex-direction: column;
}

.genesis-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 40px rgba(0,0,0,0.5);
    border-color: #333;
}

.genesis-img-wrapper {
    width: 100%;
    aspect-ratio: 4/5;
    background-color: #000;
    overflow: hidden;
    position: relative;
}

.genesis-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s ease;
}

.genesis-card:hover .genesis-img {
    transform: scale(1.05);
}

.genesis-content {
    padding: 2rem;
    display: flex;
    flex-direction: column;
    flex-grow: 1;
}

.genesis-content h4 {
    margin: 0 0 0.5rem 0;
    font-size: 1.75rem;
    font-weight: 900;
    letter-spacing: -0.5px;
}

.genesis-content .archetype {
    font-size: 0.875rem;
    font-weight: 600;
    color: #6B7280;
    margin-bottom: 1.25rem;
}

.genesis-content p {
    font-size: 1rem;
    line-height: 1.6;
    color: #9CA3AF;
    margin: 0;
}

/* Footer */
footer {
    border-top: 1px solid #1A1A1A;
    padding: 4rem 2rem;
    text-align: center;
    background-color: #000;
    margin-top: 4rem;
}

footer img {
    height: 30px;
    margin-bottom: 1rem;
    opacity: 0.5;
}

footer p {
    font-size: 0.875rem;
    color: #4B5563;
    margin: 0;
}

@media (max-width: 768px) {
    .hero-title { font-size: 5rem; }
    .hero-nav { padding: 1.5rem; }
    h2 { font-size: 2rem; }
}
</style>
</head>
<body>
"""

def process_markdown():
    with open('/Users/xeniabusigin/.gemini/antigravity/scratch/KR8TIV/text/KIN_KR8TIV_Concept_Document.md', 'r') as f:
        md = f.read()

    html_parts = [css]
    html_parts.append("""
<header class="hero">
    <div class="hero-overlay"></div>
    <nav class="hero-nav" style="align-items: center;">
        <img src="./assets/kin-logo-mark.png" alt="KIN Logo">
        <div>
            <a href="pitch_deck.html" style="color: #FFF; background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.3); padding: 8px 16px; text-decoration: none; border-radius: 20px; font-weight: 600; font-size: 0.9rem; transition: all 0.3s; backdrop-filter: blur(5px);">View Pitch Deck &rarr;</a>
        </div>
    </nav>
    <div class="hero-content">
        <h1 class="hero-title">KIN</h1>
        <div class="hero-subtitle">Concept, Vision & Investment Brief — Q2 2026</div>
    </div>
</header>
<main class="container">
""")

    sections = re.split(r'\*\*(\d{2})\s+---\s+(.*?)\*\*', md)
    
    for i in range(1, len(sections), 3):
        # We drop the section wrapper and just output clean headings
        title = sections[i+1]
        content = sections[i+2]
        
        # Don't output the title if it's the 01 EXECUTIVE SUMMARY header right at the top
        # since it's redundant to the hero, though we will just output it nicely anyway.
        html_parts.append(f'<h2>{title}</h2>')
        
        lines = content.strip().split('\n')
        in_table = False
        table_lines = []
        
        for line in lines:
            line_str = line.strip()
            if not line_str:
                continue
            
            if line_str.startswith('---'):
                if not in_table:
                    in_table = True
                    table_lines = []
                    continue
                else:
                    in_table = False
                    # Parse and render table
                    table_text = ' '.join(table_lines)
                    if 'Mischief' in table_text and 'Glitch Pup' in table_text:
                        html_parts.append('<div class="genesis-grid">')
                        img_map = {
                            'Mischief': 'Michief_profile.png',
                            'Vortex': 'Vortex_profile.png',
                            'Forge': 'Forge_profile.jpeg',
                            'Aether': 'aether_profile.jpeg',
                            'Catalyst': 'Catalyst_profile.jpeg',
                            'Cipher': 'Cypher_Profile.jpeg'
                        }
                        color_map = {
                            'Mischief': '#00D8FF',
                            'Vortex': '#FF008A',
                            'Forge': '#FFB300',
                            'Aether': '#B366FF',
                            'Catalyst': '#FF5500',
                            'Cipher': '#00D8FF'
                        }
                        for t_line in table_lines:
                            t_line = t_line.strip()
                            if not t_line or t_line.startswith('**KIN'):
                                continue
                            if '---' in t_line and not t_line.startswith('---'):
                                m = re.search(r'\*\*(.*?) ---\s*(.*?)\*\*\s+(.*?)\s{2,}(.*)', t_line)
                                if m:
                                    name = m.group(1).strip()
                                    archetype = m.group(2).strip()
                                    primary = m.group(3).strip()
                                    desc = m.group(4).strip()
                                    img = img_map.get(name, 'Michief_profile.png')
                                    color = color_map.get(name, '#FFFFFF')
                                    html_parts.append(f'''
        <div class="genesis-card">
            <div class="genesis-img-wrapper">
                <img src="./assets/{img}" class="genesis-img" alt="{name}" />
            </div>
            <div class="genesis-content">
                <h4 style="color: {color};">{name}</h4>
                <div class="archetype">{archetype}</div>
                <p>{desc}</p>
            </div>
        </div>''')
                        html_parts.append('</div>')
                    
                    elif 'Consumer: KIN Personal' in table_text:
                        html_parts.append('<blockquote>')
                        for t_line in table_lines:
                            if t_line.strip() and not t_line.startswith('**') and not t_line.startswith('---'):
                                html_parts.append(f'<p style="font-size: 1.125rem; font-style: normal; color: #9CA3AF;">{t_line.strip()}</p>')
                            elif t_line.startswith('**'):
                                html_parts.append(f'<h3 style="color: #FFF; margin-top: 1rem; margin-bottom: 0.5rem; font-size: 1.25rem;">{t_line.replace("**", "")}</h3>')
                        html_parts.append('</blockquote>')

                    else:
                        html_parts.append('<div class="table-wrapper"><table>')
                        for idx, t_line in enumerate(table_lines):
                            t_line = t_line.strip()
                            if not t_line or t_line.startswith('---'):
                                continue
                            
                            cells = [c.strip() for c in re.split(r'\s{2,}', t_line) if c.strip()]
                            if idx == 0 and len(cells) > 0 and '**' in cells[0]:
                                html_parts.append('<tr>')
                                for c in cells:
                                    html_parts.append(f'<th>{c.replace("**","")}</th>')
                                html_parts.append('</tr>')
                            elif cells:
                                html_parts.append('<tr>')
                                for c in cells:
                                    html_parts.append(f'<td>{c.replace("**","")}</td>')
                                html_parts.append('</tr>')
                        html_parts.append('</table></div>')
                    
                    table_lines = []
                continue
            
            if in_table:
                table_lines.append(line_str)
                continue
            
            if line_str.startswith('>'):
                html_parts.append(f'<blockquote><p>{line_str.replace(">", "").strip()}</p></blockquote>')
            elif line_str.startswith('**') and line_str.endswith('**') and len(line_str) < 150:
                text = line_str.replace('**', '')
                html_parts.append(f'<h3 style="color: #E5E7EB; font-size: 1.5rem; font-weight: 600; margin-top: 2rem; margin-bottom: 1rem;">{text}</h3>')
            elif line_str.startswith('- '):
                html_parts.append(f'<ul><li>{line_str[2:].replace("**", "")}</li></ul>')
            elif bool(re.match(r'^\d+\.\s+', line_str)):
                html_parts.append(f'<ul><li>{line_str.replace("**", "")}</li></ul>')
            else:
                text = line_str.replace('**', '')
                html_parts.append(f'<p>{text}</p>')
                
    html_parts.append("""
</main>
<footer>
    <img src="./assets/kr8tiv-wordmark.png" alt="KR8TIV AI">
    <p>Confidential — Q2 2026. All rights reserved.</p>
</footer>
</body></html>
""")
    
    html_text = '\n'.join(html_parts)
    html_text = html_text.replace('</ul>\n<ul>', '\n')
    
    with open('/Users/xeniabusigin/.gemini/antigravity/scratch/KR8TIV/index.html', 'w') as f:
        f.write(html_text)

process_markdown()

print("HTML Website Built.")
