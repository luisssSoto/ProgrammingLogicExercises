"""Sparse Arrays"""

def matching_strings(string_list, queries):
    # Write your code here
    index = 0
    for query in queries:
        count = 0
        if query in string_list:
            for string in string_list:
                if query == string:
                    count += 1
            queries[index] = count
        else:
            queries[index] = count
        index += 1
    return queries

'''Complexity Analysis:
Time Complexity: O(N * M)
Space Complexity: O(1)'''