from json import dumps
from pathlib import Path

path = Path(".")

directory = []

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


