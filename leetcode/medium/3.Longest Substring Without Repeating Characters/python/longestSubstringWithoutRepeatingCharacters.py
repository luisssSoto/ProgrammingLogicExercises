"""Longest Substring Without Repeating Characters"""
# Approach 1. Sliding Window
def length_of_longest_substring(s):
    greatest_len = 0
    sub_str = ""
    begin_win = 0
    end_win = 0
    while end_win < len(s):
        if s[end_win] not in sub_str:
            sub_str += s[end_win]
        elif s[end_win] in sub_str:
            if len(sub_str) > greatest_len:
                greatest_len = len(sub_str)
            was_it_found = False
            while was_it_found == False:
                if s[begin_win] == s[end_win]:
                    was_it_found = True
                begin_win += 1
            sub_str = s[begin_win : end_win]
            sub_str += s[end_win]
        end_win += 1
    if len(sub_str) > greatest_len: 
            greatest_len = len(sub_str)
    return greatest_len

# Testing
s0 = "abcabcbb"
s1 = "bbbbb"
s2 = "pwwkew"
s3 = " "
s4 = "au"
print(s4[1])
new_s = s2[0 : 3]
print(new_s)
print(type(new_s))
new_list = []
new_s.split()
print("a" not in s0)
print(length_of_longest_substring(s4))