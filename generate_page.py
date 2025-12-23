import os

def create_page(page_name):
    template_path = 'index.html' # Або ваш основний скелет
    if not os.path.exists(template_path):
        # Якщо шаблону немає, створимо базовий UX-скелет
        skeleton = """<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <title>{{TITLE}} | UkrGeekLife</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header><h1>UkrGeekLife</h1></header>
    <main id="app"></main>
    <footer>Socials: GitHub, LinkedIn, MySpace (Easter Egg)</footer>
</body>
</html>"""
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(skeleton)
    
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content.replace("{{TITLE}}", page_name.capitalize())
    
    with open(f'{page_name}.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"✅ Сторінка {page_name}.html створена успішно!")

create_page('login')

# Приклад для index.html
(Get-Content index.html) -replace '<title>.*</title>', '<title>UkrGeekLife | Андрій Івась | Головна</title>' | Set-Content index.html
``` [cite: 2025-12-23]