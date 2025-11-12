def media_dos_valores():
    try:
        a = float(input("Introduce el primer número: "))
        b = float(input("Introduce el segundo número: "))
        print("La media aritmética es:", (a + b) / 2)
    except ValueError:
        print("Por favor, introduce solo números válidos.")


