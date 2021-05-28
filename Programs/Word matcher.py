def patternMatcher(pattern: str, string: str):
    if not string or not pattern:
        return False
    strings = string.split()
    if len(pattern) != len(strings):
        return False
    str2pat = {}
    pat2str = {}
    for i in range(len(pattern)):
        if strings[i] in str2pat:
            if str2pat[strings[i]] != pattern[i]:
                return False
        else:
            str2pat[strings[i]] = pattern[i]

        if pattern[i] in pat2str:
            if pat2str[pattern[i]] != strings[i]:
                return False
        else:
            pat2str[pattern[i]] = strings[i]
    print(str2pat)
    return True


print(patternMatcher("xyyx", "dog cat cat fish"))