nota1 = float(input('Pirmeira nota do aluno: '))

if nota1 >= 0 and nota1 <= 10:
    
    nota2 = float(input('Segunda nota do aluno: '))
    
    if nota2 >= 0 and nota2 <= 10:
        
        media = (nota1 + nota2) /2
        print(f'Media do aluno é {media}')
    
    else:
        print('Nota 2 Invalida')

else:
    print('Nota 1 Invalida')





