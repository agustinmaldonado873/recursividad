def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("Ingrese un número decimal: "))
binario = decimal_a_binario(numero)
print(f"{numero} en binario es: {binario or '0'}")
