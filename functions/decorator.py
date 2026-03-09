def decoratorfun(func):
    def wrapper(*args, **kwargs):
        print("Start of iteration:")
        func(*args, **kwargs)
        print("End of iteration!")
    return wrapper

# Decorator to iterate and print elements
@decoratorfun
def decorate_iteration(iterable, extra_info=None):
    #iterable = range(5)
    it = iter(iterable)  # Create an iterator explicitly
    for item in it:
        print(item)  # Print each item
    for key, value in extra_info.items():
        print(f"{key}: {value}")  # Print extra information if provided
    

# Calling the decorator function

decorate_iteration(range(5),{'1':'saikumar','2':'lilyy'})  # Outputs numbers 0 to 4 with messages