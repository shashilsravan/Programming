def function(string):
    mapSet = {}
    start = 0
    result = 0

    for i, each in enumerate(string):
        if each in mapSet:
            start = max(mapSet[each], start)
        result = max(result, i - start + 1)
        mapSet[each] = i + 1
    return result


print(function("abcdeafbdgcbb"))