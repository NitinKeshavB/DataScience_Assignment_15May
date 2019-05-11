def ifpalindrome(val):
    if val == val[::-1]:
        return "val is palindrome"
    else:
        return "val is not palindrome"