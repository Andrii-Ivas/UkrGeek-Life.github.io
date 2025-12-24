# -*- coding: utf-8 -*-
import os, sys, subprocess, time, random

# --- CONFIG ---
IDENTITY = "UkrGeekLife | Andrii Ivas"
sys.stdout.reconfigure(encoding='utf-8')

LINKS = {
    "YOUTUBE": "https://www.youtube.com/@UkrGeekLife",
    "INSTA_MAIN": "https://www.instagram.com/ivas_andrii/",
    "INSTA_PHOTO": "https://www.instagram.com/andrii_photographer/",
    "FACEBOOK": "https://www.facebook.com/Andrii.Ivas/", 
    "LINKEDIN": "https://www.linkedin.com/in/ivas-andre/", 
    "X": "https://x.com/Andrii_Ivas",
    "TUMBLR": "https://www.tumblr.com/andre-ivas",
    "TWITCH": "https://www.twitch.tv/ivas_andre",
    "GITHUB": "https://github.com/ivas-andre",
    "SPOTIFY": "https://open.spotify.com/playlist/1BG0k1dDJN14PczoyvSD6T?si=JVz8SvIGQHeba0XCCsulzQ" 
}
VIDEO_ID = "-h7ygd0mp7c"

def run(cmd):
    try:
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"✅ Executed: {cmd}")
    except:
        print(f"ℹ️ Git: Ready.")

print("--- READING DATA ---")
try:
    with open("about_me.txt", "r", encoding="utf-8") as f: BASE_ABOUT = f.read()
except: BASE_ABOUT = "<h1>ERROR</h1><p>File missing.</p>"

# --- HTML CONTENT ---

# PHOTO PAGE (GRID)
PHOTO_CONTENT = """
<h1>/GALLERY_GRID</h1>
<p>Visual Database.</p>
<div class="photo-grid-container">
    <div class="widget-box">
        <div class="widget-header">CAM_01: INSTAGRAM_FEED</div>
        <div class="widget-content">
            <iframe src="https://snapwidget.com/embed/1115084" class="snapwidget-widget" allowtransparency="true" frameborder="0" scrolling="no" style="border:none; overflow:hidden; width:100%; height:100%" title="Posts from Instagram"></iframe>
        </div>
    </div>
    <div class="widget-box placeholder"><div class="widget-header">CAM_02: SIGNAL_LOST</div><div class="static-noise">NO SIGNAL</div></div>
    <div class="widget-box placeholder"><div class="widget-header">CAM_03: OFFLINE</div><div class="static-noise">WAITING...</div></div>
    <div class="widget-box placeholder"><div class="widget-header">CAM_04: OFFLINE</div><div class="static-noise">WAITING...</div></div>
    <div class="widget-box placeholder"><div class="widget-header">CAM_05: OFFLINE</div><div class="static-noise">WAITING...</div></div>
    <div class="widget-box placeholder"><div class="widget-header">CAM_06: OFFLINE</div><div class="static-noise">WAITING...</div></div>
</div>
"""

# TERMINAL
CONTACT_CONTENT = """
<h1>Terminal Access</h1>
<div class='terminal-window'>
    <div id='history'><p>UkrGeekLife OS v20.0 (Odyssey Edition)...</p><p>Type 'help'.</p></div>
    <div class='input-line'><span class='prompt'>root@ukrgeek:~#</span><input type='text' id='cmd' autofocus autocomplete='off' spellcheck='false'></div>
</div>
"""

# OTHER PAGES
INDEX_CONTENT = """<h1>SYSTEM INDEX</h1><ul style="list-style:none;padding:0;"><li><strong>01. Engineer:</strong> Patriot.</li><li><strong>02. Hate:</strong> 500k dead.</li><li><strong>03. Vegetarian:</strong> 10+ years.</li><li><strong>04. Atheist:</strong> Logic only.</li><li><strong>05. Automation:</strong> Scripts.</li><li><strong>06. Python:</strong> Weapon.</li><li><strong>07. Void:</strong> Survivor.</li><li><strong>08. Zoo:</strong> My family.</li><li><strong>09. UX:</strong> Design.</li><li><strong>10. Open Source:</strong> Share.</li></ul>"""
PROJECTS_CONTENT = """<h1>ARSENAL</h1><ul><li><strong>Growing Box:</strong> Hydroponics.</li><li><strong>Lighting:</strong> Spectrum.</li><li><strong>Global Box:</strong> Architecture.</li></ul><h2>SOCIAL</h2><ul><li><strong>Volunteer Cats:</strong> Helping animals.</li></ul>"""
VIDEO_CONTENT = f"""<h1>/VIDEO_STREAM</h1><div class="video-wrapper"><iframe id="main-player" width="100%" height="450" src="https://www.youtube.com/embed/{VIDEO_ID}" frameborder="0" allowfullscreen></iframe></div>"""
BLOG_CONTENT = """<h1>/SYS/LOG</h1><div class="log-entry"><span class="highlight">[2025]</span> REBOOT.</div>"""
PODCAST_CONTENT = """<h1>/AUDIO</h1><div class="alert">Offline.</div>"""

# --- CSS ---
CSS_CODE = """
/* BASE */
body { background-color: #050505; color: #0F0; font-family: 'Courier New', monospace; margin: 0; padding: 0; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
#matrix-bg { position: fixed; top: 0; left: 0; z-index: -1; opacity: 0.15; }

/* HEADER - THE SPACE ODYSSEY STYLE */
header { 
    background: #000; border-bottom: 2px solid #333; 
    padding: 15px 20px; 
    display: flex; justify-content: space-between; align-items: center; 
    position: sticky; top: 0; z-index: 1000;
}

/* IDENTITY (THE TRIGGER) */
.identity-trigger { 
    font-size: 1.1rem; font-weight: bold; color: #FFF; 
    cursor: pointer; letter-spacing: 2px; text-transform: uppercase;
    border: 1px solid transparent; padding: 5px 10px; transition: 0.3s;
    display: flex; align-items: center; gap: 10px;
}
.identity-trigger:hover { 
    color: #F00; border-color: #F00; text-shadow: 0 0 10px #F00; 
    background: rgba(20, 0, 0, 0.8);
}
.hal-mini-eye {
    width: 15px; height: 15px; background: #500; border-radius: 50%; 
    box-shadow: 0 0 5px #F00; transition: 0.3s;
}
.identity-trigger:hover .hal-mini-eye { background: #F00; box-shadow: 0 0 15px #F00; }

/* SOCIAL ICONS (CLEAN RIGHT) */
.header-social { display: flex; gap: 10px; }
.social-icon { 
    color: #555; font-size: 1.1rem; text-decoration: none; 
    width: 35px; height: 35px; display: flex; align-items: center; justify-content: center; 
    border: 1px solid #222; background: #000; border-radius: 50%; transition: 0.3s;
}
.social-icon:hover { color: #FFF; border-color: #FFF; box-shadow: 0 0 10px #FFF; }

/* THE MONOLITH MENU (POP-UP) */
#monolith-menu {
    position: fixed; top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(0, 0, 0, 0.95); z-index: 2000;
    display: none; flex-direction: column; align-items: center; justify-content: center;
    backdrop-filter: blur(5px); opacity: 0; transition: opacity 0.5s;
}
#monolith-menu.active { display: flex; opacity: 1; }

.hal-9000-eye {
    width: 80px; height: 80px; background: #300; border-radius: 50%;
    border: 4px solid #888; box-shadow: 0 0 20px #F00;
    margin-bottom: 40px; cursor: pointer; transition: 0.3s;
}
.hal-9000-eye:hover { background: #F00; box-shadow: 0 0 50px #F00; transform: scale(1.1); }

.menu-links { display: flex; flex-direction: column; gap: 20px; text-align: center; }
.menu-links a { 
    color: #FFF; text-decoration: none; font-size: 1.5rem; letter-spacing: 3px; 
    border-bottom: 1px solid transparent; transition: 0.3s;
}
.menu-links a:hover { color: #F00; border-bottom: 1px solid #F00; letter-spacing: 5px; }
.close-menu { 
    margin-top: 50px; color: #555; cursor: pointer; font-size: 2rem; 
    border: 1px solid #333; padding: 10px 20px; border-radius: 5px; 
}
.close-menu:hover { color: #FFF; border-color: #FFF; }

/* CONTAINER & GRID */
.container { flex: 1; max-width: 1200px; margin: 20px auto; padding: 20px; border: 1px solid #333; background: rgba(0, 0, 0, 0.9); width: 95%; box-sizing: border-box; }
h1, h2 { border-bottom: 1px solid #0F0; color: #FFF; }
.alert { border: 1px solid #F00; color: #F88; padding: 10px; }

/* PHOTO GRID (3 COLS DESKTOP / 1 MOBILE) */
.photo-grid-container { display: grid; gap: 20px; margin-top: 20px; }
@media (min-width: 900px) { .photo-grid-container { grid-template-columns: repeat(3, 1fr); } }
@media (max-width: 899px) { .photo-grid-container { grid-template-columns: 1fr; } }
.widget-box { border: 1px solid #0F0; height: 400px; display: flex; flex-direction: column; background: #000; }
.widget-header { background: #002200; color: #0F0; padding: 5px; font-size: 0.8rem; border-bottom: 1px solid #0F0; }
.widget-content { flex: 1; overflow: hidden; position: relative; }
.widget-content iframe { width: 100%; height: 100%; border: none; }
.placeholder .widget-header { background: #222; color: #888; border-color: #555; }
.static-noise { flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; color: #444; background: repeating-linear-gradient(0deg, #111, #111 2px, #222 3px); }

/* TERMINAL */
.terminal-window { background: #111; border: 1px solid #0F0; padding: 15px; height: 50vh; overflow-y: auto; font-family: 'Courier New', monospace; font-size: 1rem; text-align: left; }
.input-line { display: flex; align-items: center; margin-top: 10px; }
.prompt { color: #0F0; margin-right: 10px; font-weight: bold; }
input#cmd { background: transparent; border: none; color: #FFF; font-family: 'Courier New', monospace; font-size: 1rem; flex-grow: 1; outline: none; width: 100%; display: block; }
#typewriter-content { visibility: hidden; }
.cursor::after { content: '█'; animation: blink 1s infinite; color: #0F0; margin-left: 5px; }
@keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }

/* FOOTER */
footer { border-top: 1px dashed #0F0; padding: 20px; text-align: center; font-size: 0.8rem; color: #555; margin-top: auto; }
.footer-links { margin-top: 10px; }
.footer-links a { color: #555; margin: 0 10px; font-size: 1.2rem; transition: 0.3s; }
.footer-links a:hover { color: #FFF; text-shadow: 0 0 5px #FFF; }
.video-wrapper { border: 2px solid #0F0; padding: 5px; background: #000; }
"""

# --- JS ---
JS_MAIN = """
const canvas = document.getElementById('matrix-bg');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth; canvas.height = window.innerHeight;
const chars = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ0123456789'.split('');
const fontSize = 14; const columns = canvas.width/fontSize;
const drops = []; for(let x=0; x<columns; x++) drops[x]=1;
function draw() {
    ctx.fillStyle = 'rgba(0, 0, 0, 0.05)'; ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = '#0F0'; ctx.font = fontSize + 'px monospace';
    for(let i=0; i<drops.length; i++) {
        const text = chars[Math.floor(Math.random()*chars.length)];
        ctx.fillText(text, i*fontSize, drops[i]*fontSize);
        if(drops[i]*fontSize > canvas.height && Math.random() > 0.975) drops[i]=0;
        drops[i]++;
    }
}
setInterval(draw, 33);
window.addEventListener('resize', () => { canvas.width = window.innerWidth; canvas.height = window.innerHeight; });

// MENU TOGGLE (THE SPACE ODYSSEY POP-UP)
function toggleMenu() { 
    const menu = document.getElementById('monolith-menu');
    if (menu.classList.contains('active')) {
        menu.classList.remove('active');
        setTimeout(() => menu.style.display = 'none', 500);
    } else {
        menu.style.display = 'flex';
        setTimeout(() => menu.classList.add('active'), 10);
    }
}

// EASTER EGG: HAL 9000
function talkHal() { alert("I'm sorry, Dave. I'm afraid I can't do that."); }

// EASTER EGG: KONAMI CODE
let konami = "";
document.addEventListener('keydown', (e) => {
    konami += e.key;
    if (konami.includes("ArrowUpArrowUpArrowDownArrowDownArrowLeftArrowRightArrowLeftArrowRightba")) {
        alert("ALIEN PROTOCOL INITIATED");
        document.body.style.filter = "invert(1)";
        konami = "";
    }
});

// TYPEWRITER & TERMINAL
document.addEventListener("DOMContentLoaded", function() {
    const element = document.getElementById('typewriter-content');
    if (element) {
        const text = element.innerHTML;
        element.innerHTML = "";
        element.classList.add("cursor");
        element.style.visibility = "visible";
        let i = 0;
        function type() {
            if (i < text.length) {
                if (text.charAt(i) === '<') {
                    let tag = "";
                    while (text.charAt(i) !== '>' && i < text.length) { tag += text.charAt(i); i++; }
                    tag += '>'; i++; element.innerHTML += tag;
                } else { element.innerHTML += text.charAt(i); i++; }
                setTimeout(type, 1);
            }
        }
        type();
    }
    
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
                    case "help": res = "COMMANDS: [about] [photo] [video] [blog] [slava]"; break;
                    case "about": window.location='about.html'; break;
                    case "photo": window.location='photo.html'; break;
                    case "video": window.location='video.html'; break;
                    case "blog": window.location='blog.html'; break;
                    case "slava": res = "<span style='color:yellow'>GEROYAM SLAVA!</span>"; break;
                    case "clear": history.innerHTML = ""; break;
                    case "": res = ""; break;
                    default: res = `<span style='color:red'>bash: ${rawCmd}: command not found</span>`;
                }
                if(cmd !== "clear" && res !== "") history.innerHTML += `<div style='color:#DDD'>${res}</div>`;
                input.value = "";
                document.querySelector('.terminal-window').scrollTop = document.querySelector('.terminal-window').scrollHeight;
            }
        });
    }
});
"""

# --- TEMPLATES ---
BASE_HTML = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{title}</title>
<link rel="stylesheet" href="css/style.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</head><body><canvas id="matrix-bg"></canvas>

<div id="monolith-menu">
    <div class="hal-9000-eye" onclick="talkHal()"></div>
    <div class="menu-links">
        <a href="index.html">/HOME_BASE</a>
        <a href="about.html">/IDENTITY_CORE</a>
        <a href="projects.html">/ARSENAL_WEAPONS</a>
        <a href="photo.html">/VISUAL_FEED</a>
        <a href="video.html">/VIDEO_STREAM</a>
        <a href="blog.html">/SYSTEM_LOGS</a>
        <a href="contact.html">/COMMAND_LINE</a>
    </div>
    <div class="close-menu" onclick="toggleMenu()">[ CLOSE CONNECTION ]</div>
</div>

<header>
    <div class="identity-trigger" onclick="toggleMenu()">
        <div class="hal-mini-eye"></div>
        <span>{id}</span>
    </div>
    <div class="header-social">
        <a href="{yt}" class="social-icon"><i class="fab fa-youtube"></i></a>
        <a href="{im}" class="social-icon"><i class="fab fa-instagram"></i></a>
        <a href="{fb}" class="social-icon"><i class="fab fa-facebook"></i></a>
        <a href="{li}" class="social-icon"><i class="fab fa-linkedin"></i></a>
    </div>
</header>

<main class="container"><div id="typewriter-content">{content}</div></main>

<footer>
    <div style="margin-bottom:10px;">[ SYSTEM RESOURCES: 4 CATS | 2 DOGS | 1 RAT | 1 TURTLE ]</div>
    <div class="footer-links">
        <a href="{x}"><i class="fab fa-twitter"></i></a><a href="{tu}"><i class="fab fa-tumblr"></i></a>
        <a href="{tw}"><i class="fab fa-twitch"></i></a><a href="{gh}"><i class="fab fa-github"></i></a>
        <a href="{sp}"><i class="fab fa-spotify"></i></a>
        <a href="{ip}"><i class="fas fa-camera"></i></a>
    </div>
    <div style="margin-top:10px;opacity:0.5;font-size:0.7rem;">© 2025 {id} | NO FORGIVENESS</div>
</footer>
<script src="js/main.js"></script>
</body></html>"""

# --- EXECUTION ---
print("--- WRITING FILES ---")
os.makedirs("css", exist_ok=True)
os.makedirs("js", exist_ok=True)
with open("css/style.css", "w", encoding="utf-8") as f: f.write(CSS_CODE)
with open("js/main.js", "w", encoding="utf-8") as f: f.write(JS_MAIN)

pages = {
    "index.html": INDEX_CONTENT, "about.html": BASE_ABOUT, "projects.html": PROJECTS_CONTENT,
    "photo.html": PHOTO_CONTENT, "video.html": VIDEO_CONTENT, "blog.html": BLOG_CONTENT,
    "podcast.html": PODCAST_CONTENT, "contact.html": CONTACT_CONTENT
}

for fname, content in pages.items():
    html = BASE_HTML.format(
        title=f"{fname} | {IDENTITY}", content=content, id=IDENTITY,
        yt=LINKS['YOUTUBE'], im=LINKS['INSTA_MAIN'], fb=LINKS['FACEBOOK'], li=LINKS['LINKEDIN'],
        x=LINKS['X'], tu=LINKS['TUMBLR'], tw=LINKS['TWITCH'], gh=LINKS['GITHUB'], sp=LINKS['SPOTIFY'], ip=LINKS['INSTA_PHOTO']
    )
    with open(fname, "w", encoding="utf-8") as f: f.write(html)
    print(f"✅ {fname}")

print("--- DEPLOYING ---")
time.sleep(1)
run("git add .")
run(f'git commit -m "UkrGeekLife | Space Odyssey Menu | {time.strftime("%H:%M:%S")}"')
run("git push origin master")
print(">>> DONE.")