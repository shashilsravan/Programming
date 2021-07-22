def climbStairs(n):
    if n < 3:
        return n
    first = 1
    second = 2
    while n > 2:
        temp = first + second
        first = second
        second = temp
        n -= 1
    return second

print(climbStairs(4))