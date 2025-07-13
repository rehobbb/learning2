from pathlib import Path
import json
print("input a number,i will remember it!")
path = Path('number.json')
number = int(input("please input your number:"))
number_js = json.dumps(number)
path.write_text(number_js)