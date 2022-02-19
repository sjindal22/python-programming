def minTimeDiff(timeSlots: list) -> int:

    minList = []
    for time in timeSlots:
        t = int(time[:2])*60+int(time[3:])
        minList.append(t)
    length = len(timeSlots)
    minList.sort()
    res = 1440 - (minList[length-1] - minList[0])
    for i in range(1, length):
        res = min(res, (minList[i] - minList[i-1]))
    return res

print(minTimeDiff(["23:59","00:00"]))
print(minTimeDiff(["00:00","23:59","00:00"]))
print(minTimeDiff(["00:00","00:00","23:59"]))
print(minTimeDiff(["23:58","00:00","00:00"]))

'''
o/p:
1
0
0
0

The approach is to convert each element into total mins, which is done in #5.
We then sort the list followed by getting the result of difference between last
and first element. This is only because we can have the for loop starting from
the the 2nd element all the way to the end. [Yes, there will be an issue if you
don't start from the 2nd element.
'''
