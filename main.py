from Src.logica.Operaciones import Operaciones

if __name__ == '__main__':
    operacion = Operaciones()

    while True:
        try:
            sumando1 = input("\nIngrese el primer sumando: ")
            if (not type(sumando1) is float) or (not type(sumando1) is int):
                    sumando1 = float(sumando1)
            break
        except ValueError:
            print(f"\nEl dato ingresado \"{sumando1}\" no se puede convertir a float")
    print ("Correcto. Número válido")

    while True:
        try:
            sumando2 = input("\nIngrese el segundo sumando: ")
            if (not type(sumando2) is float) or (not type(sumando2) is int):
                    sumando2 = float(sumando2)
            break
        except ValueError:
            print(f"\nEl dato ingresado \"{sumando2}\" no se puede convertir a float")
    print("Correcto. Número válido")

    resultado = operacion.suma(sumando1, sumando2)
    print("\nRESULTADO")
    print("=========")
    print("{0:.2f} + {1:.2f} = {2:.2f}".format(sumando1, sumando2, resultado))



