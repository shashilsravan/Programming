def caeserEncrypt(string, key):
    key = key % 26
    result = []
    for each in string:
        total = ord(each) + key
        if total > 122:
            result.append(chr(96 + total % 122))
        else:
            result.append(chr(total))
    return result


print(caeserEncrypt("wxyz", 3))