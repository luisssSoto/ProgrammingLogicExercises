"""Minimum Index Sum Of Two Lists"""

def finde_restaurant(list1, list2):
    min_index_sum = len(list1) - 1 + len(list2) + 1
    index_sum_dict = {}
    least_index_letters_list = []
    for i in range(len(list1)):
        if list1[i] in list2:
            sum_letters = i + list2.index(list1[i])
            index_sum_dict[list1[i]] = sum_letters
            if sum_letters < min_index_sum:
                min_index_sum = sum_letters
    for (key,val) in index_sum_dict.items():
        if val == min_index_sum:
            least_index_letters_list.append(key)
    return least_index_letters_list

'''Complexity Analysis:
Time Complexity: O(N * M)
Space Complexity: O(N)'''
