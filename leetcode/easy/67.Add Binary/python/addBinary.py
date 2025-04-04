
# 1. cast a and b to decimal numbers
# 2. sum each other
# 3. cast again to binary
# 4. return it
def add_binary(a, b):
    dec_a = 0
    dec_b = 0
    count = 0
    for i in range(len(a) - 1, -1, -1):
        if int(a[i]) == 1:
            dec_a += 2 ** count
        count += 1
    count = 0
    for i in range(len(b) - 1, -1, -1):
        if int(b[i]) == 1:
            dec_b += 2 ** count
        count += 1
    result = dec_a + dec_b
    if result == 0:
        return '0'
    bin_num_list = []
    while result >= 1:
        if result % 2 == 0:
            bin_num_list.insert(0, '0')
        else: 
            bin_num_list.insert(0, '1')
        result //= 2
    bin_num = ''
    for bi in bin_num_list:
        bin_num += bi
    return bin_num

test_a = '1010'
test_b = '1011'
print(add_binary(test_a, test_b))


# More pythonistic
def add_binary1(a, b):
    dec_a, dec_b, count = 0, 0, 0
    for i in range(len(a) - 1, -1, -1):
        if a[i] == '1':
            dec_a += 2 ** count
        count += 1
    count = 0
    for i in range(len(b) - 1, -1, -1):
        if b[i] == '1':
            dec_b += 2 ** count
        count += 1
    bin_num = bin(dec_a + dec_b)
    str_bin = bin_num[2:]
    return str_bin
    

print(add_binary1(test_a,test_b))
