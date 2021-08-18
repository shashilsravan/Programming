# def intersection(n1, n2, arr1, arr2):
#     result = []
#     ptr1 = 0
#     ptr2 = 0
#     while ptr1 < n1 and ptr2 < n2:
#         if arr1[ptr1] == arr2[ptr2]:
#             result.append(arr1[ptr1])
#             ptr1 += 1
#             ptr2 += 1
#         elif arr1[ptr1] < arr2[ptr2]:
#             ptr1 += 1
#         else:
#             ptr2 += 1
#     return result
#
# def array_intersection(n1, n2, n3, arr1, arr2, arr3):
#     intersected = intersection(n1, n2, arr1, arr2)
#     return intersection(len(intersected), n2, intersected, arr3)


def array_intersection(n1, n2, n3, arr1, arr2, arr3):
    x_loc = 0
    y_loc = 0
    z_loc = 0
    res = []
    while x_loc < n1 and y_loc < n2 and z_loc < n3:
        x = arr1[x_loc]
        y = arr2[y_loc]
        z = arr3[z_loc]
        if x == y and y == z:
            res.append(x)
            x_loc += 1
            y_loc += 1
            z_loc += 1
        elif x <= y and x <= z:
            x_loc += 1
        elif y <= x and y <= z:
            y_loc += 1
        elif z <= x and z <= y:
            z_loc += 1
    return res


print(array_intersection(7, 5, 5, [0, 1, 2, 2, 3, 7, 9], [1, 2, 3, 4, 5],
      [1, 2, 3, 3, 3]))