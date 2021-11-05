repetição = int(input("Me deh um numero inteiro: ")) - 1
quantidade = 1
entrada = int(input("Me deh um numero: "))
maior = entrada

for i in range(repetição):

    entrada = int(input("Me deh um numero: "))
    
    if entrada > maior:
        maior = entrada
        quantidade = 1

    elif entrada == maior:
        quantidade += 1
        
print(f'Maior numero digitado: {maior}')

print(f'Quantidade de vezes digitada: {quantidade}')