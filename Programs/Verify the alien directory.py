def is_lexicographic (key, n, string):
    hashmap = {}
    for index, each in enumerate(key):
        hashmap[each] = index

    for i in range(n-1):
        j = 0
        while j != len(string[i]) and j!= len(string[i+1]) and string[i][j] == string[i+1][j]:
            j += 1
        if j == len(string[i]):
            continue
        if j == len(string[i+1]): return 0
        if hashmap[string[i][j]] > hashmap[string[i+1][j]]: return 0
    return 1

key = input()
n = int(input())
string = []
for _ in range(n):
    string.append(input())

out_ = is_lexicographic(key, n, string)
print(out_)