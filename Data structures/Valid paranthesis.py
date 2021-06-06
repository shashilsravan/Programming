class ValidParanthesis:
    def __init__(self):
        self.stack = []

    def isValid(self, s):
        for each in s:
            if each in ["(", "[", "{"]:
                self.stack.append(each)
            else:
                if not self.stack:
                    return False

                current = self.stack.pop()
                print(current, each)
                if current == '(' and each != ')':
                    return False
                elif current == '[' and each != ']':
                    return False
                elif current == '{' and each != '}':
                    return False

        return True if not self.stack else False



test = ValidParanthesis()
print(test.isValid("(]"))