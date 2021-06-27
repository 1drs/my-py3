# operator assignment https://www.youtube.com/watch?v=49KDyhzgCmA

a = 7
print("nilai a =", a)

a += 3 # artinya adalah a = a + 3
print("nilai a += 3 adalah", a)

a -= 3 # artinya adalah a = a - 3
print("nilai a -= 3 adalah", a)

a *= 5 # artinya adalah a = a * 5
print("nilai a *= 5 adalah", a)

a /= 7 # artinya adalah a = a / 7
print("nilai a /= 7 adalah", a)


b = 10
print("\nnilai b =", b)

b %= 4 # artinya b = b % 4
print("nilai b %= 4 adalah", b)

b = 10
print("\nnilai b =", b)

b //= 3 # artinya b = b // 3
print("nilai b //= 3 adalah", b)

a = 5
print("nilai a =", a)
a **= 3
print("nilai a **= 3 adalah", a)


# operasi bitwise
# OR
c = True
print("\nnilai c adalah", c)
c |= False
print("nilai c |= False adalah", c)
c = False
print("nilai c adalah", c)
c |= False
print("nilai c |= False adalah", c)

# AND
c = True
print("\nnilai c adalah", c)
c &= False
print("nilai c &= False adalah", c)
c = False
print("nilai c adalah", c)
c &= False
print("nilai c &= False adalah", c)

# XOR
c = True
print("\nnilai c adalah", c)
c ^= False
print("nilai c ^= False adalah", c)
c = False
print("nilai c adalah", c)
c ^= False
print("nilai c ^= False adalah", c)

# geser
d = 0b0100
print("\nnilai d =", format(d, '04b'))
d >>= 2
print("nilai d >>= 2 adalah", format(d, '04b'))

d = 0b0100
print("\nnilai d =", format(d, '04b'))
d <<= 1
print("nilai d <<= 1 adalah", format(d, '04b'))
