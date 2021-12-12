def imprimir_for_2(repetição):
    for i in range(1,repetição+1):
        for j in range(1,i+1):
            print(j,end='')
        print()


imprimir_for_2(5)