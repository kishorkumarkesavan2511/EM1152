import struct
# Writing to a binary file with randomaccess 
with open("random.bin", "wb") as file:
    data = [100, 200, 300, 400, 500]
    for num in data:
        file.write(struct.pack("i", num)) 
        # Writing integers in binaryformat 

# Reading a specific record using random access
with open("random.bin", "rb") as file:
    file.seek(2 * struct.calcsize("i")) # Move to the 3rd integer (zero-based index) 
    value = struct.unpack("i", file.read(struct.calcsize("i")))[0]
    print("Value at 3rd position:", value)