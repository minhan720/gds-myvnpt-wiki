import shutil
import os

src = "site-kb/knowledge base"
dst = "site/knowledge base"

print(f"Copying {src} to {dst}...")

# Check if src exists
if not os.path.exists(src):
    print(f"Error: {src} does not exist!")
    exit(1)

# we can use shutil.copytree but in python 3.8+ we must set dirs_exist_ok=True
try:
    shutil.copytree(src, dst, dirs_exist_ok=True)
    print("Files successfully copied.")
except Exception as e:
    print(f"Error occurred during copy: {e}")
    exit(1)
