# def groupAnagrams(array):
#     hashset = {}
#     for each in array:
#         sortedEach = "".join(sorted(each))
#         if sortedEach in hashset:
#             hashset[sortedEach].append(each)
#         else:
#             hashset[sortedEach] = [each]
#     return list(hashset.values())

from collections import defaultdict


def groupAnagrams(array):
    hashset = defaultdict(list)
    for each in array:
        temp = "".join(sorted(each))
        hashset[temp].append(each)
    return [sorted(v) for v in hashset.values()]


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(groupAnagrams(["a"]))
