from collections import Counter

def commonChars(words: list) -> list:
            
        temp = {}
        l = []
        y = ""
        
        for i, w in enumerate(words):
            count = {}
            count = dict(Counter(w)) 
            if i == 0: 
                temp = count
                continue
            for letter, v in count.items():
                if letter in temp.keys():
                    temp[letter] = min(v, count[letter])
            '''
            if this the end of the outer loop, then get the intersection of
            the final counter and the loop which is maintaining the min count
            This will result in the list with final common letters
            '''

            if i == (len(words) -1):
                count = list(set(temp.keys()) & set(count.keys()))

       #For taking the occurences of the cgaracters that are common
        for x,v in temp.items():
            if x in count:
                # multiply the letter with their occurences
                y = x*v
                l.append(y)
        y = "".join(l)
        return list(y)

print(commonChars(words = ["bella","label","roller"]))
print(commonChars(words = ["cool","lock","cook"]))

'''
O/P
['e', 'l', 'l']
['c', 'o', 'o']
'''
