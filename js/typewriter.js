
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
