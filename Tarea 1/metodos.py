# Elaborado por:
# Adrián Dittel Retana 2019007945
# Jose Fabio Navarro Naranjo 2019049626
# Tarea 1 Microprocesadores y Microcontroladores

# Metodo 1

def string_work(param):
    """
    Esta funcion invierte las mayusculas a minusculas y viceversa
    en una cadena de texto. Valida el ingreso de unicamente caracteres
    de la a a la z tanto en mayusculas como minusculas.
    """
    if isinstance(param, str):  # valida que la entrada sea string
        new_param = ""  # variable para concatenar los caracteres revisados
        for char in param:
            if char.isalpha():  # valida que sean solo letras
                new_param = new_param + char.swapcase()  # une caracteres
            else:
                return "Error -2"  # Error que tiene simbolos o numeros
        return new_param

    else:
        return "Error -1"  # Error que no es string


# Metodo 2

def num_to_str(param):  # Función para convertir el número a su nombre.
    """
    Esta función verifica que se tenga un número entero,
    si es así entonces, luego verifica que este dentro
    del rango solicitado, de ahí se hace un llamado a
    la función que le pone el nombre y se la asigna a
    la variable devol con esto, devuelve el nombre correcto,
    si no se cumplen los parámetros, entonces indica que
    tipo de error fue el que se tuvo.
    """
    if isinstance(param, int):  # Verfica que entrada sea numero entero.
        devol = ""  # Variable para asignar el nombre del número.
        if 0 <= param <= 99:  # Solo funciona con números entre 0 y 99.
            devol = nombrador(param)  # Llama función que pone los nombres.
            return devol  # Regresa el nombre en palabras del número.
        else:
            return "Error -4"  # Error que número se sale de rangos o decimal.
    elif isinstance(param, float):  # Entra si el numero es decimal
        return "Error -4"  # Error que indica cuando el número es decimal.
    else:
        return "Error -3"  # Error que valor ingresado es un string.


def nombrador(var):  # Función que regresa el nombre del número en letras.
    """
    Dentro de esta función primero se verifica que el número
    que ingresa sea menor a diez, ya que esto se hace para
    verificar que solo sea un digito, ya que a partir del diez
    hasta el noventa y nueve son de dos digitos, una vez que
    verifica la cantidad de los digitos,independientemente de
    la cantidad, convierte el valor que entro como int a un
    string para poder comparar caracter por caracter,
    de acuerdo a esto se asigna a la variable regre el nombre
    en letras de cada número, retornando al final dicha variable.
    """
    regre = ""
    if var < 10:
        vari = str(var)
        # Numeros del 0 al nueve
        if vari[0] == "0":
            regre = "Cero"
        elif vari[0] == "1":
            regre = "Uno"
        elif vari[0] == "2":
            regre = "Dos"
        elif vari[0] == "3":
            regre = "Tres"
        elif vari[0] == "4":
            regre = "Cuatro"
        elif vari[0] == "5":
            regre = "Cinco"
        elif vari[0] == "6":
            regre = "Seis"
        elif vari[0] == "7":
            regre = "Siete"
        elif vari[0] == "8":
            regre = "Ocho"
        elif vari[0] == "9":
            regre = "Nueve"
    else:
        vari = str(var)
        # Numeros del 10 al 19
        if vari[0] == "1" and vari[1] == "0":
            regre = "Diez"
        elif vari[0] == "1" and vari[1] == "1":
            regre = "Once"
        elif vari[0] == "1" and vari[1] == "2":
            regre = "Doce"
        elif vari[0] == "1" and vari[1] == "3":
            regre = "Trece"
        elif vari[0] == "1" and vari[1] == "4":
            regre = "Catorce"
        elif vari[0] == "1" and vari[1] == "5":
            regre = "Quince"
        elif vari[0] == "1" and vari[1] == "6":
            regre = "Dieciseis"
        elif vari[0] == "1" and vari[1] == "7":
            regre = "Diecisiete"
        elif vari[0] == "1" and vari[1] == "8":
            regre = "Dieciocho"
        elif vari[0] == "1" and vari[1] == "9":
            regre = "Diecinueve"
        # Numeros del 20 al 29
        elif vari[0] == "2" and vari[1] == "0":
            regre = "Veinte"
        elif vari[0] == "2" and vari[1] == "1":
            regre = "Veintiuno"
        elif vari[0] == "2" and vari[1] == "2":
            regre = "Veintidos"
        elif vari[0] == "2" and vari[1] == "3":
            regre = "Veintitres"
        elif vari[0] == "2" and vari[1] == "4":
            regre = "Veinticuatro"
        elif vari[0] == "2" and vari[1] == "5":
            regre = "Veinticinco"
        elif vari[0] == "2" and vari[1] == "6":
            regre = "Veintiseis"
        elif vari[0] == "2" and vari[1] == "7":
            regre = "Veintisiete"
        elif vari[0] == "2" and vari[1] == "8":
            regre = "Veintiocho"
        elif vari[0] == "2" and vari[1] == "9":
            regre = "Veintinueve"
        # Numeros del 30 al 39
        elif vari[0] == "3" and vari[1] == "0":
            regre = "Treinta"
        elif vari[0] == "3" and vari[1] == "1":
            regre = "Treinta_y_uno"
        elif vari[0] == "3" and vari[1] == "2":
            regre = "Treinta_y_dos"
        elif vari[0] == "3" and vari[1] == "3":
            regre = "Treinta_y_tres"
        elif vari[0] == "3" and vari[1] == "4":
            regre = "Treinta_y_cuatro"
        elif vari[0] == "3" and vari[1] == "5":
            regre = "Treinta_y_cinco"
        elif vari[0] == "3" and vari[1] == "6":
            regre = "Treinta_y_seis"
        elif vari[0] == "3" and vari[1] == "7":
            regre = "Treinta_y_siete"
        elif vari[0] == "3" and vari[1] == "8":
            regre = "Treinta_y_ocho"
        elif vari[0] == "3" and vari[1] == "9":
            regre = "Treinta_y_nueve"
        # Numeros del 40 al 49
        elif vari[0] == "4" and vari[1] == "0":
            regre = "Cuarenta"
        elif vari[0] == "4" and vari[1] == "1":
            regre = "Cuarenta_y_uno"
        elif vari[0] == "4" and vari[1] == "2":
            regre = "Cuarenta_y_dos"
        elif vari[0] == "4" and vari[1] == "3":
            regre = "Cuarenta_y_tres"
        elif vari[0] == "4" and vari[1] == "4":
            regre = "Cuarenta_y_cuatro"
        elif vari[0] == "4" and vari[1] == "5":
            regre = "Cuarenta_y_cinco"
        elif vari[0] == "4" and vari[1] == "6":
            regre = "Cuarenta_y_seis"
        elif vari[0] == "4" and vari[1] == "7":
            regre = "Cuarenta_y_siete"
        elif vari[0] == "4" and vari[1] == "8":
            regre = "Cuarenta_y_ocho"
        elif vari[0] == "4" and vari[1] == "9":
            regre = "Cuarenta_y_nueve"
        # Numeros del 50 al 59
        elif vari[0] == "5" and vari[1] == "0":
            regre = "Cincuenta"
        elif vari[0] == "5" and vari[1] == "1":
            regre = "Cincuenta_y_uno"
        elif vari[0] == "5" and vari[1] == "2":
            regre = "Cincuenta_y_dos"
        elif vari[0] == "5" and vari[1] == "3":
            regre = "Cincuenta_y_tres"
        elif vari[0] == "5" and vari[1] == "4":
            regre = "Cincuenta_y_cuatro"
        elif vari[0] == "5" and vari[1] == "5":
            regre = "Cincuenta_y_cinco"
        elif vari[0] == "5" and vari[1] == "6":
            regre = "Cincuenta_y_seis"
        elif vari[0] == "5" and vari[1] == "7":
            regre = "Cincuenta_y_siete"
        elif vari[0] == "5" and vari[1] == "8":
            regre = "Cincuenta_y_ocho"
        elif vari[0] == "5" and vari[1] == "9":
            regre = "Cincuenta_y_nueve"
        # Numeros del 60 al 69
        elif vari[0] == "6" and vari[1] == "0":
            regre = "Sesenta"
        elif vari[0] == "6" and vari[1] == "1":
            regre = "Sesenta_y_uno"
        elif vari[0] == "6" and vari[1] == "2":
            regre = "Sesenta_y_dos"
        elif vari[0] == "6" and vari[1] == "3":
            regre = "Sesenta_y_tres"
        elif vari[0] == "6" and vari[1] == "4":
            regre = "Sesenta_y_cuatro"
        elif vari[0] == "6" and vari[1] == "5":
            regre = "Sesenta_y_cinco"
        elif vari[0] == "6" and vari[1] == "6":
            regre = "Sesenta_y_seis"
        elif vari[0] == "6" and vari[1] == "7":
            regre = "Sesenta_y_siete"
        elif vari[0] == "6" and vari[1] == "8":
            regre = "Sesenta_y_ocho"
        elif vari[0] == "6" and vari[1] == "9":
            regre = "Sesenta_y_nueve"
        # Numeros del 70 al 79
        elif vari[0] == "7" and vari[1] == "0":
            regre = "Setenta"
        elif vari[0] == "7" and vari[1] == "1":
            regre = "Setenta_y_uno"
        elif vari[0] == "7" and vari[1] == "2":
            regre = "Setenta_y_dos"
        elif vari[0] == "7" and vari[1] == "3":
            regre = "Setenta_y_tres"
        elif vari[0] == "7" and vari[1] == "4":
            regre = "Setenta_y_cuatro"
        elif vari[0] == "7" and vari[1] == "5":
            regre = "Setenta_y_cinco"
        elif vari[0] == "7" and vari[1] == "6":
            regre = "Setenta_y_seis"
        elif vari[0] == "7" and vari[1] == "7":
            regre = "Setenta_y_siete"
        elif vari[0] == "7" and vari[1] == "8":
            regre = "Setenta_y_ocho"
        elif vari[0] == "7" and vari[1] == "9":
            regre = "Setenta_y_nueve"
        # Numeros del 80 al 89
        elif vari[0] == "8" and vari[1] == "0":
            regre = "Ochenta"
        elif vari[0] == "8" and vari[1] == "1":
            regre = "Ochenta_y_uno"
        elif vari[0] == "8" and vari[1] == "2":
            regre = "Ochenta_y_dos"
        elif vari[0] == "8" and vari[1] == "3":
            regre = "Ochenta_y_tres"
        elif vari[0] == "8" and vari[1] == "4":
            regre = "Ochenta_y_cuatro"
        elif vari[0] == "8" and vari[1] == "5":
            regre = "Ochenta_y_cinco"
        elif vari[0] == "8" and vari[1] == "6":
            regre = "Ochenta_y_seis"
        elif vari[0] == "8" and vari[1] == "7":
            regre = "Ochenta_y_siete"
        elif vari[0] == "8" and vari[1] == "8":
            regre = "Ochenta_y_ocho"
        elif vari[0] == "8" and vari[1] == "9":
            regre = "Ochenta_y_nueve"
        # Numeros del 90 al 99
        elif vari[0] == "9" and vari[1] == "0":
            regre = "Noventa"
        elif vari[0] == "9" and vari[1] == "1":
            regre = "Noventa_y_uno"
        elif vari[0] == "9" and vari[1] == "2":
            regre = "Noventa_y_dos"
        elif vari[0] == "9" and vari[1] == "3":
            regre = "Noventa_y_tres"
        elif vari[0] == "9" and vari[1] == "4":
            regre = "Noventa_y_cuatro"
        elif vari[0] == "9" and vari[1] == "5":
            regre = "Noventa_y_cinco"
        elif vari[0] == "9" and vari[1] == "6":
            regre = "Noventa_y_seis"
        elif vari[0] == "9" and vari[1] == "7":
            regre = "Noventa_y_siete"
        elif vari[0] == "9" and vari[1] == "8":
            regre = "Noventa_y_ocho"
        elif vari[0] == "9" and vari[1] == "9":
            regre = "Noventa_y_nueve"
    return regre
