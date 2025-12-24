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

# 1. READ ABOUT CONTENT (Separation of Concerns)
print("--- READING about_me.txt ---")
try:
    with open("about_me.txt", "r", encoding="utf-8") as f:
        ABOUT_CONTENT = f.read()
except FileNotFoundError:
    print("❌ ERROR: about_me.txt missing. Using backup.")
    ABOUT_CONTENT = "<h1>ERROR</h1><p>File missing.</p>"

# 2. CONTENT DEFINITIONS

# --- INDEX (THE 20 TRUTHS) ---
INDEX_CONTENT = """
<h1>SYSTEM INDEX: NAVIGATION & TRUTH</h1>
<p>Welcome to <strong>UkrGeekLife</strong>. Тут немає води. Тут є факти.</p>
<div class="alert"><strong>WARNING:</strong> High concentration of sarcasm and logic.</div>

<ul style="list-style-type: none; padding: 0;">
    <li style="margin-bottom: 10px;"><strong>01. Who The Fuck Am I:</strong> Engineer. Patriot. No bullshit allowed.</li>
    <li style="margin-bottom: 10px;"><strong>02. Pure Hate:</strong> 500,000 dead Ukrainians. Why I hate Russia with pure logic.</li>
    <li style="margin-bottom: 10px;"><strong>03. Vegetarian Protocol:</strong> 10+ років без трупів у тарілці.</li>
    <li style="margin-bottom: 10px;"><strong>04. No Gods, No Masters:</strong> Атеїзм як інструмент. Релігія для слабких.</li>
    <li style="margin-bottom: 10px;"><strong>05. Full Automation:</strong> Я лінивий, тому пишу скрипти. Manual work is for idiots.</li>
    <li style="margin-bottom: 10px;"><strong>06. Python & PowerShell:</strong> Мій арсенал. Клікаєш більше 3 разів? Ти помилився.</li>
    <li style="margin-bottom: 10px;"><strong>07. Mental Void:</strong> ADHD, OCD, Depression. Як не здохнути від власної голови.</li>
    <li style="margin-bottom: 10px;"><strong>08. The Zoo:</strong> 4 cats, 2 dogs, rat, turtle. My real family.</li>
    <li style="margin-bottom: 10px;"><strong>09. UX/UI Nazi:</strong> Usability is King. Bad design hurts physically.</li>
    <li style="margin-bottom: 10px;"><strong>10. Open Source Cult:</strong> Stack Overflow — це база. Don't reinvent the wheel.</li>
    <li style="margin-bottom: 10px;"><strong>11. Security Paranoia:</strong> Ваші паролі — гівно. Вас хакнуть.</li>
    <li style="margin-bottom: 10px;"><strong>12. Old School Tech:</strong> Історія — це єдиний надійний бекап.</li>
    <li style="margin-bottom: 10px;"><strong>13. Machine Learning:</strong> Це не "ШІ", це статистика. Вчіть матчастину.</li>
    <li style="margin-bottom: 10px;"><strong>14. No Free Work:</strong> Pay me or leave me alone. Charity is over (mostly).</li>
    <li style="margin-bottom: 10px;"><strong>15. Time Management:</strong> No meetings. Just tickets.</li>
    <li style="margin-bottom: 10px;"><strong>16. Truth Only:</strong> Я не згладжую кути. Truth hurts? Good.</li>
    <li style="margin-bottom: 10px;"><strong>17. Hardware Fetish:</strong> EliteBook reliability > Apple hype.</li>
    <li style="margin-bottom: 10px;"><strong>18. Digital Hygiene:</strong> Clean your disk, clean your mind.</li>
    <li style="margin-bottom: 10px;"><strong>19. My Boundaries:</strong> Заміновані. Don't step.</li>
    <li style="margin-bottom: 10px;"><strong>20. Survival Guide:</strong> Як жити під час війни і залишатися людиною.</li>
</ul>
"""

# --- PROJECTS (THE ARSENAL - NEW!) ---
PROJECTS_CONTENT = """
<h1>THE ARSENAL: WEAPONS OF MASS CREATION</h1>
<p>I don't just write code. I build reality. Більшість моїх проектів будуть <strong>Open Source</strong> і безкоштовними. Чому? Бо я можу.</p>
<p>Coming Soon / In Progress:</p>

<h2>1. ENGINEERING & HARDWARE</h2>
<ul>
    <li><strong>Growing Box Building:</strong> Повна автоматизація гідропоніки. Свіжа їжа вдома. No chemicals, just logic.</li>
    <li><strong>Lighting Building:</strong> DIY Smart Light. Керування спектром, яскравістю і таймінгами. Not cheap Chinese crap.</li>
    <li><strong>Global Box:</strong> Модульне будівництво. Універсальні конструкції. My architecture vision.</li>
</ul>

<h2>2. SOCIAL & BIO SECTOR</h2>
<ul>
    <li><strong>Volunteer Cats Helping:</strong> Соціальне волонтерство. Коти не вміють просити про допомогу, тому я роблю це за них.</li>
    <li><strong>Social Voluntar:</strong> Допомога тим, хто реально потребує, а не піариться.</li>
</ul>

<h2>3. THE COMMUNITY (MY CULT)</h2>
<ul>
    <li><strong>Smart Community Building:</strong> Я будую спільноту для розумних людей.</li>
    <li><strong>Entry Rule:</strong> It doesn't matter who you are. Gay, straight, alien, black, white — I don't give a fuck.</li>
    <li><strong>Condition:</strong> Just be smart. Думай головою. Idiots are banned properly.</li>
</ul>

<div class="alert">
    <strong>STATUS:</strong> Most repos are currently private. Preparing for public release. Wait for it.
</div>
"""

# 3. CSS & STYLES
CSS_CODE = """
body { background-color: #000; color: #0F0; font-family: 'Courier New', monospace; margin: 0; padding: 0; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
#matrix-bg { position: fixed; top: 0; left: 0; z-index: -1; opacity: 0.15; }
header { background: rgba(0, 20, 0, 0.95); border-bottom: 2px solid #0F0; padding: 15px 0; text-align: center; position: sticky; top: 0; z-index: 100; }
.logo { font-size: 1.5rem; font-weight: bold; text-transform: uppercase; letter-spacing: 3px; margin-bottom: 10px; text-shadow: 0 0 10px #0F0; display: block; }
nav a { color: #FFF; text-decoration: none; margin: 0 10px; font-size: 1.1rem; font-weight: bold; transition: 0.3s; display: inline-block; }
nav a:hover { color: #0F0; text-shadow: 0 0 8px #0F0; }
.container { flex: 1; max-width: 900px; margin: 30px auto; padding: 20px; background: rgba(0, 0, 0, 0.8); border: 1px solid #333; width: 90%; box-sizing: border-box; }
h1, h2 { border-bottom: 1px solid #0F0; padding-bottom: 10px; text-transform: uppercase; word-wrap: break-word; }
p, li { font-size: 1.1rem; line-height: 1.6; }
.red-alert { color: #FF3333; font-weight: bold; }
.alert { border: 1px solid #F00; padding: 10px; color: #F00; background: rgba(50,0,0,0.3); margin: 20px 0; }
.highlight { color: #FFF; font-weight: bold; }
footer { border-top: 2px solid #0F0; background: #020202; text-align: center; padding: 20px; margin-top: auto; font-size: 0.9rem; color: #666; }
.footer-links a { color: #AAA; text-decoration: none; margin: 0 8px; font-weight: bold; }
.footer-links a:hover { color: #0F0; text-decoration: underline; }
.zoo-counter { color: #004400; font-size: 0.85rem; letter-spacing: 1px; margin-top: 10px; }
.irony { font-style: italic; color: #444; font-size: 0.75rem; margin-top: 5px; }
.cursor::after { content: '█'; animation: blink 1s infinite; color: #0F0; margin-left: 5px; }
@keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
/* TERMINAL FIXES */
.terminal-window { background: #111; border: 1px solid #0F0; padding: 15px; height: 50vh; overflow-y: auto; font-family: 'Courier New', monospace; font-size: 1rem; }
.input-line { display: flex; align-items: center; }
.prompt { color: #0F0; margin-right: 10px; font-weight: bold; white-space: nowrap; }
input#cmd { background: transparent; border: none; color: #FFF; font-family: 'Courier New', monospace; font-size: 1rem; flex-grow: 1; outline: none; width: 100%; }
#typewriter-content { visibility: hidden; }
@media (max-width: 600px) { .logo { font-size: 1.2rem; } nav a { font-size: 0.9rem; margin: 0 5px; } .container { width: 95%; margin: 10px auto; padding: 15px; } }
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

FOOTER = f"""
<footer>
    <div>System Online :: &copy; 2025 {IDENTITY}</div>
    <div class="footer-links">
        <a href="index.html">/ROOT</a>
        <a href="about.html">/BIN/WHOAMI</a>
        <a href="projects.html">/VAR/WWW/ARSENAL</a>
        <a href="contact.html">/DEV/STDIN</a>
    </div>
    <div class="zoo-counter">Running on: 4 Cats, 2 Dogs, 1 Turtle, 1 Rat & 100L Aquarium.</div>
    <div class="irony">"I automated this footer because manual typing is a bug."</div>
    </footer>
"""

# --- TERMINAL SCRIPT (FIXED FOR MOBILE & CONTACTS) ---
TERMINAL_SCRIPT = """
<script>
    document.addEventListener("DOMContentLoaded", function() {
        const input = document.getElementById("cmd");
        const history = document.getElementById("history");
        
        if(input) {
            // Force focus on load and click
            input.focus();
            document.querySelector('.terminal-window').addEventListener('click', () => input.focus());
            
            input.addEventListener("keydown", function(e) {
                if (e.key === "Enter") {
                    const rawCmd = input.value.trim();
                    const cmd = rawCmd.toLowerCase();
                    
                    history.innerHTML += `<div><span class="prompt">guest@ukrgeek:~$</span> ${rawCmd}</div>`;
                    
                    let res = "";
                    switch(cmd) {
                        case "help": 
                            res = "Available: [about] [projects] [email] [slava] [clear]"; break;
                        case "about": 
                            res = "See Identity page (/BIN/WHOAMI)."; break;
                        case "projects": 
                            res = "See Arsenal page. Open Source & Hardware."; break;
                        case "email": 
                            res = "contact@ukrgeek.life"; break;
                        case "slava": 
                            res = "<span style='color:yellow; font-weight:bold;'>GEROYAM SLAVA! 🇺🇦</span>"; break;
                        case "russia": 
                            res = "<span style='color:red; font-weight:bold;'>ERROR 403: TERRORIST STATE DETECTED. BLOCKING CONNECTION.</span>"; break;
                        case "clear": 
                            history.innerHTML = ""; break;
                        case "": res = ""; break;
                        default: res = `<span style='color:red'>Command '${rawCmd}' not found. Try 'help'.</span>`;
                    }
                    
                    if(cmd !== "clear" && res !== "") {
                        history.innerHTML += `<div style='margin-bottom:10px; color:#DDD; line-height:1.4;'>${res}</div>`;
                    }
                    
                    input.value = "";
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
    "index.html": { "title": f"Home | {IDENTITY}", "content": INDEX_CONTENT, "js": "<script src='js/typewriter.js'></script>" },
    "about.html": { "title": f"Identity | {IDENTITY}", "content": ABOUT_CONTENT, "js": "<script src='js/typewriter.js'></script>" },
    "projects.html": { "title": f"Arsenal | {IDENTITY}", "content": PROJECTS_CONTENT, "js": "<script src='js/typewriter.js'></script>" },
    "contact.html": { 
        "title": f"Terminal | {IDENTITY}", 
        "content": "<h1>Terminal Access</h1><div class='terminal-window'><div id='history'><p>UkrGeekLife OS v10.0 (Arsenal Loaded)...</p></div><div class='input-line'><span class='prompt'>guest@ukrgeek:~$</span><input type='text' id='cmd' autofocus autocomplete='off' enterkeyhint='go'></div></div>", 
        "js": TERMINAL_SCRIPT 
    }
}

# 4. BUILD & DEPLOY
print("--- WRITING ASSETS ---")
os.makedirs("css", exist_ok=True)
os.makedirs("js", exist_ok=True)
with open("css/style.css", "w", encoding="utf-8") as f: f.write(CSS_CODE)
with open("js/matrix.js", "w", encoding="utf-8") as f: f.write(JS_MATRIX)
with open("js/typewriter.js", "w", encoding="utf-8") as f: f.write(JS_TYPEWRITER)

for fname, data in PAGES.items():
    html = BASE_HTML.format(title=data['title'], logo=IDENTITY, nav=NAV_MENU, content=data['content'], footer=FOOTER, extra_js=data['js'])
    with open(fname, "w", encoding="utf-8") as f: f.write(html)
    print(f"✅ {fname}")

print("--- DEPLOYING ---")
run("git add .")
run(f'git commit -m "UkrGeekLife | Projects Arsenal Added | {time.strftime("%H:%M:%S")}"')
run("git push origin master")
print(">>> DONE. CHECK THE ARSENAL.")