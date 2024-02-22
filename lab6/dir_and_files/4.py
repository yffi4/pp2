import os
with open("row.txt", "r", encoding="utf-8") as file:
    text = file.readlines()

num = len(text)
print(num)
