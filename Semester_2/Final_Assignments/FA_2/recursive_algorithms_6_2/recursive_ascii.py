def encrypt(word, ascii=""):
    if not word:
        return ascii
    ascii += chr(ord(word[0]) + 3)
    return encrypt(word[1:], ascii)

print(encrypt("abc"))