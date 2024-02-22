string = input()
# print(str == str[::-1])
string2 = ''.join(reversed(string))
if string == string2:
    print(True)
else:
    print(False)


