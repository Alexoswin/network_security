p = int(input("Enter the first prime number: "))
q = int(input("Enter the second prime number: "))
e = int(input("Enter the value of e: "))
m = int(input("Enter the value of m: "))

n = p * q
print("n:", n)

totient_function = (p - 1) * (q - 1)
print("Totient function (phi):", totient_function)

d = None
for k in range(1, n):
    if (1 + k * totient_function) % e == 0:
        d = (1 + k * totient_function) // e
        break

if d is None:
    print("No valid d found")
else:
    print("Value of d is", d)

c = pow(m, e, n)
print("Encrypted message (c):", c)
decrypted = pow(c, d, n)
print("Decrypted message (m):", decrypted)

