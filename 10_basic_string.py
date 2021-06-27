data = "ini adalah string"
print(data, "dengan tipe", type(data))

# 1. cara membuat string

'''
    Menggunakan single quote '...'
    Menggunakan double quote "..."
'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print("ini hari jum'at")


# 2. Menggunakan tanda \
print('ini hari jum\'at')

# tab
print("A\tB, jauhan")

# backspace
print("A \bB, deketan")

# new line
print("baris awal\nbaris akhir")


# 3. String literal atau raw

# raw
print(r'C:\new folder')

# multiline literal string
print("""
Nama\t: Andi
Alamat\t: Jogja
Status\t: Lajang / belum kawin
""")
