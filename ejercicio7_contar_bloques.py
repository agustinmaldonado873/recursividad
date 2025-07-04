def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

nivel = int(input("Ingrese el número de bloques en el nivel más bajo: "))
print("Total de bloques necesarios:", contar_bloques(nivel))
