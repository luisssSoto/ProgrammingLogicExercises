"""Migratory Birds"""

def migratory_birds(arr):
    greatest_freq_birds = {}
    for bird in arr:
        if bird in greatest_freq_birds:
            greatest_freq_birds[bird] += 1
        else:
            greatest_freq_birds[bird] = 0
    max_freq_birds = 0
    type_birds = []
    for bird in greatest_freq_birds:
        if greatest_freq_birds[bird] > max_freq_birds:
            max_freq_birds = greatest_freq_birds[bird]
            type_birds = []
            type_birds.append(bird)
        elif greatest_freq_birds[bird] == max_freq_birds:
            type_birds.append(bird)
    return min(type_birds)

'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''