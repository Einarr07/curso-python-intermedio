# Lista de productos representados como diccionarios
items = [
    {
        "product": "T-shirt",
        "price": 100,
    },
    {
        "product": "Pants",
        "price": 80,
    },
    {
        "product": "Shots",
        "price": 200,
    }
]

# Extraemos solo los precios de los productos con map + lambda
prices = list(map(lambda item: item["price"], items))


# Función que agrega un campo "taxes" a cada producto
def add_taxes(item) -> dict:
    # Se calcula un 15% de impuestos sobre el precio
    item['taxes'] = item['price'] * 0.15
    return item


# Aplicamos la función a todos los productos
taxes = list(map(add_taxes, items))


if __name__ == "__main__":
    # Imprimimos los precios en formato claro
    print(f"Precios de los productos: {prices}")

    # Imprimimos los productos ya con impuestos agregados
    print("Productos con impuestos añadidos:")
    for product in taxes:
        print(f"  - {product['product']}: Precio = {product['price']}, Impuestos = {product['taxes']}")
