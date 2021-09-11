import os
import frontmatter
from shutil import copy
import os

if not os.path.exists('./docs'):
    os.mkdir('./docs')

def files_publish(file):
    if file.endswith(".md"):
        with open(os.path.join(root, file), encoding="utf8") as f:
            content = f.read()
            metadata, content = frontmatter.parse(content)
            if 'publish' in metadata.keys():
                print("Copy publish files from zettelkasten to docs/")
                print(os.path.join(root, file))
                copy(os.path.join(root, file), './docs/')
            else:
                pass

for file in os.listdir("./zettelkasten/"):
    files_publish(file)

for root, dirs, files in os.walk("./zettelkasten/Zet/"):
    files_publish(file)

