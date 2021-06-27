# merubah satu tipe ke tipe lain


print("---INTEGER---")

data_int = 3
print("data", data_int, "dengan tipe", type(data_int), "akan menjadi :")

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)

print("-> data", data_float, "bertipe", type(data_float))
print("-> data", data_str, "bertipe", type(data_str))
print("-> data", data_bool, "bertipe", type(data_bool) , "\n" ) # akan bernilai false ketika bernilai 0



print("---FLOAT---")

data_float = 0.3
print("data", data_float, "dengan tipe", type(data_float), "akan menjadi :")

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)

print("-> data", data_int, "bertipe", type(data_int))
print("-> data", data_str, "bertipe", type(data_str))
print("-> data", data_bool, "bertipe", type(data_bool) , "\n" ) # akan bernilai False ketika bernilai 0




print("---BOOLEAN---")
data_bool = True
print("data", data_bool, "dengan tipe", type(data_bool), "akan menjadi :")

data_int = int(data_bool) # bernilai 1 ketika bool bernilai True, dan bernilai 0 ketika bool bernilai False
data_str = str(data_bool) # bernilai "True" ketika bool bernilai True
data_float = float(data_bool)

print("-> data", data_int, "bertipe", type(data_int))
print("-> data", data_str, "bertipe", type(data_str))
print("-> data", data_float, "bertipe", type(data_float), "\n" )



print("---STRING---")

data_str = "12.5"
print("data", data_str, "dengan tipe", type(data_str), "akan menjadi :")

data_int = int(float(data_str)) # String harus bernilai angka dan harus di konfersi ke float terlebih dahulu bila nilai defaultnya adalah float
data_float = float(data_str) # String harus bernilai angka
data_bool = bool(data_str) # Bernilai False ketika variable empty / kosong

print("-> data", data_int, "bertipe", type(data_int))
print("-> data", data_float, "bertipe", type(data_float))
print("-> data", data_bool, "bertipe", type(data_bool))
