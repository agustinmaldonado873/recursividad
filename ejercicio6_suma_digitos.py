def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

numero = int(input("Ingrese un número: "))
print("Suma de dígitos:", suma_digitos(numero))
