"""Perfect Squares"""

def perfect_squares(n: int) -> int:
    square_nums = [x * x for x in range(1, int(n ** 0.5) + 1)]
    level = 0
    queue = {n}
    while queue:
        level += 1
        next_queue = set()
        for remainder in queue:
            for square_num in square_nums:
                if remainder == square_num:
                    return level
                elif remainder < square_num:
                    break
                else:
                    next_queue.add(remainder - square_num)
        queue = next_queue
    return level

# testcase 
n1 = 12
print(perfect_squares(n1))
print(int(12 ** .5))