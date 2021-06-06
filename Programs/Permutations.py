def permutate(nums):
    l = len(nums)
    ans = []
    used = [False] * l

    def dfs(cur, d):
        if d == l:
            ans.append(cur.copy())
            return

        for i in range(l):
            if used[i]:
                continue
            used[i] = True
            cur.append(nums[i])
            dfs(cur, d + 1)
            cur.pop()
            used[i] = False

    dfs([], 0)
    return ans


print(permutate([1, 2, 3]))