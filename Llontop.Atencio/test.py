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


assert (libreria.validar_mes("") == False)
assert (libreria.validar_mes("MAYO") == False)
assert (libreria.validar_mes("JULIO") == True)
assert (libreria.validar_mes("AGOSTO") == True)
assert (libreria.validar_mes("OCTUBRE") == True)
print("validar_mes OK")


assert (libreria.validar_apellido("") == False)
assert (libreria.validar_apellido("LLONTOP") == True)
assert (libreria.validar_apellido("OLIVA") == False)
assert (libreria.validar_apellido("ATENCIO") == True)
assert (libreria.validar_apellido("AYALA") == False)
print("validar_apellido OK")


assert ((libreria.obtenerDescuento ("FELICIDADES") == 200.0)== True)
assert ((libreria.obtenerDescuento ("MUY BIEN") == 100.0) == True)
assert ((libreria.obtenerDescuento ("FELICICDADES") == 100.0) == False)
assert ((libreria.obtenerDescuento ("MUY BIEN") == 200.0) == False)
assert ((libreria.obtenerDescuento ("FELICIDADES") == 0.0)  ==False)
print("obtenerDescuento OK")
