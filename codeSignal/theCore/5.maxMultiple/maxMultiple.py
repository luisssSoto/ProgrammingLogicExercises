def solution(divisor, bound):
    largest = 0
    for i in range(bound+1):
        if i % divisor == 0 and i > largest: largest = i
    return largest

print(solution(10, 50))