def sockMerchant(n, ar):
    # Write your code here
    set_socks = set(ar)
    if len(set_socks) == len(ar):
        return 0
    else:
        pair_socks = {}
        for sock in ar:
            if sock not in pair_socks:
                pair_socks[sock] = 1
            else:
                pair_socks[sock] += 1
        print(pair_socks)
        count_pair = 0
        for pair in pair_socks:
            if pair_socks[pair] % 2 == 0:
                count_pair += pair_socks[pair] // 2
            else:
                count_pair += (pair_socks[pair] - 1) // 2
        print(count_pair)
    return count_pair
        
socks1 = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print(sockMerchant(9, socks1))