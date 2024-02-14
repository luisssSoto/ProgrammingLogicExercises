def solution(statues):
    statues.sort()
    statuesAreMissing=0
    for numberOfStatue in range(len(statues)-1):
        less=statues[numberOfStatue]
        greater=statues[numberOfStatue+1]
        differenceBetweenBoth=greater-less
        if differenceBetweenBoth > 1:
            statuesAreMissing+=differenceBetweenBoth-1
    return statuesAreMissing

print(solution([5,3,7,4,2]))