from pathlib import Path
path = Path("guest_book.txt")
names = []
while True:
    name=input("what's your name?")
    names.append(name)
    flag = input("do you want to continue?")
    if flag == "no" :
        break
names1 = ""
for name1 in names:
  names1 += f"{name1}\n"
path.write_text(names1)