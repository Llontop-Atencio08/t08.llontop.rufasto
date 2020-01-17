import libreria

assert (libreria.descuento("A", 100) == 0)
assert (libreria.descuento("Excelente", 100) == 10.0)
assert (libreria.descuento("EXCELENTE", 100) == 10.0)
assert (libreria.descuento("ExCeLeNtE", 100) == 10.0)
assert (libreria.descuento("", 100) == 0)
print("descuento OK")
