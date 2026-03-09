import copy

# Original list
original_list = [[1, 2, 3], [4, 5, 6]]

# Shallow copy
shallow_copy = copy.copy(original_list)
original_list[0][0] = 999  # Modify the original list
print("Shallow Copy:", shallow_copy)  # Reflects change in nested elements
print("original list:", original_list)  # Reflects change in nested elements
# Reset the original list
original_list = [[1, 2, 3], [4, 5, 6]]

""" # Deep copy
deep_copy = copy.deepcopy(original_list)
original_list[0][0] = 999  # Modify the original list again
print("Deep Copy:", deep_copy)  # Unaffected by 
print("original list:", original_list)  # Reflects change in nested elements """
