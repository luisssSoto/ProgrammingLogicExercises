"""Jumping On The Clouds"""
def jumping_on_clouds(c):
    count_jumps = 0
    consecutive_cumulus = 0
    for i in range(len(c)-1):
        if c[i] == 0 and c[i+1] == 1:
            count_jumps += 1
            consecutive_cumulus = 0
        if c[i] == 0 and c[i+1] == 0:
            count_jumps += 1
            consecutive_cumulus += 1
        if consecutive_cumulus == 2:
            count_jumps -= 1
            consecutive_cumulus = 0
    return count_jumps
    
            

'''
1.
input: binary array
output: integer which corresponds the minimum jumps to win

2. 
create a list to index the 0 position
create a count jumps
iterate array with for loop
    conditional statement whether next element is zero
        add the index
count_jumps = length of list_index
count_not_consecutive
iterate index since 1
    if next index == current inde + 1 
    count_not_consecutive += 1
    if count_consecutive == 2:
        count_jumps -= 1
        count_consecutive = 0

3.
count_jumps = -1
consecutive_cumulus = 0
for i in range(len(arr)):
    if arr[i] == 0:
        count_jumps += 1
        consecutive_cumulus += 1
    else:
        consecutive_cumulus = 0
    if consecutive_cumulus == 3:
        count_jumps -= 1
        consecutive_cumulus = 0

4.happy coding

'''
