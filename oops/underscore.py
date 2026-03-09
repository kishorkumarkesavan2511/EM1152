# 1. Using _ as a temporary variable (ignore value)
for _ in range(3):
    print("Hello")
# 2. Single leading underscore: protected variable (by convention)
class Example:
    def __init__(self):
        self._protected = "I am protected"
# 3. Double leading underscore: private variable (name mangling)
class Demo:
    def __init__(self):
        self.__private = "I am private"
    def show_private(self):
        print(self.__private)
# 4. Double leading and trailing underscores: special methods
class MagicMethods:
    def __init__(self, name):
        self.name = name   # normal instance variable
    def __str__(self):
        return f"Name is {self.name}"
# 5. Using _ in unpacking to ignore values
data = (1, 2, 3)
a, _, c = data
print("Values after unpacking:", a, c)
# Create objects and show outputs
e = Example()
print(e._protected)  # Accessing protected (not enforced, just convention)
d = Demo()
d.show_private()
m = MagicMethods("Alice")
print(m)
