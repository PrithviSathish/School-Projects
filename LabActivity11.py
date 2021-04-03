def ispalindrome(item):
    temp = item
    item = item[::-1]
    if temp == item:
        return True
    else:
        return False

print(ispalindrome("hello"))

