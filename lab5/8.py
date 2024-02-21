import re
file = open("row.txt", "r", encoding="utf-8")
string = file.read()
print(re.split("[А-Я]", string))