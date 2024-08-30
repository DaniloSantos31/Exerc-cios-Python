'''Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa.
 Caso sexo seja “F” e estado civil seja “CASADA”, solicitar o tempo de casada (anos).'''

nome = input("Qual o seu nome?")
sexo = input("Sexo: M ou F")
estCiv = input("Casado ou solteiro?")

if estCiv == 'Casado':
  tempoDeCasado = int(input("Há quantos anos você está casado?"))
  print("Nome: " , nome , " Sexo: " , sexo , " Estado civil: " , estCiv , " Anos de casado: " , tempoDeCasado)

else:
  print("Nome:" , nome ,", Sexo:" , sexo ,", Estado civil:", estCiv)