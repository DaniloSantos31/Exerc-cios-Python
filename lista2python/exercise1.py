'''Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor
que C.'''
a = int(input("Digite um valor para A: "))
b = int(input("Digite um valor para B: "))
c = int(input("Digite um valor para C: "))

soma = a + b

if soma < c:
  print(c , " é maior que " , soma)
else:
  print(c , " é menor que " , soma)