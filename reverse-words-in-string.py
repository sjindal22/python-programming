def revWordsInString(s):

    s = " ".join(w for w in s.split()[::-1])
    return f'"{s}"'

print(revWordsInString(s = "the sky is blue"))
print(revWordsInString(s = "  hello world  "))
print(revWordsInString(s = "a good   example"))
