import string
str = "HelloWorld"
upper = sum(map(lambda x: x.isupper(), str))
lower = sum(map(lambda x: x.islower(), str))
print(upper, lower)
