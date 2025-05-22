from github import Github
import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()  # Looks for .env in the same directory by default

# Access variables
token = os.getenv("token") 
# Replace with your GitHub token (with 'repo' or 'admin:org' scope)
REPO_NAME = "youssef4-75/tpGit"  # e.g., "facebook/react"

# List of collaborators (GitHub usernames)
COLLABORATORS = """

""".split()

# Initialize GitHub API
g = Github(token)
repo = g.get_repo(REPO_NAME)

# Add each collaborator
for username in COLLABORATORS:
    try:
        repo.add_to_collaborators(username, permission="push")  # "push" = write
        print(f"✅ Added {username}")
    except Exception as e:
        print(f"❌ Failed to add {username}: {e}")

print("Done!")