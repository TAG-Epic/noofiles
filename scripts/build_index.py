from json import dumps
from pathlib import Path

path = Path(".")

directory = []

for noo_file in path.glob("*/*.noofile.yml"):
    directory.append(str(noo_file))

with open("index.json", "w+") as f:
    f.write(dumps(directory))


