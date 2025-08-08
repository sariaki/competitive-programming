
def isPalindrome(s: str) -> bool:
    cpy = ""
    ls = len(s)

    for i in range(ls):
        if not s[i].isalnum():
            continue
        cpy += s[i].lower()
        #cpy += chr(ord(s[i]) - ord('A')+ord('a'))
    
    lc = len(cpy)
    if lc == 1:
        return True

    for i in range(lc // 2):
        if cpy[i] != cpy[lc-1-i]:
            return False
    return True

# print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("a."))