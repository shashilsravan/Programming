def two_sum (n, arr, target):
    hashmap = {}
    count = 0
    for each in arr:
        diff_sum = target - each
        if diff_sum in hashmap:
            count += hashmap[diff_sum]
        if each in hashmap:
            hashmap[each] += 1
        else:
            hashmap[each] = 1
    return count

n = int(input())
arr = list(map(int, input().split()))
target = int(input())

out_ = two_sum(n, arr, target)
print (out_)