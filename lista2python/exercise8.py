'''Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

● para homens: (72.7 * h) – 58;

● para mulheres: (62.1 * h) – 44.7.'''

print("Cálculo de peso ideal")
sexo = input("Qual seu sexo? (M ou F)")
h = float(input("Qual sua altura? "))

if sexo == 'M':
  pesoIdeal = (72.1 * h) - 58
  print("Seu IMC é: " , pesoIdeal)
else:
  pesoIdeal = (62.1 * h) - 44.7
  print("seu IMC é: " , pesoIdeal)