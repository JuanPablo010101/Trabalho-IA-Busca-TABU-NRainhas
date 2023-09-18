# Trabalho-IA-Busca-TABU-NRainhas
Este trabalho foi desenvolvido na disciplina de Inteligência Artificial com o
intuito de solucionar o problema das N rainhas utilizando a técnica de busca Tabu
para solucionar esse problema.

FUNÇÃO GERAR VALOR

A função "geraValor" utiliza a biblioteca `randint` para gerar um número
aleatório no intervalo de 1 até o valor máximo especificado. Esse número
aleatório é então retornado pela função e pode ser utilizado em outras funções
conforme necessário.

FUNÇÃO GERAR POSIÇÃO

A função "geraPosicao" recebe como entrada uma lista que representa as
posições das rainhas no tabuleiro e um número que representa a quantidade de
rainhas no tabuleiro de forma proporcional. Ela utiliza um loop para verificar se a
lista possui menos elementos do que o valor máximo permitido. Se a lista estiver
abaixo desse limite, a função insere as posições das rainhas utilizando a
biblioteca "geraValor" previamente descrita, garantindo que os valores inseridos
não se repitam.

FUNÇÃO DE ENCONTRAR AS DIAGONAIS QUE POSSUI RAINHAS QUE COLIDEM

As funções "diagonal_positiva" e "diagonal_negativa" têm a
responsabilidade de identificar colisões entre rainhas no tabuleiro, fornecendo o
resultado da operação com base na linha e coluna em que cada rainha está
localizada. Esses resultados são então registrados em listas, permitindo-nos
determinar a aptidão dessa posição. A aptidão é calculada pela função
"achaFitness" conforme descrito anteriormente.

FUNÇÃO ACHA FITNESS

Com a função "achaFitness," determinamos o número de colisões entre
rainhas, o que é útil como critério de parada para resolver nosso problema.
Registramos todas as operações relacionadas às diagonais em listas, em que a
aptidão é calculada como o tamanho da lista de operações menos o tamanho da
lista após a remoção de elementos repetidos. Isso nos permite encontrar a
melhor aptidão possível.

FUNÇÃO DE GERAR COMBINAÇÕES

Esta função tem como finalidade criar uma lista de combinações
potenciais para trocar as posições das linhas na lista das posições das rainhas,
garantindo que não haja repetições nos movimentos de troca possíveis.


FUNÇÃO DE REALIZAR TROCA DE ELEMENTOS

Essa função é responsável por trocar elementos de uma lista de posição entre
si.

FUNÇÃO DE ENCONTRAR A MELHOR SEQUÊNCIA.

Na função "melhor_sequencia," será realizada a busca pela melhor
aptidão, efetuando as trocas de posição possíveis na lista de posições das
rainhas. Se a aptidão resultante for menor do que a aptidão da solução inicial, a
nova lista será retornada, e a combinação de trocas realizadas será adicionada
à fila Tabu, impedindo seu uso por um período determinado de rodadas. Caso
não encontremos uma solução com fitness menor que a inicial, realizamos um
sorteio da lista de vizinhos que contem todas as trocas com o mesmo fitness e o
retornamos para que a busca não fique preso em uma área de solução e não
consiga encontrar o melhor resultado.

FUNÇÃO DE BUSCAR A MELHOR SOLUÇÃO POSSÍVEL

A função "Busca" desempenha um papel central na implementação do
algoritmo de busca local com estratégia de Tabu para resolver o desafiante
problema das "Oito Rainhas". Vamos desvendar seu funcionamento em
detalhes:
Dentro de um loop controlado, a busca persiste até que uma das
condições de parada seja alcançada: um número máximo de iterações seja
atingido ou seja encontrada uma solução ideal para o tabuleiro, na qual não
existem mais colisões entre as rainhas.
No decorrer desse processo, a função "MelhorSequencia" é utilizada para
identificar uma solução que apresente um valor de fitness (quantidade de
colisões entre as rainhas) inferior à configuração atual. No caso de sucesso, essa
nova configuração é adotada como a atual.
No interior do loop, uma estratégia crucial de controle é aplicada:
elementos da chamada "Fila Tabu", que temporariamente restringe algumas
trocas de posições, são retirados quando certas condições são atendidas. Esse
procedimento permite reavaliar as possibilidades previamente proibidas,
contribuindo para uma busca mais abrangente e eficaz.
Resumidamente, a função "Busca" é responsável por orquestrar a
execução do algoritmo de busca local com estratégia de Tabu. Ela garante que
a busca continue até que as metas sejam alcançadas e aproveita a função
"MelhorSequencia" para aprimorar constantemente as soluções em busca da

disposição ideal das oito rainhas no tabuleiro, onde não ocorre nenhum conflito
entre elas. A estratégia Tabu é empregada para evitar que o algoritmo fique
preso em soluções repetitivas, tornando a abordagem mais eficiente e eficaz.


Analise do comportamento do código:
Ao analisar o desempenho do código em relação à interação versus
fitness, conduzimos um teste no qual o algoritmo foi aplicado a um tabuleiro
contendo 100 rainhas. Definimos uma penalidade Tabu de 15 e um número
máximo de interações igual a 1000. A configuração inicial do tabuleiro foi gerada
aleatoriamente, apresentando um fitness inicial de 41, que corresponde ao
número de colisões entre as rainhas no tabuleiro.

o histórico de soluções à medida que o número de interações aumenta.
Conforme o código prossegue com a busca, o valor de fitness da solução tende
a diminuir, Neste caso específico, o código conseguiu atingir a melhor solução possível, que possui um fitness igual a 0,
após exatamente 39 interações. Este feito notável foi alcançado em um espaço
de tempo extremamente eficiente, totalizando apenas 2.93 segundos.
Essa análise demonstra a capacidade do código em encontrar soluções
otimizadas para o problema das "100 Rainhas".



Nesta seção, vamos examinar  à medida que aumentamos o tamanho do tabuleiro. Observamos que o tempo necessário para
encontrar a solução com o algoritmo de busca Tabu tende a aumentar
exponencialmente à medida que o tamanho do tabuleiro cresce. Isso se deve à
complexidade temporal do algoritmo em problemas de otimização, que é
aproximadamente O(M * N^2), onde M representa o número de iterações e N^2
é o custo do cálculo do fitness.

Essa análise indica que o aumento do tamanho do tabuleiro resulta em
um aumento quadrático no custo de calcular o fitness, tornando o processo de
busca mais demorado à medida que o tabuleiro se torna maior. Portanto, ao lidar
com tabuleiros maiores, é importante estar ciente de que o tempo de execução
pode crescer significativamente, tornando a otimização e a escolha adequada de
parâmetros críticas para alcançar um desempenho aceitável.
