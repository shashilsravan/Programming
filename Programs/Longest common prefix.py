def commonPrefix(str1, str2):
    result = ""
    n1 = len(str1) - 1
    n2 = len(str2) - 1
    i, j = 0, 0

    while i <= n1 and j <= n2:
        if str1[i] != str2[j]:
            break
        result += str1[i]
        i += 1
        j += 1
    return result

def longestCommonPrefix(strs):
    n = len(strs)
    prefix = strs[0]

    for i in range(1, n):
        prefix = commonPrefix(prefix, strs[i])

    if len(prefix): return prefix
    else: return ""