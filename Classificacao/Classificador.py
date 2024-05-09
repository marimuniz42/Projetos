# Leia a idade do usuário e classifique-o em:
# - Criança – 0 a 12 anos
# - Adolescente – 13 a 17 anos
# - Adulto – acima de 18 anos
# - Se o usuário digitar um número negativo, mostrar a mensagem que a idade é inválida

#Recebe a idade do usuário
idade = int(input('Digite sua idade: '))

#Faz a classificação
categoria = ''
if idade >= 0 and idade <= 12:
    categoria = 'Criança'
elif idade > 12 and idade <= 18:
    categoria = 'Adolescente'
elif idade > 18:
    categoria = 'Adulto'
else:
  print('Idade inválida')

#Comunica qual a classificação
if categoria != '':
    print(f'Caro usuário sua categoria é {categoria}.')