
import os
filename = "random_access.txt"
script_dir_os = os.path.dirname(os.path.abspath(__file__))
filename = script_dir_os +'/'+filename
# Create a sample file (if not present)
with open(filename, "w") as file:
    file.write("ABCDEFGH")
position = int(input("Enter byte position to overwrite (0-based index): "))
new_data = input("Enter new data (single character recommended): ")
# Random access using seek()
with open(filename, "r+") as file:
    file.seek(position)
    file.write(new_data)
print("Data written at specified byte position using random access.")