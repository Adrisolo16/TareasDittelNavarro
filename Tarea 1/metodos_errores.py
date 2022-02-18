#Elaborado por:
#Adrián Dittel Retana 2019007945
#Jose Fabio Navarro Naranjo 2019049626
#Tarea 1 Microprocesadores y Microcontroladores

#Metodo 1

def string_work(param):   
    """
    Esta funcion invierte las mayusculas a minusculas y viceversa
    en una cadena de texto. Valida el ingreso de unicamente caracteres
    de la a a la z tanto en mayusculas como minusculas.
    """
    if isinstance(param,str)# valida que la entrada sea string
        new_param = ""  # variable para concatenar los caracteres revisados
        for char in param:
            if char.isalpha():  # valida que sean solo letras
                new_param = new_param + char.swapcase()  # une caracteres
            else:
                return "Error -2"  # Error que tiene simbolos o numeros
        return new_param

    else:
        return "Error -1"  # Error que no es string
