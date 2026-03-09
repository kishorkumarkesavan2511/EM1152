


d = { 'b': 13, 'c': 12,'a': 1}  # Direct input key-value pairs
print("Input Dictionary:", d)  # Display input dictionary

k_sort = dict(sorted(d.items()))  # Sort by keys
print("Sorted by keys:", k_sort)  # Print keys-sorted dictionary

v_list = []  # List for sorted key-value pairs
sv = sorted(d.values())  # Sort dictionary values
print("Sorted by values in list:", sv)
#print("type", type(sv))  # Print values-sorted dictionary
for val in sv:
    for key, value in d.items():  # Match keys to sorted values
        if value == val and (key, value) not in v_list:  # Ensure uniqueness
            v_list.append((key, value))  # Add pair to the list

v_sort = dict(v_list)  # Convert list back to dictionary
print("Sorted by values:", v_sort)  # Print values-sorted dictionary