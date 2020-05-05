from collections import OrderedDict

class LruCache:

  def __init__(self, capacity):
    self.dict = OrderedDict()
    self.remain = capacity

  def get(self, key):
    if key not in self.dict:
      return -1

    v = self.dict.pop(key)
    self.dict[key] = v
    return v

  def put(self, key, value):
    if key in self.dict:
      self.dict.pop(key)

    else:
      if self.remain > 0:
        self.remain -= 1
      else:
        self.dict.popitem(last=False)

    self.dict[key] = value

cache = LruCache(2)

print(cache.put(1, 1))
print(cache.put(2, 2))
print(cache.get(1))  
print(cache.put(3, 3))
print(cache.get(2))       
print(cache.put(4, 4))    
print(cache.get(1))       
print(cache.get(3))      
print(cache.get(4))     

"""
None
None
1
None
-1
None
-1
3
4
""" 

