import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../")) # -> we use '../' to go up one directory
from functions.math_ops import add # -> the directory where the file is

suma = add(1, 2)
print(suma)
