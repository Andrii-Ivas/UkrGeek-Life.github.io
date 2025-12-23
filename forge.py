import json, os, difflib, datetime
from bs4 import BeautifulSoup

def forge_system():
    log_file = "version_control.log"
    with open('site_data.json', 'r', encoding='utf-8-sig') as f: data = json.load(f)
    with open('index.html', 'r', encoding='utf-8') as f: tmpl = f.read()

    report = f"\n[SESSION {datetime.datetime.now()}]\n"

    for p in data['pages']:
        soup = BeautifulSoup(tmpl, 'html.parser')
        target = soup.find(id='app_content')
        if target:
            target.clear()
            target.append(BeautifulSoup(p['content'], 'html.parser'))
        
        file_path = f"{p['name']}.html"
        new_html = soup.prettify()
        
        # Перевірка змін (Version Control Logic)
        change_info = "[NEW FILE]"
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                old_html = f.read()
            if old_html.strip() == new_html.strip():
                change_info = "[NO CHANGES]"
            else:
                change_info = "[MODIFIED]"
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_html)
        
        report += f"{change_info} -> {file_path}\n"
        print(f"{change_info} {file_path}")

    with open(log_file, "a", encoding='utf-8') as f:
        f.write(report)
    print(f"--- Changes saved to {log_file} ---")

if __name__ == "__main__": forge_system()
