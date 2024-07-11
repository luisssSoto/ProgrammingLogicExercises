"""Crawler Log Folder"""
def mini_operations(logs):
    steps_towards_main = 0
    for directory in logs:
        if directory == '../':
            steps_towards_main -= 1
            if steps_towards_main < 1:
                steps_towards_main = 0
        elif directory == './':
            continue
        else:
            steps_towards_main += 1
    return steps_towards_main

test1 = ["d1/","d2/","../","d21/","./"]
test2 = ["./","wz4/","../","mj2/","../","../","ik0/","il7/"]
print(mini_operations(test2))
#1. input: array
#   output: integer the steps you do to return the main directory

#2. iterate the array
#   three possible scenarios: ../ return one directory, ./stay in the same directory, x/go that directory
#   length the array
#   if ../ less -1
#   if ./ stay at the same place += 0
#   if is not equal ../ ./ += 1
#   the counter - 0 returns it 

#3. initialize a counter variable steps_forward = 0
#   iterate the array
#   conditional statement for every element:
#   if this element == '../' then steps_forward -= 1
#   elif this element == './' then steps_forward -= 0
#   else then steps_forward += 1
#   initialize a variable steps_back = steps_forward
#   returns steps_back

#4. but if steps_back is < than 0 returns 0