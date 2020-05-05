from collections import defaultdict

def groupAnagrams(l1):

  d = defaultdict(list)
  for item in l1:
    d[str(sorted(item))].append(item)
  
  return list(d.values())

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) 
