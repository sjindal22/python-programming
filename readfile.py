with open("sample.txt", "r+") as f:
    data = f.readlines()
    print(data)
    for each in data:
        # split each line based on spaces. This results in a list
        word = each.split()
        print(word)

L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
with open("sample.txt", "a+") as f:

    f.write("Hello\n")
    f.writelines(L)

with open("sample.txt", "r") as f:
    data = f.read()
    print(data)

'''
File:

Mango banana apple pear
Banana grapes strawberry
Apple pear mango banana
Kiwi apple mango strawberry

O/P
['Mango banana apple pear\n', 'Banana grapes strawberry\n', 'Apple pear mango banana\n', 'Kiwi apple mango strawberry\n']
['Mango', 'banana', 'apple', 'pear']
['Banana', 'grapes', 'strawberry']
['Apple', 'pear', 'mango', 'banana']
['Kiwi', 'apple', 'mango', 'strawberry']
Mango banana apple pear
Banana grapes strawberry
Apple pear mango banana
Kiwi apple mango strawberry
Hello
This is Delhi 
This is Paris 
This is London 
'''

