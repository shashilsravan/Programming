def findFibonacci(n):
    first = 0
    second = 1

    counter = 2
    while counter <= n:
        temp = first + second
        first = second
        second = temp
        counter += 1
    return second if n > 0 else first

print(findFibonacci(3))