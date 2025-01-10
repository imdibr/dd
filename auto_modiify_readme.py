import random
import time
import datetime
import subprocess

# Path to your README file
readme_path = '/Users/imadibrahim/Documents/imdibr/README.md'

# A list of example content changes
changes = [
    "This is a random change to the README.\n",
    "Added a new section for documentation.\n",
    "This project is awesome! #auto-commit\n",
    "Last update: {}\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
    "Don't forget to star the repo if you like it!\n"
]

# Function to randomly pick 1-3 changes and modify the README file
def modify_readme():
    with open(readme_path, 'a') as readme_file:
        # Pick a random number of changes (1 to 3)
        num_changes = random.randint(1, 3)
        for _ in range(num_changes):
            change = random.choice(changes)
            readme_file.write(change)
        print(f"Made {num_changes} changes to README.")

# Function to commit and push changes to the repository
def commit_and_push_changes():
    subprocess.run(['git', 'add', 'README.md'])
    subprocess.run(['git', 'commit', '-m', 'Auto update README file'])
    subprocess.run(['git', 'push'])

# Call the modify_readme function to make changes to README
modify_readme()

# Call the commit_and_push_changes function to commit and push changes
commit_and_push_changes()
