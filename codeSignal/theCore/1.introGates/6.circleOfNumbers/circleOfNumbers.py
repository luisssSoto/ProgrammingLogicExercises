""" circle of numbers """

def solution(n, first_number):
    numbers_circle = [i for i in range(n)]
    index_first_number = numbers_circle.index(first_number)
    per_circle = len(numbers_circle)
    distance_between_two_numbers = (per_circle - 2) // 2
    checking_index_opposite_number = (index_first_number + distance_between_two_numbers + 1) % per_circle
    opposite_number = numbers_circle[checking_index_opposite_number]
    return opposite_number
    

print([x for x in range(10)])
print(solution(10, 7))
