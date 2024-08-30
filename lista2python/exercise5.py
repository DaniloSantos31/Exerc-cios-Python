'''Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo, imprimindo o resultado.'''

x = int(input("Digite um número inteiro maior ou menor que zero: "))

if x > 0:
  dobro = x * 2
  print("O dobro do número digitado é: " , dobro)
if x < 0:
  triplo = x * 3
  print("O triplo do número digitado é " , triplo)