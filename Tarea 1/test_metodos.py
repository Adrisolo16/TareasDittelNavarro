# Elaborado por:
# Adrián Dittel Retana 2019007945
# Jose Fabio Navarro Naranjo 2019049626
# Tarea 1 Microprocesadores y Microcontroladores

# Importación de librerías

from metodos import string_work
from metodos import num_to_str


# Prueba 1: string_work cambia todas las letras


def test_string_work():
    assert string_work("a") == "A"
    assert string_work("b") == "B"
    assert string_work("c") == "C"
    assert string_work("d") == "D"
    assert string_work("e") == "E"
    assert string_work("f") == "F"
    assert string_work("g") == "G"
    assert string_work("h") == "H"
    assert string_work("i") == "I"
    assert string_work("j") == "J"
    assert string_work("k") == "K"
    assert string_work("l") == "L"
    assert string_work("m") == "M"
    assert string_work("n") == "N"
    assert string_work("o") == "O"
    assert string_work("p") == "P"
    assert string_work("q") == "Q"
    assert string_work("r") == "R"
    assert string_work("s") == "S"
    assert string_work("t") == "T"
    assert string_work("u") == "U"
    assert string_work("v") == "V"
    assert string_work("w") == "W"
    assert string_work("x") == "X"
    assert string_work("y") == "Y"
    assert string_work("z") == "Z"
    assert string_work("A") == "a"
    assert string_work("B") == "b"
    assert string_work("C") == "c"
    assert string_work("D") == "d"
    assert string_work("E") == "e"
    assert string_work("F") == "f"
    assert string_work("G") == "g"
    assert string_work("H") == "h"
    assert string_work("I") == "i"
    assert string_work("J") == "j"
    assert string_work("K") == "k"
    assert string_work("L") == "l"
    assert string_work("M") == "m"
    assert string_work("N") == "n"
    assert string_work("O") == "o"
    assert string_work("P") == "p"
    assert string_work("Q") == "q"
    assert string_work("R") == "r"
    assert string_work("S") == "s"
    assert string_work("T") == "t"
    assert string_work("U") == "u"
    assert string_work("V") == "v"
    assert string_work("W") == "w"
    assert string_work("X") == "x"
    assert string_work("Y") == "y"
    assert string_work("Z") == "z"

# Prueba 2: retorno de error si se utiliza un número


def test_error_not_string():
    assert string_work(1) == "Error -1"
    assert string_work(42) == "Error -1"
    assert string_work(35) == "Error -1"
    assert string_work(93) == "Error -1"

# Prueba 3: retorno de error si se utiliza un simbolo o número como string


def test_error_simbolo_numero():
    assert string_work("hao5") == "Error -2"
    assert string_work("ho1a") == "Error -2"
    assert string_work("h_o_l_a") == "Error -2"
    assert string_work("4s56c2a") == "Error -2"

# Prueba 4: num_to_str traduce todos los numeros a letras


def test_traduce_correct():
    assert num_to_str(0) == "Cero"
    assert num_to_str(1) == "Uno"
    assert num_to_str(2) == "Dos"
    assert num_to_str(3) == "Tres"
    assert num_to_str(4) == "Cuatro"
    assert num_to_str(5) == "Cinco"
    assert num_to_str(6) == "Seis"
    assert num_to_str(7) == "Siete"
    assert num_to_str(8) == "Ocho"
    assert num_to_str(9) == "Nueve"
    assert num_to_str(10) == "Diez"
    assert num_to_str(11) == "Once"
    assert num_to_str(12) == "Doce"
    assert num_to_str(13) == "Trece"
    assert num_to_str(14) == "Catorce"
    assert num_to_str(15) == "Quince"
    assert num_to_str(16) == "Dieciseis"
    assert num_to_str(17) == "Diecisiete"
    assert num_to_str(18) == "Dieciocho"
    assert num_to_str(19) == "Diecinueve"
    assert num_to_str(20) == "Veinte"
    assert num_to_str(21) == "Veintiuno"
    assert num_to_str(22) == "Veintidos"
    assert num_to_str(23) == "Veintitres"
    assert num_to_str(24) == "Veinticuatro"
    assert num_to_str(25) == "Veinticinco"
    assert num_to_str(26) == "Veintiseis"
    assert num_to_str(27) == "Veintisiete"
    assert num_to_str(28) == "Veintiocho"
    assert num_to_str(29) == "Veintinueve"
    assert num_to_str(30) == "Treinta"
    assert num_to_str(31) == "Treinta_y_uno"
    assert num_to_str(32) == "Treinta_y_dos"
    assert num_to_str(33) == "Treinta_y_tres"
    assert num_to_str(34) == "Treinta_y_cuatro"
    assert num_to_str(35) == "Treinta_y_cinco"
    assert num_to_str(36) == "Treinta_y_seis"
    assert num_to_str(37) == "Treinta_y_siete"
    assert num_to_str(38) == "Treinta_y_ocho"
    assert num_to_str(39) == "Treinta_y_nueve"
    assert num_to_str(40) == "Cuarenta"
    assert num_to_str(41) == "Cuarenta_y_uno"
    assert num_to_str(42) == "Cuarenta_y_dos"
    assert num_to_str(43) == "Cuarenta_y_tres"
    assert num_to_str(44) == "Cuarenta_y_cuatro"
    assert num_to_str(45) == "Cuarenta_y_cinco"
    assert num_to_str(46) == "Cuarenta_y_seis"
    assert num_to_str(47) == "Cuarenta_y_siete"
    assert num_to_str(48) == "Cuarenta_y_ocho"
    assert num_to_str(49) == "Cuarenta_y_nueve"
    assert num_to_str(50) == "Cincuenta"
    assert num_to_str(51) == "Cincuenta_y_uno"
    assert num_to_str(52) == "Cincuenta_y_dos"
    assert num_to_str(53) == "Cincuenta_y_tres"
    assert num_to_str(54) == "Cincuenta_y_cuatro"
    assert num_to_str(55) == "Cincuenta_y_cinco"
    assert num_to_str(56) == "Cincuenta_y_seis"
    assert num_to_str(57) == "Cincuenta_y_siete"
    assert num_to_str(58) == "Cincuenta_y_ocho"
    assert num_to_str(59) == "Cincuenta_y_nueve"
    assert num_to_str(60) == "Sesenta"
    assert num_to_str(61) == "Sesenta_y_uno"
    assert num_to_str(62) == "Sesenta_y_dos"
    assert num_to_str(63) == "Sesenta_y_tres"
    assert num_to_str(64) == "Sesenta_y_cuatro"
    assert num_to_str(65) == "Sesenta_y_cinco"
    assert num_to_str(66) == "Sesenta_y_seis"
    assert num_to_str(67) == "Sesenta_y_siete"
    assert num_to_str(68) == "Sesenta_y_ocho"
    assert num_to_str(69) == "Sesenta_y_nueve"
    assert num_to_str(70) == "Setenta"
    assert num_to_str(71) == "Setenta_y_uno"
    assert num_to_str(72) == "Setenta_y_dos"
    assert num_to_str(73) == "Setenta_y_tres"
    assert num_to_str(74) == "Setenta_y_cuatro"
    assert num_to_str(75) == "Setenta_y_cinco"
    assert num_to_str(76) == "Setenta_y_seis"
    assert num_to_str(77) == "Setenta_y_siete"
    assert num_to_str(78) == "Setenta_y_ocho"
    assert num_to_str(79) == "Setenta_y_nueve"
    assert num_to_str(80) == "Ochenta"
    assert num_to_str(81) == "Ochenta_y_uno"
    assert num_to_str(82) == "Ochenta_y_dos"
    assert num_to_str(83) == "Ochenta_y_tres"
    assert num_to_str(84) == "Ochenta_y_cuatro"
    assert num_to_str(85) == "Ochenta_y_cinco"
    assert num_to_str(86) == "Ochenta_y_seis"
    assert num_to_str(87) == "Ochenta_y_siete"
    assert num_to_str(88) == "Ochenta_y_ocho"
    assert num_to_str(89) == "Ochenta_y_nueve"
    assert num_to_str(90) == "Noventa"
    assert num_to_str(91) == "Noventa_y_uno"
    assert num_to_str(92) == "Noventa_y_dos"
    assert num_to_str(93) == "Noventa_y_tres"
    assert num_to_str(94) == "Noventa_y_cuatro"
    assert num_to_str(95) == "Noventa_y_cinco"
    assert num_to_str(96) == "Noventa_y_seis"
    assert num_to_str(97) == "Noventa_y_siete"
    assert num_to_str(98) == "Noventa_y_ocho"
    assert num_to_str(99) == "Noventa_y_nueve"


# Prueba 5:retorno de error si se utiliza un string


def test_ingr_str():
    assert num_to_str("hola") == "Error -3"
    assert num_to_str("mundo") == "Error -3"
    assert num_to_str("micro") == "Error -3"
    assert num_to_str("procesador") == "Error -3"

# Prueba 6:retorno de error si se utilizan numeros decimales o fuera de rango


def test_sale_rango():
    assert num_to_str(-10) == "Error -4"
    assert num_to_str(-25) == "Error -4"
    assert num_to_str(104) == "Error -4"
    assert num_to_str(201) == "Error -4"
    assert num_to_str(12.5) == "Error -4"
    assert num_to_str(17.54) == "Error -4"
    assert num_to_str(35.67) == "Error -4"
    assert num_to_str(45.88) == "Error -4"