def quadrado_perfeito(numero):
    raiz = numero ** 0.5
    if numero == raiz ** 2:
        return 'Numero Quadado Perfeito'
    else:
        return 'Não é Quadrado Perfeito'


print(quadrado_perfeito(9))
print(quadrado_perfeito(12))