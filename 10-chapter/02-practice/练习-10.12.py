from pathlib import Path
import json
def get_stored_number(path):
    if path.exists():
        number_js = path.read_text()
        number = json.loads(number_js)
        return number
    else :
        return None
def get_new_number(path):
    number = int(input("please input your number:"))
    number_js = json.dumps(number)
    path.write_text(number_js)
    return number
def show_number():
    path = Path('number.json')
    number = get_stored_number(path)
    if number:
        print(f"your favorite number is {number}")
    else :
        number = get_new_number(path)
        print(f"you have input number {number},i will remember it!")
show_number()