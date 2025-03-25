def generate(numRows):
    main_array = [[1]]
    for i in range(numRows - 1):
        temp_array = [0] + main_array[-1] + [0]
        sub_array = []
        for j in range(len(temp_array) - 1):
            new_element = temp_array[j] + temp_array[j + 1]
            sub_array.append(new_element)
        main_array.append(sub_array)
    return main_array


# Testing
test_data1 = 5
expected1 = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
print(generate(test_data1))
a1 = [1,2,3]
a2 = a1[:]
a1.pop()
print(a1)
print(a2)