def minRewards(array):
    rewards = [1 for _ in array]
    for i in range(1, len(array)):
        if array[i] > array[i-1]:
            rewards[i] = rewards[i-1] + 1
    for i in range(len(array) - 2, -1, -1):
        if array[i] > array[i+1] and rewards[i] <= rewards[i+1]:
            rewards[i] = rewards[i+1] + 1
    return sum(rewards)


print(minRewards([8, 4, 2, 1, 3, 6, 7, 9, 5]))