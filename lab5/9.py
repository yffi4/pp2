import re
file = open("row.txt", "r", encoding="utf-8")
string = file.read()
print(re.sub("([А-Я])", lambda x: " " + x.group(1), string))