
def extra_candy (n, candies, extra_candies):
    res = []
    maxEle = max(candies)
    for each in candies:
        if each + extra_candies >= maxEle:
            res.append(1)
        else:
            res.append(0)
    return res

n = int(input())
candies = list(map(int, input().split()))
extra_candies = int(input())

out_ = extra_candy(n, candies, extra_candies)
print (' '.join(map(str, out_)))