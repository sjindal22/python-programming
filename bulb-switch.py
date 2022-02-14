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

There are n bulbs that are initially off. You first turn on all the bulbs. 
Then, you turn off every second bulb. On the third round, you toggle every 
third bulb (turning on if it's off or turning off if it's on). For the ith 
round, you toggle every i bulb. For the nth round, you only toggle the last 
bulb. Find how many bulbs are on after n rounds.
"""
