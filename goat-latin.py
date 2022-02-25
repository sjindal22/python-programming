'''
If the word starts with a vowel append ma to the end of the word otherwise
add remove and append first letter of the word to the end and then append ma.
With each succession of the word append that many 'a's. For example, first word
would be 'Imaa' for 'I', then 'ordwmaaa' for 'word'
'''

def goatLatin(words):

    l1 = " ".join(w+'ma'+'a'*(i+1) if w in 'aeiouAEIOU' else (w[1:]+w[0]+'ma'+'a'*(i+1)) for i, w in enumerate(words.split()))
    return l1

print(goatLatin("I"))
print(goatLatin("I speak Goat Latin"))
print(goatLatin("The quick brown fox jumped over the lazy dog"))
