"""Counting Valleys"""
def countingValleys(steps, path):
    # Write your code here
    sea_level = 0
    is_it_valley = False
    valleys = 0
    for step in path:
        if step == "U":
            sea_level += 1
        elif step == "D":
            sea_level -= 1
        if sea_level == -1:
            is_it_valley = True
        if is_it_valley == True and sea_level == 0:
            is_it_valley = False
            valleys += 1
    return valleys

valleys = "UDDDUDUU"
print(countingValleys(8, valleys))