from pathlib import Path
path = Path("write_multiple_texts.txt")
contents = "i love programming\n"
contents += "do you love it?\n"
contents += "yes, i do\n"
path.write_text(contents)