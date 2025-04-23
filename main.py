while True:
    print("================================")
    print("Verificador de año Bisiesto")
    print("================================")
    print("1. Comprobar")
    print("2. Salir")
    opcion = input("Porfavor, escoja una opción: ")
    match opcion:
        case "1":
            anio = int(input("Porfavor, ponga el año: "))
            if (anio % 400 == 0) or (anio % 4 == 0 and anio % 100 != 0):
                print("================================")
                print(f"El año {anio} es bisiesto.")
            else:
                print("================================")
                print(f"El año {anio} NO es bisiesto.")
        case "2":
            break
        case _:
            print("Porfavor, escoja una opción valida.")
