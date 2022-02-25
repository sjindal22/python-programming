from collections import OrderedDict

d = {}
d['a'] = 2
d['b'] = 3
d['c'] = 1
d['d'] = 9

ordered = OrderedDict()
ordered['a'] = 0
ordered['b'] = 1
ordered['c'] = 4
ordered['d'] = 5

# Prints in the order key and values were receievd.
for i, v in ordered.items():
    print(i,v)

print("----")

#Prints in random order

for i,v in d.items():
    print(i,v)

