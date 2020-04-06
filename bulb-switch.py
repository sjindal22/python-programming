class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(n**0.5)

bulbsOn = Solution()
print(bulbsOn.bulbSwitch(9))
print(bulbsOn.bulbSwitch(26))

"""
Pattern:
for 1th bulb : 1
2nd : 1 0
3rd : 1 0 0
4th : 1 0 0 1
5th : 1 0 0 1 0
6th : 1 0 0 1 0 0
7th : 1 0 0 1 0 0 0
8th : 1 0 0 1 0 0 0 0
9th : 1 0 0 1 0 0 0 0 1
"""
