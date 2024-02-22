import os
path = os.getcwd()
print(f"existence: {os.access(path, os.F_OK)}\n"
      f"readability: {os.access(path, os.R_OK)}\n"
      f"writability: {os.access(path, os.W_OK)}\n"
      f"executability: {os.access(path, os.X_OK)}")
