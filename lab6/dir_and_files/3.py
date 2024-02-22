import os
path = os.getcwd()

if os.path.exists(path):
    print(os.name)
    print(os.listdir())
else:
    print(False)
