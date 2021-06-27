# menyambung string

nama_awal = "Andi"
nama_tengah = "Surya"
nama_akhir = "Flame"

nama_lengkap = nama_awal + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

#menghitung panjang string
panjang = len(nama_lengkap)
print("jumlah karakter dari nama lengkap :", str(panjang))

#operator untuk string

#cek string di sebuah string
d = 'd'
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))

s = 's'
status = s not in nama_lengkap
print(s + " tidak ada di " + nama_lengkap + " = " + str(status))

#looping string
print("+"*10)

#indexing
print('nama lengkap', nama_lengkap)
print("index ke-0 : ", nama_lengkap[0])
print("index ke-1 : ", nama_lengkap[1])
print("index ke- (-1) : ", nama_lengkap[-1])
print("index ke- (-2) : ", nama_lengkap[-2])
print("index ke-[0:4] : ", nama_lengkap[0:4])
print("index ke-[5:10] : ", nama_lengkap[5:10])
print("\n" + "-"*10 + "\n")
angka = "123456789"
print("angka",angka)
print('index angka ganjil : ', angka[0:9:2])
print('index angka genap : ', angka[1:9:2])


print("\n" + "-"*10 + "\n")
#item terkecil
print('item terkecil : ' + min(nama_lengkap))
ascii_code_result = ord(min(nama_lengkap))
print("ASCII code  : " + str(ascii_code_result))
print("char unutk ASCII " + str(ascii_code_result) + " adalah " + chr(ascii_code_result))

#item terbesar
print('item terbesar : ' + max(nama_lengkap))
ascii_code_result = ord(max(nama_lengkap))
print("ASCII code  : " + str(ascii_code_result))
print("char unutk ASCII " + str(ascii_code_result) + " adalah " + chr(ascii_code_result))

print("\n" + "-"*10 + "\n")

#operator dalam bentuk method

data = 'otong surotong pararotong'
jumlah = data.count("o")
print("jumlah huruf o pada " + data + " adalah " + str(jumlah))

print("\n" + "="*10 + "\n")
## manipulasi string part 2

# ubah case dari string

# ubah ke semua up
salam = 'bro!'
print("normal mode = " + str(salam))
salam = salam.upper()
print("upper mode = " + str(salam))

salam = 'KuY!'
print("normal mode = " + str(salam))
salam = salam.lower()
print("lower mode = " + str(salam))

## pengecekan dengan isX method

# pengecekan lower case

salam = "sist"
cek_lower = salam.islower() # hasilnya bool
print(salam + " is lower = " + str(cek_lower))
cek_upper = salam.isupper() # hasilnya bool
print(salam + " is upper = " + str(cek_upper))

# isalpha() > huruf saja
# isalnum() > huruf dan angka
# isdecimal() > angka saja
# isspace() > spasi, tab, newline \n
# istitle() > semua kata dimulai dengan huruf besar

judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle() # bool
print(judul + " is title = " + str(cek_judul))

judul = "It's Okay Not To Be Orkay"
cek_judul = judul.istitle() # bool
print(judul + " is title = " + str(cek_judul))

## cek komponen startswith() endswith() >
cek_start = "ada aqua".startswith("ada")
print("starts with ada = " + str(cek_start))

cek_end = "ada aqua".endswith("qua")
print("end with qua = " + str(cek_end))

## penggabungan komponen join() split()
pisah = ["aku", "kamu", "dia"]
print(pisah)
gabung = ','.join(pisah)
print(gabung)
gabung = ' '.join(pisah)
print(gabung)

gabungan = "kamu+dia+mereka"
print(gabungan)
print(gabungan.split('+'))


## alokasi karakter
print(5*"=" + 'sample string' + 5*'=')

## alokasi karakter left, right, center
kanan = 'kanan'.rjust(30)
print("'" + kanan + "'")

kiri = 'kiri'.ljust(30)
print("'" + kiri + "'")

tengah = 'tengah'.center(30,"-")
print("'" + tengah + "'")

cap = 'kapital'.capitalize()
print('"' + cap + '"')
