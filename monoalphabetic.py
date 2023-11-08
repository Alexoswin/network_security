import string

plaintext = "hello world oswin abcd"
key = "orangebcdfhijklmpqustuvwxyz"
cipher =""


for c in plaintext:
    if c in string.ascii_lowercase:
        index =ord(c)-ord('a')
        cipher = cipher + key[index]

    else:
        cipher = cipher +c
print(plaintext)
print()
print(cipher)
