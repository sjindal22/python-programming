def rotateString(s: str, goal: str) -> bool:

    for i in range(len(s)):
        s = s[1:] + s[:1]
        if s == goal:
            return True
    return False

print(rotateString(s = "abcde", goal = "cdeab"))
print(rotateString(s = "abcde", goal = "abced"))

'''
O/P:
True
False
'''
