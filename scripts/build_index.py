from json import dumps
from pathlib import Path
from os import getenv

path = Path(".")
directory = []
origin = getenv("origin", "https://noo.farfrom.world/")

for noo_file in path.glob("*/*.noofile.yml"):
    directory.append(str(noo_file))
# Export as json
with open("index.json", "w+") as f:
    f.write(dumps(directory))

# Export as html
# Yes this sucks, I didn't want to add the complexity of svelte.
html = ""
for noo_file in directory:
    html += f"<a href=\"/{noo_file}\">{noo_file}</a><br>"
with open("index.html", "w+") as f:
    f.write(html)


# Build registry
with open("registry.json", "w+") as f:
    registry = {}
    for noo_file in directory:
        name = noo_file.replace(".noofile.yml", "")
        url = origin + noo_file
        registry[name] = url
    f.write(dumps(registry))


