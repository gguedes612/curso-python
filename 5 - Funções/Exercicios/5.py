def convertendo_em_segundos(horas,minutos,segundos):
    segundos += (horas * 3600) + (minutos * 60)
    return segundos

print(convertendo_em_segundos(2,30,20))