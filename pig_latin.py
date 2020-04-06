def pig_latin(myword):
  split_word = list(myword)
  if split_word[0] not in ['a', 'e', 'i', 'o', 'u']:
    split_word.append(split_word[0])
    split_word.pop(0)
    myword = ''.join(split_word)
  return(myword + 'ay')

print(pig_latin('word'))
print(pig_latin('apple'))

def ping_latin_2(word):
  first_word = word[0]
  if first_word in 'aeiou':
    return word + 'ay'
  else:
    return(word[1:] + first_word + 'ay')

print(ping_latin_2('iamshivika'))
print(ping_latin_2('myword'))
