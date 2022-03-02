
from collections import defaultdict
class Solution:

    def findDuplicate(self, paths: list) -> list:
        d = defaultdict(list)
        pop = [] # Files containing that content to be popped

        for each in paths:
            root = each.split(" ")[0]
            files = each.split(" ")[1:]
            for each in files:
                start,end = each.index('(')+1, each.index(')')
                d[each[start:end]].append(root+ '/' + each[:start-1])

        # Keep only those files that have duplicated content        
        for i, v in d.items():
            if len(v) > 1:
                continue
            else:
                pop.append(i)

        for i in pop:
            d.pop(i)

        return list(d.values())[::-1]

paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]

sol = Solution()
print(sol.findDuplicate(paths))

'''
Input: ["root/a 1.txt(abcd) 2.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh)"]
Output: []
'''
