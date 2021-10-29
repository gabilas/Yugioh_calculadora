# Yugioh_calculadora

Calculadora para o card game yugioh. Onde cada jogador começa com 8000 (oito mil) pontos de vida,
e a condição de vitória é deixar o oponente com 0 pontos de vida ou fazer com que ele fique sem 
cartas no seu deck para que possa comprar cartas.



## To Do


- [X] Permitir que os jogadores indiquem os seus nomes;
- [X] Calcular todo o dano causado aos pontos de vida dos jogador;
- [X] Calcular todo o acréscimo de pontos de vida dos jogadores;
- [X] Identificar qual jogador venceu quando o oponente chega a 0 pts de vida.



## Instruções de uso



- Instalar o python 3;
- Identificar se quer alterar ou não o nome dos jogadores (O padrão é 'Jogador1' e Jogador2');
- Identificar qual jogador terá seus pontos de vida alterado;
- Digitar a quantidade de pontos de vida com o simbolo '-' antes do valor para caso de decréssimo;
- Digitar a quantidade de pontos de vida para caso de acréssimo;
- Quando um jogador chegar a 0 pts de vida o programa identificará o vencedor.



**Exemplo:**

- Cálculo de acréssimo:

=========================================================================
```
Pontos de vida dos jogadores:
Jogador1: 8000 pts
Jogador2: 8000 pts

Vai modificar a vida de qual jogador?
Jogador1 (1) ou Jogador2 (2)? 1

Caso o jogador esteja perdendo pontos de vida digite '-' antes do valor.
Quantos pontos ?200

Pontos de vida dos jogadores:
Jogador1: 8200 pts
Jogador2: 8000 pts
```
=========================================================================

- Cálculo de decréssimo:

=========================================================================
```
Pontos de vida dos jogadores:
Jogador1: 8000 pts
Jogador2: 8000 pts

Vai modificar a vida de qual jogador?
Jogador1 (1) ou Jogador2 (2)? 1

Caso o jogador esteja perdendo pontos de vida digite '-' antes do valor.
Quantos pontos?-200

Pontos de vida dos jogadores:
Jogador1: 7800 pts
Jogador2: 8000 pts
```
=========================================================================
