tc1 = ['10101', '11100', '11010', '00101']
tc1 = [int(t, 2) for t in tc1]
print(tc1)
for i in range(len(tc1) - 1):
    for j in range(i + 1, len(tc1)):
         combined_topics = tc1[i] | tc1[j]
         print(combined_topics)
         b = (combined_topics.bit_count())
         print(b)