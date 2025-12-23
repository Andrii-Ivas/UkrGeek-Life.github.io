import time, os, datetime, subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(('site_data.json', 'index.html')):
            now = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"[{now}] Detected changes in {os.path.basename(event.src_path)}. Rebuilding...")
            # Запускаємо твій основний forge.py
            subprocess.run(["python", "forge.py"])

if __name__ == "__main__":
    print("--- WATCHDOG ACTIVE: System is monitoring your changes... ---")
    print("--- Press Ctrl+C to stop. ---")
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
