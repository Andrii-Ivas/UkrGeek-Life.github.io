
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
