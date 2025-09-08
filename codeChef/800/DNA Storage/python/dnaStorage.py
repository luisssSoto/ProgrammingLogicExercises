t = int(input())

while t > 0:
    n = int(input())
    s = input()
    # Your code goes here
    dna_dict = {
        "00":"A",
        "01":"T",
        "10":"C",
        "11":"G" }
    dna_str = ""
    i = 0
    while i < len(s):
        dna_code = s[i] + s[i + 1]
        dna_str += dna_dict[dna_code]
        i += 2
    print(dna_str)
    t -= 1

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''