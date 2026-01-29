"""Flipping An Image"""

def flipping_an_image(image: list[list[int]]) -> list[list[int]]:
    for i in range(len(image)):
        for j in range(len(image[i])):
            if image[i][j] == 1:
                image[i][j] = 0
            else:
                image[i][j] = 1
        image[i] = image[i][::-1]
    return image

'''Complexity Analysis: 
Time Complexity: O(N * M)
Space Complexity: O(1)'''