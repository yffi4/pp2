import re
file = open("row.txt", "r", encoding="utf-8")
string = file.read()
regex_string = re.findall("[а-я]+_", string)
print(regex_string)