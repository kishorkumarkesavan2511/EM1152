class Parent:
    species = "Human"   # class variable
    def __init__(self, name):
        self.__name = name   # private variable (data hiding)
        print("Parent constructor")
    def show(self):   # instance method
        print("Name:", self.__name)
    @classmethod
    def change_species(cls):   # class method
        cls.species = "Homo Sapiens"
        print("Class method")
        print("Species changed")
    @staticmethod
    def greet():   # static method
        print("Hello from static method!")
    def __del__(self):   # destructor
        print("Parent destructor")
class Child(Parent):
    def __init__(self, name):
        super().__init__(name)   # using super()
        print("Child constructor")
# Object creation and method calls
p = Parent("Alice")
p.show()
Parent.change_species()
Parent.greet()
c = Child("Bob")
c.show()