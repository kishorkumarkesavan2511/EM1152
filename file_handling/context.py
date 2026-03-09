import os
def add_line(filename):
    line = input("Enter the line to add: ")
    with open(filename, "a") as file:  # Context manager used here
        file.write(line + "\n")
    print("Line added successfully.\n")
def delete_line(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    print("File contents:")
    for i, line in enumerate(lines, start=1):
        print(f"{i}: {line.strip()}")
    line_num = int(input("Enter line number to delete: "))
    if 1 <= line_num <= len(lines):
        del lines[line_num - 1]
        with open(filename, "w") as file:
            file.writelines(lines)
        print("Line deleted successfully.\n")
    else:
        print("Invalid line number!\n")
filename = "data.txt"
script_dir_os = os.path.dirname(os.path.abspath(__file__))
filename = script_dir_os +'/'+filename
while True:
    print("Menu:")
    print("1. Add a line")
    print("2. Delete a line")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_line(filename)
    elif choice == 2:
        delete_line(filename)
    elif choice == 3:
        print("Exiting program.")
        break
    else:
        print("Invalid choice! Please try again.\n")