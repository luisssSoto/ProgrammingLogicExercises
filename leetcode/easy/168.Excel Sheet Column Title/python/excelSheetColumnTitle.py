def convert_to_title(column_number: int) -> str:
        ans = ""
        while column_number > 0:
            column_number -= 1
            letter = chr(column_number % 26 + ord("A"))
            ans = letter + ans
            column_number //= 26
        return ans

'''Complexity Analysis:
Time Complexity: O(Log26(Columnnumber))
Space Complexity: O(Log26(Columnnumber))'''
