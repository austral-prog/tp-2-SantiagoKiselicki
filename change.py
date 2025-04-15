def change():
    expense = 23.75
    money = 100

    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print()  # línea en blanco

    # Cálculo del vuelto
    change = money - expense

    # Extraemos pesos y centavos
    pesos = int(change)
    centavos = int(round((change - pesos) * 100))

    print("Vuelto\n")
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)
