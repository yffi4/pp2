import os
lst = list(input().split())
with open("examplefile.txt", "w") as file:
    for i in lst:
        file.write(str(i) + ' ')