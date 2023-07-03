def switch_pairs(s):
    result = ''
    i = 0
    if len(s) < 2:
        return s
    while i < len(s) - 1:
        result += s[i + 1]
        result += s[i]
        i += 2
    if len(s) % 2 != 0:
        result += s[-1]
    return result