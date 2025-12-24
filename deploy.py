# -*- coding: utf-8 -*-
import os, sys, subprocess, time, random

# --- CONFIG ---
ID_PROJECT = "UkrGeekLife"
ID_NAME = "Andrii Ivas"
IDENTITY = f"{ID_PROJECT} | {ID_NAME}"
DONATE_LINK = "https://send.monobank.ua/jar/YOUR_JAR_ID" 

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
    "SPOTIFY_LINK": "https://open.spotify.com/playlist/1BG0k1dDJN14PczoyvSD6T?si=JVz8SvIGQHeba0XCCsulzQ",
    "SPOTIFY_EMBED_SRC": "https://open.spotify.com/embed/playlist/1BG0k1dDJN14PczoyvSD6T?utm_source=generator&theme=0"
}
VIDEO_ID = "-h7ygd0mp7c"

def run(cmd):
    try:
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"✅ Executed: {cmd}")
    except: pass

print("--- READING DATA ---")
try:
    with open("about_me.txt", "r", encoding="utf-8") as f: BASE_ABOUT = f.read()
except: BASE_ABOUT = "<h1>ERROR</h1><p>File missing.</p>"

# --- HTML PARTS ---

CODE_LINKS = f"""
<div class="code-block-links">
    <p class="comment">// SOCIAL_NETWORKS_ARRAY</p>
    <div class="code-line"><span class="var">const</span> <span class="name">uplink</span> = {'{'}</div>
    <a href="{LINKS['YOUTUBE']}" target="_blank" class="code-item">&nbsp;&nbsp;YouTube: <span class="str">"Subscribe"</span>,</a>
    <a href="{LINKS['INSTA_MAIN']}" target="_blank" class="code-item">&nbsp;&nbsp;Instagram_Life: <span class="str">"Follow"</span>,</a>
    <a href="{LINKS['INSTA_PHOTO']}" target="_blank" class="code-item">&nbsp;&nbsp;Instagram_Art: <span class="str">"View"</span>,</a>
    <a href="{LINKS['LINKEDIN']}" target="_blank" class="code-item">&nbsp;&nbsp;LinkedIn: <span class="str">"Connect"</span>,</a>
    <a href="{LINKS['GITHUB']}" target="_blank" class="code-item">&nbsp;&nbsp;GitHub: <span class="str">"Fork"</span></a>
    <div class="code-line">{'}'};</div>
</div>
"""

SPOTIFY_SECTION = f"""
<div style="margin-top: 50px; padding-top: 20px; border-top: 1px dashed #0F0;">
    <h3 style="color: #0F0; font-family: monospace;">public void PlayMusic() {'{'}</h3>
    <iframe style="border-radius:12px; margin-top:10px;" src="{LINKS['SPOTIFY_EMBED_SRC']}" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
    <h3 style="color: #0F0; font-family: monospace;">{'}'}</h3>
</div>
"""
ABOUT_CONTENT = BASE_ABOUT + CODE_LINKS + SPOTIFY_SECTION

WIDGET_CODE = """<div class="widget-box"><div class="widget-header">var img = new Image();</div><div class="widget-content"><iframe src="https://snapwidget.com/embed/1115084" class="snapwidget-widget" allowtransparency="true" frameborder="0" scrolling="no" style="border:none; overflow:hidden; width:100%; height:100%" title="Posts from Instagram"></iframe></div></div>"""
PHOTO_CONTENT = f"""<h1>/GALLERY_GRID</h1><p>Visual Database initialized...</p><div class="photo-grid-container">{WIDGET_CODE*8}</div>"""

CONTACT_CONTENT = """<h1>Terminal Access</h1><div class='terminal-window'><div id='history'><p>UkrGeekLife OS v27.0 (UA Matrix)...</p><p>Type 'help'.</p></div><div class='input-line'><span class='prompt'>root@ukrgeek:~#</span><input type='text' id='cmd' autofocus autocomplete='off' spellcheck='false'></div></div>"""

INDEX_CONTENT = """<h1>SYSTEM INDEX</h1><ul style="list-style:none;padding:0;"><li><strong>[01] Engineer:</strong> Patriot.</li><li><strong>[02] Hate:</strong> 500k dead.</li><li><strong>[03] Vegetarian:</strong> 10+ years.</li><li><strong>[04] Atheist:</strong> Logic only.</li><li><strong>[05] Automation:</strong> Scripts.</li><li><strong>[06] Python:</strong> Weapon.</li><li><strong>[07] Void:</strong> Survivor.</li><li><strong>[08] Zoo:</strong> My family.</li><li><strong>[09] UX:</strong> Design.</li><li><strong>[10] Open Source:</strong> Share.</li></ul>"""
PROJECTS_CONTENT = """<h1>ARSENAL</h1><ul><li><strong>Growing Box:</strong> Hydroponics.</li><li><strong>Lighting:</strong> Spectrum.</li><li><strong>Global Box:</strong> Architecture.</li></ul><h2>SOCIAL</h2><ul><li><strong>Volunteer Cats:</strong> Helping animals.</li></ul>"""
VIDEO_CONTENT = f"""<h1>/VIDEO_STREAM</h1><div class="video-wrapper"><iframe id="main-player" width="100%" height="450" src="https://www.youtube.com/embed/{VIDEO_ID}" frameborder="0" allowfullscreen></iframe></div>"""
BLOG_CONTENT = """<h1>/SYS/LOG</h1><div class="log-entry"><span class="highlight">[2025]</span> REBOOT.</div>"""
PODCAST_CONTENT = """<h1>/AUDIO</h1><div class="alert">Offline.</div>"""

# --- CSS ---
CSS_CODE = """
body { background-color: #050505; color: #0F0; font-family: 'Courier New', monospace; margin: 0; padding: 0; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; }
#matrix-bg { position: fixed; top: 0; left: 0; z-index: -1; opacity: 0.15; }
#preloader { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: #000; z-index: 9999; display: flex; align-items: center; justify-content: center; flex-direction: column; color: #0F0; font-size: 1.2rem; font-family: monospace; transition: opacity 1s ease-out; }
.hidden { opacity: 0; pointer-events: none; }
header { background: #000; border-bottom: 2px solid #333; padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; position: sticky; top: 0; z-index: 1000; }
.identity-wrapper { display: flex; align-items: center; gap: 10px; font-size: 1.1rem; font-weight: bold; color: #FFF; text-transform: uppercase; letter-spacing: 2px; }
.id-project { cursor: pointer; transition: 0.3s; padding: 5px; } .id-project:hover { color: #F00; text-shadow: 0 0 10px #F00; }
.id-name { text-decoration: none; color: #FFF; padding: 5px; transition: 0.3s; } .id-name:hover { color: #0F0; text-shadow: 0 0 10px #0F0; }
.alien-tracker { width: 40px; height: 40px; border: 2px solid #0F0; border-radius: 50%; position: relative; display: flex; align-items: center; justify-content: center; cursor: pointer; background: #001100; margin-right: 15px; transition: 0.2s; }
.alien-tracker:hover { box-shadow: 0 0 15px #0F0; border-color: #FFF; }
.tracker-blip { width: 4px; height: 15px; background: #0F0; position: absolute; top: 2px; left: 18px; transform-origin: 2px 18px; box-shadow: 0 0 5px #0F0; }
.tracker-text { position: absolute; bottom: -20px; left: -10px; width: 60px; font-size: 0.6rem; color: #0F0; text-align: center; display: none; }
.alien-tracker:hover .tracker-text { display: block; }
.header-right { display: flex; align-items: center; }
.social-icon { color: #555; font-size: 1.1rem; text-decoration: none; margin-left: 10px; transition: 0.3s; } .social-icon:hover { color: #FFF; text-shadow: 0 0 5px #FFF; }
#monolith-menu { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0, 0, 0, 0.95); z-index: 2000; display: none; flex-direction: column; align-items: center; justify-content: center; backdrop-filter: blur(5px); opacity: 0; transition: opacity 0.5s; }
#monolith-menu.active { display: flex; opacity: 1; }
.menu-links a { color: #FFF; text-decoration: none; font-size: 1.5rem; letter-spacing: 3px; border-bottom: 1px solid transparent; transition: 0.3s; display: block; margin: 10px 0; text-align: center; }
.menu-links a:hover { color: #F00; border-bottom: 1px solid #F00; }
.close-menu { margin-top: 50px; color: #555; cursor: pointer; font-size: 2rem; border: 1px solid #333; padding: 10px 20px; }
.close-menu:hover { color: #FFF; border-color: #FFF; }
.container { flex: 1; max-width: 1400px; margin: 20px auto; padding: 20px; border: 1px solid #333; background: rgba(0, 0, 0, 0.9); width: 95%; box-sizing: border-box; }
h1 { border-bottom: 2px solid #0F0; color: #FFF; padding-bottom: 5px; margin-bottom: 20px; }
.code-block-links { background: #0a0a0a; border-left: 3px solid #0F0; padding: 15px; font-family: 'Consolas', monospace; margin-top: 20px; }
.comment { color: #555; font-style: italic; } .var { color: #d7ba7d; } .name { color: #9cdcfe; } .str { color: #ce9178; }
.code-item { display: block; text-decoration: none; color: #d4d4d4; padding: 2px 0; transition: 0.2s; } .code-item:hover { background: #222; color: #FFF; }
.photo-grid-container { display: grid; gap: 15px; margin-top: 20px; }
@media (min-width: 1200px) { .photo-grid-container { grid-template-columns: repeat(4, 1fr); } }
@media (max-width: 1199px) and (min-width: 768px) { .photo-grid-container { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 767px) { .photo-grid-container { grid-template-columns: 1fr; } }
.widget-box { border: 1px solid #0F0; background: #000; display: flex; flex-direction: column; width: 100%; aspect-ratio: 1 / 1; overflow: hidden; }
.widget-header { background: #002200; color: #0F0; padding: 5px; font-size: 0.8rem; border-bottom: 1px solid #0F0; flex-shrink: 0; }
.widget-content { flex: 1; overflow: hidden; position: relative; }
.widget-content iframe { width: 100%; height: 100%; border: none; }
.terminal-window { background: #111; border: 1px solid #0F0; padding: 15px; height: 50vh; overflow-y: auto; font-family: 'Courier New', monospace; font-size: 1rem; text-align: left; }
.input-line { display: flex; align-items: center; margin-top: 5px; }
.prompt { color: #0F0; margin-right: 10px; font-weight: bold; white-space: nowrap; flex-shrink: 0; }
input#cmd { background: transparent; border: none; color: #FFF; font-family: 'Courier New', monospace; font-size: 1rem; flex-grow: 1; outline: none; padding: 0; margin: 0; }
footer { border-top: 1px dashed #0F0; padding: 20px; text-align: center; font-size: 0.8rem; color: #555; margin-top: auto; }
.footer-links a { color: #555; margin: 0 10px; font-size: 1.2rem; transition: 0.3s; } .footer-links a:hover { color: #FFF; text-shadow: 0 0 5px #FFF; }
"""

# --- JS ---
JS_MAIN = """
// 1. UA MATRIX
const canvas = document.getElementById('matrix-bg');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth; canvas.height = window.innerHeight;
const chars = 'ҐЄЇИІЙЬ'.split('');
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

// 2. BOOT LOADER
window.addEventListener('load', () => {
    const log = document.getElementById('boot-log');
    const msgs = ["> INIT_UKR_KERNEL...", "> CHECKING_INTEGRITY...", "> MOUNTING_VOLUMES...", "> ACCESS_GRANTED."];
    let i = 0;
    const interval = setInterval(() => {
        if(i < msgs.length) { log.innerHTML += msgs[i] + "<br>"; i++; } 
        else { clearInterval(interval); setTimeout(() => { document.getElementById('preloader').classList.add('hidden'); }, 500); }
    }, 500);
});

// 3. MENU
function toggleMenu() { 
    const menu = document.getElementById('monolith-menu');
    if (menu.classList.contains('active')) { menu.classList.remove('active'); setTimeout(() => menu.style.display = 'none', 500); } 
    else { menu.style.display = 'flex'; setTimeout(() => menu.classList.add('active'), 10); }
}

// 4. ALIEN TRACKER
document.addEventListener('mousemove', (e) => {
    const tracker = document.querySelector('.alien-tracker');
    const blip = document.querySelector('.tracker-blip');
    if(tracker && blip) {
        const rect = tracker.getBoundingClientRect();
        const x = rect.left + rect.width / 2;
        const y = rect.top + rect.height / 2;
        const rad = Math.atan2(e.clientX - x, e.clientY - y);
        const rot = (rad * (180 / Math.PI) * -1) + 180;
        blip.style.transform = `rotate(${rot}deg)`;
    }
});

// 5. TERMINAL
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
                    case "help": res = "COMMANDS: [about] [photo] [video] [blog] [slava]"; break;
                    case "about": window.location='about.html'; break;
                    case "photo": window.location='photo.html'; break;
                    case "video": window.location='video.html'; break;
                    case "blog": window.location='blog.html'; break;
                    case "slava": res = "<span style='color:yellow'>GEROYAM SLAVA!</span>"; break;
                    case "clear": history.innerHTML = ""; break;
                    default: res = `<span style='color:red'>bash: ${rawCmd}: command not found</span>`;
                }
                if(cmd !== "clear") history.innerHTML += `<div style='color:#DDD'>${res}</div>`;
                input.value = "";
                document.querySelector('.terminal-window').scrollTop = document.querySelector('.terminal-window').scrollHeight;
            }
        });
    }
});
"""

# --- BUILD ---
BASE_HTML = f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{{title}}</title><link rel="stylesheet" href="css/style.css"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"></head><body><canvas id="matrix-bg"></canvas>
<div id="preloader"><div id="boot-log"></div><div style="margin-top:20px; animation: blink 1s infinite;">_</div></div>
<div id="monolith-menu">
    <div class="menu-links">
        <a href="index.html">[0] /HOME</a><a href="about.html">[1] /IDENTITY</a><a href="projects.html">[2] /ARSENAL</a>
        <a href="photo.html">[3] /PHOTO</a><a href="video.html">[4] /VIDEO</a><a href="blog.html">[5] /BLOG</a><a href="contact.html">[6] /CMD</a>
    </div>
    <div class="close-menu" onclick="toggleMenu()">// CLOSE</div>
</div>
<header>
    <div class="identity-wrapper"><div class="id-project" onclick="toggleMenu()">[{ID_PROJECT}]</div><span class="id-divider">::</span><a href="index.html" class="id-name">{ID_NAME}</a></div>
    <div class="header-right">
        <a href="{DONATE_LINK}" target="_blank" class="alien-tracker" title="Support"><div class="tracker-blip"></div><div class="tracker-text">// DONATE</div></a>
        <div class="header-social"><a href="{LINKS['YOUTUBE']}" class="social-icon"><i class="fab fa-youtube"></i></a><a href="{LINKS['INSTA_MAIN']}" class="social-icon"><i class="fab fa-instagram"></i></a><a href="{LINKS['FACEBOOK']}" class="social-icon"><i class="fab fa-facebook"></i></a><a href="{LINKS['LINKEDIN']}" class="social-icon"><i class="fab fa-linkedin"></i></a></div>
    </div>
</header>
<main class="container">{{content}}</main>
<footer>
    <div style="margin-bottom:10px;">[ SYS: 4_CATS | 2_DOGS | 1_RAT | 1_TURTLE ]</div>
    <div class="footer-links"><a href="{LINKS['X']}"><i class="fab fa-twitter"></i></a><a href="{LINKS['TUMBLR']}"><i class="fab fa-tumblr"></i></a><a href="{LINKS['TWITCH']}"><i class="fab fa-twitch"></i></a><a href="{LINKS['GITHUB']}"><i class="fab fa-github"></i></a><a href="{LINKS['SPOTIFY_LINK']}"><i class="fab fa-spotify"></i></a><a href="{LINKS['INSTA_PHOTO']}"><i class="fas fa-camera"></i></a></div>
    <div style="margin-top:10px;opacity:0.5;font-size:0.7rem;">© 2025 {IDENTITY} | NO FORGIVENESS</div>
</footer>
<script src="js/main.js"></script></body></html>"""

print("--- WRITING FILES ---")
os.makedirs("css", exist_ok=True)
os.makedirs("js", exist_ok=True)
with open("css/style.css", "w", encoding="utf-8") as f: f.write(CSS_CODE)
with open("js/main.js", "w", encoding="utf-8") as f: f.write(JS_MAIN)

pages = {"index.html": INDEX_CONTENT, "about.html": ABOUT_CONTENT, "projects.html": PROJECTS_CONTENT, "photo.html": PHOTO_CONTENT, "video.html": VIDEO_CONTENT, "blog.html": BLOG_CONTENT, "podcast.html": PODCAST_CONTENT, "contact.html": CONTACT_CONTENT}
for f, c in pages.items():
    with open(f, "w", encoding="utf-8") as fl: fl.write(BASE_HTML.format(title=f"{f} | {IDENTITY}", content=c))
    print(f"✅ {f}")

print("--- DEPLOYING ---")
time.sleep(1)
run("git add .")
run(f'git commit -m "UkrGeekLife | UA Matrix & Alien Loader | {time.strftime("%H:%M:%S")}"')
run("git push origin master")
print(">>> DONE.")