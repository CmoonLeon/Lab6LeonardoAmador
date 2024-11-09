# Función para consultar
def consultar_inventario(inventario, producto):
    # Si está en el inventario
    if producto in inventario:
        # Retorna la cantidad
        return f"La cantidad de {producto} en inventario es: {inventario[producto]}"
    else:
        # No está en el inventario
        return f"El producto {producto} no se encuentra en el inventario."


# Función para agregar
def agregar_producto(inventario, producto, cantidad):
    # Si existe el producto
    if producto in inventario:
        # Aumentamos la cantidad
        inventario[producto] += cantidad
        return f"Se ha incrementado la cantidad de {producto} en {cantidad} unidades."
    else:
        # Lo agregamos al inventario
        inventario[producto] = cantidad
        return f"Producto {producto} agregado con {cantidad} unidades al inventario."


# Función para eliminar productos por cantidad
def eliminar_producto(inventario, producto, cantidad):
    # Verificamos si el producto está en el inventario
    if producto in inventario:
        # Si la cantidad a eliminar es mayor que la cantidad disponible
        if cantidad > inventario[producto]:
            respuesta = input(f"Productos insuficientes, desea llevar los que hay? (sí/no): ").lower()
            if respuesta == "sí":
                # Si dice sí, eliminamos todo el producto
                print(f"Se eliminaron {inventario[producto]} unidades de {producto}.")
                del inventario[producto]  # Eliminamos el producto
            else:
                print("Operación cancelada.")
        elif cantidad == 0:
            print(f"No se puede eliminar una cantidad de 0 para {producto}.")
        else:
            # Si la cantidad a eliminar es válida, la restamos del inventario
            inventario[producto] -= cantidad
            print(f"Se han eliminado {cantidad} unidades de {producto}.")

            # Si la cantidad llega a 0, eliminamos el producto del inventario
            if inventario[producto] == 0:
                del inventario[producto]
                print(f"{producto} ha sido completamente eliminado del inventario.")
    else:
        # Si el producto no está en el inventario
        return f"El producto {producto} no se encuentra en el inventario."


# Función para mostrar inventario
def mostrar_inventario(inventario):
    # Si está vacío
    if not inventario:
        print("El inventario está vacío.")
    else:
        # Mostramos los productos
        print("Inventario actual:")
        for producto, cantidad in sorted(inventario.items()):  # Se ordenan los productos
            # Imprime el nombre y cantidad
            print(f"- {producto}: {cantidad}")


# Función principal que maneja las operaciones
def gestionar_inventario():
    # Inventario inicial
    inventario = {
        "manzanas": 50,
        "bananas": 30,
        "naranjas": 40
    }

    # Mostrar inventario inicial
    mostrar_inventario(inventario)

    # Bucle principal para las acciones
    while True:
        # Acción que quiere hacer el usuario
        accion = input("¿Qué acción deseas realizar? (consultar/agregar/eliminar/mostrar/salir): ").lower()

        # Consultar producto
        if accion == "consultar":
            producto = input("Ingresa el nombre del producto a consultar: ").lower()
            print(consultar_inventario(inventario, producto))

        # Agregar producto
        elif accion == "agregar":
            producto = input("Ingresa el nombre del producto: ").lower()
            cantidad = int(input("Ingresa la cantidad: "))
            print(agregar_producto(inventario, producto, cantidad))

        # Eliminar producto
        elif accion == "eliminar":
            producto = input("Ingresa el nombre del producto a eliminar: ").lower()
            cantidad = int(input(f"Ingresa la cantidad a eliminar de {producto}: "))
            print(eliminar_producto(inventario, producto, cantidad))

        # Mostrar inventario
        elif accion == "mostrar":
            mostrar_inventario(inventario)

        # Salir
        elif accion == "salir":
            print("¡Hasta luego!")
            break

        # Acción no válida
        else:
            print("Acción no válida. Intenta de nuevo.")

        # Mostrar inventario actualizado
        mostrar_inventario(inventario)


# Ejecutamos el programa
gestionar_inventario()
