from pathlib import Path
try:
  path = Path('book1.txt')
except FileNotFoundError:
   print("sorry,the file has not been found")
else:
  contents = path.read_text(encoding='utf-8')
  contents_lines = contents.splitlines()
  word_count ,word_count1 = 0,0
  for line in contents_lines:
    word_count += line.lower().count('the')
    word_count1 += line.lower().count('the ')
  print(f"there are {word_count} words contain 'the'")
  print(f"there are {word_count1} 'the'")