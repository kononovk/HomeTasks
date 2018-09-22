s = input("Input string: ").lower().replace(' ', '')
if s == s[::-1]:
    print("This string is palindrome")
else:
    print("This string is not palindrome")
