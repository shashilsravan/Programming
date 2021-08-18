def sort_square(n, arr):
    neg = []
    pos = []
    res = []
    for each in arr:
        if each > -1:
            pos.append(each)
        else:
            neg.append(each)

    ptr1 = 0
    ptr2 = len(neg) - 1

    while ptr1 < len(pos) and ptr2 >= 0:
        pos_ptr = pow(pos[ptr1], 2)
        neg_ptr = pow(neg[ptr2], 2)
        if pos_ptr < neg_ptr:
            res.append(pos_ptr)
            ptr1 += 1
        else:
            res.append(neg_ptr)
            ptr2 -= 1
    while ptr1 < len(pos):
        res.append(pow(pos[ptr1], 2))
        ptr1 += 1
    while ptr2 >= 0:
        res.append(pow(neg[ptr2], 2))
        ptr2 -= 1
    return res


n = int(input())
arr = list(map(int, input().split()))

out_ = sort_square(n, arr)
print(' '.join(map(str, out_)))