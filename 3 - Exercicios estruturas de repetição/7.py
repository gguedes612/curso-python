qtdeLidos = 0
qtdePares = 0

entrada = int(input("Me deh um numero:"))

while entrada != 1000:
    
    if entrada % 2 == 0:
        qtdePares += 1
    
    qtdeLidos +=1

    entrada = int(input("Me deh um numero:"))

print(f'Quantidade de numeros lidos foi: {qtdeLidos}')
print(f'Quantidade de numeros pares foi: {qtdePares}')
