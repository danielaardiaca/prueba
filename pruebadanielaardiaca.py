import numpy as np

lotes_disponibles = np.array([
    [" ", " ", "X", " ", "X"],
    ["X", " ", "X", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", "X", " ", " ", " "]
])

lotes = [
    [
        {"numero": 1, "tamaño": "500 m²", "precio": "$100,000"},
        {"numero": 2, "tamaño": "400 m²", "precio": "$80,000"},
        {"numero": 3, "tamaño": "600 m²", "precio": "$120,000"},
        {"numero": 4, "tamaño": "350 m²", "precio": "$70,000"},
        {"numero": 5, "tamaño": "450 m²", "precio": "$90,000"}
    ]
]

clientes = []

def mostrar_disponibilidad_lotes():
    print("Lotes Disponibles:")
    for fila in lotes_disponibles:
        fila_str = " ".join(fila)
        print(fila_str)

def seleccionar_lote():
    rut = input("Ingrese su RUT: ")
    nombre = input("Ingrese su nombre completo: ")
    telefono = input("Ingrese su teléfono: ")
    email = input("Ingrese su email: ")

    try:
        fila = int(input("Ingrese la fila del lote: "))
        columna = int(input("Ingrese la columna del lote: "))
        
        if lotes_disponibles[fila, columna] == " ":
            lotes_disponibles[fila, columna] = "X"
            clientes.append({"RUT": rut, "nombre": nombre, "telefono": telefono, "email": email})
            print("Lote seleccionado con éxito.")
        else:
            print("El lote seleccionado no está disponible.")
    except IndexError:
        print("Coordenadas inválidas. Por favor, elija nuevamente.")

def ver_detalles_lote():
    print()
    try:
        fila = int(input("Ingrese la fila del lote seleccionado: "))
        columna = int(input("Ingrese la columna del lote seleccionado: "))
        
        if lotes_disponibles[fila, columna] == "X":
            numero_lote = lotes[fila][columna]["numero"]
            tamaño_terreno = lotes[fila][columna]["tamaño"]
            precio = lotes[fila][columna]["precio"]
            print("Detalles del lote seleccionado:")
            print(f"Número de lote: {numero_lote}")
            print(f"Tamaño del terreno: {tamaño_terreno}")
            print(f"Precio: {precio}")
        else:
            print("El lote seleccionado no está vendido.")
    except IndexError:
        print("Coordenadas inválidas. Por favor, elija nuevamente.")

def ver_clientes():
    print()
    print("Clientes que han comprado un lote:")
    for cliente in clientes:
        print(f"RUT: {cliente['RUT']}")
        print(f"Nombre: {cliente['nombre']}")
        print(f"Teléfono: {cliente['telefono']}")
        print(f"Email: {cliente['email']}")
        print()

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
            print("/// ¡Opción inválida. Por favor, ingrese una opción válida!. ///")

# Ejecutar el menú principal del programa
main()

