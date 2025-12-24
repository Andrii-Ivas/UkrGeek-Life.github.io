
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
