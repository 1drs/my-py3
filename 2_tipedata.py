# angka (integer)
data_integer = 3
print("data : ", data_integer, ", tipe : ", type(data_integer))


# desimal / angka dengan koma (float)
data_float = 1.315
print("data : ", data_float, ", tipe : ", type(data_float))


# kumpulan karakter (string)
data_string = "kamus"
print("data : ", data_string, ", tipe : ", type(data_string))


# biner true/false (boolean)
data_bool = True
print("data : ", data_bool, ", tipe : ", type(data_bool))


# bilangan kompleks
data_complex = complex(5,6)
print("data : ", data_complex, ", tipe : ", type(data_complex))


# tipe data dari bahasa C
from ctypes import c_double
data_c_double = c_double(10.5)
print("data : ", data_c_double, ", tipe : ", type(data_c_double))
