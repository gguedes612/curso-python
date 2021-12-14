"""
Set Comprehension

Lista = [1,2,3]
Set = {1,2,3}

"""

numeros = {num for num in range(1,7)}
print(numeros)

numeros = {num ** 2 for num in range(10)}
print(numeros)