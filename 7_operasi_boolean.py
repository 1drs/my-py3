# not, or, and, xor

print("--- NOT ---")

a = False
c = not a
e = not (not a)
g = not c
print('data a =', a)
print("---")
print('data c =', c)
print("---")
print('data e =', e)
print("---")
print('data g =', g)


print("--- OR ---")
# jika salah satu True maka hasilnya True
a = False
b = False
c = a or b
e = a or b or c
print(a, "OR", b, "=", c)
print(a, "OR", b, "OR", c, "=", e)


a = False
b = True
c = a or b
e = a or b or c
print(a, "OR", b, " =", c)
print(a, "OR", b, "OR", c, "=", e)

a = True
b = False
c = a or b
e = a or b or c
print(a, " OR", b, "=", c)
print(a, "OR", b, "OR", c, "=", e)

a = True
b = True
c = a or b
e = a or b or c
print(a, " OR", b, " =", c)
print(a, "OR", b, "OR", c, "=", e)


print("--- AND ---")
# jika dua buah nilai True maka hasilnya True
a = False
b = False
c = a and b
print(a, "AND", b, "=", c)

a = False
b = True
c = a and b
print(a, "AND", b, " =", c)

a = True
b = False
c = a and b
print(a, " AND", b, "=", c)

a = True
b = True
c = a and b
print(a, " AND", b, " =", c)


print("--- XOR ---")
# jika salah satu True maka hasilnya True
a = False
b = False
c = a ^ b
print(a, "XOR", b, "=", c)

a = False
b = True
c = a ^ b
print(a, "XOR", b, " =", c)

a = True
b = False
c = a ^ b
print(a, " XOR", b, "=", c)

a = True
b = True
c = a ^ b
print(a, " XOR", b, " =", c)
