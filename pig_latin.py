'''
If the word starts with a vowel append ay to the end of the word otherwise     
add remove and append first letter of the word to the end and then append ay  
'''

# Approach 1

def pig_latin(myword):
  split_word = list(myword)
  if split_word[0] not in ['a', 'e', 'i', 'o', 'u']:
    split_word.append(split_word[0])
    split_word.pop(0)
    myword = ''.join(split_word)
  return(myword + 'ay')

print(pig_latin('word'))
print(pig_latin('apple'))

# Approach 2
def ping_latin_2(word):
  first_word = word[0]
  if first_word in 'aeiou':
    return word + 'ay'
  else:
    return(word[1:] + first_word + 'ay')

print(ping_latin_2('iamshivika'))
print(ping_latin_2('myword'))

# Approach 3
words = ['word', 'apple', 'Iam', 'Ian', 'Dorsey']
l1 = [w+'ay' if w[0] in 'aeiouAEIOU' else (w[1:] + w[0] + 'ay') for w in words]
print(l1)
