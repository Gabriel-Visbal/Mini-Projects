tareas = []
opcion = "0"
numeros = ["1", "2", "3", "4", "5"]


try:
    with open("tareas.txt", "r") as f:
        for linea in f:
            nombre, estado = linea.strip().split(",")
            tareas.append([nombre, estado])
except FileNotFoundError:
    pass

while opcion != "5":
    print("*" * 20)
    print("1 Agregar tarea" + "\n"
       + "2 Ver Tareas" + "\n"
       + "3 Marcar tarea completada" + "\n"
       + "4 Eliminar tarea" + "\n"
         + "5 Salir")
    print("*" * 20)
    opcion = input("Seleccione una opcion: ")
    continuar = True
    permitidos = 0

    for i in numeros:
        if i != opcion:
            permitidos +=1
    if permitidos == 5:
        print("Selecciona otra opcion.")
        print()

    while opcion == "1" and continuar:
        tarea = [input("Que tarea quieres agregar? "), "Incompleto"]
        tareas.append(tarea)
        verificar = input("Quieres agregar mas tareas?(Y/N) ")
        if verificar == "N" or verificar == 'n':
            print()
            continuar = False
        
        with open("tareas.txt", "w") as f:
            for nombre, estado in tareas:
                f.write(f"{nombre},{estado}\n")

    if opcion == "2":
        for i in tareas:
            print(i)
        print()

    while opcion == "3" and continuar and (len(tareas) != 0):
        for i in tareas:
            print(i)
        print()

        tarea  = input("Que tarea completastes? ")
        for i, (nombre, estado) in enumerate(tareas):
            if nombre == tarea:
                tareas[i][1] = "Completo"

        verificar = input("Alguna tarea mas que hayas completado?(Y/N) ")
        if verificar == "N" or verificar == "n":
            print()
            continuar = False

        with open("tareas.txt", "w") as f:
            for nombre, estado in tareas:
                f.write(f"{nombre},{estado}\n")

    while opcion == "4" and continuar and len(tareas) != 0:
        for i in tareas:
            print(i)
        print()
        eliminar = input("Que tarea deseas eliminar? ")
        for i, (nombre, estado) in enumerate(tareas):
            if nombre == eliminar:
                tareas.pop(i)
                break
        verificar = input("Hay alguna otra tarea que quieras eliminar?(Y/N) ")
        if verificar == "N" or verificar == "n":
            print()
            continuar = False

        with open("tareas.txt", "w") as f:
            for nombre, estado in tareas:
                f.write(f"{nombre},{estado}\n")
