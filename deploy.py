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

# 1. READ CONTENT
print("--- READING about_me.txt ---")
try:
    with open("about_me.txt", "r", encoding="utf-8") as f:
        ABOUT_CONTENT = f.read()
except FileNotFoundError:
    print("❌ ERROR: about_me.txt missing. Using backup.")
    ABOUT_CONTENT = "<h1>ERROR</h1><p>File missing.</p>"

# 2. CONTENT DEFINITIONS (UNCHANGED)
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
    <li style="margin-bottom: 10px;"><strong>14. No Free Work:</strong> Pay me or leave me alone. Charity is over.</li>
    <li style="margin-bottom: 10px;"><strong>15. Time Management:</strong> No meetings. Just tickets.</li>
    <li style="margin-bottom: 10px;"><strong>16. Truth Only:</strong> Я не згладжую кути. Truth hurts? Good.</li>
    <li style="margin-bottom: 10px;"><strong>17. Hardware Fetish:</strong> EliteBook reliability > Apple hype.</li>
    <li style="margin-bottom: 10px;"><strong>18. Digital Hygiene:</strong> Clean your disk, clean your mind.</li>
    <li style="margin-bottom: 10px;"><strong>19. My Boundaries:</strong> Заміновані. Don't step.</li>
    <li style="margin-bottom: 10px;"><strong>20. Survival Guide:</strong> Як жити під час війни і залишатися людиною.</li>
</ul>
"""

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
<div class="alert"><strong>STATUS:</strong> Most repos are currently private. Preparing for public release. Wait for it.</div>
"""

# 3. CSS (CYBER WINDOW STYLE + BURGER MENU)
CSS_CODE = """
/* RESET & BASE */
body { 
    background-color: #050505; 
    color: #0F0; 
    font-family: 'Courier New', monospace; 
    margin: 0; padding: 0; 
    min-height: 100vh; 
    display: flex; flex-direction: column; 
    overflow-x: hidden;
    transition: filter 0.3s ease;
}
#matrix-bg { position: fixed; top: 0; left: 0; z-index: -1; opacity: 0.15; pointer-events: none; }

/* LINUX WINDOW HEADER */
header {
    background: #1a1a1a;
    border-bottom: 1px solid #333;
    padding: 10px 15px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: sticky; top: 0; z-index: 1000;
    box-shadow: 0 5px 15px rgba(0,0,0,0.5);
}
.window-controls { display: flex; gap: 8px; }
.dot { width: 12px; height: 12px; border-radius: 50%; cursor: pointer; transition: 0.2s; }
.dot.red { background: #ff5f56; } .dot.red:hover { box-shadow: 0 0 10px #f00; }
.dot.yellow { background: #ffbd2e; } .dot.yellow:hover { box-shadow: 0 0 10px #ff0; }
.dot.green { background: #27c93f; } .dot.green:hover { box-shadow: 0 0 10px #0f0; }
.window-title { color: #888; font-size: 0.9rem; font-weight: bold; }

/* BURGER MENU (THE HACKER WAY) */
.burger-menu { cursor: pointer; display: flex; flex-direction: column; gap: 4px; z-index: 1001; }
.line { width: 25px; height: 3px; background: #0F0; transition: 0.3s; }
.burger-menu.active .line:nth-child(1) { transform: rotate(45deg) translate(5px, 5px); background: #F00; }
.burger-menu.active .line:nth-child(2) { opacity: 0; }
.burger-menu.active .line:nth-child(3) { transform: rotate(-45deg) translate(5px, -5px); background: #F00; }

/* NAVIGATION PANEL (MOBILE HIDDEN) */
nav {
    position: fixed; top: 50px; right: -100%;
    width: 250px; height: 100vh;
    background: rgba(0, 10, 0, 0.95);
    border-left: 1px solid #0F0;
    display: flex; flex-direction: column;
    padding-top: 20px;
    transition: 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: -10px 0 30px rgba(0,0,0,0.8);
}
nav.active { right: 0; }
nav a {
    color: #FFF; text-decoration: none;
    padding: 15px 20px;
    border-bottom: 1px solid #030;
    font-size: 1.1rem;
    transition: 0.2s;
}
nav a:hover { background: #002200; padding-left: 30px; color: #0F0; }
nav a::before { content: '> '; opacity: 0; }
nav a:hover::before { opacity: 1; }

/* DESKTOP NAV (Fallback if needed, but we use burger primarily now or hybrid) */
@media(min-width: 768px) {
    nav { 
        position: static; width: auto; height: auto; 
        background: transparent; border: none; 
        flex-direction: row; box-shadow: none;
        padding-top: 0;
    }
    nav a { border: none; padding: 0 15px; font-size: 1rem; }
    nav a:hover { background: transparent; padding-left: 15px; text-shadow: 0 0 5px #0F0; }
    .burger-menu { display: none; }
}
@media(max-width: 767px) {
    .window-title { display: none; } /* Save space on mobile */
}

/* MAIN CONTENT */
.container { 
    flex: 1; max-width: 900px; margin: 30px auto; padding: 20px; 
    border: 1px solid #333; 
    background: rgba(0, 0, 0, 0.85); 
    box-shadow: 0 0 20px rgba(0, 255, 0, 0.05);
}
h1 { border-bottom: 2px solid #0F0; padding-bottom: 5px; color: #FFF; }
.red-alert { color: #FF3333; text-shadow: 0 0 5px #F00; }
.alert { border: 1px solid #F00; background: rgba(50,0,0,0.2); padding: 10px; color: #F88; }
.highlight { color: #FFF; font-weight: bold; background: #003300; padding: 2px 5px; }

/* FOOTER (THE ZOO RETURNS - CYBER EDITION) */
footer {
    background: #000; border-top: 1px dashed #0F0;
    padding: 20px; text-align: center; font-size: 0.8rem;
    color: #555; position: relative;
    overflow: hidden;
}
footer:hover { color: #888; }
.zoo-list { color: #006600; margin-bottom: 5px; cursor: help; }
.zoo-list:hover { color: #0F0; }
.ip-trace { font-family: monospace; color: #333; margin-top: 5px; }

/* EASTER EGG CLASSES */
.hidden-trigger { cursor: crosshair; }
.hidden-trigger:active { color: red; }
.shutdown-overlay {
    position: fixed; top: 0; left: 0; width: 100%; height: 100%;
    background: #000; color: #F00;
    display: flex; flex-direction: column; justify-content: center; align-items: center;
    z-index: 9999; display: none;
}

/* PRELOADER */
#preloader {
    position: fixed; top: 0; left: 0; width: 100%; height: 100%;
    background: #000; z-index: 9999;
    display: flex; align-items: center; justify-content: center;
    color: #0F0; font-size: 1.5rem; transition: opacity 1s;
}
.loaded { opacity: 0; pointer-events: none; }
"""

# --- JS: MATRIX (UA) + WINDOW LOGIC + EASTER EGGS ---
JS_MAIN = """
// 1. MATRIX BACKGROUND (UKRAINIAN)
const canvas = document.getElementById('matrix-bg');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
const chars = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ0123456789'.split('');
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

// 2. WINDOW CONTROLS (THE RED BUTTON KILL SWITCH)
function killSystem() {
    const overlay = document.getElementById('shutdown-overlay');
    overlay.style.display = 'flex';
    document.body.style.overflow = 'hidden';
    
    let seconds = 3;
    const timer = document.getElementById('shutdown-timer');
    const interval = setInterval(() => {
        seconds--;
        timer.innerText = `CONNECTION TERMINATED IN ${seconds}...`;
        if(seconds <= 0) {
            clearInterval(interval);
            timer.innerText = "SYSTEM HALTED. IT IS SAFE TO TURN OFF YOUR COMPUTER.";
            document.title = "DISCONNECTED";
        }
    }, 1000);
}

function minimizeSystem() {
    document.querySelector('.container').style.opacity = '0.1';
    document.querySelector('footer').style.opacity = '0.1';
    alert("System running in background. Click OK to restore.");
    document.querySelector('.container').style.opacity = '1';
    document.querySelector('footer').style.opacity = '1';
}

function maximizeSystem() {
    if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen();
    } else {
        if (document.exitFullscreen) {
            document.exitFullscreen();
        }
    }
}

// 3. BURGER MENU TOGGLE
function toggleMenu() {
    const nav = document.querySelector('nav');
    const burger = document.querySelector('.burger-menu');
    nav.classList.toggle('active');
    burger.classList.toggle('active');
}

// 4. EASTER EGGS & FOOTER LOGIC
document.addEventListener("DOMContentLoaded", function() {
    // Fake IP in footer
    const ips = ["192.168.0.1 (Local)", "10.0.0.13 (Proxy)", "Trace Failed...", "SBU_Node_7"];
    document.getElementById('fake-ip').innerText = "Route: " + ips[Math.floor(Math.random() * ips.length)];
    
    // Console Egg
    console.log("%c STOP! ", "color: red; font-size: 30px; font-weight: bold;");
    console.log("%c If someone told you to paste code here, they are trying to hack your Zoo.", "color: white; font-size: 16px;");
    console.log("Follow the white rabbit...");
});
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
    const speed = 3; 
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

# --- TERMINAL SCRIPT (With "Russia" Easter Egg) ---
TERMINAL_SCRIPT_INLINE = """
<script>
    document.addEventListener("DOMContentLoaded", function() {
        const input = document.getElementById("cmd");
        const history = document.getElementById("history");
        if(input) {
            input.focus();
            document.querySelector('.terminal-window').addEventListener('click', () => input.focus());
            input.addEventListener("keydown", function(e) {
                if (e.key === "Enter") {
                    const rawCmd = input.value.trim();
                    const cmd = rawCmd.toLowerCase();
                    history.innerHTML += `<div><span class="prompt">root@ukrgeek:~#</span> ${rawCmd}</div>`;
                    let res = "";
                    switch(cmd) {
                        case "help": res = "COMMANDS: [about] [projects] [email] [slava] [sudo rm -rf /]"; break;
                        case "about": res = "Redirecting to Identity..."; setTimeout(()=>window.location='about.html', 1000); break;
                        case "projects": res = "Accessing Arsenal..."; setTimeout(()=>window.location='projects.html', 1000); break;
                        case "slava": res = "<span style='color:yellow; font-weight:bold;'>GEROYAM SLAVA! 🇺🇦</span>"; break;
                        case "russia": res = "<span style='color:red; font-weight:bold; font-size: 1.5em;'>FATAL ERROR: BIOWASTE DETECTED. PURGING...</span>"; break;
                        case "clear": history.innerHTML = ""; break;
                        case "sudo rm -rf /": res = "Nice try, kid. Permission Denied."; break;
                        case "": res = ""; break;
                        default: res = `<span style='color:red'>bash: ${rawCmd}: command not found</span>`;
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

# --- HTML TEMPLATES ---

# HEADER with Window Controls & Burger
HEADER_HTML = """
<header>
    <div class="window-controls">
        <div class="dot red" onclick="killSystem()" title="Close Connection"></div>
        <div class="dot yellow" onclick="minimizeSystem()" title="Minimize"></div>
        <div class="dot green" onclick="maximizeSystem()" title="Fullscreen"></div>
    </div>
    <div class="window-title">root@ukrgeek:~</div>
    <div class="burger-menu" onclick="toggleMenu()">
        <div class="line"></div>
        <div class="line"></div>
        <div class="line"></div>
    </div>
    <nav>
        <a href="index.html">/HOME</a>
        <a href="about.html">/IDENTITY</a>
        <a href="projects.html">/ARSENAL</a>
        <a href="contact.html">/TERMINAL</a>
    </nav>
</header>
"""

# FOOTER with "Zoo" and Fake IP
FOOTER_HTML = f"""
<footer>
    <div class="zoo-list" title="My support team">
        [ SYSTEM RESOURCES: 4 CATS | 2 DOGS | 1 RAT | 1 TURTLE | 100L WATER ]
    </div>
    <div style="margin: 10px 0;">
        &copy; 2025 {IDENTITY} | NO FORGIVENESS
    </div>
    <div class="ip-trace" id="fake-ip">Trace pending...</div>
    <div class="irony" style="font-size: 0.6rem; margin-top:10px; opacity: 0.5;">
        "If you are looking for cookies, I ate them."
    </div>
    </footer>
"""

# SHUTDOWN OVERLAY (Hidden by default)
SHUTDOWN_OVERLAY = """
<div id="shutdown-overlay" class="shutdown-overlay">
    <h1 style="color:red; font-size: 3rem;">SIGNAL LOST</h1>
    <p id="shutdown-timer">TERMINATING SESSION...</p>
</div>
"""

BASE_HTML = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{title}</title><link rel="stylesheet" href="css/style.css"></head><body>
    <div id="preloader"><div style="text-align:center">INITIALIZING PROTOCOL<br><span style="font-size:0.8rem">LOADING MODULES...</span></div></div>
    {shutdown}
    <canvas id="matrix-bg"></canvas>
    {header}
    <main class="container"><div id="typewriter-content">{content}</div></main>
    {footer}
    <script src="js/main.js"></script>
    {extra_js}
    <script>
        window.addEventListener('load', () => {{
            setTimeout(() => {{ document.getElementById('preloader').classList.add('loaded'); }}, 1500);
        }});
    </script>
</body></html>"""

PAGES = {
    "index.html": { "title": f"Home | {IDENTITY}", "content": INDEX_CONTENT, "js": "<script src='js/typewriter.js'></script>" },
    "about.html": { "title": f"Identity | {IDENTITY}", "content": ABOUT_CONTENT, "js": "<script src='js/typewriter.js'></script>" },
    "projects.html": { "title": f"Arsenal | {IDENTITY}", "content": PROJECTS_CONTENT, "js": "<script src='js/typewriter.js'></script>" },
    "contact.html": { "title": f"Terminal | {IDENTITY}", "content": "<h1>Terminal Access</h1><div class='terminal-window'><div id='history'><p>UkrGeekLife OS v12.0 (Red Button Edition)...</p></div><div class='input-line'><span class='prompt'>root@ukrgeek:~#</span><input type='text' id='cmd' autofocus autocomplete='off' enterkeyhint='go'></div></div>", "js": TERMINAL_SCRIPT_INLINE }
}

# 4. BUILD & DEPLOY
print("--- WRITING ASSETS ---")
os.makedirs("css", exist_ok=True)
os.makedirs("js", exist_ok=True)
with open("css/style.css", "w", encoding="utf-8") as f: f.write(CSS_CODE)
with open("js/main.js", "w", encoding="utf-8") as f: f.write(JS_MAIN)
with open("js/typewriter.js", "w", encoding="utf-8") as f: f.write(JS_TYPEWRITER)

for fname, data in PAGES.items():
    html = BASE_HTML.format(
        title=data['title'], 
        header=HEADER_HTML, 
        content=data['content'], 
        footer=FOOTER_HTML, 
        shutdown=SHUTDOWN_OVERLAY,
        extra_js=data['js']
    )
    with open(fname, "w", encoding="utf-8") as f: f.write(html)
    print(f"✅ {fname}")

print("--- DEPLOYING ---")
run("git add .")
run(f'git commit -m "UkrGeekLife | Cyber Deck UI Update | {time.strftime("%H:%M:%S")}"')
run("git push origin master")
print(">>> DONE. TRY THE RED BUTTON.")