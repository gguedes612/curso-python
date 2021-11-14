lista = []
for i in range(10):
    lista.append(int(input(f"Adicione o indicie {i} na lista: ")))

lista.reverse()

for i in lista:
    print(i)