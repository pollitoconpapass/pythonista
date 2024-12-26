import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../")) # -> consider using another '..' in case it is in another folder subdirectory
from functions.math_ops import subtract

rest = subtract(2, 1)
print(rest)