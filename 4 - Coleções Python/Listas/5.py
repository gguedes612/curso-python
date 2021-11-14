listaNum = []
listaPar = []
listaImpar = []

for i in range(20):
    
    numero = int(input("Me deh um numero: "))
    listaNum.append(numero)

    if numero % 2 == 0:
        listaPar.append(numero)
    else:
        listaImpar.append(numero)


print(listaNum)
print(listaPar)
print(listaImpar)