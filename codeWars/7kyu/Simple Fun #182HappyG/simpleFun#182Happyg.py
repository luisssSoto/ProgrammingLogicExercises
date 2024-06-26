"""Simple Fun #182:Happy"g"""
def happy_g(st):
    is_happy_g = False
    checks = st.count('g')
    count = 0
    if checks == 0:
        is_happy_g = True
        return is_happy_g
    else:
        for i in range(len(st)):
            if st[i] == 'g':
                if i == 0:
                    if st[i] == st[i+1]:
                        count += 1
                        continue
                    else:
                        return is_happy_g
                elif i < len(st)-1:
                    if st[i] == st[i+1] or st[i] == st[i-1]:
                        count += 1
                        continue
                    else:
                        return is_happy_g
                else:
                    if st[i] == st[i-1]:
                        count += 1
                        continue
                    else:
                        return is_happy_g
    if checks == count:
        is_happy_g = True
        return is_happy_g
        
test1 = "gg0gg3gg0gg"
test2 = "gog"
test3 = "ggg ggg g ggg"
test4 = "A half of a half is a quarter."
print(happy_g(test4))