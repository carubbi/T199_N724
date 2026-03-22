# Respostas dos exercícios de Barbetta (2010), capítulos 1, 2 e 3

Fonte dos enunciados: `exs/und1/barbetta2010_exercicios_cap_1_2_3.md`

## Capítulo 1

### Exercício 1

#### Enunciado

Dê um exemplo de uma situação prática em que é mais razoável um modelo empírico do que um modelo determinístico.

#### Resposta

Exemplo de situação em que um modelo empírico é mais razoável que um modelo determinístico:

- um exemplo adequado, na computação, é o estudo do tempo de carregamento de um aplicativo em uma rede compartilhada;
- um exemplo análogo, na engenharia, é o estudo da resistência à compressão de corpos de prova de concreto produzidos sob as mesmas condições nominais de dosagem.

#### Explicação conceitual

- um **modelo determinístico** é apropriado quando, dadas as mesmas condições de entrada, o resultado é sempre exatamente o mesmo;
- um **modelo empírico** é apropriado quando o fenômeno observado apresenta variabilidade, de modo que, mesmo sob condições aparentemente semelhantes, os resultados mudam de uma observação para outra;
- nesse caso, o objetivo não é supor uma relação exata e invariável entre entradas e saída, mas **descrever e explicar a variação observada nos dados**;
- isso não exclui o uso de relações matemáticas: em modelos empíricos, elas são tipicamente **ajustadas com base em dados observados** e interpretadas levando em conta a variabilidade aleatória.

Por que esse exemplo é empírico:

- no caso da computação, mesmo conhecendo fatores relevantes, como hardware, tamanho do arquivo, tráfego da rede e número de usuários simultâneos, o tempo de carregamento não permanece exatamente constante;
- no caso da engenharia, mesmo conhecendo fatores relevantes, como traço do concreto, tipo de cimento, relação água/cimento, tempo de cura e dimensões do corpo de prova, a resistência medida não permanece exatamente constante;
- em ambos os casos, existem fontes de variação difíceis de controlar integralmente;
- portanto, duas execuções computacionais em condições muito parecidas podem produzir tempos diferentes, assim como dois corpos de prova preparados sob condições nominais semelhantes podem apresentar resistências diferentes.

Consequência metodológica:

- em vez de assumir uma relação exata do tipo “dadas essas entradas, o resultado será precisamente tal valor”, é mais rigoroso coletar observações e resumir o comportamento por medidas como média, mediana, variância e desvio-padrão;
- além disso, pode-se estudar a distribuição dos tempos de resposta ou das resistências e verificar como ela muda conforme os fatores de interesse.

Conclusão:

- esses são casos em que o modelo empírico é mais razoável, porque o fenômeno real envolve incerteza e variabilidade observável, e a análise estatística fornece uma representação mais fiel do comportamento do sistema ou do material do que uma fórmula determinística exata.

### Exercício 2

#### Enunciado

Apresente, em uma situação prática, qual é a população, uma forma de amostragem e uma possível amostra.

#### Resposta

Exemplo:

- população: todos os estudantes matriculados em uma universidade no semestre atual;
- forma de amostragem: amostragem aleatória simples a partir da lista completa de matrícula, de modo que cada estudante tenha a mesma probabilidade de ser selecionado;
- possível amostra: $80$ estudantes sorteados dessa lista.

Nesse exemplo:

- a população é o conjunto total de interesse;
- a amostragem é o procedimento usado para selecionar os elementos;
- a amostra é o subconjunto efetivamente observado.

### Exercício 3

#### Enunciado

Dada a seguinte amostra: $\{7, 8, 6, 5, 9, 4\}$, calcule:

- a média;
- a variância;
- o desvio padrão.

#### Resposta

Dada a amostra $\{7, 8, 6, 5, 9, 4\}$, com $n = 6$:

$$
\bar{x} = \frac{7+8+6+5+9+4}{6} = \frac{39}{6} = 6,5
$$

$$
s^2 = \frac{(7-6,5)^2+(8-6,5)^2+(6-6,5)^2+(5-6,5)^2+(9-6,5)^2+(4-6,5)^2}{5}
$$

$$
s^2 = \frac{0,25+2,25+0,25+2,25+6,25+6,25}{5} = \frac{17,5}{5} = 3,5
$$

$$
s = \sqrt{3,5} \approx 1,871
$$

Resposta:

- média: $6,5$
- variância amostral: $3,5$
- desvio-padrão amostral: $1,871$

#### Observações

- o uso de $n-1$ no denominador corresponde à **correção de Bessel**;
- essa correção é necessária porque a média amostral $\bar{x}$ é estimada com os próprios dados, o que consome um grau de liberdade e faz com que apenas $n-1$ desvios em relação à média possam variar livremente;
- seu significado estatístico é compensar a tendência de a variância calculada com denominador $n$ subestimar a variabilidade populacional quando se trabalha com uma amostra;
- seu impacto é produzir uma estimativa de variância amostral maior do que a obtida com denominador $n$, reduzindo esse viés de subestimação;
- se os seis valores fossem tratados como a população completa de interesse, a variância populacional seria calculada com denominador $n$, produzindo valor diferente.

### Exercício 4

#### Enunciado

Para avaliar a qualidade de três empacotadoras $(A, B, C)$ de uma indústria de torrefação de café, realizou-se uma amostra de dez pacotes de café de cada empacotadora e mediu-se o peso líquido. O valor declarado é de $500\,g$. A empacotadora $A$ apresentou peso médio igual a $500,1\,g$ e variância $6,2$; a $B$ resultou em peso médio igual a $499,9\,g$ e variância $40,5$; e a $C$, peso médio igual a $530,3\,g$ e variância $5,8$. O que se pode dizer sobre as empacotadoras?

#### Resposta

Comparando as três empacotadoras com o valor declarado de $500\,g$:

- A: média amostral $500,1\,g$ e variância $6,2$. Na amostra observada, ficou muito próxima do alvo e com baixa variabilidade.
- B: média amostral $499,9\,g$ e variância $40,5$. Na amostra observada, ficou próxima do alvo, mas com variabilidade muito alta.
- C: média amostral $530,3\,g$ e variância $5,8$. Na amostra observada, apresentou baixa variabilidade, porém forte afastamento positivo em relação ao valor declarado.

Conclusão:

- a empacotadora **A** é a melhor;
- a **B** apresentou média amostral próxima do valor nominal, mas grande dispersão;
- a **C** mostrou-se pouco dispersa, porém fortemente **descalibrada** em relação ao alvo e inadequada do ponto de vista de conformidade.

#### Explicação conceitual

- uma empacotadora pode ter média amostral próxima do valor nominal e, ainda assim, produzir valores muito dispersos, o que compromete a qualidade;
- também pode ocorrer o oposto: baixa variabilidade, mas média deslocada do alvo, caracterizando um processo estável porém mal regulado;
- em controle de qualidade, o desempenho desejável combina **proximidade do alvo** em relação ao valor declarado e **baixa variabilidade** na produção.

### Exercício 5

#### Enunciado

Ao calcular a variância de um conjunto de valores, encontrou-se o valor $s^2 = 0$. O que se pode dizer sobre o conjunto de valores?

#### Resposta

Se $s^2 = 0$, então todos os valores do conjunto são iguais entre si. Logo, não há dispersão.

#### Explicação conceitual

- a variância mede o grau de afastamento dos valores em relação à média;
- se ela é nula, então a soma dos quadrados dos desvios em relação à média também é nula;
- como quadrados não podem assumir valores negativos, isso só é possível se todos os desvios em relação à média forem nulos;
- portanto, a única possibilidade é que todas as observações coincidam exatamente.

## Capítulo 2

### Exercício 1

#### Enunciado

Considerando a população apresentada a seguir, extraia uma amostra aleatória simples de $n = 6$ funcionários. Use a segunda linha da tabela de números aleatórios.

01. Aristóteles  
02. Anastácia  
03. Arnaldo  
04. Bartolomeu  
05. Bernardino  
06. Cardoso  
07. Carlito  
08. Cláudio  
09. Ermílio  
10. Ercílio  
11. Emestino  
12. Endevaldo  
13. Francisco  
14. Felício  
15. Fabrício  
16. Geraldo  
17. Gabriel  
18. Getúlio  
19. Hiraldo  
20. João da Silva  
21. Joana  
22. Joaquim  
23. Joaquina  
24. José da Silva  
25. José de Souza  
26. Josefa  
27. Josefina  
28. Maria José  
29. Maria Cristina  
30. Mauro  
31. Paula  
32. Paulo César

Tabela-base da população:

| Código | Nome | Código | Nome |
| ---: | --- | ---: | --- |
| 01 | Aristóteles | 17 | Gabriel |
| 02 | Anastácia | 18 | Getúlio |
| 03 | Arnaldo | 19 | Hiraldo |
| 04 | Bartolomeu | 20 | João da Silva |
| 05 | Bernardino | 21 | Joana |
| 06 | Cardoso | 22 | Joaquim |
| 07 | Carlito | 23 | Joaquina |
| 08 | Cláudio | 24 | José da Silva |
| 09 | Ermílio | 25 | José de Souza |
| 10 | Ercílio | 26 | Josefa |
| 11 | Emestino | 27 | Josefina |
| 12 | Endevaldo | 28 | Maria José |
| 13 | Francisco | 29 | Maria Cristina |
| 14 | Felício | 30 | Mauro |
| 15 | Fabrício | 31 | Paula |
| 16 | Geraldo | 32 | Paulo César |

#### Resposta

Consultando o livro original, a segunda linha da tabela de números aleatórios é:

$$
24,\ 50,\ 04,\ 55,\ 03,\ 24,\ 16,\ 41,\ 21,\ 96,\ 01,\ 71,\ 28,\ 50,\ 34,\ 31,\ 55,\ 36,\ 35,\ 73,\ 29,\ 13,\ 80,\ 21,\ 78,\ 89,\ 67,\ 59,\ 75,\ 53
$$

Lendo os pares na ordem e aplicando as regras do sorteio:

- $24$: aceita;
- $50$: rejeita, pois está fora do intervalo $01$ a $32$;
- $04$: aceita;
- $55$: rejeita;
- $03$: aceita;
- $24$: rejeita, pois já foi sorteado;
- $16$: aceita;
- $41$: rejeita;
- $21$: aceita;
- $96$: rejeita;
- $01$: aceita.

Assim, a amostra aleatória simples de tamanho $n = 6$ é formada pelos códigos:

$$
24,\ 04,\ 03,\ 16,\ 21,\ 01
$$

Correspondendo aos funcionários:

- $24$: José da Silva
- $04$: Bartolomeu
- $03$: Arnaldo
- $16$: Geraldo
- $21$: Joana
- $01$: Aristóteles

Observação:

- a ordem acima reflete a sequência de aceitação dos códigos na leitura da tabela de números aleatórios;
- como amostra aleatória simples, o ponto essencial é o conjunto dos elementos selecionados, e não uma ordenação alfabética ou numérica posterior dos sorteados.

Procedimento correto:

1. numerar os $32$ funcionários de $01$ a $32$;
2. ler pares de dígitos na segunda linha da tabela;
3. aceitar apenas números entre $01$ e $32$ ainda não sorteados;
4. rejeitar $00$, números acima de $32$ e repetições;
5. parar ao obter $6$ códigos válidos.

### Exercício 2

#### Enunciado

Usando a terceira linha da tabela de números aleatórios, extraia uma amostra aleatória simples de quatro letras do alfabeto da língua portuguesa.

#### Resposta

Consultando o livro original, a terceira linha da tabela de números aleatórios é:

$$
37,\ 18,\ 35,\ 56,\ 91,\ 02,\ 46,\ 60,\ 42,\ 61,\ 30,\ 39,\ 97,\ 56,\ 80,\ 66,\ 99,\ 11,\ 25,\ 62,\ 85,\ 03,\ 55,\ 70,\ 87,\ 30,\ 44,\ 10,\ 21,\ 77
$$

Adotando a convenção atual do alfabeto da língua portuguesa, com $26$ letras,

$$
01=A,\ 02=B,\ 03=C,\ \ldots,\ 26=Z,
$$

Aplicando as regras do sorteio:

- $37$: rejeita, pois está fora do intervalo $01$ a $26$;
- $18$: aceita;
- $35$: rejeita;
- $56$: rejeita;
- $91$: rejeita;
- $02$: aceita;
- $46$: rejeita;
- $60$: rejeita;
- $42$: rejeita;
- $61$: rejeita;
- $30$: rejeita;
- $39$: rejeita;
- $97$: rejeita;
- $56$: rejeita;
- $80$: rejeita;
- $66$: rejeita;
- $99$: rejeita;
- $11$: aceita;
- $25$: aceita.

Assim, a amostra aleatória simples de quatro letras é:

$$
18,\ 02,\ 11,\ 25
$$

Correspondendo a:

- $18$: R
- $02$: B
- $11$: K
- $25$: Y

Observação de rigor:

- essa resposta depende da convenção adotada para o alfabeto;
- sob a convenção atual, com $26$ letras, $K$, $W$ e $Y$ pertencem ao alfabeto e a codificação acima é válida;
- se fosse adotada uma convenção antiga, com menos letras, a amostra obtida a partir da mesma linha da tabela poderia ser diferente.

Procedimento:

1. numerar as letras do alfabeto;
2. ler os números da terceira linha em pares de dígitos;
3. aceitar apenas códigos válidos ainda não escolhidos;
4. continuar até obter $4$ letras distintas.

### Exercício 3

#### Enunciado

Os elementos de certa população estão dispostos numa lista, cuja numeração vai de $1.650$ a $8.840$. Descreva como você usaria uma tabela de números aleatórios para obter uma amostra de 100 elementos. Seria necessário efetuar nova numeração?

#### Resposta

Não é necessário efetuar nova numeração. Basta usar a própria numeração de $1650$ a $8840$.

Uma forma correta de proceder é a seguinte:

1. ler grupos de $4$ dígitos na tabela de números aleatórios;
2. aceitar somente números entre $1650$ e $8840$;
3. rejeitar números fora desse intervalo e repetições;
4. continuar até obter $100$ elementos distintos.

Por exemplo, se começarmos pela primeira linha da tabela do livro,

$$
3820\ 1007\ 5964\ 8990\ 8845\ 9584\ 0145\ 4074\ 8632\ 1386\ 3002\ 8021\ 6960\ 2715\ 9040,
$$

então a leitura inicial seria:

- $3820$: aceita, pois pertence ao intervalo $[1650, 8840]$;
- $1007$: rejeita, pois é menor que $1650$;
- $5964$: aceita;
- $8990$: rejeita, pois é maior que $8840$;
- $8845$: rejeita, pois é maior que $8840$;
- $9584$: rejeita;
- $0145$: rejeita;
- $4074$: aceita;
- $8632$: aceita;
- $1386$: rejeita;
- $3002$: aceita;
- $8021$: aceita;
- e assim sucessivamente, até completar $100$ elementos distintos.

Logo, a resposta conceitualmente correta é:

- **não** é necessário renumerar a população;
- a numeração de $1650$ a $8840$ já permite o sorteio direto por blocos de quatro dígitos;
- o cuidado necessário é apenas rejeitar valores fora do intervalo e valores repetidos.

#### Explicação conceitual

- a renumeração só seria necessária se a codificação existente não permitisse aplicar diretamente o mecanismo de sorteio;
- aqui isso não ocorre, porque todos os elementos já estão identificados por códigos numéricos de quatro algarismos;
- portanto, a tabela de números aleatórios pode ser usada diretamente sobre a própria lista original.

### Exercício 4

#### Enunciado

Seja um conjunto de 20 corpos de prova numerados de 1 a 20. Usando uma tabela de números aleatórios, divida aleatoriamente esses corpos de prova em dois grupos de dez elementos.

#### Resposta

Adotando a leitura da tabela de números aleatórios em pares de dígitos, e aceitando apenas valores entre $01$ e $20$ sem repetição, podemos proceder da seguinte forma.

Começando pela segunda linha da tabela do livro e prosseguindo para as seguintes quando necessário, os códigos válidos vão surgindo na seguinte ordem:

- 2ª linha: $04,\ 03,\ 16,\ 01,\ 13$
- 3ª linha: $18,\ 02,\ 11$
- 4ª linha: $05,\ 01,\ 14$
- 5ª linha: $07,\ 19,\ 06,\ 04,\ 07,\ 11,\ 10$

Aplicando a regra de aceitar apenas valores entre $01$ e $20$ sem repetição, os $10$ primeiros códigos válidos são:

$$
04,\ 03,\ 16,\ 01,\ 13,\ 18,\ 02,\ 11,\ 05,\ 14
$$

Assim, podemos formar:

- Grupo 1: $04,\ 03,\ 16,\ 01,\ 13,\ 18,\ 02,\ 11,\ 05,\ 14$
- Grupo 2: $06,\ 07,\ 08,\ 09,\ 10,\ 12,\ 15,\ 17,\ 19,\ 20$

Procedimento geral:

1. numerar os corpos de prova de $01$ a $20$;
2. ler pares de dígitos na tabela de números aleatórios;
3. aceitar apenas códigos entre $01$ e $20$, sem repetição;
4. formar o grupo 1 com os $10$ primeiros códigos válidos;
5. colocar os $10$ códigos restantes no grupo 2.

#### Explicação conceitual

- a aleatorização serve para evitar que a divisão em grupos seja influenciada por ordem, posição ou preferência do pesquisador;
- ao usar uma tabela de números aleatórios e uma regra fixa de aceitação, reduz-se a interferência subjetiva do pesquisador, o que ajuda a evitar viés de alocação;
- quando os $10$ primeiros códigos válidos são escolhidos aleatoriamente, cada corpo de prova tem a mesma chance inicial de ser selecionado para o Grupo 1;
- isso ajuda a tornar os grupos comparáveis e reduz viés na etapa experimental.

### Exercício 5

#### Enunciado

Selecione uma amostra estratificada uniforme, de tamanho $n = 12$, da população do Exercício 1.

#### Resposta

O enunciado não explicita a variável de estratificação. Portanto, **não existe uma única amostra correta** sem definir antes os estratos.

Se adotarmos, por exemplo, a variável $sexo$ como critério de estratificação, então uma amostragem estratificada **uniforme** com dois estratos teria:

- $6$ pessoas no estrato masculino;
- $6$ pessoas no estrato feminino.

Uma possível amostra, sob esse critério, seria:

- homens: $01$ Aristóteles, $03$ Arnaldo, $04$ Bartolomeu, $05$ Bernardino, $06$ Cardoso, $07$ Carlito;
- mulheres: $02$ Anastácia, $21$ Joana, $23$ Joaquina, $26$ Josefa, $27$ Josefina, $28$ Maria José.

#### Observação

- essa alocação é uniforme, mas **não proporcional**, porque a população não tem a mesma quantidade de homens e mulheres.
- a amostra acima é apenas um exemplo possível; em uma aplicação efetiva, os $6$ elementos de cada estrato deveriam ser sorteados aleatoriamente dentro de cada grupo.

#### Explicação conceitual

- na amostragem estratificada uniforme, cada estrato recebe o mesmo tamanho amostral, independentemente de seu tamanho na população;
- isso pode ser útil quando se deseja comparar estratos com o mesmo nível de detalhe;
- já na amostragem proporcional, o tamanho amostral em cada estrato preserva a composição relativa da população.

### Exercício 6

#### Enunciado

Considerando a população de funcionários do exercício 1, faça uma amostragem estratificada proporcional de tamanho $n = 8$, usando a variável sexo para a formação dos estratos.

#### Resposta

Adotando a variável $sexo$ e classificando os nomes da lista:

- homens: $24$
- mulheres: $8$
- total: $32$

Na amostragem estratificada proporcional com $n = 8$:

$$
n_h = n\cdot \frac{N_h}{N}
$$

Logo,

$$
n_{\text{homens}} = 8\cdot \frac{24}{32} = 6
$$

$$
n_{\text{mulheres}} = 8\cdot \frac{8}{32} = 2
$$

Resposta:

- selecionar $6$ homens e $2$ mulheres, de modo aleatório dentro de cada estrato.

Uma possível amostra estratificada proporcional seria:

- homens: $01$ Aristóteles, $03$ Arnaldo, $04$ Bartolomeu, $05$ Bernardino, $06$ Cardoso, $07$ Carlito;
- mulheres: $02$ Anastácia, $21$ Joana.

#### Explicação conceitual

- a vantagem da alocação proporcional é reproduzir, na amostra, a estrutura da população em relação à variável de estratificação;
- isso tende a melhorar a representatividade global quando os estratos têm tamanhos muito diferentes;
- além disso, a estratificação só é metodologicamente útil quando os sorteios dentro de cada estrato continuam sendo aleatórios;
- a amostra listada acima é apenas um exemplo possível, já que outras seleções aleatórias dentro dos mesmos estratos também seriam válidas.

### Exercício 7

#### Enunciado

Comente os seguintes planos de amostragens, apontando suas incoerências, quando for o caso.

- Com a finalidade de estudar o perfil dos consumidores de um supermercado, observaram-se os consumidores que compareceram ao supermercado no primeiro sábado do mês.
- Com a finalidade de estudar o perfil dos consumidores de um supermercado, fez-se a coleta de dados durante um mês, tomando a cada dia um consumidor da fila de cada caixa do supermercado, variando sistematicamente o horário da coleta dos dados.
- Para avaliar a qualidade dos itens que saem de uma linha de produção, observaram-se todos os itens das $14h$ às $14h30min$.
- Para avaliar a qualidade dos itens que saem de uma linha de produção, observou-se um item a cada meia hora, durante todo o dia.
- Para estimar a percentagem de empresas que investiram em novas tecnologias no último ano, enviou-se um questionário a todas as empresas. A amostra foi formada pelas empresas que responderam ao questionário.

#### Resposta

#### Item a

Plano inadequado. Observar apenas o primeiro sábado do mês induz viés temporal e pode não representar o perfil médio dos consumidores.

#### Item b

Plano adequado com ressalvas. Distribui a coleta ao longo do mês, em horários variados e em diferentes caixas. Ainda assim, pode haver viés de seleção se a escolha do consumidor em cada fila não for aleatória.

#### Item c

Plano inadequado. Observar todos os itens apenas das $14h$ às $14h30min$ pode capturar apenas uma faixa específica do processo produtivo.

#### Item d

Plano adequado com ressalvas. A observação ao longo de todo o dia tende a captar variações temporais do processo, embora ainda possa deixar de detectar padrões mais complexos do processo produtivo.

#### Item e

Plano inadequado como amostra probabilística. A amostra final é formada por **auto-seleção** dos respondentes, com forte risco de viés de não resposta.

#### Explicação conceitual

- nos itens acima, o ponto central é avaliar se a amostra consegue representar a população sem privilegiar certos períodos, perfis ou comportamentos;
- sempre que a coleta fica concentrada em um único horário, dia ou condição operacional, surge risco de **viés de seleção**;
- quando a participação depende da iniciativa do próprio elemento, como no caso do questionário respondido voluntariamente, aparece também o problema de **viés de não resposta**;
- por isso, um plano amostral adequado deve distribuir a observação ao longo das fontes relevantes de variação e reduzir mecanismos de auto-seleção.

### Exercício 8

#### Enunciado

Apresente as 32 combinações de sinais em que os fatores $A$, $B$, $C$, $D$ e $E$ devem ser ensaiados em um projeto $2^5$ completo. Anote os ensaios que devem ser realizados em um projeto $2^{5-1}$, considerando a relação $I = ABCDE$. Repare que você pode construir o mesmo projeto fazendo, inicialmente, um projeto $2^4$ completo e, depois, inserindo a coluna $E$ com a relação $E = ABCD$.

#### Resposta

Um projeto $2^5$ completo possui $32$ combinações de sinais:

| Cond. | A | B | C | D | E | ABCDE |
| ---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | - | - | - | - | - | - |
| 2 | - | - | - | - | + | + |
| 3 | - | - | - | + | - | + |
| 4 | - | - | - | + | + | - |
| 5 | - | - | + | - | - | + |
| 6 | - | - | + | - | + | - |
| 7 | - | - | + | + | - | - |
| 8 | - | - | + | + | + | + |
| 9 | - | + | - | - | - | + |
| 10 | - | + | - | - | + | - |
| 11 | - | + | - | + | - | - |
| 12 | - | + | - | + | + | + |
| 13 | - | + | + | - | - | - |
| 14 | - | + | + | - | + | + |
| 15 | - | + | + | + | - | + |
| 16 | - | + | + | + | + | - |
| 17 | + | - | - | - | - | + |
| 18 | + | - | - | - | + | - |
| 19 | + | - | - | + | - | - |
| 20 | + | - | - | + | + | + |
| 21 | + | - | + | - | - | - |
| 22 | + | - | + | - | + | + |
| 23 | + | - | + | + | - | + |
| 24 | + | - | + | + | + | - |
| 25 | + | + | - | - | - | - |
| 26 | + | + | - | - | + | + |
| 27 | + | + | - | + | - | + |
| 28 | + | + | - | + | + | - |
| 29 | + | + | + | - | - | + |
| 30 | + | + | + | - | + | - |
| 31 | + | + | + | + | - | - |
| 32 | + | + | + | + | + | + |

Com a relação geradora

$$
I = ABCDE
$$

devem ser realizados os ensaios com $ABCDE = +$, isto é, as condições:

$$
2,\ 3,\ 5,\ 8,\ 9,\ 12,\ 14,\ 15,\ 17,\ 20,\ 22,\ 23,\ 26,\ 27,\ 29,\ 32.
$$

Equivalente:

$$
E = ABCD.
$$

#### Explicação conceitual

- em um projeto fatorial completo $2^5$, todas as combinações possíveis dos níveis são observadas;
- já na fração $2^{5-1}$, trabalha-se com apenas metade dos ensaios, escolhidos segundo uma relação geradora;
- a vantagem é reduzir custo experimental; a desvantagem é introduzir **confundimento** entre certos efeitos, o que exige cuidado na interpretação.

### Exercício 9

#### Enunciado

Calcule a variância agregada do experimento do Exemplo 2.4. Quantos graus de liberdade estão associados a essa medida?

#### Resposta

Pela fórmula da variância agregada:

$$
s_p^2 = \frac{\sum_{i=1}^{g}(n_i-1)s_i^2}{\sum_{i=1}^{g}(n_i-1)}
$$

No Exemplo 2.4, há:

- $g = 8$ condições experimentais;
- $n = 2$ replicações por condição.

Logo, os graus de liberdade são:

$$
gl = g(n-1) = 8(2-1)=8.
$$

Entretanto, a tabela transcrita do Exemplo 2.4 **não fornece as variâncias ou os dados das replicações em cada condição**. Assim:

- graus de liberdade: $8$
- variância agregada numérica: **não determinável com os dados transcritos**

#### Explicação conceitual

- a variância agregada combina a variabilidade interna de todos os tratamentos em uma única medida;
- os graus de liberdade indicam quanta informação independente sustenta essa estimativa;
- por isso, mesmo conhecendo a fórmula e os graus de liberdade, não é possível obter o valor numérico sem as variâncias dos tratamentos ou os dados brutos das replicações.

### Exercício 10

#### Enunciado

Para avaliar o efeito dos fatores: $(A)$ tempo de hidratação ($14$ dias/$28$ dias), $(B)$ relação água/cimento ($0,38$ e $0,58$) e $(C)$ tipo de cimento (comum e pozolânico) na resistência à compressão de um concreto $(Y)$, realizou-se um experimento cujos resultados da resistência (em MPa) são apresentados a seguir. Calcule os efeitos principais e as interações de segunda ordem.

| Tipo de cimento | Relação água/cimento | 14 dias | 28 dias |
| --- | --- | ---: | ---: |
| comum | 0,38 | 23,1 | 42,2 |
| comum | 0,58 | 12,0 | 27,9 |
| pozolânico | 0,38 | 24,3 | 39,5 |
| pozolânico | 0,58 | 11,1 | 24,3 |

#### Resposta

Adotando:

- $A$: tempo de hidratação ($14$ dias = $-$, $28$ dias = $+$);
- $B$: relação água/cimento ($0,38$ = $-$, $0,58$ = $+$);
- $C$: tipo de cimento (comum = $-$, pozolânico = $+$).

Pelo efeito

$$
ef = \bar{y}_{+} - \bar{y}_{-},
$$

obtém-se:

- $ef(A) = 15,85$
- $ef(B) = -13,45$
- $ef(C) = -1,50$
- $ef(AB) = -1,30$
- $ef(AC) = -1,65$
- $ef(BC) = -0,75$

Interpretação:

- o tempo de hidratação ($A$) tem forte efeito positivo;
- aumentar a relação água/cimento ($B$) reduz fortemente a resistência;
- o tipo de cimento ($C$) tem efeito pequeno, na forma transcrita do exercício;
- as interações de segunda ordem são pequenas em comparação com os efeitos principais de $A$ e $B$.

#### Explicação conceitual

- um **efeito principal** mede a mudança média na resposta quando se altera um fator, mantendo-se a estrutura do experimento;
- uma **interação** mede se o efeito de um fator depende do nível de outro;
- como os efeitos de interação ficaram pequenos em módulo, a leitura dominante é que os fatores $A$ e $B$ influenciam a resposta de forma mais direta e relevante do que suas combinações de segunda ordem.

### Exercício 11

#### Enunciado

Em *Applied Statistics*, $v.\ 42$, nº $4$, $p.\ 671\text{-}681$ ($1993$), M. G. Tuck e J. I. L. Cottrell realizaram vários experimentos para obter uma farinha de pão de melhor qualidade. Misturaram à farinha de trigo pequenas quantidades de ingredientes permitidos. Os fatores correspondem à quantidade de cada ingrediente adicionado à farinha, sendo que o nível inferior corresponde à ausência do ingrediente.

Parte de um dos experimentos foi realizada sob um projeto $2^{6-2}$, em que os fatores $A$, $B$, $C$ e $E$ formaram um projeto $2^4$ completo. Os sinais do fator $D$ foram obtidos através da relação $D = ABC$ e os sinais do fator $F$ foram obtidos através da relação $F = BCE$. A resposta $(y)$ foi o volume médio dos pães. Em cada condição experimental, realizaram-se quatro ensaios. A tabela a seguir apresenta a média $y$ e o desvio padrão $s$ do volume específico nas quatro replicações em cada combinação dos níveis dos fatores.

| Condição experimental | A | B | C | D | E | F | y | s |
| ---: | :---: | :---: | :---: | :---: | :---: | :---: | ---: | ---: |
| 1 | - | - | - | - | - | - | 429,25 | 75,39 |
| 2 | - | - | - | - | + | + | 433,00 | 69,40 |
| 3 | - | - | + | + | - | + | 454,25 | 88,99 |
| 4 | - | - | + | + | + | - | 456,75 | 82,24 |
| 5 | - | + | - | + | - | + | 446,75 | 74,09 |
| 6 | - | + | - | + | + | - | 447,75 | 80,93 |
| 7 | - | + | + | - | - | - | 455,50 | 89,58 |
| 8 | - | + | + | - | + | + | 448,25 | 74,24 |
| 9 | + | - | - | + | - | - | 458,75 | 79,47 |
| 10 | + | - | - | + | + | + | 449,50 | 84,58 |
| 11 | + | - | + | - | - | + | 463,75 | 91,67 |
| 12 | + | - | + | - | + | - | 466,00 | 88,99 |
| 13 | + | + | - | - | - | + | 449,50 | 88,88 |
| 14 | + | + | - | - | + | - | 452,75 | 98,27 |
| 15 | + | + | + | + | - | - | 469,00 | 82,30 |
| 16 | + | + | + | + | + | + | 471,50 | 75,11 |

#### Resposta

#### Item a

Efeitos principais sobre a média $y$:

- $ef(A) = 13,65625$
- $ef(B) = 3,71875$
- $ef(C) = 14,71875$
- $ef(D) = 7,03125$
- $ef(E) = -0,15625$
- $ef(F) = -2,40625$

Os fatores que mais alteram o nível médio da resposta são:

1. $C$
2. $A$
3. $D$

Para maximizar o volume dos pães pela lógica dos efeitos principais:

- escolher nível $+$ para fatores com efeito positivo;
- escolher nível $-$ para fatores com efeito negativo.

Assim, a recomendação é:

- $A = +$
- $B = +$
- $C = +$
- $D = +$
- $E = -$
- $F = -$

Observação importante de rigor:

- como se trata de fração $2^{6-2}$, apenas parte desses fatores é independente;
- pelas relações geradoras, a combinação acima é consistente e corresponde à condição $15$;
- empiricamente, a maior média observada na tabela foi a condição $16$ ($471,50$), muito próxima da condição $15$ ($469,00$), o que sugere cautela na interpretação dos efeitos pequenos de $E$ e $F$.

#### Item b

Efeitos principais sobre o desvio-padrão $s$:

- $ef(A) = 6,80125$
- $ef(B) = 0,33375$
- $ef(C) = 2,76375$
- $ef(D) = -3,58875$
- $ef(E) = -2,07625$
- $ef(F) = -3,77625$

O fator que mais altera a variabilidade é $A$.

Como $ef(A) > 0$, o nível $+$ aumenta o desvio-padrão. Logo, para **minimizar a variabilidade**, $A$ deve ser fixado no nível $-$.

#### Explicação conceitual

- aqui aparecem dois objetivos experimentais distintos: elevar a média da resposta e reduzir sua variabilidade;
- em problemas de engenharia, essas metas nem sempre apontam para a mesma configuração;
- por isso, a interpretação correta deve separar **efeito sobre o nível médio** e **efeito sobre a estabilidade do processo**.

## Capítulo 3

### Exercício 3

#### Enunciado

Dado o seguinte conjunto de dados: $\{7, 8, 6, 10, 5, 9, 4, 12, 7, 8\}$, calcule:

- a média;
- o desvio padrão.

#### Resposta

Dados:

$$
\{7,8,6,10,5,9,4,12,7,8\}
$$

Com $n = 10$:

$$
\bar{x} = \frac{76}{10} = 7,6
$$

$$
s^2 = 5,6
$$

$$
s = \sqrt{5,6} \approx 2,366
$$

Resposta:

- média: $7,6$
- desvio-padrão amostral: $2,366$

### Exercício 4

#### Enunciado

Calcule a média e o desvio padrão da seguinte distribuição de frequências, a qual se refere ao número de defeitos encontrados em placas de circuito integrado.

#### Resposta

Distribuição:

| Número de defeitos | Frequência |
| ---: | ---: |
| 0 | 30 |
| 1 | 25 |
| 2 | 10 |
| 3 | 5 |
| 4 | 2 |

Total:

$$
n = 30+25+10+5+2 = 72
$$

Média:

$$
\bar{x} = \frac{0\cdot 30 + 1\cdot 25 + 2\cdot 10 + 3\cdot 5 + 4\cdot 2}{72}
= \frac{68}{72}
= 0,9444
$$

Variância amostral:

$$
s^2 \approx 1,0955
$$

Desvio-padrão amostral:

$$
s \approx 1,0466
$$

Resposta:

- média: $0,9444$
- desvio-padrão amostral: $1,0466$

### Exercício 5

#### Enunciado

Considerando os dados do **Exemplo 3.2** sobre os 50 tempos de carga de um aplicativo em um sistema compartilhado, obtenha a mediana e os quartis.

#### Resposta

Considerando os dados do **Exemplo 3.2** sobre os 50 tempos de carga do aplicativo, e usando a convenção de posições adotada no próprio material:

$$
\text{posição da mediana} = \frac{n+1}{2} = \frac{51}{2} = 25,5
$$

Logo,

$$
md = \frac{5,9 + 6,0}{2} = 5,95
$$

Para os quartis:

$$
\text{posição de } q_i = \frac{n+1}{4} = 12,75 \Rightarrow q_i = 5,175
$$

$$
\text{posição de } q_s = \frac{3(n+1)}{4} = 38,25 \Rightarrow q_s = 6,925
$$

Resposta:

- mediana: $5,95$
- quartil inferior: $5,175$
- quartil superior: $6,925$

#### Observação

- os quartis foram obtidos pela convenção de posições baseada em $p(n+1)$, adotada no próprio material, com interpolação linear quando a posição teórica do quantil não é inteira.

### Exercício 6

#### Enunciado

Com o objetivo de direcionar campanhas de marketing, uma livraria virtual está registrando o número de acessos diários em algumas de suas páginas da Web, nos últimos três meses. A tabela a seguir mostra medidas descritivas desses registros, em páginas de três categorias de livros.

| Livro | Média | Desvio padrão | Quartil inferior | Mediana | Quartil superior |
| --- | ---: | ---: | ---: | ---: | ---: |
| Romance | 910 | 690 | 412 | 650 | 1.500 |
| Ficção | 220 | 180 | 145 | 398 | 1.023 |
| Técnico | 630 | 480 | 115 | 190 | 1.500 |

- Quais as diferenças das três distribuições em termos de posição central e dispersão?
- As medidas sugerem distribuições simétricas?

#### Resposta

#### Item a

Em termos de posição central:

- $Romance$ tem maior média e mediana que $Técnico$ e, pelos dados transcritos, média maior que $Ficção$;
- $Técnico$ tem mediana baixa ($190$), mas média relativamente alta ($630$), o que indica forte influência de valores altos;
- $Ficção$ apresenta, na transcrição, média ($220$) bem abaixo da mediana ($398$).

Em termos de dispersão:

- $Romance$ tem alta dispersão: $s = 690$ e $DIQ = 1500 - 412 = 1088$;
- $Ficção$ também tem grande dispersão central: $DIQ = 1023 - 145 = 878$;
- $Técnico$ apresenta $s = 480$ e $DIQ = 1500 - 115 = 1385$, indicando forte heterogeneidade.

#### Item b

As medidas **não sugerem simetria**.

- $Romance$: como média $910$ é maior que mediana $650$, há indício de assimetria à direita.
- $Técnico$: a diferença entre média $630$ e mediana $190$, além do quartil superior muito alto, sugere assimetria acentuada à direita.
- $Ficção$: os valores transcritos sugerem **inconsistência ou forte assimetria**, porque a média é menor que a mediana, mas o quartil superior é muito elevado. Assim, não há suporte para supor simetria.

#### Explicação conceitual

- em distribuições aproximadamente simétricas, média e mediana tendem a assumir valores próximos;
- quando a média fica muito acima da mediana, costuma haver cauda à direita, pois valores altos puxam a média para cima;
- os quartis complementam essa leitura, pois mostram se a metade central dos dados está concentrada ou espalhada e se há desbalanceamento entre as caudas.

### Exercício 7

#### Enunciado

Os dados a seguir são leituras da pressão do homogeneizador de um laticínio.

#### Leite tipo C

$$
3,0\ 3,1\ 3,0\ 3,0\ 3,0\ 2,9\ 2,9\ 3,0\ 3,1\ 2,9\ 3,0\ 3,0\ 3,0\ 3,0\ 3,0\ 3,0\ 3,0\ 3,0\ 3,0\ 3,0\ 2,9
$$

#### Leite UHT

$$
2,2\ 2,2\ 2,3\ 2,2\ 2,2\ 2,2\ 2,4\ 2,4\ 2,2\ 2,4\ 2,6\ 2,6\ 2,4\ 2,2\ 2,2\ 2,8\ 2,6\ 2,2\ 2,6\ 2,4\ 2,0
$$

Para cada conjunto de dados, calcule as medidas descritivas que você conhece. Com base nessas medidas, comente as principais diferenças entre os dois conjuntos de valores.

#### Resposta

#### Leite tipo C

Medidas descritivas:

- $n = 21$
- média: $2,9905$
- variância amostral: $0,0029$
- desvio-padrão amostral: $0,0539$
- mediana: $3,0$
- $Q_1 = 3,0$
- $Q_3 = 3,0$
- mínimo: $2,9$
- máximo: $3,1$
- amplitude: $0,2$
- coeficiente de variação: aproximadamente $1,80\%$

#### Leite UHT

Medidas descritivas:

- $n = 21$
- média: $2,3476$
- variância amostral: $0,0396$
- desvio-padrão amostral: $0,1990$
- mediana: $2,3$
- $Q_1 = 2,2$
- $Q_3 = 2,5$
- mínimo: $2,0$
- máximo: $2,8$
- amplitude: $0,8$
- coeficiente de variação: aproximadamente $8,48\%$

#### Comparação

- o leite tipo $C$ tem nível central mais alto, concentrado em torno de $3,0$;
- o $UHT$ tem nível central menor, em torno de $2,3$ a $2,4$;
- o $UHT$ é muito mais variável;
- o tipo $C$ é extremamente estável, com valores quase todos iguais a $3,0$.

#### Explicação conceitual

- essa comparação mostra que duas distribuições podem diferir ao mesmo tempo em **posição** e **dispersão**;
- posição descreve o nível típico da variável, enquanto dispersão informa o grau de oscilação em torno desse nível;
- o coeficiente de variação reforça essa leitura porque expressa a dispersão em termos relativos ao nível médio.

### Exercício 8

#### Enunciado

Bernardin (Mestrado Engenharia Mecânica/UFSC, 1994) realizou um experimento que tinha o objetivo de melhorar a qualidade do processo de formulação de massa cerâmica para pavimento. Os corpos de prova eram “biscoitos” que saíam do processo de queima e a qualidade era avaliada por três variáveis:

- $X_1 =$ retração linear (%)
- $X_2 =$ resistência mecânica
- $X_3 =$ absorção de água (%)

O experimento foi realizado sob 8 condições diferentes (no estudo original eram 18). Foram feitos 5 ensaios em cada uma das 8 condições experimentais. Os dados são apresentados a seguir:

| C | X1 | X2 | X3 | C | X1 | X2 | X3 | C | X1 | X2 | X3 | C | X1 | X2 | X3 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 8,9 | 41,1 | 5,5 | 3 | 9,4 | 50,0 | 0,8 | 5 | 13,4 | 60,6 | 0,5 | 7 | 12,9 | 41,1 | 0,2 |
| 1 | 9,2 | 39,0 | 4,8 | 3 | 9,9 | 48,3 | 0,6 | 5 | 13,4 | 60,0 | 0,5 | 7 | 12,4 | 39,0 | 0,4 |
| 1 | 8,0 | 36,9 | 6,2 | 3 | 9,6 | 50,1 | 0,6 | 5 | 13,6 | 68,4 | 0,2 | 7 | 12,6 | 36,9 | 0,5 |
| 1 | 8,7 | 39,2 | 5,7 | 3 | 9,2 | 49,9 | 0,7 | 5 | 13,4 | 60,8 | 0,7 | 7 | 12,6 | 39,2 | 0,4 |
| 1 | 8,7 | 35,9 | 5,5 | 3 | 9,4 | 56,2 | 0,5 | 5 | 12,4 | 51,4 | 1,0 | 7 | 12,9 | 35,9 | 0,3 |
| 2 | 12,6 | 52,7 | 0,9 | 4 | 6,6 | 31,2 | 9,0 | 6 | 9,6 | 41,2 | 3,9 | 8 | 8,2 | 40,8 | 4,4 |
| 2 | 13,6 | 53,5 | 0,4 | 4 | 6,4 | 25,3 | 10,2 | 6 | 10,6 | 53,0 | 4,5 | 8 | 9,2 | 43,8 | 3,9 |
| 2 | 11,6 | 47,0 | 1,3 | 4 | 5,9 | 22,8 | 10,5 | 6 | 8,9 | 37,0 | 3,3 | 8 | 9,2 | 48,6 | 4,0 |
| 2 | 10,1 | 31,1 | 1,8 | 4 | 5,9 | 27,5 | 10,6 | 6 | 7,5 | 30,1 | 3,0 | 8 | 8,5 | 46,9 | 4,3 |
| 2 | 12,1 | 50,9 | 1,1 | 4 | 6,8 | 31,9 | 9,3 | 6 | 8,9 | 41,6 | 3,5 | 8 | 8,7 | 46,2 | 4,1 |

- Como as variáveis $X_1$, $X_2$ e $X_3$ podem ser classificadas (qualitativas, quantitativas discretas ou quantitativas contínuas)?
- Apresente a distribuição de frequências de $X_1$ através de um diagrama ramo-e-folhas. Comente a forma da distribuição.
- Apresente as distribuições de frequências de $X_2$ e $X_3$ através de histogramas. Comente as formas das distribuições.
- Calcule a média e o desvio padrão de $X_3$ para cada condição experimental (por simplicidade, considere apenas as condições 1, 4 e 8). Quais as informações que podem ser extraídas com estas medidas?
- Construa diagramas de pontos para $X_3$ nas condições experimentais 1, 4 e 8. As informações fornecidas por esses diagramas são iguais às obtidas no item anterior?
- Calcule a mediana e quartis de $X_1$ (sugestão: use o diagrama ramo-e-folhas do item (b)).
- Construa um diagrama em caixas para $X_1$.
- Considere o objetivo de verificar qual das variáveis ($X_1$, $X_2$ e $X_3$) apresenta maior variabilidade. Qual medida de dispersão você deve usar?

#### Resposta

#### Item a

As três variáveis são **quantitativas contínuas**, pois representam medidas em escala contínua:

- $X_1$: retração linear (%)
- $X_2$: resistência mecânica
- $X_3$: absorção de água (%)

#### Item b

Ramo-e-folhas de $X_1$ (caule = parte inteira; folha = décimo):

```text
5 | 9 9
6 | 4 6 8
7 | 5
8 | 0 2 5 7 7 7 9 9 9
9 | 2 2 2 2 4 4 6 6 9
10 | 1 6
11 | 6
12 | 1 4 4 6 6 6 9 9
13 | 4 4 4 6 6
```

Comentário:

- a distribuição não parece unimodal nem aproximadamente simétrica;
- há concentração em faixas distintas, refletindo a mistura de várias condições experimentais;
- visualmente, trata-se de uma distribuição **heterogênea e multimodal**.

#### Explicação conceitual

- quando os dados são produzidos sob várias condições experimentais, a distribuição conjunta pode deixar de representar uma única população homogênea;
- nesse caso, picos em diferentes regiões sugerem a presença de **subgrupos** com comportamentos distintos;
- por isso, a análise gráfica ajuda a detectar estruturas que uma única média global pode esconder.

#### Item c

Sem construir as figuras, a leitura dos dados indica:

- $X_2$: distribuição ampla e heterogênea, com concentrações em regiões distintas, também sugerindo multimodalidade;
- $X_3$: distribuição ainda mais claramente multimodal, com grupos próximos de $0$, outro em torno de $3$ a $6$ e outro próximo de $9$ a $10,6$.

Logo, os histogramas de $X_2$ e $X_3$ tenderiam a mostrar **mistura de subpopulações**, e não uma única distribuição simples.

#### Item d

Para $X_3$:

| Condição | Média | Desvio-padrão |
| ---: | ---: | ---: |
| 1 | $5,54$ | $0,503$ |
| 4 | $9,92$ | $0,726$ |
| 8 | $4,14$ | $0,207$ |

Interpretação:

- a condição $4$ tem a maior média de absorção de água e também maior variabilidade;
- a condição $8$ tem média intermediária, mas é a mais estável;
- a condição $1$ tem média mais alta que a $8$, porém menor que a $4$, com variabilidade intermediária.

#### Explicação conceitual

- a média resume o nível típico da resposta em cada condição;
- o desvio-padrão mede o grau de oscilação entre as repetições;
- por isso, analisar os dois em conjunto permite comparar não apenas desempenho médio, mas também regularidade do processo.

#### Item e

Não. Os diagramas de pontos não fornecem exatamente as mesmas informações das medidas-resumo.

- média e desvio-padrão resumem posição e dispersão;
- diagramas de pontos mostram também forma da distribuição, agrupamentos, lacunas e possíveis valores isolados.

Portanto, os diagramas de pontos **complementam** as medidas numéricas.

#### Explicação conceitual

- medidas-resumo comprimem a informação em poucos números;
- gráficos preservam aspectos estruturais como agrupamentos, assimetria, lacunas e valores atípicos;
- em análise exploratória, o procedimento mais robusto é usar ambos de forma complementar.

#### Item f

Usando as $40$ observações transcritas de $X_1$:

- mediana: $9,4$
- quartil inferior $Q_1$: $8,7$
- quartil superior $Q_3$: $12,55$

Logo,

$$
DIQ = Q_3 - Q_1 = 12,55 - 8,7 = 3,85
$$

#### Item g

Resumo de cinco números para o boxplot de $X_1$:

- mínimo: $5,9$
- $Q_1 = 8,7$
- mediana: $9,4$
- $Q_3 = 12,55$
- máximo: $13,6$

Limites para discrepantes:

$$
LI = 8,7 - 1,5(3,85) = 2,925
$$

$$
LS = 12,55 + 1,5(3,85) = 18,325
$$

Como todos os valores estão entre $5,9$ e $13,6$, **não há outliers pelo critério $1,5\,DIQ$**.

#### Item h

Para comparar variabilidade entre $X_1$, $X_2$ e $X_3$, a medida mais apropriada é o **coeficiente de variação**, porque:

- as variáveis estão em escalas diferentes;
- o desvio-padrão isolado não é diretamente comparável entre grandezas distintas.

Com os dados transcritos:

- $CV(X_1) \approx 23,28\%$
- $CV(X_2) \approx 23,90\%$
- $CV(X_3) \approx 98,12\%$

Assim, $X_3$ é a variável relativamente mais variável.

#### Explicação conceitual

- quando as variáveis estão em escalas diferentes, comparar apenas desvios-padrão absolutos pode ser enganoso;
- o coeficiente de variação corrige isso ao relacionar a dispersão com o tamanho médio da variável;
- por isso, ele é a medida mais apropriada para comparar variabilidade relativa entre grandezas distintas.

### Exercício 9

#### Enunciado

Com respeito ao exercício anterior, o estudo da variabilidade natural do processo, em termos das 50 observações de $X_1$, $X_2$ e $X_3$, fica prejudicado, pois os ensaios foram feitos sob 8 condições experimentais diferentes. Considerando, porém, que, para cada variável, a média $X_j$ corresponde a uma estimativa da $j$-ésima condição experimental ($j = 1, 2, \ldots, 8$), então os desvios $d_{ij} = X_{ij} - X_j$ ($i = 1, 2, \ldots, 5$) fornecem informações da variabilidade natural do processo.

Apresente as distribuições de frequências de $d_1$, $d_2$ e $d_3$ através de histogramas ou ramo-e-folhas. O que você pode dizer da dispersão dessas distribuições comparadas às distribuições construídas no exercício anterior, itens $(b)$ e $(c)$?

#### Resposta

Usando os desvios dentro de condição,

$$
d_{ij} = X_{ij} - \bar{X}_j,
$$

obtém-se:

| Variável | Média dos desvios | Desvio-padrão |
| --- | ---: | ---: |
| $d_1$ | aproximadamente $0$ | $0,629$ |
| $d_2$ | aproximadamente $0$ | $4,893$ |
| $d_3$ | aproximadamente $0$ | $0,397$ |

Distribuições resumidas:

- $d_1$: muito concentrada em torno de zero, com maior parte entre $-0,5$ e $0,5$;
- $d_2$: também centrada em zero, mas com dispersão maior que $d_1$ e $d_3$;
- $d_3$: fortemente concentrada em torno de zero, com a maior parte entre $-0,2$ e $0,2$.

Comparação com o exercício anterior:

- as distribuições dos desvios são **muito menos dispersas** que as distribuições originais de $X_1$, $X_2$ e $X_3$;
- isso ocorre porque a variação entre condições experimentais foi removida;
- portanto, os desvios refletem melhor a **variabilidade natural intrínseca** do processo em cada condição.

#### Explicação conceitual

- os dados originais misturam duas fontes de variação: diferenças entre condições experimentais e flutuações naturais dentro de cada condição;
- ao centralizar cada observação pela média da sua condição, elimina-se a componente de nível entre grupos;
- assim, os desvios isolam melhor a variabilidade própria do processo, separando-a do efeito do planejamento experimental.

### Exercício 10

#### Enunciado

Os dados abaixo apresentam a distância (em km) entre a residência e o local de trabalho dos funcionários da empresa AAA.

$$
1,8\ 2,5\ 0,4\ 1,9\ 4,4\ 2,2\ 3,5\ 0,2\ 0,9\ 1,4\ 1,1\ 1,7\ 1,2\ 2,3\ 1,9\ 0,8\ 1,5\ 1,7\ 1,4\ 2,1\ 3,2\ 15,1\ 2,1\ 1,4\ 0,5\ 0,9\ 1,7\ 0,5\ 0,8\ 3,7\ 1,4\ 1,8\ 2,0\ 1,1\ 1,0\ 0,8
$$

- Apresente esses dados em ramo-e-folhas.
- Na empresa BBB, a distância (em km) até a residência de seus 300 funcionários apresenta as seguintes medidas descritivas:

$$
\text{Mediana} = 2,8,\quad Q_1 = 1,6,\quad Q_3 = 4,2,\quad \text{Extremo inferior} = 0,4,\quad \text{Extremo superior} = 8,8
$$

Quais as principais diferenças entre as empresas AAA e BBB, em termos da distância entre a residência e o local de trabalho dos funcionários?

#### Resposta

#### Item a

Ramo-e-folhas das distâncias da empresa AAA:

```text
0 | 2 4 5 5 8 8 8 9 9
1 | 0 1 1 2 4 4 4 4 5 7 7 7 8 8 9 9
2 | 0 1 1 2 3 5
3 | 2 5 7
4 | 4
15 | 1
```

#### Item b

Para a empresa AAA, a partir dos dados:

- mínimo: $0,2$
- $Q_1 = 0,925$
- mediana: $1,6$
- $Q_3 = 2,1$
- máximo: $15,1$
- $DIQ = 1,175$

Para a empresa BBB, o enunciado fornece:

- mínimo: $0,4$
- $Q_1 = 1,6$
- mediana: $2,8$
- $Q_3 = 4,2$
- máximo: $8,8$
- $DIQ = 2,6$

Comparação:

- a empresa $BBB$ tem funcionários, em geral, morando mais longe do trabalho, pois seus quartis e mediana são maiores;
- a empresa $BBB$ também tem maior dispersão na faixa central ($DIQ = 2,6$ contra $1,175$);
- a empresa $AAA$ apresenta forte assimetria à direita, causada principalmente pelo valor extremo $15,1$;
- a empresa $BBB$ também pode ter assimetria à direita, mas menos acentuada no resumo fornecido.

#### Explicação conceitual

- a mediana e os quartis são especialmente úteis quando há assimetria ou valores extremos;
- isso ocorre porque eles são medidas **resistentes**, menos sensíveis a observações muito afastadas;
- neste exercício, essa propriedade é importante para não deixar que um único valor extremo domine a comparação entre as empresas.

### Exercício 11

#### Enunciado

Apresentam-se, abaixo, algumas medidas descritivas da distribuição de salários, em $R\$$, de três empresas do mesmo ramo.

| Empresa | Média | Desvio padrão | Extremo inferior | Quartil inferior | Mediana | Quartil superior | Extremo superior |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| A | 300 | 100 | 100 | 200 | 302 | 400 | 510 |
| B | 400 | 180 | 100 | 250 | 398 | 550 | 720 |
| C | 420 | 350 | 100 | 230 | 300 | 650 | 10.000 |

O que se pode dizer sobre a distribuição dos salários nas três empresas? Quais as diferenças em termos da posição central, dispersão e assimetria?

#### Resposta

#### Posição central

- $A$: centro em torno de $300$
- $B$: centro em torno de $400$
- $C$: média $420$, mas mediana $300$

Logo:

- $B$ e $C$ têm médias maiores que $A$;
- pela mediana, $B$ tem centro mais alto;
- em $C$, a média é puxada para cima por salários muito altos.

#### Dispersão

- $A$: menor dispersão ($s = 100$, amplitude $510 - 100 = 410$)
- $B$: dispersão intermediária ($s = 180$, amplitude $620$)
- $C$: maior dispersão ($s = 350$, amplitude $9900$)

Pelos quartis:

- $DIQ_A = 400 - 200 = 200$
- $DIQ_B = 550 - 250 = 300$
- $DIQ_C = 650 - 230 = 420$

Então $C$ é a mais dispersa também no miolo da distribuição.

#### Assimetria

- $A$: aproximadamente simétrica, pois média $300$ e mediana $302$ são muito próximas;
- $B$: também aproximadamente simétrica, com leve assimetria à direita;
- $C$: fortemente assimétrica à direita, pois a média é bem maior que a mediana e o máximo é $10.000$.

Conclusão:

- $A$ tem distribuição mais concentrada e aproximadamente simétrica;
- $B$ tem centro mais alto e dispersão maior que $A$, ainda sem assimetria severa;
- $C$ apresenta forte desigualdade salarial, grande dispersão e cauda longa à direita.

#### Explicação conceitual

- esse exercício reúne três dimensões clássicas da análise exploratória: **posição central**, **dispersão** e **assimetria**;
- duas distribuições podem ter médias parecidas e, ainda assim, diferir muito no formato e na desigualdade interna;
- por isso, uma interpretação estatística adequada não deve se basear em uma única medida-resumo.

### Exercício 12

#### Enunciado

Cada diagrama em caixas da figura do livro foi construído com 95 leituras da pressão do homogeneizador. Discuta as diferenças.

#### Resposta

Pelo boxplot da figura:

- o leite tipo $C$ tem mediana mais alta, em torno de $3,0$;
- o $UHT$ tem mediana mais baixa, em torno de $2,4$;
- a variabilidade do $UHT$ é maior, pois seu boxplot é mais largo e os whiskers cobrem faixa mais extensa;
- o tipo $C$ é mais estável, mas apresenta dois valores baixos discrepantes;
- o $UHT$ não mostra outliers tão evidentes na figura, embora apresente maior dispersão total;
- em termos de processo, o leite tipo $C$ parece mais consistente, enquanto o $UHT$ é menos estável.

#### Explicação conceitual

- o boxplot resume simultaneamente mediana, quartis, dispersão central e possíveis outliers;
- por isso, ele é especialmente útil para comparar grupos de forma rápida e resistente a valores extremos;
- neste caso, a leitura visual reforça a diferença entre **nível mediano do processo** e **estabilidade do processo**.
