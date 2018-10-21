def encrypt(offset, text):
    cipher = ""

    for i in text:
        if i.isspace():
            cipher += ' '
            continue
        ans = chr(ord('a') + (ord(i.lower()) - ord('a') + offset) % 26)
        if i.isupper():
            cipher += ans.upper()
            continue
        cipher += ans
    return cipher


def decrypt(offset, text):
    return encrypt(-offset, text)
