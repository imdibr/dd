import os
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class AutoCommitHandler(FileSystemEventHandler):
    def __init__(self, repo_path):
        self.repo_path = repo_path

    def on_any_event(self, event):
        # Run git commands when a change is detected
        if event.is_directory:
            return
        try:
            print(f"Change detected: {event.src_path}")
            os.chdir(self.repo_path)
            
            # Stage changes
            subprocess.run(["git", "add", "."], check=True)
            print("Changes staged.")
            
            # Commit changes
            commit_message = f"Auto-commit: {time.strftime('%Y-%m-%d %H:%M:%S')}"
            subprocess.run(["git", "commit", "-m", commit_message], check=True)
            print(f"Changes committed with message: {commit_message}")
            
            # Push changes
            subprocess.run(["git", "push"], check=True)
            print("Changes pushed to the repository.")
        except subprocess.CalledProcessError as e:
            print(f"Error during Git operation: {e}")


def main():
    # Directory to watch (replace this with your repo path)
    repo_path = "/Users/imadibrahim/documents/imdibr"

    if not os.path.exists(os.path.join(repo_path, ".git")):
        print("The specified directory is not a Git repository.")
        return

    # Create an event handler
    event_handler = AutoCommitHandler(repo_path)

    # Set up an observer to monitor the directory
    observer = Observer()
    observer.schedule(event_handler, repo_path, recursive=True)
    observer.start()

    print(f"Watching for changes in: {repo_path}")
    try:
        while True:
            time.sleep(1)  # Keep the script running
    except KeyboardInterrupt:
        observer.stop()
        print("Stopping auto-committer.")
    observer.join()


if __name__ == "__main__":
    main()
