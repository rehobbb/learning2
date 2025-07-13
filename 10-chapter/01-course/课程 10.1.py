from pathlib import Path
path = Path("2.txt")
contents = path.read_text()
print(contents)