#Número 7

hora= (input("Escreva uma hora junto dos minutos [00:00]"))
horas= int(hora[0:2])
minutos= int(hora[3:6])
print("Horas:", horas)
print("Minutos:", minutos)
tempo_em_minutos= int((horas * 60)+ minutos)
print(("Tempo decorrido em minutos:", tempo_em_minutos))