from pathlib import Path
import json
def get_stored_username(path):
    if path.exists():
        user_js = path.read_text()
        user = json.loads(user_js)
        return user
    else:
        return None
def get_new_username(path):
    user = input("please inuput your name:")
    user_js = json.dumps(user)
    path.write_text(user_js)
    return user
def greet():
    path = Path('username.txt')
    username = get_stored_username(path)
    if username:
        username_yes = input(f"is {username} your name ?")
        if username_yes == 'yes':
            print(f'welcome come back {username}')
        else :
           username = get_new_username(path)
           print(f'your name  {username} have been stored!')
    else:
        username = get_new_username(path)
        print(f'your name  {username} have been stored!')
greet()

