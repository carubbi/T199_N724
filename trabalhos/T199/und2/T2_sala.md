# Mini Trabalho em Sala: Probabilidade e Perfis de Jogadores da NBA

## Contexto

Esta atividade é uma versão reduzida de [T2.md](/Users/carubbi/Documents/aulas/T199/trabalhos/und2/T2.md), pensada para ser realizada em **60 minutos de aula**.

O objetivo é aplicar, de forma breve e guiada, os principais conceitos de probabilidade ao dataset completo `dataset/nba_stats_preprocessed.csv`.

## Objetivo

Ao final da atividade, o grupo deverá ser capaz de:

- construir eventos binários a partir de variáveis do dataset;
- calcular probabilidades condicionais e conjuntas;
- comparar cálculo direto e cálculo pela regra do produto;
- aplicar o Teorema de Bayes;
- aplicar o Teorema da Probabilidade Total;
- interpretar os resultados em linguagem descritiva, sem afirmar causalidade.

## Unidade de Análise

- Cada linha do dataset representa um caso `jogador-temporada`.

## Eventos Fixos da Atividade

Para reduzir a complexidade, todos os grupos deverão usar apenas estes eventos:

- $A$: jogador está no quartil superior de `salario_usd`;
- $B$: jogador está no quartil superior de `pontos`;
- $C$: jogador é armador, com `sigla_posicao` em `{PG, SG, G}`.

## Cortes Fixos

Use diretamente os seguintes cortes, já calculados previamente para esta versão da atividade:

- `salario_alto`: `salario_usd >= 8193029.75`
- `pontos_alto`: `pontos >= 885.75`

## O que o grupo deve entregar

Cada grupo deverá entregar um **notebook curto e executável**, com:

- 1 célula markdown de identificação;
- 1 célula de carregamento do dataset e criação dos eventos $A$, $B$ e $C$;
- 5 ou 6 células de cálculo;
- 5 ou 6 respostas interpretativas curtas em markdown.

## Tarefas

### Bloco 1. Preparação dos dados

1. Carregue o arquivo `dataset/nba_stats_preprocessed.csv`.
2. Crie três colunas booleanas correspondentes aos eventos $A$, $B$ e $C$.
3. Informe o número total de observações do dataset.

### Bloco 2. Probabilidade condicional

Calcule:

$$
P(B \mid A)
$$

Interprete o resultado em uma frase curta:

> Calcule a probabilidade de ter **alta pontuação** dado que o jogador pertence ao grupo de **salário alto**.

### Bloco 3. Regra do produto

Calcule a mesma quantidade de duas formas:

1. diretamente, por:

$$
P(A \cap B)
$$

2. pela regra do produto:

$$
P(A)\,P(B \mid A)
$$

Registre apenas se os valores coincidem ou são praticamente iguais.

### Bloco 4. Independência empírica

Compare:

$$
P(A \cap B)
$$

e

$$
P(A)P(B)
$$

Escreva uma frase curta dizendo se os dados sugerem independência plausível ou dependência entre **salário alto** e **pontuação alta**.

Use a formulação correta:

- trate isso como **verificação empírica aproximada**;
- não trate isso como prova formal de independência;
- se os valores forem próximos, isso pode ser compatível com independência empírica aproximada;
- se forem bem diferentes, isso sugere dependência empírica.

### Bloco 5. Teorema de Bayes

Calcule:

$$
P(A \mid C)
$$

de duas formas:

1. diretamente;
2. via Teorema de Bayes:

$$
P(A \mid C) = \frac{P(A)\,P(C \mid A)}{P(C)}
$$

Registre apenas se os dois resultados coincidem.

### Bloco 6. Teorema da Probabilidade Total

Use a partição:

- $A_1$: armador;
- $A_2$: não armador.

Calcule:

$$
P(B)
$$

de duas formas:

1. diretamente;
2. por probabilidade total:

$$
P(B) = P(B \mid A_1)P(A_1) + P(B \mid A_2)P(A_2)
$$

Registre apenas se os dois resultados coincidem ou são praticamente iguais.

### Fechamento

Responda em **3 a 5 linhas**:

> O que os resultados sugerem sobre a relação entre salário alto e pontuação alta no dataset da NBA?

Sua resposta deve:

- usar linguagem descritiva;
- mencionar pelo menos um dos resultados obtidos;
- evitar qualquer afirmação causal.

## Organização do Tempo

Distribuição sugerida para os 60 minutos:

- 10 min: carregamento do dataset e criação dos eventos;
- 10 min: probabilidade condicional e regra do produto;
- 10 min: independência empírica;
- 10 min: Teorema de Bayes;
- 10 min: probabilidade total;
- 10 min: interpretação final e revisão.

## Critérios de Avaliação

O grupo terá bom desempenho se:

- usar corretamente os eventos $A$, $B$ e $C$;
- comparar cálculo direto e indireto na regra do produto;
- comparar cálculo direto e Bayes para $P(A \mid C)$;
- usar corretamente a partição `armador` / `não armador`;
- escrever interpretações curtas com universo de referência claro;
- não afirmar causalidade;
- não tratar independência empírica como prova formal.

## Observação Final

Esta atividade foi desenhada para ser viável em sala de aula. Por isso, o escopo foi reduzido e todos os grupos devem seguir os mesmos eventos e os mesmos cortes.
