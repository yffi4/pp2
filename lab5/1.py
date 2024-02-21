import re
file = open("row.txt", "r", encoding="utf-8")
rows = file.read()
regex_string = re.findall(".*аб*", rows)
print(regex_string)
