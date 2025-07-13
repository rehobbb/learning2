from pathlib import Path
def read_files(path):
  try:
    contents = path.read_text(encoding = 'gbk')
  except FileNotFoundError:
    print("the file is not exist")
  else:
    contentsline = contents.splitlines()
    for line in contentsline:
      print(line)
filenames = ['cats.txt','dogs.txt']
for filename in filenames:
  path = Path(filename)
  read_files(path)