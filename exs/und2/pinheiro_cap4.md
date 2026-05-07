# Pinheiro et al. (2009) - Capítulo 4: Variáveis Aleatórias

Fonte: `livros/Pinheiro_2009.pdf`

Observação: os enunciados abaixo foram reorganizados e parafraseados para uso didático, preservando dados, hipóteses, unidades e itens necessários. Os exercícios resolvidos são mantidos como referência de padrão de raciocínio; as respostas detalhadas são dadas somente para os exercícios propostos.

## Fórmulas úteis

### Variável aleatória discreta

Para uma variável aleatória discreta $X$:

$$
p(x)=P(X=x)
$$

com:

$$
p(x)\ge 0,\qquad \sum_x p(x)=1.
$$

A função de distribuição acumulada é:

$$
F(x)=P(X\le x).
$$

### Esperança, variância e desvio-padrão

Para $X$ discreta:

$$
E(X)=\sum_x x\,p(x)
$$

$$
Var(X)=\sum_x (x-E(X))^2p(x)
$$

ou, equivalentemente:

$$
Var(X)=E(X^2)-[E(X)]^2.
$$

O desvio-padrão é:

$$
DP(X)=\sqrt{Var(X)}.
$$

O coeficiente de variação, quando $E(X)\ne 0$, é:

$$
CV(X)=\frac{DP(X)}{E(X)}.
$$

Para uma função $Y=h(X)$:

$$
E(Y)=E[h(X)]=\sum_x h(x)p(x).
$$

### Bernoulli

Se $X$ assume apenas os valores 0 e 1, com:

$$
P(X=1)=p,\qquad P(X=0)=1-p,
$$

então $X$ tem distribuição Bernoulli com parâmetro $p$:

$$
E(X)=p,\qquad Var(X)=p(1-p).
$$

### Binomial

Se $X$ conta o número de sucessos em $n$ ensaios de Bernoulli independentes, cada um com probabilidade de sucesso $p$, então:

$$
P(X=k)=\binom{n}{k}p^k(1-p)^{n-k},
\qquad k=0,1,\ldots,n.
$$

Além disso:

$$
E(X)=np,\qquad Var(X)=np(1-p).
$$

### Poisson

Se $X$ conta ocorrências em um intervalo e segue uma distribuição de Poisson com média $\lambda t$, então:

$$
P(X=k)=\frac{e^{-\lambda t}(\lambda t)^k}{k!},
\qquad k=0,1,2,\ldots
$$

e:

$$
E(X)=\lambda t,\qquad Var(X)=\lambda t.
$$

### Variável aleatória contínua

Para uma variável aleatória contínua com densidade $f$:

$$
P(a\le X\le b)=\int_a^b f(x)\,dx.
$$

Para variáveis contínuas:

$$
P(X=x)=0.
$$

### Uniforme contínua

Se $X\sim U(a,b)$:

$$
f(x)=\frac{1}{b-a},\qquad a\le x\le b.
$$

Além disso:

$$
E(X)=\frac{a+b}{2},\qquad Var(X)=\frac{(b-a)^2}{12}.
$$

### Exponencial

Se $X$ tem distribuição exponencial com parâmetro $\lambda>0$:

$$
f(x)=\lambda e^{-\lambda x},\qquad x\ge 0,
$$

$$
F(x)=P(X\le x)=1-e^{-\lambda x},\qquad x\ge 0.
$$

Além disso:

$$
E(X)=\frac{1}{\lambda},\qquad Var(X)=\frac{1}{\lambda^2}.
$$

### Normal

Se $X\sim N(\mu,\sigma^2)$, então:

$$
Z=\frac{X-\mu}{\sigma}\sim N(0,1).
$$

Para usar a tabela da Normal padrão:

$$
P(X\le x)=P\left(Z\le \frac{x-\mu}{\sigma}\right).
$$

## Exemplos

### 4.1 - Escolha aleatória em prova de múltipla escolha

Cesar precisa acertar pelo menos 2 de 3 questões de múltipla escolha. Cada questão tem cinco alternativas e ele escolhe ao acaso. Seja $X$ o número de acertos. O exemplo constrói a distribuição de $X$:

| $k$ | 0 | 1 | 2 | 3 |
| ---: | ---: | ---: | ---: | ---: |
| $P(X=k)$ | 0,512 | 0,384 | 0,096 | 0,008 |

O objetivo é introduzir variável aleatória discreta e função de probabilidade.

### 4.2 - Variáveis aleatórias do cotidiano

Discute duas situações: número de mensagens acumuladas no e-mail de Marta após uma semana sem acesso e tempo de deslocamento de Jorge de casa ao trabalho. O objetivo é identificar a variável aleatória e interpretar probabilidades como $P(X\le 100)$ ou $P(X\le 30)$.

### 4.3 - Número de filhos em uma família

Em um condomínio, a distribuição do número de filhos por família é:

| $x$ | 0 | 1 | 2 | 3 |
| ---: | ---: | ---: | ---: | ---: |
| $P(X=x)$ | 0,3 | 0,4 | 0,2 | 0,1 |
| $F(x)=P(X\le x)$ | 0,3 | 0,7 | 0,9 | 1,0 |

O exemplo calcula probabilidades usando a função de probabilidade e a função acumulada.

### 4.4 - Soma dos pontos em dois dados

No lançamento de dois dados, seja $X$ a soma dos pontos. A distribuição de $X$ é:

| $x$ | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| $P(X=x)$ | 1/36 | 2/36 | 3/36 | 4/36 | 5/36 | 6/36 | 5/36 | 4/36 | 3/36 | 2/36 | 1/36 |

### 4.5 - Esperança do número de filhos

Retoma o Exemplo 4.3 e calcula:

$$
E(X)=0\cdot0{,}3+1\cdot0{,}4+2\cdot0{,}2+3\cdot0{,}1=1{,}1.
$$

### 4.6 - Esperança da soma em dois dados

Retoma a soma dos pontos em dois dados e obtém:

$$
E(X)=7.
$$

### 4.7 - Escolha de investimento por retorno esperado

Compara cinco companhias sob três cenários:

| Cenário | A | B | C | D | E |
| --- | ---: | ---: | ---: | ---: | ---: |
| Otimista | 12% | 17% | 15% | 9% | 20% |
| Neutro | 11% | 15% | 9% | 8% | 10% |
| Pessimista | 10% | 8% | 5% | 7% | 5% |

Com probabilidades $0{,}33$, $0{,}52$ e $0{,}15$ para os cenários, calcula-se o retorno esperado de cada companhia para comparar estratégias de decisão.

### 4.8 - Variância do número de filhos

Para o número de filhos do Exemplo 4.3:

$$
Var(X)=0{,}89,\qquad DP(X)=0{,}943,\qquad CV(X)=0{,}857.
$$

### 4.9 - Variância da soma em dois dados

Para a soma dos pontos em dois dados:

$$
Var(X)=5{,}833,\qquad DP(X)=2{,}415,\qquad CV(X)=0{,}345.
$$

### 4.10 - Esperança de uma função do número de filhos

Define $Y=(X-1{,}1)^2$ para o número de filhos do Exemplo 4.3. O exemplo mostra que:

$$
E(Y)=0{,}89=Var(X).
$$

### 4.11 - Aquarianos

Escolhem-se quatro pessoas ao acaso e considera-se sucesso "ser de Aquário", admitindo os 12 signos equiprováveis. Então:

$$
X\sim Binomial\left(4,\frac{1}{12}\right).
$$

O exemplo calcula probabilidades como $P(X=0)$, $P(X=2)$, $P(X\ge 2)$ e $E(X)$.

### 4.12 - Formas da distribuição binomial

Compara graficamente distribuições binomiais para diferentes valores de $n$ e $p$, mostrando como a forma da distribuição muda com os parâmetros.

### 4.13 - Formas da distribuição de Poisson

Compara graficamente distribuições de Poisson para $\lambda t=1$, $\lambda t=3$ e $\lambda t=10$.

### 4.14 - Consultas ao site de uma empresa

O número de consultas à página de uma empresa segue Poisson com média de 2 consultas por dia. O exemplo calcula probabilidades para um dia, uma semana e um mês.

### 4.15 - Erros de arredondamento

O erro de arredondamento $X$ é modelado como contínuo uniforme em $[-0{,}5,0{,}5]$. O exemplo calcula:

$$
P(|X|<0{,}2)=0{,}4.
$$

### 4.16 - Tempo de atendimento em supermercado

O tempo $T$ de atendimento no caixa é descrito por uma densidade contínua. O exemplo mostra que probabilidades para variáveis contínuas são áreas sob a curva de densidade.

### 4.17 - Média do erro de arredondamento

Pela simetria da distribuição uniforme em $[-0{,}5,0{,}5]$:

$$
E(X)=0.
$$

### 4.18 - Média do tempo de atendimento

Para o tempo de atendimento do Exemplo 4.16:

$$
E(T)=4\text{ minutos}.
$$

### 4.19 - Variância do erro de arredondamento

Para $X\sim U(-0{,}5,0{,}5)$:

$$
Var(X)=\frac{1}{12},\qquad DP(X)=0{,}289.
$$

Como $E(X)=0$, o coeficiente de variação não existe.

### 4.20 - Variância do tempo de atendimento

Para o tempo de atendimento do supermercado:

$$
Var(T)=8,\qquad DP(T)=2{,}83,\qquad CV(T)=0{,}707.
$$

### 4.21 - Densidade, média e variância

Usa gráficos de densidades para comparar distribuições com mesma variância e médias diferentes e distribuições com mesma média e variâncias diferentes.

### 4.22 - Ponteiro de segundos

Se $X$ é o ângulo, em graus, formado pelo ponteiro dos segundos de um relógio com a vertical do número 12, então:

$$
X\sim U(0,360).
$$

### 4.23 - Erro de arredondamento como uniforme

Retoma o erro de arredondamento e reconhece:

$$
X\sim U(-0{,}5,0{,}5).
$$

### 4.24 - Tempo de vida de lâmpadas

O tempo de vida de uma lâmpada segue distribuição exponencial com média de 1000 horas. O exemplo calcula a proporção que queima antes de 1000 horas e o tempo até 90% das lâmpadas queimarem.

### 4.25 - Peso de pessoas adultas

Os pesos de uma população adulta seguem Normal com média 70 kg e desvio-padrão 10 kg. O exemplo usa a regra aproximada dos dois desvios-padrão para concluir que cerca de 95% estão entre 50 kg e 90 kg.

### 4.26 - Média e variância em curvas normais

Compara pares de curvas normais para interpretar visualmente diferenças de média e de variância.

### 4.27 - Uso da tabela da Normal padrão

Mostra como obter probabilidades e quantis na tabela da Normal padrão, incluindo casos de caudas, intervalos e transformação de uma Normal qualquer em $Z$.

### 4.28 - Retorno de uma ação

O retorno de uma ação segue Normal com média 20% e desvio-padrão 2%. O retorno de um título de renda fixa é 17%. O exemplo calcula a probabilidade de a ação superar o título.

### 4.29 - Tempo para executar uma tarefa

O tempo de execução de uma tarefa segue Normal. Sabendo que $P(X\le 70)=0{,}75$ e $P(X\le 50)=0{,}25$, o exemplo determina $\mu$ e $\sigma$ e calcula uma probabilidade condicional envolvendo tempos superiores a 75 e 85 minutos.

## Exercícios Resolvidos

### 4.1_R - Condição para concretização de uma venda

Um componente é vendido em lotes de 1000 itens pelo preço usual de 60 u.m. Um comprador propõe retirar uma amostra de 20 itens por lote. Se a amostra não tiver defeituosos, paga 70 u.m.; se tiver exatamente 1 defeituoso, paga 60 u.m.; se tiver 2 ou mais defeituosos, paga 50 u.m. Sabendo que cerca de 5% dos itens são defeituosos, avalie se o vendedor deve aceitar a proposta.

Objetivo didático: modelar o número de defeituosos por uma binomial e calcular o valor esperado do preço recebido.

### 4.2_R - Ler ou não ler os e-mails

A chegada de mensagens à caixa de e-mail segue Poisson com média de 30 mensagens por semana. A pessoa consulta a caixa uma vez por dia e só lê as mensagens se houver no máximo 3 mensagens. Em 5 dias, calcule:

a) a probabilidade de ela não ler os e-mails em cada um dos 5 dias;

b) a probabilidade de ela não ler os e-mails em pelo menos um dos 5 dias.

Objetivo didático: usar Poisson para contagens no tempo e independência entre dias.

### 4.3_R - Estoque de camisas

A circunferência do pescoço dos clientes segue Normal com média 15,25 polegadas e desvio-padrão 0,50 polegada. Os tamanhos de colarinho são 15,00 (PP), 15,50 (P), 16,00 (M), 16,50 (G) e 17,00 (GG). Admitindo folga mínima de 0,75 polegada entre colarinho e pescoço:

a) calcule os percentuais de camisas de cada tamanho;

b) verifique se os percentuais somam 100% e explique.

Objetivo didático: aplicar padronização Normal, intervalos e interpretação de caudas.

## Exercícios Propostos

### 4.1_P - Conceitos probabilísticos

Para cada afirmação, diga se ela está correta e justifique:

a) o desvio-padrão de uma variável aleatória é sempre não negativo;

b) dois eventos mutuamente exclusivos são necessariamente independentes;

c) se uma variável segue uma curva Normal, em aproximadamente 68% dos casos os valores observados estão a no máximo um desvio-padrão da média.

### 4.2_P - Aposta

Você é convidado a participar de um jogo. Deve lançar um dado até obter o primeiro 6, com no máximo 3 tentativas. Cada lançamento custa R$ 10,00. Se obtiver um 6 em até 3 tentativas, ganha um prêmio de R$ 100,00. O jogo termina quando sai o primeiro 6 ou quando as 3 tentativas acabam sem sucesso.

a) A expectativa de ganho líquido é positiva? Justifique.

b) Qual deveria ser o prêmio, no lugar de R$ 100,00, para que a expectativa de ganho líquido fosse nula?

c) Calcule o desvio-padrão do ganho líquido nas condições do item b.

### 4.3_P - Futebol: cobrando pênaltis

Um jogador cobra 3 pênaltis seguidos. Admita:

- a probabilidade de converter o primeiro é $0{,}70$;
- a probabilidade de converter o segundo é $0{,}80$ se converteu o primeiro e $0{,}60$ caso contrário;
- a probabilidade de converter o terceiro é $0{,}90$ se converteu os dois primeiros, $0{,}70$ se converteu exatamente um dos dois primeiros e $0{,}50$ se não converteu nenhum dos dois primeiros.

Seja $X$ o número total de gols feitos.

a) obtenha a função de probabilidade de $X$;

b) determine a média e o desvio-padrão de $X$.

### 4.4_P - Alternativas de aplicação financeira

Um investidor considera duas alternativas:

- alternativa A: investir em uma ação cuja taxa de retorno é Normal com média 15% e desvio-padrão 2%;
- alternativa B: apostar em um jogo no qual a taxa de retorno é 16% com probabilidade $0{,}6$ e 13% com probabilidade $0{,}4$.

Responda:

a) em qual alternativa o retorno esperado é maior?

b) em qual alternativa a variância do retorno é maior?

c) imagine uma alternativa C com retorno $j\%$ com probabilidade $0{,}5$ e $k\%$ com probabilidade $0{,}5$. Obtenha $j$ e $k$ para que o valor esperado e a variância da alternativa C sejam iguais aos da alternativa A.

### 4.5_P - Tiro ao alvo

Um atirador aposta que fará 10 disparos e ganhará se acertar na mosca pelo menos 8 vezes. Com base no desempenho usual, ele acerta na mosca em 70% das vezes.

Qual é a probabilidade de ele ganhar a aposta?

### 4.6_P - Como reconhecer a lei binomial

Considere as variáveis aleatórias discretas $X$, $Y$ e $Z$ com funções de probabilidade:

| Variável | $p(0)$ | $p(1)$ | $p(2)$ | $p(3)$ | $p(4)$ | $p(5)$ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| $X$ | 0,16666 | 0,16667 | 0,16667 | 0,16667 | 0,16667 | 0,16666 |
| $Y$ | 0,07776 | 0,25920 | 0,34560 | 0,23040 | 0,07680 | 0,01024 |
| $Z$ | 0,04762 | 0,09524 | 0,14286 | 0,19048 | 0,23809 | 0,28571 |

Qual dessas variáveis segue distribuição binomial? Qual é a probabilidade de sucesso $p$?

### 4.7_P - Chegadas de navios a um porto

O número de chegadas de navios a um porto durante um dia segue distribuição de Poisson. Sabe-se que, considerando apenas os dias em que chegam no máximo 2 navios, em 60% desses dias chega no máximo 1 navio.

a) qual é o número médio diário de chegadas de navios?

b) considerando apenas os dias em que chegam pelo menos 2 navios, em que percentual desses dias chegam pelo menos 3 navios?

### 4.8_P - Tempo de atendimento em loja

O tempo gasto no atendimento dos clientes de uma loja de roupas segue distribuição exponencial com média de 15 minutos.

a) qual é a probabilidade de que o tempo de atendimento de um cliente selecionado ao acaso seja de pelo menos 30 minutos?

b) qual é o valor de $c$ para que um cliente seja atendido em no máximo $c$ minutos com 98% de probabilidade?

### 4.9_P - Altura de jogadores de basquetebol

Admita que a distribuição da altura entre jogadores de basquetebol é Normal com desvio-padrão 20 cm. Sabe-se que 40% dos jogadores têm mais de 2 m de altura.

a) determine a média dessa distribuição;

b) que percentual dos jogadores tem menos de 1,80 m de altura?

### 4.10_P - Teste amostral para venda de fluido

Em condições normais, o conteúdo, em mg/ml, de uma substância $S$ no fluido $F$ segue Normal com média 87 e desvio-padrão 2. A companhia A compra barris desse fluido, mas antes extrai uma pequena amostra e mede o conteúdo de $S$. Se o valor estiver entre 82 e 92, a compra é efetuada; caso contrário, o barril é rejeitado.

a) qual é a probabilidade de que um barril de $F$, com conteúdo de $S$ em condições normais, seja comprado?

b) em uma remessa de 100 barris, todos em condições normais, qual é a probabilidade de pelo menos um barril ser rejeitado?
