import libreria

assert (libreria.descuento("A", 100) == 0)
assert (libreria.descuento("Excelente", 100) == 10.0)
assert (libreria.descuento("EXCELENTE", 100) == 10.0)
assert (libreria.descuento("ExCeLeNtE", 100) == 10.0)
assert (libreria.descuento("", 100) == 0)
print("descuento OK")


assert (libreria.validar_edad(51) == True)
assert (libreria.validar_edad(55) == True)
assert (libreria.validar_edad(60) == True)
assert (libreria.validar_edad(11) == False)
assert (libreria.validar_edad(19) == False)
print("validar_edad OK")
