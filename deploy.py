# -*- coding: utf-8 -*-
import os
import sys
import subprocess
import time
import random

# --- CONFIGURATION ---
IDENTITY = "UkrGeekLife | Andrii Ivas"
# FORCE UTF-8 OUTPUT
sys.stdout.reconfigure(encoding='utf-8')

# SOCIAL LINKS DATABASE
LINKS = {
    "YOUTUBE": "https://www.youtube.com/@UkrGeekLife",
    "INSTA_MAIN": "https://www.instagram.com/ivas_andrii/",
    "INSTA_PHOTO": "https://www.instagram.com/andrii_photographer/",
    "FACEBOOK": "#", 
    "LINKEDIN": "https://www.linkedin.com/in/ivas-andre/", 
    "X": "https://x.com/Andrii_Ivas",
    "TUMBLR": "https://www.tumblr.com/andre-ivas",
    "TWITCH": "https://www.twitch.tv/ivas_andre",
    "GITHUB": "https://github.com/ivas-andre",
    "SPOTIFY": "https://open.spotify.com/user/0" 
}

# VIDEO ID
CURRENT_VIDEO_ID = "-h7ygd0mp7c"

def run(cmd):
    try:
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"✅ Executed: {cmd}")
    except subprocess.CalledProcessError:
        if "commit" in cmd:
            print(f"ℹ️ Note: No changes to commit (Git is up to date).")
        else:
            print(f"⚠️ Warning: Error running {cmd}")

# 1. READ CONTENT
print("--- READING about_me.txt ---")
try:
    with open("about_me.txt", "r", encoding="utf-8") as f:
        ABOUT_CONTENT = f.read()
except FileNotFoundError:
    print("❌ ERROR: about_me.txt missing. Using backup.")
    ABOUT_CONTENT = "<h1>ERROR</h1><p>File missing.</p>"

# 2. CONTENT DEFINITIONS

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
<p>I don't just write code. I build reality. Більшість моїх проектів будуть <strong>Open Source</strong> і безкоштовними.</p>
<h2>1. ENGINEERING & HARDWARE</h2>
<ul>
    <li><strong>Growing Box Building:</strong> Повна автоматизація гідропоніки. Свіжа їжа вдома.</li>
    <li><strong>Lighting Building:</strong> DIY Smart Light. Керування спектром.</li>
    <li><strong>Global Box:</strong> Модульне будівництво. My architecture vision.</li>
</ul>
<h2>2. SOCIAL & BIO SECTOR</h2>
<ul>
    <li><strong>Volunteer Cats Helping:</strong> Соціальне волонтерство.</li>
    <li><strong>Social Voluntar:</strong> Допомога тим, хто реально потребує.</li>
</ul>
<h2>3. PHOTO STREAM (EVIDENCE)</h2>
<div class="photo-grid">
    <div class="photo-placeholder">[ IMG_001.JPG: CAT_SERVER_RACK ]</div>
    <div class="photo-placeholder">[ IMG_002.JPG: HYDROPONICS_V1 ]</div>
    <div class="photo-placeholder">[ IMG_003.JPG: CYBER_DECK_BUILD ]</div>
</div>
<div class="alert"><strong>STATUS:</strong> Most repos are currently private. Preparing for public release.</div>
"""

VIDEO_CONTENT = f"""
<h1>/VAR/VIDEO/STREAM</h1>
<p>Broadcasts from the bunker. Engineering, automation, and life.</p>
<div class="video-wrapper">
    <iframe id="main-player" width="100%" height="450" src="https://www.youtube.com/embed/{CURRENT_VIDEO_ID}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
<div class="playlist-controls">
    <h3>SELECT FREQUENCY:</h3>
    <button onclick="changeVideo('{CURRENT_VIDEO_ID}')">[ LIVE STREAM ]</button>
    <button onclick="changeVideo('LXb3EKWsInQ')">[ AUTOMATION ]</button>
    <button onclick="changeVideo('5qap5aO4i9A')">[ LOFI CODE ]</button>
</div>
<p style="margin-top:20px;">Filters: <span class="highlight">ALL</span> | <span style="color:#555">HARDWARE</span></p>
"""

BLOG_CONTENT = """
<h1>/VAR/LOG/SYS_JOURNAL</h1>
<p>Personal logs. Thoughts. Errors. Fixes.</p>
<div class="log-entry">
    <div class="log-header"><span class="highlight">[2025-01-15]</span> :: SYSTEM_REBOOT</div>
    <p>Restarted the core. New philosophy loaded. No more manual deployment.</p>
</div>
<div class="log-entry">
    <div class="log-header"><span class="highlight">[2024-12-20]</span> :: DEPRESSION_DUMP</div>
    <p>Memory overflow. Clearing cache. Sometimes the hardest code to debug is your own brain.</p>
</div>
"""

PODCAST_CONTENT = """
<h1>/DEV/AUDIO/OUTPUT</h1>
<p>Voice logs. Rants. Unfiltered audio streams.</p>
<div class="audio-list">
    <div class="audio-item">
        <button class="play-btn">▶ PLAY</button>
        <span class="track-name">EP_01: WHY_PYTHON_IS_KING.mp3</span>
        <span class="track-time">[12:04]</span>
    </div>
    <div class="audio-item">
        <button class="play-btn">▶ PLAY</button>
        <span class="track-name">EP_02: HATING_RUSSIANS_AS_A_SERVICE.mp3</span>
        <span class="track-time">[45:00]</span>
    </div>
</div>
<div class="alert">Audio modules currently offline. Connecting to server...</div>
"""

# 3. CSS (COMPLETE)
CSS_CODE = """
/* BASE */
body { background-color: #050505; color: #0F0; font-family: 'Courier New', monospace; margin: 0; padding: 0; min-height: 100vh; display: flex; flex-direction: column; overflow-x: hidden; transition: filter 0.3s ease; }
#matrix-bg { position: fixed; top: 0; left: 0; z-index: -1; opacity: 0.15; pointer-events: none; }

/* HEADER */
header { background: #1a1a1a; border-bottom: 1px solid #333; padding: 10px 15px; display: flex; justify-content: space-between; align-items: center; position: sticky; top: 0; z-index: 1000; box-shadow: 0 5px 15px rgba(0,0,0,0.5); }
.header-left { display: flex; align-items: center; gap: 15px; }
.window-controls { display: flex; gap: 8px; }
.dot { width: 12px; height: 12px; border-radius: 50%; cursor: pointer; transition: 0.2s; }
.dot.red { background: #ff5f56; } .dot.red:hover { box-shadow: 0 0 10px #f00; }
.dot.yellow { background: #ffbd2e; } .dot.yellow:hover { box-shadow: 0 0 10px #ff0; }
.dot.green { background: #27c93f; } .dot.green:hover { box-shadow: 0 0 10px #0f0; }
.window-title { color: #888; font-size: 0.9rem; font-weight: bold; }

/* HEADER SOCIAL ICONS */
.header-social { display: flex; gap: 15px; align-items: center; }
.social-icon { color: #888; font-size: 1.2rem; transition: 0.3s; text-decoration: none; display: flex; align-items: center; justify-content: center; width: 30px; height: 30px; border-radius: 4px; background: rgba(0,0,0,0.3); border: 1px solid #333; }
.social-icon:hover { color: #0F0; border-color: #0F0; box-shadow: 0 0 8px #0F0; transform: translateY(-2px); }

/* BURGER */
.burger-menu { cursor: pointer; display: flex; flex-direction: column; gap: 4px; z-index: 1001; margin-left: 15px; }
.line { width: 25px; height: 3px; background: #0F0; transition: 0.3s; }
.burger-menu.active .line:nth-child(1) { transform: rotate(45deg) translate(5px, 5px); background: #F00; }
.burger-menu.active .line:nth-child(2) { opacity: 0; }
.burger-menu.active .line:nth-child(3) { transform: rotate(-45deg) translate(5px, -5px); background: #F00; }

/* NAV */
nav { position: fixed; top: 50px; right: -100%; width: 250px; height: 100vh; background: rgba(0, 10, 0, 0.95); border-left: 1px solid #0F0; display: flex; flex-direction: column; padding-top: 20px; transition: 0.4s cubic-bezier(0.4, 0, 0.2, 1); box-shadow: -10px 0 30px rgba(0,0,0,0.8); }
nav.active { right: 0; }
nav a { color: #FFF; text-decoration: none; padding: 15px 20px; border-bottom: 1px solid #030; font-size: 1.1rem; transition: 0.2s; }
nav a:hover { background: #002200; padding-left: 30px; color: #0F0; }
@media(min-width: 900px) { nav { position: static; width: auto; height: auto; background: transparent; border: none; flex-direction: row; box-shadow: none; padding-top: 0; } nav a { border: none; padding: 0 10px; font-size: 0.9rem; } nav a:hover { background: transparent; padding-left: 10px; text-shadow: 0 0 5px #0F0; } .burger-menu { display: none; } }
@media(max-width: 899px) { .window-title { display: none; } .header-social { display: none; } }

/* MAIN CONTENT */
.container { flex: 1; max-width: 900px; margin: 30px auto; padding: 20px; border: 1px solid #333; background: rgba(0, 0, 0, 0.85); box-shadow: 0 0 20px rgba(0, 255, 0, 0.05); }
h1 { border-bottom: 2px solid #0F0; padding-bottom: 5px; color: #FFF; }
.red-alert { color: #FF3333; text-shadow: 0 0 5px #F00; }
.alert { border: 1px solid #F00; background: rgba(50,0,0,0.2); padding: 10px; color: #F88; }
.highlight { color: #FFF; font-weight: bold; background: #003300; padding: 2px 5px; }

/* MODULE STYLES */
.video-wrapper { border: 2px solid #0F0; padding: 5px; background: #000; box-shadow: 0 0 15px rgba(0, 255, 0, 0.2); }
.playlist-controls { margin-top: 20px; display: flex; flex-wrap: wrap; gap: 10px; }
.playlist-controls button { background: #111; border: 1px solid #0F0; color: #0F0; padding: 10px; font-family: 'Courier New', monospace; cursor: pointer; transition: 0.3s; flex-grow: 1; }
.playlist-controls button:hover { background: #0F0; color: #000; font-weight: bold; }
.photo-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 10px; margin-top: 20px; }
.photo-placeholder { border: 1px dashed #555; height: 150px; display: flex; align-items: center; justify-content: center; color: #555; font-size: 0.8rem; background: rgba(255,255,255,0.05); }
.log-entry { border-left: 2px solid #0F0; padding-left: 15px; margin-bottom: 20px; }
.log-header { font-weight: bold; margin-bottom: 5px; color: #AAA; }
.audio-item { border: 1px solid #333; padding: 10px; margin-bottom: 10px; display: flex; align-items: center; background: #0a0a0a; }
.play-btn { background: #0F0; color: #000; border: none; padding: 5px 10px; font-weight: bold; cursor: pointer; margin-right: 15px; }

/* FOOTER */
footer { background: #000; border-top: 1px dashed #0F0; padding: 20px; text-align: center; font-size: 0.8rem; color: #555; position: relative; overflow: hidden; margin-top: auto; }
.zoo-list { color: #006600; font-size: 0.9rem; margin-bottom: 10px; cursor: help; border-bottom: 1px solid #111; padding-bottom: 10px; display: inline-block; }
.zoo-list:hover { color: #0F0; text-shadow: 0 0 5px #0F0; }
.footer-bottom { display: flex; justify-content: center; gap: 15px; align-items: center; flex-wrap: wrap; margin-top: 10px; }
.footer-icon-link { color: #555; font-size: 1.2rem; transition: 0.3s; }
.footer-icon-link:hover { color: #FFF; text-shadow: 0 0 5px #FFF; }
.ip-trace { font-family: monospace; color: #333; }
.uptime { color: #333; font-family: monospace; }
.shutdown-overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: #000; color: #F00; display: flex; flex-direction: column; justify-content: center; align-items: center; z-index: 9999; display: none; }
#preloader { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: #000; z-index: 9999; display: flex; align-items: center; justify-content: center; color: #0F0; font-size: 1.5rem; transition: opacity 1s; }
.loaded { opacity: 0; pointer-events: none; }
"""

# 4. JS (COMPLETE)
JS_MAIN = """
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
    alert("System minimized. Click OK.");
    document.querySelector('.container').style.opacity = '1';
}
function maximizeSystem() {
    if (!document.fullscreenElement) { document.documentElement.requestFullscreen(); } 
    else { if (document.exitFullscreen) { document.exitFullscreen(); } }
}
function toggleMenu() {
    const nav = document.querySelector('nav');
    const burger = document.querySelector('.burger-menu');
    nav.classList.toggle('active');
    burger.classList.toggle('active');
}
function changeVideo(id) {
    const player = document.getElementById('main-player');
    if(player) { player.src = "https://www.youtube.com/embed/" + id + "?autoplay=1"; }
}
document.addEventListener("DOMContentLoaded", function() {
    const ips = ["192.168.0.1 (Local)", "10.0.0.13 (Proxy)", "Trace Failed...", "SBU_Node_7"];
    document.getElementById('fake-ip').innerText = "Route: " + ips[Math.floor(Math.random() * ips.length)];
    let seconds = 0;
    setInterval(() => { seconds++; document.getElementById('uptime-counter').innerText = "UPTIME: " + seconds + "s"; }, 1000);
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
                        case "help": res = "COMMANDS: [about] [projects] [video] [blog] [email] [slava] [kill]"; break;
                        case "about": res = "Redirecting to Identity..."; setTimeout(()=>window.location='about.html', 1000); break;
                        case "projects": res = "Accessing Arsenal..."; setTimeout(()=>window.location='projects.html', 1000); break;
                        case "video": res = "Loading Stream..."; setTimeout(()=>window.location='video.html', 1000); break;
                        case "blog": res = "Reading Logs..."; setTimeout(()=>window.location='blog.html', 1000); break;
                        case "slava": res = "<span style='color:yellow; font-weight:bold;'>GEROYAM SLAVA! 🇺🇦</span>"; break;
                        case "russia": res = "<span style='color:red; font-weight:bold; font-size: 1.5em;'>FATAL ERROR: BIOWASTE DETECTED. PURGING...</span>"; break;
                        case "kill": killSystem(); break;
                        case "clear": history.innerHTML = ""; break;
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

# --- TEMPLATES ---

HEADER_HTML = f"""
<header>
    <div class="header-left">
        <div class="window-controls">
            <div class="dot red" onclick="killSystem()" title="Close Connection"></div>
            <div class="dot yellow" onclick="minimizeSystem()" title="Minimize"></div>
            <div class="dot green" onclick="maximizeSystem()" title="Fullscreen"></div>
        </div>
        <div class="window-title">root@ukrgeek:~</div>
    </div>
    <div class="header-social">
        <a href="{LINKS['YOUTUBE']}" target="_blank" class="social-icon" title="YouTube"><i class="fab fa-youtube"></i></a>
        <a href="{LINKS['INSTA_MAIN']}" target="_blank" class="social-icon" title="Instagram (Main)"><i class="fab fa-instagram"></i></a>
        <a href="{LINKS['FACEBOOK']}" target="_blank" class="social-icon" title="Facebook"><i class="fab fa-facebook"></i></a>
        <a href="{LINKS['LINKEDIN']}" target="_blank" class="social-icon" title="LinkedIn"><i class="fab fa-linkedin"></i></a>
    </div>
    <div style="display:flex; align-items:center;">
        <nav>
            <a href="index.html">/HOME</a>
            <a href="about.html">/IDENTITY</a>
            <a href="projects.html">/ARSENAL</a>
            <a href="video.html">/VIDEO</a>
            <a href="blog.html">/BLOG</a>
            <a href="podcast.html">/PODCAST</a>
            <a href="contact.html">/TERMINAL</a>
        </nav>
        <div class="burger-menu" onclick="toggleMenu()">
            <div class="line"></div>
            <div class="line"></div>
            <div class="line"></div>
        </div>
    </div>
</header>
"""

FOOTER_HTML = f"""
<footer>
    <div class="zoo-list" title="My support team">
        [ SYSTEM RESOURCES: 4 CATS | 2 DOGS | 1 RAT | 1 TURTLE | 100L WATER ]
    </div>
    <div class="footer-bottom" style="margin: 15px 0;">
        <a href="{LINKS['X']}" target="_blank" class="footer-icon-link" title="X"><i class="fab fa-twitter"></i></a>
        <a href="{LINKS['TUMBLR']}" target="_blank" class="footer-icon-link" title="Tumblr"><i class="fab fa-tumblr"></i></a>
        <a href="{LINKS['TWITCH']}" target="_blank" class="footer-icon-link" title="Twitch"><i class="fab fa-twitch"></i></a>
        <a href="{LINKS['GITHUB']}" target="_blank" class="footer-icon-link" title="GitHub"><i class="fab fa-github"></i></a>
        <a href="{LINKS['INSTA_PHOTO']}" target="_blank" class="footer-icon-link" title="Photo Instagram"><i class="fas fa-camera"></i></a>
        <a href="{LINKS['SPOTIFY']}" target="_blank" class="footer-icon-link" title="Spotify"><i class="fab fa-spotify"></i></a>
    </div>
    <div class="footer-bottom">
        <span class="ip-trace" id="fake-ip">Trace...</span>
        <span>::</span>
        <span class="uptime" id="uptime-counter">UPTIME: 0s</span>
    </div>
    <div style="margin-top: 15px; opacity: 0.5; font-size: 0.7rem;">© 2025 {IDENTITY} | NO FORGIVENESS</div>
    </footer>
"""

SHUTDOWN_OVERLAY = """
<div id="shutdown-overlay" class="shutdown-overlay">
    <h1 style="color:red; font-size: 3rem;">SIGNAL LOST</h1>
    <p id="shutdown-timer">TERMINATING SESSION...</p>
</div>
"""

BASE_HTML = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{title}</title>
<link rel="stylesheet" href="css/style.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</head><body>
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
    "video.html": { "title": f"Stream | {IDENTITY}", "content": VIDEO_CONTENT, "js": "<script src='js/typewriter.js'></script>" },
    "blog.html": { "title": f"Log | {IDENTITY}", "content": BLOG_CONTENT, "js": "<script src='js/typewriter.js'></script>" },
    "podcast.html": { "title": f"Audio | {IDENTITY}", "content": PODCAST_CONTENT, "js": "<script src='js/typewriter.js'></script>" },
    "contact.html": { "title": f"Terminal | {IDENTITY}", "content": "<h1>Terminal Access</h1><div class='terminal-window'><div id='history'><p>UkrGeekLife OS v15.0 (Socials Connected)...</p></div><div class='input-line'><span class='prompt'>root@ukrgeek:~#</span><input type='text' id='cmd' autofocus autocomplete='off' enterkeyhint='go'></div></div>", "js": TERMINAL_SCRIPT_INLINE }
}

# 5. EXECUTION
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
# Force small delay to ensure FS write
time.sleep(1)
run("git add .")
run(f'git commit -m "UkrGeekLife | Full Fix | {time.strftime("%H:%M:%S")}"')
run("git push origin master")
print(">>> DONE. CHECK THE ICONS.")