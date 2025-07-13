from pathlib import Path
import json
path = Path('remember.json')
people_info = {}
print("print input peoples information!")
while True:
    name = input('please input name:')
    people_info[name] = input("please input age:")
    repeat = input("do you want to continue?")
    if repeat == 'no':
        break
people_info_js = json.dumps(people_info)
path.write_text(people_info_js)
peps_js = path.read_text()
peps = json.loads(peps_js)
for pep,age in peps.items():
    print(pep)
    print(age)