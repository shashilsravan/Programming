def isValid(s):
    if len(s) % 2 == 1:
        return False
    array = []
    for each in s:
        if each in ['(', '[', '{']:
            array.append(each)
        else:
            if not array:
                return False
            current = array.pop()
            if current == '(' and each != ')':
                return False
            elif current == '[' and each != ']':
                return False
            elif current == '{' and each != '}':
                return False
    return len(array) == 0