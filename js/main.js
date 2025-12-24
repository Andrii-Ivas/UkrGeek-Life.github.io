
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

function killSystem() { document.body.innerHTML='<div style="display:flex;justify-content:center;align-items:center;height:100vh;background:#000;color:red;font-size:2rem;">SYSTEM HALTED</div>'; }
function toggleMenu() { document.querySelector('nav').classList.toggle('active'); }

// TERMINAL & TYPEWRITER
document.addEventListener("DOMContentLoaded", function() {
    // TYPEWRITER
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
                setTimeout(type, 1); // Fast typing
            }
        }
        type();
    }
    // TERMINAL
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
                    case "help": res = "COMMANDS: [about] [photo] [video] [blog] [slava] [kill]"; break;
                    case "about": window.location='about.html'; break;
                    case "photo": window.location='photo.html'; break;
                    case "video": window.location='video.html'; break;
                    case "blog": window.location='blog.html'; break;
                    case "slava": res = "<span style='color:yellow'>GEROYAM SLAVA!</span>"; break;
                    case "kill": killSystem(); break;
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
