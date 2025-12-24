# -*- coding: utf-8 -*-
import os
import sys

# 1. SETUP
sys.stdout.reconfigure(encoding='utf-8')
IDENTITY = "UkrGeekLife | Andrii Ivas"
os.makedirs("css", exist_ok=True)
os.makedirs("js", exist_ok=True)

# 2. ASSETS
CSS_CODE = """
body { background-color: #000; color: #0F0; font-family: 'Courier New', monospace; margin: 0; padding: 0; min-height: 100vh; display: flex; flex-direction: column; }
#matrix-bg { position: fixed; top: 0; left: 0; z-index: -1; opacity: 0.15; }

/* HEADER (English UI) */
header { background: rgba(0, 20, 0, 0.95); border-bottom: 2px solid #0F0; padding: 15px 0; text-align: center; position: sticky; top: 0; z-index: 100; }
.logo { font-size: 1.5rem; font-weight: bold; text-transform: uppercase; letter-spacing: 3px; margin-bottom: 10px; text-shadow: 0 0 10px #0F0; }
nav a { color: #FFF; text-decoration: none; margin: 0 15px; font-size: 1.1rem; font-weight: bold; transition: 0.3s; }
nav a:hover { color: #0F0; text-shadow: 0 0 8px #0F0; }

/* CONTAINER */
.container { flex: 1; max-width: 900px; margin: 40px auto; padding: 20px; background: rgba(0, 0, 0, 0.8); border: 1px solid #333; width: 90%; }
h1, h2 { border-bottom: 1px solid #0F0; padding-bottom: 10px; text-transform: uppercase; }
p, li { font-size: 1.1rem; line-height: 1.6; }
.alert { color: #FF3333; font-weight: bold; border: 1px solid #F00; padding: 10px; margin: 10px 0; background: rgba(50, 0, 0, 0.5); }
.highlight { color: #FFF; font-weight: bold; }
.red-alert { color: #FF3333; font-weight: bold; }

/* FOOTER (The Brilliant Part) */
footer { 
    border-top: 2px solid #0F0; 
    background: #020202; 
    text-align: center; 
    padding: 30px; 
    margin-top: auto; 
    font-size: 0.9rem; 
    color: #666; 
}
.footer-row { margin-bottom: 10px; }
.footer-links a { color: #AAA; text-decoration: none; margin: 0 10px; font-weight: bold; }
.footer-links a:hover { color: #0F0; text-decoration: underline; }
.irony { font-style: italic; color: #444; font-size: 0.8rem; }
.zoo-counter { color: #004400; font-size: 0.8rem; letter-spacing: 1px; }

/* EASTER EGG: Red glitch effect on hover */
.hazard-zone { cursor: help; transition: 0.3s; }
.hazard-zone:hover { color: #F00; text-shadow: 2px 2px 0px #FFF; content: "RM -RF /"; }
.hazard-zone:hover::after { content: " [DO NOT TOUCH]"; font-size: 0.7rem; }

/* Typing Cursor */
.cursor::after { content: '█'; animation: blink 1s infinite; color: #0F0; margin-left: 5px; }
@keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }

/* Terminal */
.terminal-window { background: #111; border: 1px solid #0F0; padding: 20px; height: 60vh; overflow-y: auto; }
.input-line { display: flex; align-items: center; }
.prompt { color: #0F0; margin-right: 10px; font-weight: bold; }
input#cmd { background: transparent; border: none; color: #FFF; font-family: monospace; font-size: 1.2rem; flex-grow: 1; outline: none; }
#typewriter-content { visibility: hidden; }
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

JS_TYPEWRITER = """
document.addEventListener("DOMContentLoaded", function() {
    const element = document.getElementById('typewriter-content');
    if (!element) return;
    const text = element.innerHTML;
    element.innerHTML = "";
    element.classList.add("cursor");
    element.style.visibility = "visible";
    let i = 0;
    const speed = 10;
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
                case "about": res = "Andrii Ivas. Vegetarian. Patriot. Automation Architect."; break;
                case "projects": res = "GitHub: ivas-andre. Automation. Security."; break;
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

# 3. TEMPLATES (ENGLISH UI ONLY)

# English Navigation
NAV_MENU = """
<nav role="navigation">
    <a href="index.html">[ HOME ]</a>
    <a href="about.html">[ IDENTITY ]</a>
    <a href="projects.html">[ ARSENAL ]</a>
    <a href="contact.html">[ TERMINAL ]</a>
</nav>
"""

# The Brilliant Ironic Footer
FOOTER_TEMPLATE = """
<footer>
    <div class="footer-row">
        <span class="hazard-zone" title="System Kernel: Stable">System Online</span> :: &copy; 2025 {logo}
    </div>
    
    <div class="footer-row footer-links">
        <a href="index.html">/ROOT</a>
        <a href="about.html">/BIN/WHOAMI</a>
        <a href="projects.html">/VAR/WWW/PROJECTS</a>
        <a href="contact.html">/DEV/STDIN</a>
    </div>

    <div class="footer-row zoo-counter">
        Running on: 4 Cats, 2 Dogs, 1 Turtle, 1 Rat & 100L of Water.
    </div>

    <div class="irony">
        "I automated this footer because I was too lazy to type it twice."
    </div>
</footer>
"""

# Base HTML Structure
BASE_HTML = """<!DOCTYPE html>
<html lang="en"> <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <canvas id="matrix-bg"></canvas>
    <header><div class="logo">{logo}</div>{nav}</header>
    <main class="container">
        <div id="typewriter-content">
            {content}
        </div>
    </main>
    {footer}
    <script src="js/matrix.js"></script>
    {extra_js}
</body>
</html>"""

# 4. CONTENT (MIXED LANGUAGE BODY - YOUR TEXT)
ABOUT_CONTENT = """
<h1>The Protocol: No Gods, No Masters, No Forgiveness</h1>
<p>Let’s be crystal clear. Я не буду підбирати слова, щоб комусь було "комфортно". Comfort is a lie. Реальність — це датасет, і він часто буває потворним.</p>

<h2>1. The Enemy & The Context</h2>
<div class="alert">
    Перше і найголовніше: I hate Russia. І це не емоція, це логічний висновок. We must remember every single second: they came here to kill us.
    Більше <strong>500,000 українців</strong> — жінки, діти, чоловіки — знищені цим біосміттям.
    Я патріот України. І коли я чую про "примирення" або "хороших росіян" — that’s bullshit.
    There are no barriers for them, so I have no mercy for them. Це аксіома.
</div>

<h2>2. The Origins of Logic</h2>
<p>Мене часто питають про "сімейні цінності". Fuck that.<br>
Моє дитинство було жахливим. Poor grandparents, no support, just classic poverty. Ніхто не хотів мене нічому вчити.
I looked around and realized: God doesn't exist. Religion is a control system for those who can't think.</p>
<p>Я атеїст. I don't believe in "higher powers," I don't believe in myself, I don't believe in you.<br>
Віра не потрібна. Потрібен розрахунок.</p>
<p>Мій раціон — це теж розрахунок. <strong>10+ років без м'яса.</strong> Рік без seafood. Зараз викидаю яйця і лактозу.
Це не про "духовність", це про результат. I don't kill animals because I don't need to.</p>

<h2>3. The Void: ADHD, OCD & Depression</h2>
<p>Давайте чесно про "успішний успіх". Я був у такій глибокій сраці, що ви не повірите.<br>
У мене <strong>ADHD і OCD</strong>. Я випав з життя на рік. Deep depression — це коли ти знаєш, що можеш все, але фізично не робиш ніхуя. Ти просто існуєш.<br>
Але я вибрався. I survived. І тепер я повертаюсь у гру.<br>
Раніше я волонтерив, робив купу роботи for free. The charity ends now. Я переходжу в комерцію.
Мені потрібні гроші, щоб відновити житло, закрити діри в бюджеті і годувати свій "ковчег":
<span class="highlight">4 cats, 2 dogs, a turtle, a rat, and a 100L aquarium.</span></p>

<h2>4. Machine Learning (Not "AI")</h2>
<p>І припиніть називати це "Штучним Інтелектом". There is no intelligence there. Це <strong>Machine Learning</strong>. Це статистика і математика. Але це працює.<br>
Зараз я використовую ML для повної автоматизації. I save my time. Те, що раніше займало роки, я роблю за місяці.<br>
Чому? Тому що в мене немає часу на булшіт. Мені треба 100 годин у добі, а є тільки 24.</p>

<h2>5. The Bottom Line</h2>
<p>Я люблю старі камери, люблю вело, люблю збирати старий софт. Я ціную історію, бо це факти.<br>
Але я не живу вчорашнім днем. Важливий кожен байт інформації сьогодні, щоб не проїбати завтра.</p>
<p class="red-alert">Бережіть свої кордони. Бо мої — заміновані.</p>
"""

PAGES = {
    "index.html": { 
        "title": f"Home | {IDENTITY}", 
        "content": "<h1>System Online</h1><p>Welcome to the digital space of Andrii Ivas.</p><p>All systems nominal.</p>", 
        "js": "",
        "extra_js_file": "" 
    },
    "about.html": { 
        "title": f"Identity | {IDENTITY}", 
        "content": ABOUT_CONTENT, 
        "js": "",
        "extra_js_file": "<script src='js/typewriter.js'></script>" # TYPING EFFECT ONLY HERE
    },
    "projects.html": { 
        "title": f"Arsenal | {IDENTITY}", 
        "content": "<h1>Arsenal</h1><ul><li><strong>Full Automation Deploy:</strong> No manual bullshit.</li><li><strong>Security Audit:</strong> Protecting the code.</li></ul>", 
        "js": "",
        "extra_js_file": "" 
    },
    "contact.html": { 
        "title": f"Terminal | {IDENTITY}", 
        "content": "<h1>Terminal Access</h1><div class='terminal-window'><div id='history'><p>UkrGeekLife OS v4.0 initialized...</p><p>Type 'help'...</p></div><div class='input-line'><span class='prompt'>guest@ukrgeek:~$</span><input type='text' id='cmd' autofocus></div></div>", 
        "js": f"<script>{JS_TERMINAL}</script>",
        "extra_js_file": "" 
    }
}

# 5. GENERATE
def generate():
    print("--- UPDATING SYSTEM: ENGLISH UI + MIXED CONTENT ---")
    with open("css/style.css", "w", encoding="utf-8") as f: f.write(CSS_CODE)
    with open("js/matrix.js", "w", encoding="utf-8") as f: f.write(JS_MATRIX)
    with open("js/typewriter.js", "w", encoding="utf-8") as f: f.write(JS_TYPEWRITER)
    
    for filename, data in PAGES.items():
        # Inject the correct extra JS (Typewriter only on About page)
        final_html = BASE_HTML.format(
            title=data['title'], 
            logo=IDENTITY, 
            nav=NAV_MENU, 
            content=data['content'], 
            footer=FOOTER_TEMPLATE.format(logo=IDENTITY), 
            extra_js=data['js'] + data['extra_js_file']
        )
        with open(filename, "w", encoding="utf-8") as f: f.write(final_html)
        print(f"✅ {filename} Generated")

if __name__ == "__main__":
    generate()