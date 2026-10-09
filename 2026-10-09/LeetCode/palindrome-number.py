class Solution:
    def isPalindrome(self, x: int) -> bool:

        t=str(x)

        if x < 0:
            return False
        
        else:
            if t==t[::-1]:
                return True
            else:
                return False

        
        