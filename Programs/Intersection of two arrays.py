def intersectionOfTwoArrays(nums1, nums2):
    hashmap = {}
    result = []

    for each in nums1:
        if each in hashmap:
            hashmap[each] += 1
        else:
            hashmap[each] = 1

    for each in nums2:
        if each in hashmap and hashmap[each] > 0:
            hashmap[each] -= 1
            result.append(each)

    return result


# print(intersectionOfTwoArrays([1, 2, 2, 1], [2, 2]))
print(intersectionOfTwoArrays([4, 9, 5], [9, 4, 9, 8, 4]))