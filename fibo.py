def fiboSeries(n):
    if n < 0:
        return "Please enter a positive number"
    elif n <= 1:
        return n
    else:
        return (fiboSeries(n-1) + fiboSeries(n-2))
n = 10
x = [fiboSeries(i) for i in range(n)]
print(x)
