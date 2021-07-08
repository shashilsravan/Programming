def isBadVersion(num):
    return num >= 1

def checkBadVersion(num):
    return isBadVersion(num-1) != isBadVersion(num)

def firstBadVersion(n):
    if checkBadVersion(n):
        return n
    left = 0
    right = n
    mid = (left + right)//2
    while True:
        if not isBadVersion(mid):
            left = mid
            mid = (left + right)//2
        else:
            if not checkBadVersion(mid):
                right = mid
                mid = (left+right)//2
            else:
                break
    return mid

print(firstBadVersion(1))