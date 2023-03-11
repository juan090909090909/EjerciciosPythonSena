personas = {
    "juan": {
        "nombre": "Juan",
        "apellido": "Pérez",
        "edad": 30,
        "ciudad": "Buenos Aires"
    },
    "maria": {
        "nombre": "Maria",
        "apellido": "Gómez",
        "edad": 25,
        "ciudad": "Córdoba"
    },
    "pedro": {
        "nombre": "Pedro",
        "apellido": "Martínez",
        "edad": 40,
        "ciudad": "Rosario"
    }
}
print(personas)


def eliminar_dato_persona(personas):
    nombre = input("Ingrese el nombre de la persona: ")
    dato = input("Ingrese el tipo de dato a eliminar: ")
    if nombre in personas:
        if dato in personas[nombre]:
            del personas[nombre][dato]
            print("Se ha eliminado el dato " + dato + " de la persona con nombre " + nombre + " del diccionario anidado.")

        else:
            print("No se encontró el" + dato + "para la persona con nombre" + nombre + "en el diccionario anidado.")
    else:
        print("No se encontró a la persona con nombre " + nombre + " en el diccionario anidado.")
eliminar_dato_persona(personas)

print(personas)
