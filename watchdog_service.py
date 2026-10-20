import datetime
import subprocess
import sys
import time
from pathlib import Path

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

PROJECT_DIR = Path(__file__).resolve().parent
SOURCE_FILE = PROJECT_DIR / "site_data.json"
FORGE_SCRIPT = PROJECT_DIR / "forge.py"
DEBOUNCE_SECONDS = 1.5


class ChangeHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self.last_build = 0.0

    def on_modified(self, event):
        if event.is_directory or Path(event.src_path).resolve() != SOURCE_FILE:
            return
        now = time.monotonic()
        if now - self.last_build < DEBOUNCE_SECONDS:
            return
        self.last_build = now
        stamp = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"[{stamp}] site_data.json changed; rebuilding...", flush=True)
        try:
            subprocess.run(
                [sys.executable, str(FORGE_SCRIPT)],
                cwd=PROJECT_DIR,
                check=True,
            )
        except subprocess.CalledProcessError as exc:
            print(f"[ERROR] Build failed with exit code {exc.returncode}", file=sys.stderr)


if __name__ == "__main__":
    print("--- WATCHDOG ACTIVE: monitoring site_data.json ---")
    print("--- Press Ctrl+C to stop. ---")
    observer = Observer()
    observer.schedule(ChangeHandler(), path=str(PROJECT_DIR), recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        observer.stop()
        observer.join()
