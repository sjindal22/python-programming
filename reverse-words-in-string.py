def revWordsInString(s):

  s = list(" ".join(i[::-1] for i in ("".join(s[::-1])).split(" ")))
  return s

print(revWordsInString(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]))
