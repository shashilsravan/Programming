def validPalindrome(s):
    def isPalindrome(i, j):
        if i >= j:
            return True
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            if isPalindrome(i+1, j) or isPalindrome(i, j-1):
                return True
            else:
                return False
    return True


print(validPalindrome("abczdcba"))
# should return true