import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

class Watcher:
    def __init__(self, directory_to_watch):
        self.directory_to_watch = directory_to_watch
        self.event_handler = FileSystemEventHandler()
        self.event_handler.on_modified = self.on_modified
        self.observer = Observer()

    def on_modified(self, event):
        if event.is_directory:
            return
        print(f"Change detected in {event.src_path}, committing changes...")
        subprocess.run(['python3', 'auto_commiter.py'])

    def start(self):
        self.observer.schedule(self.event_handler, self.directory_to_watch, recursive=True)
        self.observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
            print("Observer stopped.")
        except Exception as e:
            print(f"Error: {e}")
            self.observer.stop()

if __name__ == "__main__":
    directory_to_watch = "/Users/imadibrahim/Documents/imdibr"  # Replace with the directory you want to monitor
    watcher = Watcher(directory_to_watch)
    watcher.start()
