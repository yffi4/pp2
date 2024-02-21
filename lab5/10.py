import re
file = open("row.txt", "r", encoding="utf-8")
string = file.read()
print(re.sub(r'([A-Z])', r'_\1', string).lower())