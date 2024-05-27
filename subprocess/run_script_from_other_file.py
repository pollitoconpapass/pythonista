import sys
import subprocess


command = "python script.py"  # -> the running command of a different file
subprocess.run(command, shell=True)


# In case it comes from another directory (folder):
config_dir = "path/to/script"
new_command = "python subscript.py"
subprocess.run(new_command, cwd=config_dir, shell=True)


# If there are some parameters:
# Suppose there is a function called "function_name" in the other file you want to run as subprocess
def function_name(param): # -> example
    print(param)

param = sys.argv[1]
function_name(param)