import re
file = open("row.txt", "r", encoding="utf-8")
filest = file.read()
regex_string = re.findall(".*аб{2,3}", filest)
print(regex_string)
