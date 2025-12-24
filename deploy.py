# -*- coding: utf-8 -*-
import os
import sys
import subprocess
import time

# --- CONFIGURATION ---
IDENTITY = "UkrGeekLife | Andrii Ivas"
sys.stdout.reconfigure(encoding='utf-8')

def run(cmd):
    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"✅ Executed: {cmd}")
    except subprocess.CalledProcessError:
        print(f"⚠️ Warning: Error running {cmd}")

# 1. READ CONTENT (Separation of Concerns)
print("--- READING about_me.txt ---")
try:
    with open("about_me.txt", "r", encoding="utf-8") as f:
        ABOUT_CONTENT = f.read()
except FileNotFoundError:
    # Fallback content if file is missing, to prevent crash
    print("❌ ERROR: about_me.txt missing. Using backup text.")
    ABOUT_CONTENT = "<h1>SYSTEM ERROR</h1><p>about_me.txt not found.</p>"

# 2. DEFINITIONS

# --- CSS (UPDATED FOR RESPONSIVENESS) ---
CSS_CODE = """
/* BASE STYLES */
body { 
    background-color: #000; 
    color: #0F0; 
    font-family: 'Courier New', Courier, monospace;
    margin: 0; 
    padding: 0; 
    min-height: 100vh; 
    display: flex; 
    flex-direction: column; 
    overflow-x: hidden;
}
#matrix-bg { position: fixed; top: 0; left: 0; z-index: -1; opacity: 0.15; }

/* HEADER */
header { 
    background: rgba(0, 20, 0, 0.95); 
    border-bottom: 2px solid #0F0; 
    padding: 15px 0; 
    text-align: center; 
    position: sticky; 
    top: 0; 
    z-index: 100; 
}
.logo { 
    font-size: 1.5rem; 
    font-weight: bold; 
    text-transform: uppercase; 
    letter-spacing: 3px; 
    margin-bottom: 10px; 
    text-shadow: 0 0 10px #0F0; 
    display: block;
}
nav a { 
    color: #FFF; 
    text-decoration: none; 
    margin: 0 10px; 
    font-size: 1.1rem; 
    font-weight: bold; 
    transition: 0.3s; 
    display: inline-block;
}
nav a:hover { color: #0F0; text-shadow: 0 0 8px #0F0; }

/* CONTAINER */
.container { 
    flex: 1; 
    max-width: 900px; 
    margin: 30px auto; 
    padding: 20px; 
    background: rgba(0, 0, 0, 0.8); 
    border: 1px solid #333; 
    width: 90%; 
    box-sizing: border-box;
}
h1, h2 { border-bottom: 1px solid #0F0; padding-bottom: 10px; text-transform: uppercase; word-wrap: break-word; }
p, li { font-size: 1.1rem; line-height: 1.6; }
.red-alert { color: #FF3333; font-weight: bold; }
.highlight { color: #FFF; font-weight: bold; }

/* FOOTER (THE ZOO) */
footer { 
    border-top: 2px solid #0F0; 
    background: #020202; 
    text-align: center; 
    padding: 20px; 
    margin-top: auto; 
    font-size: 0.9rem; 
    color: #666; 
}
.footer-links { margin: 10px 0; }
.footer-links a { color: #AAA; text-decoration: none; margin: 0 8px; font-weight: bold; }
.footer-links a:hover { color: #0F0; text-decoration: underline; }
.zoo-counter { color: #004400; font-size: 0.85rem; letter-spacing: 1px; margin-top: 10px; }
.irony { font-style: italic; color: #444; font-size: 0.75rem; margin-top: 5px; }

/* ANIMATIONS */
.cursor::after { content: '█'; animation: blink 1s infinite; color: #0F0; margin-left: 5px; }
@keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }

/* TERMINAL SPECIFIC */
.terminal-window { 
    background: #111; 
    border: 1px solid #0F0; 
    padding: 15px; 
    height: 50vh; 
    overflow-y: auto; 
    font-family: 'Courier New', monospace; 
    font-size: 1rem;
}
.input-line { display: flex; align-items: center; }
.prompt { color: #0F0; margin-right: 10px; font-weight: bold; white-space: nowrap; }
input#cmd { 
    background: transparent; 
    border: none; 
    color: #FFF; 
    font-family: 'Courier New', monospace; 
    font-size: 1rem; 
    flex-grow: 1; 
    outline: none; 
    width: 100%;
}
#typewriter-content { visibility: hidden; }

/* --- RESPONSIVE / ADAPTIVE DESIGN --- */
@media (max-width: 600px) {
    .logo { font-size: 1.2rem; letter-spacing: 1px; }
    nav a { font-size: 0.9rem; margin: 0 5px; padding: 5px 0; }
    .container { width: 95%; margin: 10px auto; padding: 15px; }
    h1 { font-size: 1.4rem; }
    h2 { font-size: 1.2rem; }
    p, li { font-size: 1rem; }
    .terminal-window { height: 60vh; font-size: 0.9rem; }
    input#cmd { font-size: 0.9rem; }
}
"""

JS_MATRIX = """
const canvas = document.getElementById('matrix-bg');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
const chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
const fontSize = 14; 
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

JS_TYPEWRITER = """
document.addEventListener("DOMContentLoaded", function() {
    const element = document.getElementById('typewriter-content');
    if (!element) return;
    const text = element.innerHTML;
    element.innerHTML = "";
    element.classList.add("cursor");
    element.style.visibility = "visible";
    let i = 0;
    const speed = 5; 
    function type() {
        if (i < text.length) {
            if (text.charAt(i) === '<') {
                let tag = "";
                while (text.charAt(i) !== '>' && i < text.length) { tag += text.charAt(i); i++; }
                tag += '>'; i++; element.innerHTML += tag;
            } else { element.innerHTML += text.charAt(i); i++; }
            setTimeout(type, speed);
        }
    }
    type();
});
"""

# --- FOOTER CONTENT ---
FOOTER = f"""
<footer>
    <div>System Online :: &copy; 2025 {IDENTITY}</div>
    <div class="footer-links">
        <a href="index.html">/ROOT</a>
        <a href="about.html">/BIN/WHOAMI</a>
        <a href="contact.html">/DEV/STDIN</a>
    </div>
    <div class="zoo-counter">Running on: 4 Cats, 2 Dogs, 1 Turtle, 1 Rat & 100L Aquarium.</div>
    <div class="irony">"I automated this footer because manual typing is a bug."</div>
    </footer>
"""

# --- TERMINAL SCRIPT (ROBUST & INLINE) ---
TERMINAL_SCRIPT = """
<script>
    document.addEventListener("DOMContentLoaded", function() {
        const input = document.getElementById("cmd");
        const history = document.getElementById("history");
        
        // 1. Force Focus logic
        if(input) {
            input.focus();
            // Refocus if user clicks anywhere on terminal
            document.querySelector('.terminal-window').addEventListener('click', () => input.focus());
            
            input.addEventListener("keydown", function(e) {
                if (e.key === "Enter") {
                    const rawCmd = input.value.trim();
                    const cmd = rawCmd.toLowerCase();
                    
                    // Echo command
                    history.innerHTML += `<div><span class="prompt">guest@ukrgeek:~$</span> ${rawCmd}</div>`;
                    
                    let res = "";
                    switch(cmd) {
                        case "help": 
                            res = "Available: [about] [projects] [email] [slava] [clear]"; 
                            break;
                        case "about": 
                            res = "See Identity page (/BIN/WHOAMI)."; 
                            break;
                        case "projects": 
                            res = "GitHub: ivas-andre. Automation. Security."; 
                            break;
                        case "email": 
                            res = "contact@ukrgeek.life"; 
                            break;
                        case "slava": 
                            res = "<span style='color:yellow; font-weight:bold;'>GEROYAM SLAVA! 🇺🇦</span>"; 
                            break;
                        case "russia": 
                            res = "<span style='color:red; font-weight:bold;'>ERROR 403: TERRORIST STATE DETECTED. BLOCKING.</span>"; 
                            break;
                        case "clear": 
                            history.innerHTML = ""; 
                            break;
                        case "":
                            res = ""; 
                            break;
                        default: 
                            res = `<span style='color:red'>Command '${rawCmd}' not found. Try 'help'.</span>`;
                    }
                    
                    if(cmd !== "clear" && res !== "") {
                        history.innerHTML += `<div style='margin-bottom:10px; color:#DDD; line-height:1.4;'>${res}</div>`;
                    }
                    
                    input.value = "";
                    // Auto-scroll to bottom
                    const win = document.querySelector('.terminal-window');
                    win.scrollTop = win.scrollHeight;
                }
            });
        }
    });
</script>
"""

NAV_MENU = """
<nav role="navigation">
    <a href="index.html">[ HOME ]</a>
    <a href="about.html">[ IDENTITY ]</a>
    <a href="projects.html">[ ARSENAL ]</a>
    <a href="contact.html">[ TERMINAL ]</a>
</nav>
"""

BASE_HTML = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{title}</title><link rel="stylesheet" href="css/style.css"></head><body><canvas id="matrix-bg"></canvas><header><div class="logo">{logo}</div>{nav}</header><main class="container"><div id="typewriter-content">{content}</div></main>{footer}<script src="js/matrix.js"></script>{extra_js}</body></html>"""

PAGES = {
    "index.html": { "title": f"Home | {IDENTITY}", "content": "<h1>System Online</h1><p>Welcome to the digital space.</p><p>All systems nominal.</p>", "js": "" },
    "about.html": { "title": f"Identity | {IDENTITY}", "content": ABOUT_CONTENT, "js": "<script src='js/typewriter.js'></script>" },
    "projects.html": { "title": f"Arsenal | {IDENTITY}", "content": "<h1>Arsenal</h1><ul><li>Full Automation</li><li>Security Audits</li><li>Python/PowerShell</li></ul>", "js": "" },
    "contact.html": { 
        "title": f"Terminal | {IDENTITY}", 
        "content": """
        <h1>Terminal Access</h1>
        <div class='terminal-window'>
            <div id='history'>
                <p>UkrGeekLife OS v8.1 (Mobile Ready)...</p>
                <p>Type 'help' to verify privileges...</p>
            </div>
            <div class='input-line'>
                <span class='prompt'>guest@ukrgeek:~$</span>
                <input type='text' id='cmd' autofocus autocomplete="off" enterkeyhint="go">
            </div>
        </div>
        """, 
        "js": TERMINAL_SCRIPT 
    }
}

# 3. BUILD
print("--- WRITING ASSETS & HTML ---")
os.makedirs("css", exist_ok=True)
os.makedirs("js", exist_ok=True)
with open("css/style.css", "w", encoding="utf-8") as f: f.write(CSS_CODE)
with open("js/matrix.js", "w", encoding="utf-8") as f: f.write(JS_MATRIX)
with open("js/typewriter.js", "w", encoding="utf-8") as f: f.write(JS_TYPEWRITER)

for fname, data in PAGES.items():
    html = BASE_HTML.format(title=data['title'], logo=IDENTITY, nav=NAV_MENU, content=data['content'], footer=FOOTER, extra_js=data['js'])
    with open(fname, "w", encoding="utf-8") as f: f.write(html)
    print(f"✅ {fname}")

# 4. DEPLOY
print("--- FORCE DEPLOY ---")
run("git add .")
run(f'git commit -m "UkrGeekLife | Responsive Fix & Footer | {time.strftime("%H:%M:%S")}"')
run("git push origin master")
print(">>> DONE. REFRESH YOUR BROWSER.")