def demo_args(*args, **kwargs):
    """
    Demonstrates arbitrary arguments and keyword arguments.
    """
    # Printing arbitrary arguments
    print("Arbitrary arguments (*args):")
    for arg in args:
        print(arg)
    
    # Printing keyword arguments
    print("\nKeyword arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def demo_list(lst):
    """
    Demonstrates passing a list as an argument.
    """
    print("\nList items:")
    for item in lst:
        print(item)

# Example usage of the functions
demo_args(1, 2, 3, {'a',90,'b',80},name="Vijay", age=30, location="Tamil Nadu")
demo_list([4, 5, 6, 7])