class Solution:
    def isPalindrome(self, x: int) -> bool:
        if 0 <= x <= 9:
            return True
        if x > 9:
            y = int("".join(str(abs(x))[::-1]))
            if y == x:
                return True
        return False            

checkNum = Solution()
print(checkNum.isPalindrome(121))
print(checkNum.isPalindrome(-121))


