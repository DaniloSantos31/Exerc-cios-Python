'''10) O IMC – Indice de Massa Corporal é um critério da Organização Mundial de Saúde para dar umaindicação sobre a condição de peso de uma pessoa adulta.
A fórmula é IMC = peso / ( altura )*2
Elabore um algoritmo que leia o peso e a altura de um adulto e mostre sua condição de acordo com a tabela abaixo.
IMC em adultos Condição:
Abaixo de 18,5 = Abaixo do peso
Entre 18,5 e 25 = Peso normal
Entre 25 e 30 = Acima do peso
Acima de 30 = obeso'''
#Calculadora de IMC
peso = float(input("Informe seu peso: "))
h = float(input("Informe a sua altura em metros: "))

imc = peso / (h ** 2)

if imc < 18.5:
  print(imc , "é abaixo do peso")

elif 18.5 < imc < 25:
  print(imc , "é peso normal")

elif 25 < imc < 30:
  print(imc , "é acima do peso")

elif imc > 30:
  print(imc , "é obeso")