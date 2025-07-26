"""Dynamic Array"""

def dynamic_array(n, queries):
    new_arrays = [[x for x in range(0)]for _ in range(n)]
    index = 0
    last_answer = 0
    last_answers_list = []
    for query in queries:
        if query[0] == 1:
            index = (query[1] ^ last_answer) % n
            new_arrays[index].append(query[2])
        elif query[0] == 2:
            index = (query[1] ^ last_answer) % n
            last_answer = new_arrays[index][query[2] % len(new_arrays[index])]
            last_answers_list.append(last_answer)
    return last_answers_list

# Testing
n = 2
queries = [
[1, 0, 5],
[1, 1, 7],
[1, 0, 3],
[2, 1, 0],
[2, 1, 1]
]

print(dynamic_array(n, queries))