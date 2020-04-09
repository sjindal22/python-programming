def isPalindrome(str_input):

  str_input = "".join(item for item in str_input if item.isalnum()).lower()
  return str_input == str_input[::-1]

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome("121ama121"))
print(isPalindrome("121"))
print(isPalindrome("0"))
print(isPalindrome("123"))
