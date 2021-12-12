def calcular_imposto(produto,taxa):
    imposto = produto * (taxa / 100) 
    return imposto

print(calcular_imposto(100,10))