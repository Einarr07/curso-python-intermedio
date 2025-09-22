# Lista original de números
numbers = [1, 2, 3, 4, 5]

# Usando un bucle for para duplicar cada número
numbers_v2 = []
for i in numbers:
    numbers_v2.append(i * 2)

# Usando map() y una función lambda para duplicar cada número
numbers_v3 = list(map(lambda x: x * 2, numbers))


if __name__ == "__main__":
    # Imprimimos las diferentes listas con etiquetas claras
    print("Lista original:", numbers)
    print("Lista duplicada con for:", numbers_v2)
    print("Lista duplicada con map/lambda:", numbers_v3)

    # Dos listas diferentes
    numbers_1 = [1, 2, 3, 4]
    numbers_2 = [5, 6, 7]

    print("\nLista 1:", numbers_1)
    print("Lista 2:", numbers_2)

    # Sumamos los elementos de ambas listas en paralelo
    result = list(map(lambda x, y: x + y, numbers_1, numbers_2))

    print("Resultado de la suma de listas:", result)
