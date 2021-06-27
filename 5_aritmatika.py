a = 6
b = 3

# tambah +

hasil = a + b
print(a, '+', b, '=', hasil)

# kurang -

hasil = a - b
print(a, '-', b, '=', hasil)

# kali *

hasil = a * b
print(a, '*', b, '=', hasil)

# bagi /

hasil = a / b
print(a, '/', b, '=', int(hasil))

# exponen (pangkat) **

hasil = a ** b
print(a, '**', b, '=', hasil)

# modulus (sisa bagi) **

hasil = a % b
print(a, '%', b, '=', hasil)

# floor division (kebalikan modulus) **

hasil = a // b
print(a, '//', b, '=', hasil)

# Priotitas operasi, operational precedence

'''
    1. ()
    2. exponen **
    3. perkalian * / ** % //
    4. pertambahan & pengurangan + -
'''


x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x, "**", y, "*", z, "+", x, "/", y, "-", y, "%", z, "//", x, "=", hasil)
print("   9  " , "*", z, "+", x, "/", y, "-", y, "%", z, "//", x, "=", hasil)
print("      36  ", "+", " 1.5 ", "-", "  0", "  //", x, "=", hasil)
print("      36  ", "+", " 1.5 ", "-", "     0    ", "=", hasil)


hasil = (x + y) ** z
print("(", x, "+", y, ") **", z, "=", hasil)
