lista = []
for i in range(4):
    lista.append(float(input(f"Me diga a nota {i+1}: ")))

media = sum(lista) / 4

print(f"Media do aluno é: {media}")