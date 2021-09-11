import os
import frontmatter
from shutil import copy

if not os.path.exists('./docs'):
    os.mkdir('./docs')

for root, dirs, files in os.walk("./zettelkasten/Zet/"):
    for file in files:
        if file.endswith(".md"):
            with open(os.path.join(root, file), encoding="utf8") as f:
                content = f.read()
                metadata, content = frontmatter.parse(content)
                if 'publish' in metadata.keys():
                    print(metadata['title'])
                    copy(os.path.join(root, file), './docs/')
                else:
                    pass
