# Projeto Cálculo Litros

Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz 12 Km por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem.

```py
#Pegando os dados necessários para o cálculo
tempoViagem = float(input('Qual foi o tempo gasto na viagem? '))
velocidadeMedia = float(input('Qual foi a velocidade média durante a viagem? '))

#Fazendo os cálculos
distancia = tempoViagem * velocidadeMedia
litrosUsados = distancia/12

#Mostrando os resultados
print(f'\nA sua velocidade média foi: {velocidadeMedia}')
print(f'\nO seu tempo gasto na viagem foi: {tempoViagem}')
print(f'\nA sua distância percorrida foi: {distancia}')
print(f'\nA sua quantidade de litros ultilizado na viagem foi: {round(litrosUsados,2)}')
```