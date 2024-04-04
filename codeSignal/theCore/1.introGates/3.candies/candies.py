def solution(n,m):
    m = m - (m % n) 
    return m

print(solution(3, 10))