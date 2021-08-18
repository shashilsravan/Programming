def remove_pair(string):
    ptr = 1
    res = [string[0]]
    while ptr < len(string):
        if len(res) > 1 and string[ptr] == res[-1]:
            res.pop()
        else:
            res.append(string[ptr])
        ptr += 1
    return "".join(res)


string = input()
out_ = remove_pair(string)
print (out_)