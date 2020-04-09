def goatLatin(w):

  def check(w, i = 0):
    vowels = ['aeiouAEIOU']
  
    if w[0] not in vowels:
      w = w[1:] + w[0]
    return w + 'ma' + 'a'*(i+1)
  
  w = " ".join(check(w, i) for i, w in enumerate(w.split()))
  return w

print(goatLatin("peak Goat Latin"))
print(goatLatin("I speak Goat Latin"))
print(goatLatin("I"))
