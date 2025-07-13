from pathlib import Path
import json
path = Path('number.json')
number_js = path.read_text()
number = json.loads(number_js)
print(number)