#Exercicio 1
## Você tem uma lista de número: [6,7,4,7,8,4,2,5,7,'hum', 'dois'].
# A ideia do exercício é tirar a média de todos os valores contidos na lista,
# porém para fazer o cálculo precisa remover as strings.


lista_numeros=[6,7,4,7,8,4,2,5,7,'hum', 'dois']
cont=0
soma=0
for valor in lista_numeros:
    cont+=1
    if isinstance(valor, (int,float)):
        soma+=valor
media=soma/cont
print(soma)
print(cont)
print(media)

#Exercicio 2
#crie um método que receba duas matrizes, some os valores total de cada matriz e depois multiple o
#resultado delas e retorne o valor.

def calculaVMatriz(m1,m2):
    soma1=0
    soma2=0
    for x in m1:
        soma1+=x
    for x in m2:
        soma2+=x
    valor=soma1*soma2
    print('A soma da matriz 1 é ' + str(soma1))
    print('A soma da matriz 2 é ' + str(soma2))
    print('A multiplicação é ' + str(valor))
    return valor

teste=calculaVMatriz([1,3,5,6], [3,4,5,2])
print(teste)

#Exercicio 3
#Criar uma matriz nxm (n = 5, m =7)
#faça a matriz transposta desta matriz
#somar toda matrix
#somar todas as colunas
#somar todas as linhas.
#retorne o maior valor
#retorne o menor valor.

import numpy as np
from numpy import random
#Criar uma matriz nxm (n = 5, m =7)
n=5
m=7
matriz1 = np.random.randint(1,99, (n,m))
print('Matriz')
print(matriz1)
#faça a matriz transposta desta matriz
matriz2=matriz1.T
print('Matriz Transposta')
print(matriz2)
#somar toda matrix
print('Soma todos os valores da Matriz')
print(matriz2.sum())
#somar todas as colunas
print('Soma todos os valores das Colunas')
print(matriz2.sum(axis=0))
#somar todas as linhas.
print('Soma todos os valores das Linhas')
print(matriz2.sum(axis=1))
#retorne o maior valor
print('Retorne o maior valor da Matriz')
print(matriz2.max())

#retorne o menor valor.
print('Retorne o menor valor da Matriz')
print(matriz2.min())

#Exercicio 4
n=5
matriz3 = np.random.randint(1,99, (n,n))
print(matriz2.sum()+matriz3.sum())

#Exercicio 5
n=5
matriz4 = np.random.randint(1,1000, (n,n))
print(matriz4)

#Exercicio 6
matriz5=np.zeros(5)
#ou
matriz6=[0] * 5
print(matriz5)
print(matriz6)
