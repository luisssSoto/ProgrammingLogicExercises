l = ['1,', '2,', '3,', 'None,', 'None,', '4,', '5,']
s = "".join(l)
print(s)
s = s.rstrip(',')
sp = s.split(",")
print(sp)