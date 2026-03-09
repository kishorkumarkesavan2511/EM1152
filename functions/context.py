import os
""" from pathlib import Path

current_directory = os.getcwd()
print("Current Working Directory:", current_directory)

current_directory = Path.cwd()
print("Current Working Directory:", current_directory)

# Using os.path
script_dir_os = os.path.dirname(os.path.abspath(__file__))
print("Script Location (os):", script_dir_os)

# Using pathlib
script_dir_pathlib = Path(__file__).parent.resolve()
print("Script Location (pathlib):", script_dir_pathlib) """


#print("Current Working Directory:", os.path.abspath(__file__))
# Using os.path
script_dir_os = os.path.dirname(os.path.abspath(__file__))

# Using a Context Manager to read a file
with open(script_dir_os +"/example.txt", "r") as f:  # Open file in read mode
    lines = [line.strip() for line in f]  # List comprehension to strip newline characters

# Display the processed lines
print(lines) #output : 'hello', 'world', 'Kitten']