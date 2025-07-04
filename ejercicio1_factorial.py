def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Mostrar el factorial de los números del 1 al número ingresado
limite = int(input("Ingrese un número: "))
for i in range(1, limite + 1):
    print(f"{i}! = {factorial(i)}")
