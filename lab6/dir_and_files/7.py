with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()
with open("examplefile.txt", "w", encoding="utf-8") as file2:
    file2.write(text)
