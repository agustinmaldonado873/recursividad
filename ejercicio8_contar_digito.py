def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

numero = int(input("Ingrese un número: "))
digito = int(input("Ingrese un dígito a contar: "))
print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces.")
