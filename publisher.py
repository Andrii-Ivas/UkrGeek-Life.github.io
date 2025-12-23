import os

# --- НАЛАШТУВАННЯ UTF-8 ДЛЯ КОНСОЛІ WINDOWS ---
import sys
# Примушуємо Python писати в консоль UTF-8, щоб не було помилок при print()
sys.stdout.reconfigure(encoding='utf-8')

# --- КОНФІГУРАЦІЯ ---
IDENTITY = "UkrGeekLife | Андрій Івась"

# МЕНЮ (Перевіряємо, щоб лінки вели на існуючі файли)
NAV_MENU = """
<nav role="navigation" aria-label="Головне меню" class="main-nav">
    <a href="index.html" class="nav-link">[ ГОЛОВНА ]</a>
    <a href="about.html" class="nav-link">[ ПРО МЕНЕ ]</a>
    <a href="projects.html" class="nav-link">[ ПРОЄКТИ ]</a>
    <a href="contact.html" class="nav-link">[ ТЕРМІНАЛ ]</a>
</nav>
"""

# ШАБЛОН (Зверни увагу на meta charset="UTF-8")
BASE_TEMPLATE = """<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div class="matrix-bg"></div>
    <header>
        <div class="logo">{logo}</div>
        {nav}
    </header>
    <main class="container">
        {content}
    </main>
    <script src="js/matrix.js"></script>
</body>
</html>"""

# КОНТЕНТ СТОРІНОК
PAGES = {
    "index.html": {
        "title": f"Головна | {IDENTITY}",
        "content": "<h1>Система UkrGeekLife</h1><p>Ідентичність підтверджено.</p><p>Статус: Онлайн.</p>"
    },
    "about.html": {
        "title": f"Про Мене | {IDENTITY}",
        "content": "<h1>Андрій Івась</h1><p>IT-фахівець. Патріот. Архітектор автоматизації.</p>"
    },
    "projects.html": {
        "title": f"Проєкти | {IDENTITY}",
        "content": "<h1>Арсенал</h1><ul><li>Автоматизація PowerShell</li><li>Python Backend</li><li>Web Security</li></ul>"
    },
    "contact.html": {
        "title": f"Термінал | {IDENTITY}",
        "is_terminal": True
    }
}

def update_system():
    print(f"--- ПОЧАТОК ГЕНЕРАЦІЇ: {IDENTITY} ---")
    
    for filename, data in PAGES.items():
        # ЛОГІКА ТЕРМІНАЛУ
        if data.get("is_terminal"):
            html_content = f"""<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{data['title']}</title>
    <link rel="stylesheet" href="css/style.css">
    <style>body {{ overflow: hidden; }}</style>
</head>
<body>
    <div class="matrix-bg"></div>
    <header>
        <div class="logo">{IDENTITY}</div>
        {NAV_MENU}
    </header>
    <div class="terminal-wrapper">
        <div id="history">
            <p>UkrGeekLife OS v2.0 initialized...</p>
            <p>Type 'help' for commands.</p>
        </div>
        <div class="input-line">
            <span class="prompt">guest@ukrgeek:~$</span>
            <input type="text" id="cmd" autofocus>
        </div>
    </div>
    <script src="js/matrix.js"></script>
    <script src="js/terminal.js"></script>
</body>
</html>"""
        else:
            # ЗВИЧАЙНА СТОРІНКА
            html_content = BASE_TEMPLATE.format(
                title=data['title'],
                logo=IDENTITY,
                nav=NAV_MENU,
                content=data['content']
            )

        # !!! ГОЛОВНИЙ ФІКС: encoding="utf-8" !!!
        # Це змушує Python записувати файл саме в UTF-8, а не в кодуванні Windows.
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_content)
        
        print(f"✅ Згенеровано (UTF-8): {filename}")

if __name__ == "__main__":
    update_system()