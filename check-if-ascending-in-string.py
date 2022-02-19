# Method 1 - with using another list

def checkIfAscending(s: list) -> bool:

    x = -1
    l2 = [int(i) for i in s.split() if i.isnumeric()]
    for i in range(1,len(l2)):
        if l2[x+1] < l2[i]:
            continue
        else:
            return False

    return True

# Method 2 - using an int var (less memory usage)

def checkIfAscending_2(s: list) -> bool:

    prev = 0
    for s in s.split():
        if s.isnumeric() and prev:
            if prev < int(s):
                continue
            else:
                return False
        elif s.isnumeric():
            prev = int(s)
    return True

print(checkIfAscending('1 box has 3 blue 4 red 6 green and 12 yellow marbles'))
print(checkIfAscending(s = "hello world 5 x 5"))
print(checkIfAscending(s = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"))

print(checkIfAscending_2('1 box has 3 blue 4 red 6 green and 12 yellow marbles'))
print(checkIfAscending_2(s = "hello world 5 x 5"))
print(checkIfAscending_2(s = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"))

'''
O/P:
True
False
True
True
False
True

If using method 1, the trick is to filter only the digits and compare i+1, 
whre i is initialized to 0 with the next consecutive number in the list.

Method 2 involves utilizing only other int var which takes less memory and does
two nested if checks, if the item in the for loop is a digit but previous is none
and if it is a digit but previous is not None. This way, you would start from
the 1st element of the list.

'''
