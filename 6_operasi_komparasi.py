# setiap hasil dari operasi komparasi hasilnya adalah boolean
# >, <, >=, <=, ==, !=, is, is not

print("--- lebih dari (>)")
a = 9
b = 7
hasil = a > b
print(a, ">", b, "=", hasil)
hasil = a > 9
print(a, ">", "9", "=", hasil)



print("--- kurang dari (<)")
a = 9
b = 7
hasil = a < b
print(a, "<", b, "=", hasil)
hasil = a < 9
print(a, "<", "9", "=", hasil)



print("--- lebih dari sama dengan (>=)")
a = 9
b = 7
hasil = a >= b
print(a, ">=", b, "=", hasil)
hasil = a >= 9
print(a, ">=", "9", "=", hasil)



print("--- kurang dari sama dengan (<=)")
a = 9
b = 7
hasil = a <= b
print(a, "<=", b, "=", hasil)
hasil = a <= 9
print(a, "<=", "9", "=", hasil)



print("--- sama dengan (==)")
a = 9
b = 7
hasil = a == b
print(a, "==", b, "=", hasil)
hasil = a == 9
print(a, "==", "9", "=", hasil)



print("--- tidak sama dengan (!=)")
a = 9
b = 7
hasil = a != b
print(a, "!=", b, "=", hasil)
hasil = a != 9
print(a, "!=", "9", "=", hasil)



print("--- object identities (is)")
#untuk non literal (antar object / variable)
a = 9
b = 7
c = 9
hasil = a is b
print(a, "is", b, "=", hasil)
hasil = a is c
print(a, "is", c, "=", hasil)



print("--- object identities (is not)")
#untuk non literal (antar object / variable)
a = 9
b = 7
c = 9
hasil = a is not b
print(a, "is not", b, "=", hasil)
hasil = a is not c
print(a, "is not", c, "=", hasil)
