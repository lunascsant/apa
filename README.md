# TRABALHO DE ANÁLISE E PROJETO DE ALGORITMOS

Trabalho da disciplina Análise e Projeto de Algoritmos – 2023/3
Seja uma lista de n inteiros positivos. Considerar três cenários de simulação: lista
pouco, médio e muito desordenada.
Para se criar uma instância realizar certo número de swaps ou trocas de 2 valores,
selecionados de forma aleatória, a partir de uma lista ordenada. Para tanto,
considerar os percentuais de 5, 25 e 45 % em relação ao tamanho da lista. 

Para cada cenário de simulação executar o algoritmo QuickSort considerando a
possibilidade de 6 tipos de escolhas de pivô.

<ol>
  <li>Pivô fixo na primeira posição da lista</li>
  <li>Pivô fixo na posição central da lista: [1+n] / 2</li>
  <li>Pivô média considerando a média do primeiro , central e último valores da lista</li>
  <li>Pivô randômico</li>
  <li>Pivô mediana</li>
  <li>Pivô computado pelo procedimento Acha Pivô</li>
</ol>

Construir para cada cenário e para cada alternativa de escolha do pivô um gráfico
relacionando o tempo de execução do algoritmo ao tamanho da lista. Portanto
deverão ser executadas simulações com tamanhos de lista 10², 10³, 10⁴... para
que o gráficos possam ser plotados com precisão. No total serão 18 gráficos. Para
cada medida de tempo de execução considerar a média de 10 execuções. Portanto
cada experimento deverá ser executado 10 vezes para que se obtenha uma média
do tempo de execução.

Realizar uma análise comparativa dos resultados destacando a influência da escolha
do pivô nos mesmos para cada cenário.
