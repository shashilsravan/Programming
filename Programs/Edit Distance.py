def editDistance(word1, word2):
    array = [[x for x in range(len(word1) + 1)] for _ in range(len(word2)+1)]

    for i in range(1, len(word2) + 1):
        array[i][0] = array[i-1][0] + 1

    for i in range(1, len(word2) + 1):
        for j in range(1, len(word1) + 1):
            if word2[i-1] == word1[j-1]:
                array[i][j] = array[i-1][j-1]
            else:
                array[i][j] = 1 + min(array[i-1][j],
                                      array[i][j-1], array[i-1][j-1])
    return array[-1][-1]

# def editDistance(word1, word2):
#     small = word1 if len(word1) < len(word2) else word2
#     big = word1 if len(word1) >= len(word2) else word2
#     evenEdits = [x for x in range(len(small) + 1)]
#     oddEdits = [None for x in range(len(small) + 1)]
#     for i in range(1, len(big)):
#         if i % 2 == 1:
#             currentEdits = oddEdits
#             previousEdits = evenEdits
#         else:
#             currentEdits = evenEdits
#             previousEdits = oddEdits
#         currentEdits[0] = i
#         for j in range(1, len(small) + 1):
#             if big[i-1] == small[j-1]:
#                 currentEdits[j] = previousEdits[j-1]
#             else:
#                 currentEdits[j] = 1 + min(previousEdits[j-1], previousEdits[j], currentEdits[j-1])
#
#     return evenEdits[-1] if len(big) % 2 == 0 else oddEdits[-1]



print(editDistance("abc", "yabd"))
