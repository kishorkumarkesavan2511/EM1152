# Demonstrating the use of self and dunder methods
class Student:
    # __init__ is a dunder method (constructor)
    def __init__(self, name, roll):
        self.name = name   # 'self' refers to the current object
        self.roll = roll
    # Instance method using self
    def show_details(self):
        print("Name:", self.name)
        print("Roll No:", self.roll)
    # __str__ is a dunder method that returns a string representation
    def __str__(self):
        return f"Student(Name: {self.name}, Roll: {self.roll})"
# Create object of Student class
s1 = Student("Alice", 101)
# Call instance method
s1.show_details()
# Using __str__ dunder method implicitly
print(s1)