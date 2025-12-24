import os
import time

def run_cmd(cmd):
    print(f"Executing: {cmd}")
    os.system(cmd)

print("--- ☢️ FORCING UPDATE ☢️ ---")

# 1. Просто дописуємо невидимий коментар в кінець файлу, щоб змінити його
with open("index.html", "a", encoding="utf-8") as f:
    f.write(f"\n")

print("✅ index.html modified.")

# 2. Жорсткий Git Push
run_cmd("git add .")
run_cmd('git commit -m "Emergency Fix"')
run_cmd("git push origin master")

print("--- DONE. NOW CHECK GITHUB ---")