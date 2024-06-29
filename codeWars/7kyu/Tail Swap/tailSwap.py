"""Tail Swap"""
def tail_swap(strings):
    last_part_words = []
    begin_part_words = []
    for i in range(len(strings)):
        for j in range(len(strings[i])):
            if strings[i][j] == ':':
                last_part = strings[i][j:]
                last_part_words.insert(0, last_part)
                begin_part = strings[i][:j]
                begin_part_words.append(begin_part)
    strings[0] = begin_part_words[0] + last_part_words[0]
    strings[1] = begin_part_words[1] + last_part_words[1]
    return strings

test1 = ["abc:123", "cde:456"]
print(tail_swap(test1))

'''clever solution by: Zhenengxie,'''
def tail_swap(strings):
    head0, tail0 = strings[0].split(':')
    head1, tail1 = strings[1].split(':')
    return [head0 + ':' + tail1, head1 + ':' + tail0]