from collections import defaultdict

n = int(input())
lis = [int(x) for x in input().split()]

count = 0
hashset = defaultdict(int)


for i in range(n):
    temp = lis[i] + pow(i+1, 2)
    hashset[temp] += 1

for i in range(n):
    temp = lis[i] - pow(i+1, 2)
    if temp in hashset:
        count += hashset[temp]

print(count)