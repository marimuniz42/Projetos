# Calcular a média de um aluno que cursou a disciplina de Programação I, a partir da leitura das notas M1, M2 e M3; 
#passando por um cálculo da média aritmética. Após a média calculada, devemos anunciar se o aluno foi aprovado, reprovado ou pegou exame.

# - Se a média estiver entre 0.0 e 4.0, o aluno está reprovado
# - Se a média estiver entre 4.1 e 6.0, o aluno pegou exame
# - Se a média for maior do que 6.0, o aluno está aprovado
# - Se o aluno pegou exame, deve ser lida a nota do exame. Se a nota do exame for maior do que 6.0, está aprovado, senão; está reprovado

# Recebe as notas do aluno
M1 = float(input('Digite a nota da sua M1: '))
M2 = float(input('\nDigite a nota da sua M2: '))
M3 = float(input('\nDigite a nota da sua M3: '))

# Faz o cálculo da média aritmética
media = (M1 + M2 + M3) / 3
print(f'\nA média do aluno foi {media}')

# Mostra o resultado do aluno na matéria
if media >= 0.0 and media <= 4.0:
    print('\nO aluno foi reprovado.')
elif media >= 4.1 and media <= 6.0:
        print('\nO aluno pegou exame')
        notaExame = float(input('\nDigite a nota do seu exame: '))
        if notaExame >= 6.0:
            print('\nO aluno foi aprovado.')
        else:
            print('\nO aluno foi reprovado.')
else:
    print('\nO aluno foi aprovado.')