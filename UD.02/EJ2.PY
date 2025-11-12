a=int(input("Ingrese el primer numero "))
b=int(input("Ingrese el segundo numero "))
if a > b:
    print("El numero mayor es", a)

elif b > a:
    print("El numero mayor es", b)
else:
    print("Ambos numeros son iguales")

except ValueError:
    print("Por favor, ingresa un número válido.")