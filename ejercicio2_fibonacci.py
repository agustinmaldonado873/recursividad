def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)

# Mostrar la serie hasta la posición indicada
n = int(input("Ingrese la posición límite de Fibonacci: "))
print("Serie de Fibonacci:")
for i in range(n + 1):
    print(fibonacci(i), end=" ")
