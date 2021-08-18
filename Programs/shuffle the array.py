def shuffle (n, arr):
    first = arr[:n]
    second = arr[n:]
    res = []
    ptr1 = 0
    ptr2 = 0
    while ptr1 < len(first) and ptr2 < len(second):
        res.append(first[ptr1])
        res.append(second[ptr2])
        ptr1 += 1
        ptr2 += 1
    return res

n = int(input())
arr = list(map(int, input().split()))

out_ = shuffle(n, arr)
print (' '.join(map(str, out_)))