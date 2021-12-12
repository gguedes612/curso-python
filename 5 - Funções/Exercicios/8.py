def imprimir_for(repetição):
    for i in range(1,repetição+1):
        for j in range(1,i+1):
            print(i,end='')
        print()


imprimir_for(5)