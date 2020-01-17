#ejercicio1

def descuento(tipo, prestamo):
    # Si el tipo de cliente es EXCELENTE
    # Aqui se usa la funcion upper()
    if ( tipo.upper() == "EXCELENTE" ):
        return 0.10 * prestamo
    else:
        return 0

def reporte_prestamo(cliente, monto,descuento):
    print("########################")
    print("# REPORTE DE PRESTAMO #")
    print("# Nombre:"  ""+ nombre+"")
    print("# Precio: S/." "+ str(precio)+")
    print("# Descuento: S/." + str(descuento)+"")
    print("#########################")

#fin_descuento
