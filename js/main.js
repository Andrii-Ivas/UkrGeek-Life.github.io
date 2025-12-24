
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

window.addEventListener('load', () => {
    const log = document.getElementById('boot-log');
    const msgs = ["> INIT_KERNEL...", "> MOUNTING_VOLUMES...", "> SYSTEM_READY."];
    let i = 0;
    const interval = setInterval(() => {
        if(i < msgs.length) { log.innerHTML += msgs[i] + "<br>"; i++; } 
        else { clearInterval(interval); setTimeout(() => { document.getElementById('preloader').classList.add('hidden'); }, 500); }
    }, 600);
});

function toggleMenu() { 
    const menu = document.getElementById('monolith-menu');
    if (menu.style.display === 'flex') { menu.style.display = 'none'; } 
    else { menu.style.display = 'flex'; }
}
function halSpeak() { alert("I'm sorry, Andrii. I'm afraid I can't do that."); }

// RADAR TRACKING LOGIC
document.addEventListener('mousemove', (e) => {
    const radar = document.querySelector('.radar-display');
    const dot = document.querySelector('.radar-dot');
    if(radar && dot) {
        const rect = radar.getBoundingClientRect();
        const centerX = rect.left + rect.width / 2;
        const centerY = rect.top + rect.height / 2;
        
        const dx = e.clientX - centerX;
        const dy = e.clientY - centerY;
        const dist = Math.sqrt(dx*dx + dy*dy);
        
        const maxDist = (rect.width / 2) - 4; 
        const scale = dist > maxDist ? maxDist / dist : 1;
        const finalX = dx * scale;
        const finalY = dy * scale;

        dot.style.top = `calc(50% + ${finalY}px)`;
        dot.style.left = `calc(50% + ${finalX}px)`;
    }
});

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
                    case "help": res = "COMMANDS: [about] [photo] [video] [blog] [kill]"; break;
                    case "about": window.location='about.html'; break;
                    case "photo": window.location='photo.html'; break;
                    case "video": window.location='video.html'; break;
                    case "blog": window.location='blog.html'; break;
                    case "kill": document.body.innerHTML='SYSTEM_HALTED'; break;
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
