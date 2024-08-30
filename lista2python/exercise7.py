#Escreva um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem decrescente.

#Ordem decrescente dos números
a = int(input('Escreva um número inteiro: '))
b = int(input('Escreva outro número: '))
c = int(input('Escreva mais um número: '))

#Ordena os valores através de atribuição múltipla
if a < c:
    a, c = c, a
#Se a for menor que c tupla (a, c) recebe os valores da tupla (c, a)
#Ou seja, a recebe c e c recebe a

if a < b:
    a, b = b, a

if b < c:
    b, c = c, b

print(f'A ordem decrescente é: {a}, {b} e {c}')