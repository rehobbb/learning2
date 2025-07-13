from pathlib import Path
path = Path("pi_digits.txt")
contents = path.read_text("utf-8")
lines = contents.splitlines()
str = "" 
for line in lines:
    str += line.lstrip()
print(f"{str[:4]}")
print(len(str))