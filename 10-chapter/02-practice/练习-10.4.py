from pathlib import Path
path = Path("guest_book.txt")
name = input("what's your name?")
path.write_text(name)