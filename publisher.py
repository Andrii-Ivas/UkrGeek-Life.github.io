# -*- coding: utf-8 -*-
import os
import sys

# 1. SETUP
sys.stdout.reconfigure(encoding='utf-8')
IDENTITY = "UkrGeekLife | Андрій Івась"
os.makedirs("css", exist_ok=True)
os.makedirs("js", exist_ok=True)

# 2. ASSETS (CSS & JS)
# Я використовую одинарні лапки для надійності
CSS_CODE = """
body { background-color: #000; color: #0F0; font-family: 'Courier New', monospace; margin: 0; padding: 0; min-height: 100vh; display: flex; flex-direction: column; }
#matrix-bg { position: fixed; top: 0; left: 0; z-index: -1; opacity: 0.15; }
header { background: rgba(0, 20, 0, 0.95); border-bottom: 2px solid #0F0; padding: 15px 0; text-align: center; position: sticky; top: 0; z-index: 100; }
.logo { font-size: 1.5rem; font-weight: bold; text-transform: uppercase; letter-spacing: 3px; margin-bottom: 10px; text-shadow: 0 0 10px #0F0; }
nav a { color: #FFF; text-decoration: none; margin: 0 15px; font-size: 1.1rem; font-weight: bold; transition: 0.3s; }
nav a:hover { color: #0F0; text-shadow: 0 0 8px #0F0; }
.container { flex: 1; max-width: 900px; margin: 40px auto; padding: 20px; background: rgba(0, 0, 0, 0.8); border: 1px solid #333; width: 90%; }
h1, h2 { border-bottom: 1px solid #0F0; padding-bottom: 10px; }
p, li { font-size: 1.1rem; line-height: 1.6; }
footer { border-top: 2px solid #0F0; background: #050505; text-align: center; padding: 20px; margin-top: auto; font-size: 0.9rem; color: #888; }
footer a { color: #888; text-decoration: none; margin: 0 10px; }
footer a:hover { color: #0F0; }
.terminal-window { background: #111; border: 1px solid #0F0; padding: 20px; height: 60vh; overflow-y: auto; }
.input-line { display: flex; align-items: center; }
.prompt { color: #0F0; margin-right: 10px; font-weight: bold; }
input#cmd { background: transparent; border: none; color: #FFF; font-family: monospace; font-size: 1.2rem; flex-grow: 1; outline: none; }
"""

JS_MATRIX = """
const canvas = document.getElementById('matrix-bg');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
const chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
const fontSize = 16;
const columns = canvas.width/fontSize;
const drops = [];
for(let x=0; x<columns; x++) drops[x]=1;
function draw() {
    ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = '#0F0';
    ctx.font = fontSize + 'px monospace';
    for(let i=0; i<drops.length; i++) {
        const text = chars[Math.floor(Math.random()*chars.length)];
        ctx.fillText(text, i*fontSize, drops[i]*fontSize);
        if(drops[i]*fontSize > canvas.height && Math.random() > 0.975) drops[i]=0;
        drops[i]++;
    }
}
setInterval(draw, 33);
window.addEventListener('resize', () => { canvas.width = window.innerWidth; canvas.height = window.innerHeight; });
"""

JS_TERMINAL = """
const input = document.getElementById("cmd");
const history = document.getElementById("history");
if(input) {
    input.addEventListener("keydown", function(e) {
        if (e.key === "Enter") {
            const cmd = input.value.trim().toLowerCase();
            history.innerHTML += `<div><span class="prompt">guest@ukrgeek:~$</span> ${input.value}</div>`;
            let res = "";
            switch(cmd) {
                case "help": res = "COMMANDS: [about] [projects] [email] [slava] [clear]"; break;
                case "about": res = "Andrii Ivas. Engineer. Patriot."; break;
                case "projects": res = "Full Deploy System, Security Scripts."; break;
                case "slava": res = "<span style='color:yellow'>GEROYAM SLAVA!</span>"; break;
                case "clear": history.innerHTML = ""; break;
                default: res = "<span style='color:red'>Command not found.</span>";
            }
            if(cmd!=="clear") history.innerHTML += `<div style='margin-bottom:10px; color:#DDD'>${res}</div>`;
            input.value = "";
            document.querySelector('.terminal-window').scrollTop = document.querySelector('.terminal-window').scrollHeight;
        }
    });
    document.addEventListener('click', () => input.focus());
}
"""

# 3. TEMPLATES
NAV_MENU = """
<nav role="navigation">
    <a href="index.html">[ ГОЛОВНА ]</a>
    <a href="about.html">[ ПРО МЕНЕ ]</a>
    <a href="projects.html">[ ПРОЄКТИ ]</a>
    <a href="contact.html">[ ТЕРМІНАЛ ]</a>
</nav>
"""

FOOTER_TEMPLATE = """
<footer>
    <div>&copy; 2025 {logo}</div>
    <div style="margin-top:10px;">
        <a href="index.html">Main</a> | <a href="contact.html">Terminal</a>
    </div>
</footer>
"""

BASE_HTML = """<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <canvas id="matrix-bg"></canvas>
    <header><div class="logo">{logo}</div>{nav}</header>
    <main class="container">{content}</main>
    {footer}
    <script src="js/matrix.js"></script>
    {extra_js}
</body>
</html>"""

# 4. CONTENT
PAGES = {
    "index.html": { "title": f"Головна | {IDENTITY}", "content": "<h1>System Online</h1><p>Ласкаво просимо в цифровий простір.</p>", "js": "" },
    "about.html": { "title": f"Про Мене | {IDENTITY}", "content": "<h1>Identity</h1><p>Андрій Івась. Інженер.</p>", "js": "" },
    "projects.html": { "title": f"Проєкти | {IDENTITY}", "content": "<h1>Projects</h1><p>Automation & Security.</p>", "js": "" },
    "contact.html": { "title": f"Термінал | {IDENTITY}", "content": "<h1>Terminal Access</h1><div class='terminal-window'><div id='history'><p>System Ready...</p></div><div class='input-line'><span class='prompt'>guest@ukrgeek:~$</span><input type='text' id='cmd' autofocus></div></div>", "js": f"<script>{JS_TERMINAL}</script>" }
}

# 5. GENERATE
def generate():
    print("--- WRITING FILES ---")
    with open("css/style.css", "w", encoding="utf-8") as f: f.write(CSS_CODE)
    with open("js/matrix.js", "w", encoding="utf-8") as f: f.write(JS_MATRIX)
    
    for filename, data in PAGES.items():
        html = BASE_HTML.format(title=data['title'], logo=IDENTITY, nav=NAV_MENU, content=data['content'], footer=FOOTER_TEMPLATE.format(logo=IDENTITY), extra_js=data['js'])
        with open(filename, "w", encoding="utf-8") as f: f.write(html)
        print(f"✅ {filename} Generated")

if __name__ == "__main__":
    generate()