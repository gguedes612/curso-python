def numero_reverso(numero):
    numero = str(numero)
    numero = numero[::-1]
    numero = int(numero)
    return numero

print(numero_reverso(123))