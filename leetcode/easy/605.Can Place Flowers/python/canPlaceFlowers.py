"""Can Place Flowers"""

def can_place_flowers(flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True
        elif len(flowerbed) == 1 and flowerbed[0] == 1:
            return False
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            n -= 1
        if n <= 0:
            return True
        else:
            return False
        
'''Complexity Analysis:
Time Complexity: O(N)
Space Complexity: O(1)'''