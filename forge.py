import json, os, difflib, datetime

def forge_forensic_system():
    log_file = "system_audit.txt"
    with open('site_data.json', 'r', encoding='utf-8-sig') as f: data = json.load(f)
    with open('index.html', 'r', encoding='utf-8') as f: master = f.read().splitlines()

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report = f"\n{'='*60}\nAUDIT LOG: {now}\n{'='*60}\n"

    for p in data['pages']:
        from bs4 import BeautifulSoup
        soup = BeautifulSoup("\n".join(master), 'html.parser')
        
        target = soup.find(id='app_content') or soup.find('main')
        if target:
            target.clear()
            target.append(BeautifulSoup(p['content'], 'html.parser'))

        new_content = soup.prettify().splitlines()
        file_path = f"{p['name']}.html"
        
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                old_content = f.read().splitlines()
            
            # Пошук різниці з номерами рядків
            diff = list(difflib.unified_diff(old_content, new_content, lineterm=''))
            
            if diff:
                report += f"\n[MODIFIED] File: {file_path}\n"
                # diff[2:] прибирає заголовок diff, залишаючи суть
                for line in diff[2:]:
                    report += f"  {line}\n"
                print(f"✅ {file_path} - Changes logged.")
            else:
                report += f"\n[STABLE] File: {file_path} - No changes detected.\n"
                print(f"⚪ {file_path} - No changes.")
        else:
            report += f"\n[CREATED] File: {file_path}\n"
            print(f"🆕 {file_path} - Created.")

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(new_content))

    with open(log_file, "a", encoding='utf-8') as f:
        f.write(report)
    print(f"\n--- AUDIT COMPLETE. Check {log_file} for line-by-line details. ---")

if __name__ == "__main__":
    forge_forensic_system()
