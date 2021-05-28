def selfDividingNumbers(left: int, right: int):
    ans = []
    for i in range(left, right + 1):
        flag = 1
        if '0' not in str(i):
            for digit in str(i):
                if i % int(digit) != 0:
                    flag = 0
                    break
            if flag == 1: ans.append(i)
    return ans

print(selfDividingNumbers(100, 200))
print(selfDividingNumbers(1000, 2000))