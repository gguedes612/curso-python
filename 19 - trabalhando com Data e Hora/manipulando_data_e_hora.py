"""
Manipulando data e hora

Python tem um modulo built-in(integrado) para se trabalhar com data e hora chamado datetime
"""

import datetime

print(datetime.MAXYEAR) #mostra o ano maximo que pode ser trabalhado

print(datetime.MINYEAR) #mostra o ano minimo que pode ser trabalhado

print(datetime.datetime.now()) #2022-04-25 21:36:57.021614

print(repr(datetime.datetime.now())) #datetime.datetime(2022, 4, 25, 21, 38, 35, 652165) year, month, day , minute, second and microsecond

inicio = datetime.datetime.now()

print(inicio)

inicio = inicio.replace(hour=16, minute=0)

print(inicio)

