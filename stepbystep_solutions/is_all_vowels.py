def is_all_vowels(s):
    vowels = 'AEIOUaeiou'
    count=0
    for i in s:
        if (i in vowels):
            count += 1
    if(count==len(s)):
        return True
    else:
        return False