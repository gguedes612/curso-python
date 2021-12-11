"""
***kwards

Poderiamos chamar este parametros de **xis, mas por converção chamamos de **kwards

Este é só um parametro, mas diferente do *args que coloca os valores extras em uma tupla, o **kwards exige que utilizamos parametros nomeados, e transforma esses parametros extras em dicionario.
"""

def cores_favoritas(**kwargs):
    print(kwargs)

cores_favoritas(Guilherme='Amarelo', Finho='Preto')

#Os parametrosw **kwards e *args não são obrigatorios