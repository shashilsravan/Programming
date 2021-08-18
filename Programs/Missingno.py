# def missing_no (n, arr):
#     target_sum = (n * (n + 1))//2
#     sum_got = sum(arr)
#     return target_sum - sum_got
def missing_no(n, A):
    xor = 0
    for i in A:
        xor = xor ^ i
    for i in range(1, len(A) + 2):
        xor = xor ^ i
    return xor

n = int(input())
arr = list(map(int, input().split()))

out_ = missing_no(n, arr)
print (out_)