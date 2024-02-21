import re
file = open("row.txt", "r", encoding="utf-8")
string = file.read()
regex_string = re.findall("[А-Я][а-я]+", string)
print(regex_string)
file.close()
