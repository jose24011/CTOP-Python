numero=int(input("Ingrese un numero: "))
print(f"tabla de multiplicar del {numero}")
for i in range(1,11):
    resultado=numero*i
    print(f"{numero} x {i} = {resultado}")
    