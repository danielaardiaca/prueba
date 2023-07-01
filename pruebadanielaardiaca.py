# Diagrama para el mapeo de los lotes
lotes_disponibles = [[" ", " ", "X", " ", "X"],
                     ["X", " ", "X", " ", " "],
                     [" ", " ", " ", " ", " "],
                     [" ", "X", " ", " ", " "]]

"""
Para seleccionar correctamente los lotes en el programa lo haremos por medio de indices por ejemplo, si quiero el lote marcado con la letra "B" voy a digitar en la fila el indice 0 y en la columna el indice 0.
Otro ejemplo seria comprar el lote marcado con la letra "Z", para hacerlo voy a digitar en la fila el indice 2 y en la columna el indice 4.

["B", " ", "X", " ", "X"]
["X", " ", "X", " ", " "]
[" ", " ", " ", " ", "Z"]
[" ", "X", " ", " ", " "]
"""


# Lista de los detalles de cada lote
lotes = [
    [{"numero": 1, "tamaño": "500 m²", "precio": "$100,000"},
     {"numero": 2, "tamaño": "400 m²", "precio": "$80,000"},
     {"numero": 3, "tamaño": "600 m²", "precio": "$120,000"},
     {"numero": 4, "tamaño": "350 m²", "precio": "$70,000"},
     {"numero": 5, "tamaño": "450 m²", "precio": "$90,000"}],
]

# Funcion para mostrar una lista de clientes que han comprado un lote
clientes = []

def mostrar_disponibilidad_lotes():
    print("Lotes Disponibles:")
    for fila in lotes_disponibles:
        for lote in fila:
            print(f"[{lote}]", end=" ")
        print()

# Funcion para la compra de un nuevo lote pidiendo datos del cliente
def seleccionar_lote():

    rut = input("Ingrese su RUT: ")
    nombre = input("Ingrese su nombre completo: ")
    telefono = input("Ingrese su teléfono: ")
    email = input("Ingrese su email: ")

    fila = int(input("Ingrese la fila del lote: "))
    columna = int(input("Ingrese la columna del lote: "))

    if fila < 0 or fila >= len(lotes_disponibles) or columna < 0 or columna >= len(lotes_disponibles[0]):
        print("Coordenadas inválidas. Por favor, elija nuevamente.")
        return

    if lotes_disponibles[fila][columna] == " ":
        lotes_disponibles[fila][columna] = "X"
        clientes.append({"RUT": rut, "nombre": nombre, "telefono": telefono, "email": email})
        print("""
        Lote seleccionado con éxito.
        """)
    else:
        print("""El lote seleccionado no está disponible.""")

# Fcuncion para detalles de cada lote ya vendido
def ver_detalles_lote():
    print()
    fila = int(input("Ingrese la fila del lote seleccionado: "))
    columna = int(input("Ingrese la columna del lote seleccionado: "))

    if fila < 0 or fila >= len(lotes_disponibles) or columna < 0 or columna >= len(lotes_disponibles[0]):
        print("Coordenadas inválidas. Por favor, elija nuevamente.")
        return

    lote_seleccionado = lotes_disponibles[fila][columna]
    if lote_seleccionado == "X":
        numero_lote = lotes[fila][columna]["numero"]
        tamaño_terreno = lotes[fila][columna]["tamaño"]
        precio = lotes[fila][columna]["precio"]
        print("Detalles del lote seleccionado:")
        print(f"Número de lote: {numero_lote}")
        print(f"Tamaño del terreno: {tamaño_terreno}")
        print(f"Precio: {precio}")
    else:
        print("El lote seleccionado no está vendido.")

# Funcion para ver detalles de los nuevos clientes que han comprado un lote
def ver_clientes():
    print()
    print("Clientes que han comprado un lote:")
    for cliente in clientes:
        print(f"RUT: {cliente['RUT']}")
        print(f"Nombre: {cliente['nombre']}")
        print(f"Teléfono: {cliente['telefono']}")
        print(f"Email: {cliente['email']}")
        print()

# Función para el menu principal del programa
def main():
    while True:

        print("       ////// Menú //////")
        print("1. Ver disponibilidad de lotes")
        print("2. Seleccionar un lote")
        print("3. Ver detalles del lote seleccionado")
        print("4. Ver Clientes")
        print("5. Salir")
        print()

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            mostrar_disponibilidad_lotes()
        
        elif opcion == "2":
            seleccionar_lote()
        
        elif opcion == "3":
            ver_detalles_lote()
            
        elif opcion == "4":
            ver_clientes()
            
        elif opcion == "5":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            
            break
        else:
            print("""
            /// ¡Opción inválida. Por favor, ingrese una opción válida!. ///
            """)

# Ejecutar el menu principal del programa
main()
