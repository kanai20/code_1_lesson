def palindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False

a = input()
print(palindrome(a))


