
try:
    N = int(input("Introduce un número entre 5 y 50: "))


    if 5 <= N <= 50:
        print(f"Cuenta atrás desde {N} hasta 1:")
        for i in range(N, 0, -1):
            print(i)
    else:
        print(" El número debe estar entre 5 y 50.")
except ValueError:

    print("Por favor, ingresa un número válido.")   
