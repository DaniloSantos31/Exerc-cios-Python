'''Faça um algoritmo que leia uma variável e some 5 caso seja par ou some 8 caso seja ímpar, imprimir o resultado desta operação.'''

x = int(input("Digite um número maior que zero "))

if x % 2 == 0:
  soma = x + 5
  print("O número digitado + 5 é " , soma)
else:
  soma2 = x + 8
  print("O número digitado + 8 é " , soma2)