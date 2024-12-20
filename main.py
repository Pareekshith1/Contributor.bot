# Importing the datetime module
from datetime import datetime

# Importing the Git module for performing different push and pull tasks
from git import Repo

# Importing the random module for generating randomness
import random

# Importing the os package
import os

# Initialize y with an empty string or None to compare dates
y = ""

while True:
    # Get the current date
    x = datetime.now().strftime("%Y-%m-%d")  # Use only the date part for comparison
    
    # Compare the current date with the stored date
    if y != x:
        # Generate a random number between 1 and 10
        rand_no = random.randint(1, 10)
        print(f"Random Number for Today: {rand_no}")
        
        # Perform actions based on the random number
        for j in range(rand_no):
            print(f"Contribution {j + 1} on {x}")

            try:
                # making some updatable changes to the text file
                txt_file = r"C:\\Users\\DELL\\Desktop\\Contributor.bot\\updator.txt"
                with open(txt_file, "a") as p:
                    p.write(f"\n new text {rand_no}")

                # Initialize the Git repository
                repo_path = r"C:\\Users\\DELL\\Desktop\\Contributor.bot"  # Path to the repository
                repo = Repo(repo_path)

                # repo branch changer
                branch = "updater"
                repo.git.checkout(branch)
                
                # adding the file for the commit
                add_file = [txt_file] 
                repo.index.add(add_file)

                # committing the file
                commit_message = f"Update no {j}"
                repo.index.commit(commit_message)

                # pushing the file into the sub branch {updater}
                # define the branch
                sub_branch = "updater"

                # setting up the origin
                origin = repo.remotes.origin
                origin.push(refspec=f"refs/heads/{sub_branch}")

            except Exception as e:
                print(f"An error occurred: {e}")


        # Update y with the current date
        y = x
