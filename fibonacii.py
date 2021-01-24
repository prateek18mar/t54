# Code for fibonacci series for 10 numbers
# (0, 1, 2, 3, 5)
fiblist = []


def fib(y=10):
    i = 0
    j = 1
    for x in range(2, y):
        k = i + j
        i = j
        j = k
        fiblist.append(j)
    print(fiblist)


fib()
