# Lista de productos representados como diccionarios
# Nota: los diccionarios en Python son MUTABLES (se pueden modificar en memoria).
# Para evitar modificar el original, usamos .copy() dentro de la función.
items = [
    {
        "product": "Laptop",
        "price": 1200,
    },
    {
        "product": "Headphones",
        "price": 150,
    },
    {
        "product": "Smartphone",
        "price": 800,
    }
]

# Función que agrega un campo "taxes" a cada producto
def add_taxes(item) -> dict:
    # ⚡ Aquí usamos .copy(), que es un MÉTODO de los diccionarios.
    # Esto genera una copia superficial del diccionario (shallow copy).
    # Así, modificamos esa copia sin alterar el diccionario original en la lista `items`.
    new_item = item.copy()

    # Se calcula un 15% de impuestos sobre el precio
    new_item['taxes'] = new_item['price'] * 0.15

    # Retornamos la copia modificada (con impuestos añadidos)
    return new_item


# Aplicamos la función a todos los productos
taxes = list(map(add_taxes, items))

if __name__ == "__main__":
    # Mostramos los productos originales (sin impuestos)
    print("Productos originales (sin impuestos añadidos):")
    for product in items:
        print(f"  - {product['product']}: Precio = {product['price']}")

    print("\nProductos con impuestos añadidos (usando .copy()):")
    for product in taxes:
        print(f"  - {product['product']}: Precio = {product['price']}, Impuestos = {product['taxes']}")
