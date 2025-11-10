class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
    
        palabra = str(x)
        n = len(palabra)

        for i in range(n // 2):
            if palabra[i] != palabra[n - i - 1]:
                return False
        
        return True


