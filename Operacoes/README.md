# Projeto Operações

Ler dois números inteiros, executar e mostrar o resultado das seguintes operações: adição, subtração, multiplicação e divisão.

```py
#Pegando os dados
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

#Fazendo os cálculos
adicao = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2

#Mostrando os resultados
print(f'\nA soma dos dois números é {adicao}')
print(f'\nA subtração dos dois números é {subtracao}')
print(f'\nA multiplicação dos dois números é {multiplicacao}')
print(f'\nA divisão dos dois números é {round(divisao, 2)}')
```