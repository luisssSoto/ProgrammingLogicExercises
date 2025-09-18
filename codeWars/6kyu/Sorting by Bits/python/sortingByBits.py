"""Sorting By Bits"""
def sort_by_bit(arr): 
    # your code
    bits_dict = {}
    for i in range(len(arr)):
        bits = sum(1 for n in bin(arr[i]) if n == "1")
        if bits not in bits_dict:
            bits_dict[bits] = []
            bits_dict[bits].append(arr[i])
        else:
            bits_dict[bits].append(arr[i])
    print(bits_dict)
    for (key, val) in bits_dict.items():
        if len(bits_dict[key]) > 1:
            bits_dict[key].sort()
    print(bits_dict)
    i = 0
    bits = 0
    while i < len(arr):
        if bits in bits_dict:
            for num in bits_dict[bits]:
                arr[i] = num
                i += 1
        bits += 1
    print(arr)
    
        