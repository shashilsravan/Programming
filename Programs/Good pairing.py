def good_pairs (n, arr):
    hashmap = {}
    count = 0
    for each in arr:
        if each in hashmap:
            count += hashmap[each]
            hashmap[each] += 1
        else:
            hashmap[each] = 1
    return count


n = int(input())
arr = list(map(int, input().split()))

out_ = good_pairs(n, arr)
print (out_)