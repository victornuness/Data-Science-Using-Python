# Data-Science-Using-Python
from datetime import datetime
import calendar
from pathlib import Path
from collections import Counter
import collections

Dia_Semana, Time, arrayPalavras = [], [], []

with open('_chat.txt', 'r') as Text:
    for lin in f:
        try:
           
            if linha[0:1] != "[":                
                arrayPalavras.append(linha[linha.find(": ") + 2 : linha[2:].find("[")].replace('\n','').split(' '))
            else:
                Dia_Semana.append(calendar.day_name[datetime.strptime(str(linha[1:11]), '%d/%m/%Y').weekday()])
                Time.append(linha[12:14])
                arrayPalavras.append(linha[linha.find(": ") + 2 : linha[2:].find("[")].replace('\n','').split(' '))                
        except:
            pass

palavras = [ j for i in arrayPalavras for j in i]

#Remove
artigos=['a','à','e','é','i','o','u','os','as','às','um','uma','uns','umas','de','do','nos','nas','']
for p in palavras:
    for i in artigos:
        if p == i:
            palavras.remove(p)

print(f'As 3 palavras mais trocadas na conversa: {Counter(palavras).most_common()[0]} {Counter(palavras).most_common()[1]} {Counter(palavras).most_common()[2]}')
print(f'Dia da semana que mais troca mensagem: {Counter(Dia_Semana).most_common()[1]}')
print(f'Horário do dia que mais troca mensagem: {Counter(Time).most_common()[1]}')
print(f'Horário do dia que menos troca mensagem: {Counter(Time).most_common()[-1]}')
