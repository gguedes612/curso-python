lista = []
for i in range(10):
    lista.append(input(f"Me passe um caracter: "))

contadorLetras = 0
contadorNum = 0

for i in lista:
    if i >= 'a' and i <= 'z' or i >= 'A' and i <= 'Z':
        contadorLetras += 1
    else:
        contadorNum += 1

print(contadorLetras)
print(contadorNum)