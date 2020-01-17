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

#ejercicio2
def validar_edad(intEdad):
    #1.El tipo de dato es intEdad es int
    #2.La longitud del entero es al menos de 50
    if (isinstance(intEdad,int)):
        if((intEdad) >= 50):
            return True   #Es edad valido
        else:
            return False  #Insuficiencia caracteres
    else:
        return False   #No es int
#fin_validar_edad
