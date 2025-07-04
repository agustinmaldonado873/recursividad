def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# Prueba
base = int(input("Base: "))
exponente = int(input("Exponente: "))
print(f"{base}^{exponente} = {potencia(base, exponente)}")
