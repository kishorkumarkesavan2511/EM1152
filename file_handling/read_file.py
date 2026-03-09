import os
filename = "data.txt"
script_dir_os = os.path.dirname(os.path.abspath(__file__))
filename = script_dir_os +'/'+filename

# Open the file in read mode
with open(filename, "r") as file:
    # Read and print each line
    for line in file:
        print(line.strip())  # strip() removes extra spaces/newlines