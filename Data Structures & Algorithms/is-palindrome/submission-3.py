class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:

            while left < right and not s[left].isalnum(): #skips over blank spaces(non-characters)
                left +=1

            while left < right and not s[right].isalnum(): 
                right -=1

            if s[left].lower() != s[right].lower(): #returns false is they aren't equal
                return False

            left +=1
            right -=1

        return True 