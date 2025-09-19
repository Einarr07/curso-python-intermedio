# Definimos un conjunto (set) de países
set_coutries = {
    'colombia',
    'mexico',
    'bolivia'
}

# Definimos un conjunto con números del 1 al 17
set_numbers = {
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17
}

# Definimos un conjunto con diferentes tipos de datos:
# un entero, un string, un booleano y un flotante
set_types = {
    1,
    'hola',
    False,
    12.43
}

# Creamos un conjunto a partir de un string.
# Cada carácter será un elemento único del conjunto
set_from_string = set('hola')  # {'h', 'o', 'l', 'a'}

# Creamos un conjunto a partir de una tupla.
# Los elementos repetidos se eliminan automáticamente
set_from_tuples = set(('abc', 'cba', 'as', 'cvb', 'abc'))

# Creamos una lista con números, incluyendo elementos repetidos
numbers = [1, 2, 3, 4, 0, 3, 4, 2, 5, 1, 1, 1, 3, 4]

# Convertimos la lista en un conjunto para eliminar duplicados
set_numbers_1 = set(numbers)

# Convertimos nuevamente el conjunto en lista
# para tener solo los números únicos
unique_numbers = list(set_numbers_1)

# Punto de entrada del programa
if __name__ == "__main__":
    print(set_coutries)       # Imprime los países
    print(set_numbers)        # Imprime los números del 1 al 17
    print(set_types)          # Imprime los distintos tipos de datos
    print(set_from_string)    # Imprime los caracteres únicos de "hola"
    print(set_from_tuples)    # Imprime los valores únicos de la tupla
    print(set_numbers_1)      # Imprime los números únicos de la lista
    print(unique_numbers)     # Imprime los números únicos como lista
