

from pathlib import Path
import json
path = Path('username.json')
def get_storted_uername(path):
    if path.exists():
        contents = path.read_text()
        username = json.load(contents)
        return username
    else:
        return None
def remember_new(path):
    username = input("please input your name,i will remember:")
    contents = json.dumps(username)
    path.write_text(contents)
    return username
def greet():
    username = get_storted_uername(path)
    if username:
        print(f"welcome bak {username}")
    else:
        username=remember_new(path)
        print(f"we'll remember you when you come back,{username}")
greet()