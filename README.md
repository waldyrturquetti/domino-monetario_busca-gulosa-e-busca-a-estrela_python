# Dominó Monetário

## Descrição

Sabe-se  que  jogos  educacionais  são  uma forma  lúdica  de  aprender.  Pensando  nisso,  uma variação do jogo do Dominó é jogo deDominó Monetário, que consisteem se
utilizar do Sistema Monetário para a criação das peças do jogo.Tendo em vista que o Sistema Monetário Brasileiro é formado por 7 Cédulas e 5 Moedas, ou seja, tem-se 12 tipos de valores. 
Sendo assim, adapte a quantidade de peçasdo Dominó tradicionalpara o Dominó Monetário. A Figura ilustra um exemplo de peças duplas do dominó monetário.


![image](https://user-images.githubusercontent.com/44614612/197432012-5776f2af-b51e-4ee2-9b12-4b735ccde9bd.png)


A quantidade de peças distribuídas paras os jogadores pode ser de 12 a 13 peças.  No Dominó Monetário inicia-se o jogo aquele que tem a peça R$200 x R$200 ou R$ 100 x R$ 100 ou R$ 50 x R$ 50 e assim por diante. O jogador que baixar todas as peças primeiro termina a jogada, assim como no jogo tradicional. As peças (valor monetário) que sobrarem na mão do adversário serão somadas eadicionadas a poupança do jogadorque terminou primeiro a jogada. Vence aquele que após 3 jogadastivermaisdinheiro acumulado na sua poupança.


## Implementação 

As peças devem ser distribuídas de forma aleatória para os jogadores (usuário e agente). Para a implementaçãodas jogadas do agente deverá ser utilizada a estratégia de busca com informação ou heurística por meio dos algoritmos: guloso e A*. Dessa forma, dois jogos devem ser implementados, um que utilize a busca gulosa para a jogada do agente e outro que utilize a busca A*.


## Resolução

### Busca Gulosa

A busca gulosa de melhor escolha foi implementada
através de um código em Python. Serão utilizados, no jogo
descrito no código, os nomes agente para se referir ao
agente inteligente, e jogador, para se referir ao usuário da
máquina.
A heurística da busca gulosa é aplicada da seguinte
maneira: no cenário em que o agente é o primeiro a jogar, é
escolhida a peça que possui o valor que mais se repete entre
os valores presentes em cada peça. São fornecidas treze (13)
peças a ambos. Primeiramente, observa-se qual peça mais se
repete para o agente. Caso entre essas treze (13) peças o
número cem (100) for o que aparecer mais vezes entre as
peças que o agente possui em seu rol de peças, é selecionada
em sua jogada todas as peças que possuírem o número cem
(100), e a peça a ser enviada à mesa é a peça com o valor
mais baixo na outra ponta, visando poupar o outro valor
para vencer o jogo.
Já nos casos em que a mesa não está vazia, ou seja, já
possui peças na mesa, são selecionadas todas as peças na
posse do computador que possuam o valor do canto
esquerdo ou do canto direito indicado na mesa. Depois de
selecionadas essas peças é escolhida a de valor mais baixo,
com o intuito de poupar valores altos. Depois de selecionadas as possíveis peças relativas à jogada, é
escolhida, entre estas, a que possui o menor valor na outra
ponta da peça. Dessa forma, tem-se certeza de que a peça
jogada é a de menor valor possível para aquela jogada.
O código abaixo demonstra o algoritmo da Busca Gulosa
de melhor escolha. O primeiro passo foi definir uma lista de
listas de tamanho 2 cada, onde o valor de índice zero
(esquerda) é referente a uma nota e o valor de índice um
(direita) é a quantidade de vezes que ele aparece na posse do
agente.
Em um segundo passo, faz-se a contagem da quantidade
de vezes que cada valor de nota aparece nas peças do
agente, de forma a incrementar uma unidade o segundo
valor de cada lista referente a cada nota.
Tendo essa contagem finalizada, o próximo passo é
identificar se a mesa está vazia (não possui nenhuma peça)
ou se possui outras peças. Caso não tenha nenhuma peça na
mesa, são selecionadas todas as peças que contém o número
de maior aparição e escolhe-se a de menor valor na outra
ponta.
Caso a mesa não esteja vazia, obtém-se os valores do
canto esquerdo e do canto direito da mesa. Em seguida,
selecionam-se todas as peças com o valor de maior número
de aparições das peças do agente que sejam igual ao valor
do canto esquerdo ou igual ao canto direito. Depois de
selecionadas todas essas peças, escolhe-se a de menor valor
na outra ponta.
Por fim, retorna-se dessa função dois valores, o primeiro
valor é a peça que o agente jogará entre as peças disponíveis
para a sua jogada, e o segundo valor é a posição a ser
jogada, podendo ser o canto esquerdo ou o canto direito.

### Busca A*

A implementação na busca A* se deu conforme o código
em linguagem de programação Python, e se difere em
relação ao código da busca Gulosa, vez que neste código é
possível intuir as possíveis jogadas através de um método
probabilístico. A fórmula heurística no método A* é f(n) =
g(n) + h(n).
Da mesma maneira que na busca gulosa, utilizamos
as notações agente para agente inteligente e jogador para o
usuário do computador.
Nesse algoritmo, a primeira etapa é selecionar as
possíveis peças a serem jogadas. Na seleção das peças
utiliza-se um método que retorna uma sub-lista de peças em
que tais peças possuem, ou no lado direito ou no lado
esquerdo, um valor que encaixe em uma das pontas da mesa.
A segunda etapa é definir a probabilidade por
peça de cada uma das peças selecionadas na primeira etapa.
A probabilidade é um mecanismo importante no
código em questão, pois é com ele que conseguimos fazer as
previsões de melhor jogada. Utilizou-se a probabilidade para definir qual a melhor
peça entre as possíveis peças a serem jogadas, com o
objetivo de bloquear a jogada do usuário, e assim ele ter que
comprar mais peças. O método de probabilidade por peça retorna a
probabilidade de que uma peça tem de bloquear a jogada do
usuário, sendo que probabilidade é um valor, retornado
dessa função, que calcula a chance de que o usuário não vai
ter a peça em questão para jogar em uma das duas pontas do
tabuleiro. Na f(n), a probabilidade por peça é o g(n).
Em relação a h(n), é o método quantidade de peças,
em que é feita a probabilidade de chances de ainda ter o
valor disponível para comprar (em ambos os lados) ou na
mão do jogador.

