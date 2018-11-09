from string import ascii_lowercase


def encrypt(offset, text):
    cipher = ''

    for i in text:
        if i not in ascii_lowercase and i not in ascii_lowercase.upper():
            cipher += i
            continue
        tmp1 = ord(i.lower()) - ord('a') + offset
        ans = chr(ord('a') + tmp1 % 26)
        if i.isupper():
            cipher += ans.upper()
            continue
        cipher += ans
    return cipher


def decrypt(offset, text):
    return encrypt(-offset, text)
