'''Faça um algoritmo que leia dois valores inteiros A e B se os valores forem iguais deverá se somar os dois, caso contrário multiplique A por B.
 Ao final de qualquer um dos cálculos deve-se atribuir o resultado para uma variável C e mostrar seu conteúdo na tela.'''

a = int(input("Digite um número inteiro: "))
b = int(input("Digite outro número inteiro: "))

if a == b:
  soma = a + b
  print("A soma dos valores digitados é: " , soma)
else:
  multi = a * b
  print("A multiplicação dos valores digitados é: " , multi)