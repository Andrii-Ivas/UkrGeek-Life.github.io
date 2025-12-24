# -*- coding: utf-8 -*-
import os, sys, subprocess, time, random

# --- [0] HELPER MODULE: Constants & Git ---
ID_PROJECT, ID_NAME = "UkrGeekLife", "Andrii Ivas"
IDENTITY = f"{ID_PROJECT} | {ID_NAME}"
UA_CHARS = "ҐЄЇИІЙЬ"

def run(cmd):
    try: subprocess.run(cmd, shell=True, check=True, capture_output=True); print(f"✅ {cmd}")
    except: pass

# --- [1] HEAD MODULE: Styles & Metadata ---
def get_head(title):
    return f"""<head><meta charset="UTF-8"><title>{title}</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        body{{background:#050505;color:#0F0;font-family:monospace;margin:0;overflow-x:hidden}}
        #matrix-bg{{position:fixed;top:0;left:0;z-index:-1;opacity:0.2}}
        header{{background:#000;border-bottom:2px solid #333;padding:10px 20px;display:flex;justify-content:space-between;align-items:center;position:sticky;top:0;z-index:1000}}
        .id-wrapper{{display:flex;align-items:center;gap:20px;font-weight:bold;letter-spacing:2px}}
        /* HAL 9000 DIVIDER */
        .hal-divider{{width:30px;height:30px;background:#200;border:2px solid #555;border-radius:50%;display:flex;align-items:center;justify-content:center}}
        .hal-lens{{width:10px;height:10px;background:#F00;border-radius:50%;box-shadow:0 0 10px #F00}}
        /* FLAT SILHOUETTE ICONS */
        .flat-icon{{color:#444;font-size:1.2rem;text-decoration:none;transition:0.3s;filter:grayscale(1)}}
        .flat-icon:hover{{color:#0F0;filter:grayscale(0) drop-shadow(0 0 5px #0F0)}}
        /* SHATTER BUTTON */
        #shatter-container{{position:relative;display:inline-block}}
        .shatter-btn{{background:#0F0;color:#000;border:none;padding:8px 16px;font-family:monospace;font-weight:bold;cursor:pointer;z-index:2}}
        .radar{{width:40px;height:40px;border:1px solid #050;border-radius:50%;position:relative;overflow:hidden}}
        .radar-sweep{{position:absolute;width:100%;height:100%;background:conic-gradient(from 0deg,transparent,rgba(0,255,0,0.3));animation:spin 2s linear infinite}}
        @keyframes spin{{to{{transform:rotate(360deg)}}}}
    </style></head>"""

# --- [2] HEADER MODULE ---
def get_header():
    return f"""<header>
    <div class="id-wrapper">
        <span style="cursor:pointer">[{ID_PROJECT}]</span>
        <div class="hal-divider"><div class="hal-lens"></div></div>
        <a href="index.html" style="color:#FFF;text-decoration:none">{ID_NAME}</a>
    </div>
    <div style="display:flex;align-items:center;gap:20px">
        <div id="shatter-container"><button class="shatter-btn" onclick="shatter(this)">DONATE;</button></div>
        <div class="radar"><div class="radar-sweep"></div></div>
        <div style="display:flex;gap:15px">
            <a href="#" class="flat-icon"><i class="fab fa-youtube"></i></a>
            <a href="#" class="flat-icon"><i class="fab fa-instagram"></i></a>
            <a href="#" class="flat-icon"><i class="fab fa-github"></i></a>
        </div>
    </div>
</header>"""

# --- [3] FOOTER & JS MODULE ---
def get_footer():
    return f"""<footer>
    <script>
        // MATRIX UA
        const canvas=document.createElement('canvas');canvas.id='matrix-bg';document.body.appendChild(canvas);
        const ctx=canvas.getContext('2d');
        const resize=()=>{{canvas.width=window.innerWidth;canvas.height=window.innerHeight}};
        window.onresize=resize;resize();
        const drops=Array(Math.floor(canvas.width/14)).fill(1);
        setInterval(()=>{{
            ctx.fillStyle='rgba(0,0,0,0.05)';ctx.fillRect(0,0,canvas.width,canvas.height);
            ctx.fillStyle='#0F0';ctx.font='14px monospace';
            drops.forEach((y,i)=>{{
                ctx.fillText('{UA_CHARS}'[Math.floor(Math.random()*7)],i*14,y*14);
                if(y*14>canvas.height&&Math.random()>0.975)drops[i]=0;drops[i]++;
            }});
        }},33);
        // SHATTER EFFECT
        function shatter(el){{
            el.style.display='none';
            alert('RE-ROUTING TO ZSU SUPPORT...');
            window.location.href='donate.html';
        }}
    </script>
    <p style="text-align:center;opacity:0.3;font-size:0.7rem">© 2025 {IDENTITY} | PATRIOTS ONLY</p>
</footer>"""

# --- [4] BUILDER ---
print(">>> Deploying Modular Architecture...")
content = "<h1>CORE_LOADED</h1><p>Welcome to the Void.</p>"
html = f"<!DOCTYPE html><html>{get_head('HOME')}<body style='margin:0'><canvas id='matrix-bg'></canvas>{get_header()}<main style='padding:20px;background:rgba(0,0,0,0.8);margin:20px;border:1px solid #333'>{content}</main>{get_footer()}</body></html>"
with open("index.html","w",encoding="utf-8") as f: f.write(html)
run("git add ."); run("git commit -m 'Refactored to Modular Structure'"); run("git push origin master")