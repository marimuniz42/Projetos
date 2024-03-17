#include <stdio.h>

int main()
{
    //declaraçôes de variáveis
    float nota1, nota2, nota3, dividedendo, mediaPonderada, peso1, peso2, peso3, somaPesos;
    char classificacao;
    
    //entrada de dados
    printf("Nota 1: ");
    scanf("%f" , &nota1); 
    printf("Nota 2: ");
    scanf("%f" , &nota2); 
    printf("Nota 3: ");
    scanf("%f" , &nota3);
    
    //processamento
    peso1 = 2;
    peso2 = 5;
    peso3 = 3;
    somaPesos = peso1 + peso2 + peso3;
    dividedendo = ((peso1 * nota1) + (peso2 * nota2) + (peso3 * nota3));
    mediaPonderada = dividedendo/somaPesos;
    
    //Classificação
    if (mediaPonderada > 9) {
        classificacao = 'A';
    } else if(mediaPonderada > 8) {
        classificacao = 'B';
    } else if(mediaPonderada > 7) {
        classificacao = 'C';
    } else if(mediaPonderada > 6) {
        classificacao = 'D';
    } else if(mediaPonderada > 5) {
        classificacao = 'E';
    } else {
        classificacao = 'F';
    }
    
    //saida de dados
    printf("A média aluno é = %.2f e a sua Classificação é %c", mediaPonderada, classificacao);
    
    return 0;
}