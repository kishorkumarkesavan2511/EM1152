import os
filename = "data.txt"
script_dir_os = os.path.dirname(os.path.abspath(__file__))
filename = script_dir_os +'/'+filename
# Create a sample file (only once, can skip later)
with open(filename, "w") as file:
    file.write("Line 1\nLine 2\nLine 3\n")
# Read existing lines
with open(filename, "r") as file:
    lines = file.readlines()
position = int(input("Enter position to insert line at (starting from 1): "))
new_line = input("Enter the new line to insert: ") + "\n"
# Insert the new line
if 1 <= position <= len(lines)+1:
    lines.insert(position - 1, new_line)
    # Write back updated lines
    with open(filename, "w") as file:
        file.writelines(lines)
    print("Line inserted successfully using sequential access.")
else:
    print("Invalid position.")