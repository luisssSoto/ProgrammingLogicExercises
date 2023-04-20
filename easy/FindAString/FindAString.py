def count_substring(string, sub_string):
    count=0
    findIt=string.find(sub_string)
    print(findIt)
    while findIt != -1:
        findIt=string.find(sub_string,findIt+1)
        count+=1
    return count

count = count_substring("ABCDCDCD", "CD")
print(count)