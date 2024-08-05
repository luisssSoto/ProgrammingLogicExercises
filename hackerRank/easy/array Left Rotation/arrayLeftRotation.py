"""Array Left Rotation"""
def rot_left(a, d):
    for i in range(d):
        temp = a[0]
        a.append(temp)
        del a[0]
    return a

data1 = [x for x in range(1,6)]
print(data1)
print(rot_left(data1,4))
'''
1.
input integer array and integer number of rotations
output: sorted array according to the number of rotations towards left

2.
edge cases: nothing so far
key: iterate for loop in a range according d parameter
range(-1, -d, -1)
1 2 3 4 5
a[i] 



'''