# Respostas dos exercícios de Pinheiro et al. (2009), capítulo 4

Fonte dos enunciados: `exs/und2/pinheiro_cap4.md`

Conferência com o gabarito extraído do livro: o livro fornece respostas resumidas para os exercícios `4.2_P` a `4.10_P`. Há uma inconsistência no `4.8_P`: o enunciado extraído do PDF pergunta "pelo menos 30 minutos", mas o gabarito apresenta a resposta de "no máximo 30 minutos". A solução abaixo registra os dois valores e marca a divergência.

## Respostas dos Exemplos

### Exemplo 4.1

Com $X$ = número de acertos:

| $k$ | 0 | 1 | 2 | 3 |
| ---: | ---: | ---: | ---: | ---: |
| $P(X=k)$ | 0,512 | 0,384 | 0,096 | 0,008 |

Logo:

$$
P(X\ge 2)=0{,}096+0{,}008=0{,}104.
$$

### Exemplo 4.2

As variáveis aleatórias são:

- número de mensagens acumuladas na caixa de entrada;
- tempo de deslocamento casa-trabalho.

O objetivo é reconhecer a grandeza aleatória e formular probabilidades como $P(X\le 100)$ e $P(X\le 30)$.

### Exemplo 4.3

Para o número de filhos:

$$
P(X\le 2)=0{,}3+0{,}4+0{,}2=0{,}9.
$$

### Exemplo 4.4

Para a soma de dois dados, a distribuição é triangular, com maior probabilidade em $X=7$:

$$
P(X=7)=\frac{6}{36}.
$$

### Exemplo 4.5

$$
E(X)=1{,}1\text{ filho por família}.
$$

### Exemplo 4.6

Para a soma dos dois dados:

$$
E(X)=7.
$$

### Exemplo 4.7

Com probabilidades $0{,}33$, $0{,}52$ e $0{,}15$ para os cenários, os retornos esperados são:

| Companhia | Retorno esperado |
| --- | ---: |
| A | 11,18% |
| B | 14,61% |
| C | 10,38% |
| D | 8,18% |
| E | 12,55% |

Pelo critério de maximização do retorno esperado, a escolha seria a companhia B.

### Exemplo 4.8

Para o número de filhos:

$$
Var(X)=0{,}89,\qquad DP(X)=0{,}943,\qquad CV(X)=0{,}857.
$$

### Exemplo 4.9

Para a soma dos pontos nos dois dados:

$$
Var(X)=5{,}833,\qquad DP(X)=2{,}415,\qquad CV(X)=0{,}345.
$$

### Exemplo 4.10

Para $Y=(X-1{,}1)^2$:

$$
E(Y)=0{,}89=Var(X).
$$

### Exemplo 4.11

Com $X\sim Binomial(4,1/12)$:

$$
P(X=0)=\left(\frac{11}{12}\right)^4=0{,}7061.
$$

$$
P(X=2)=\binom{4}{2}\left(\frac{1}{12}\right)^2\left(\frac{11}{12}\right)^2=0{,}0350.
$$

$$
E(X)=4\cdot\frac{1}{12}=0{,}3333.
$$

### Exemplo 4.12

O exemplo é gráfico: aumenta-se $n$ e varia-se $p$ para observar mudança de forma, concentração e assimetria da binomial.

### Exemplo 4.13

O exemplo é gráfico: compara distribuições de Poisson com médias $\lambda t=1$, $3$ e $10$.

### Exemplo 4.14

Com média de 2 consultas por dia:

$$
P(X=3\text{ em 1 dia})=0{,}1804.
$$

Para uma semana:

$$
P(X\le 10)=0{,}1757.
$$

Para 30 dias:

$$
P(X\ge 50)=0{,}9156.
$$

### Exemplo 4.15

Para $X\sim U(-0{,}5,0{,}5)$:

$$
P(|X|<0{,}2)=0{,}4.
$$

### Exemplo 4.16

O cálculo de probabilidades para o tempo de atendimento exige áreas sob a curva de densidade.

### Exemplo 4.17

Por simetria:

$$
E(X)=0.
$$

### Exemplo 4.18

Para o tempo de atendimento:

$$
E(T)=4\text{ minutos}.
$$

### Exemplo 4.19

Para o erro de arredondamento:

$$
Var(X)=\frac{1}{12},\qquad DP(X)=0{,}289.
$$

### Exemplo 4.20

Para o tempo de atendimento:

$$
Var(T)=8,\qquad DP(T)=2{,}83,\qquad CV(T)=0{,}707.
$$

### Exemplo 4.21

O deslocamento horizontal da densidade altera a média; o espalhamento da densidade em torno da média altera a variância.

### Exemplo 4.22

$$
X\sim U(0,360).
$$

### Exemplo 4.23

$$
X\sim U(-0{,}5,0{,}5).
$$

### Exemplo 4.24

Com média 1000 horas:

$$
\lambda=\frac{1}{1000}=0{,}001.
$$

Antes de 1000 horas:

$$
P(T\le 1000)=1-e^{-1}=0{,}632.
$$

Tempo até 90% queimarem:

$$
1-e^{-0{,}001t}=0{,}9
\Rightarrow t=2303\text{ horas}.
$$

### Exemplo 4.25

Se $X\sim N(70,10^2)$, aproximadamente 95% dos pesos ficam entre 50 kg e 90 kg.

### Exemplo 4.26

O exemplo compara visualmente curvas normais com mesma média, mesma variância ou ambas diferentes.

### Exemplo 4.27

Exemplo de uso da tabela:

$$
P(Z<0{,}83)=0{,}7967.
$$

O capítulo usa a padronização:

$$
Z=\frac{X-\mu}{\sigma}.
$$

### Exemplo 4.28

Se $X\sim N(20,2^2)$:

$$
P(X>17)=P(Z>-1{,}5)=0{,}933.
$$

### Exemplo 4.29

Dos quantis:

$$
P(X\le 70)=0{,}75,\qquad P(X\le 50)=0{,}25,
$$

obtém-se:

$$
\mu=60,\qquad \sigma=14{,}9.
$$

E:

$$
P(X>85\mid X>75)=0{,}297.
$$

## Exercício 4.1_P

### a)

Verdadeira. A variância é não negativa e o desvio-padrão é sua raiz quadrada não negativa:

$$
DP(X)=\sqrt{Var(X)}\ge 0.
$$

### b)

Falsa. Eventos mutuamente exclusivos não podem ocorrer simultaneamente:

$$
P(A\cap B)=0.
$$

Para serem independentes, seria necessário:

$$
P(A\cap B)=P(A)P(B).
$$

Se ambos têm probabilidades positivas, então $P(A)P(B)>0$, logo não são independentes.

### c)

Verdadeira, aproximadamente. Para uma variável Normal, cerca de 68% dos valores ficam no intervalo:

$$
\mu-\sigma < X < \mu+\sigma.
$$

## Exercício 4.2_P

As possibilidades são:

| Resultado | Probabilidade | Ganho líquido com prêmio de R$ 100 |
| --- | ---: | ---: |
| 6 na 1ª tentativa | $1/6$ | 90 |
| 6 na 2ª tentativa | $(5/6)(1/6)$ | 80 |
| 6 na 3ª tentativa | $(5/6)^2(1/6)$ | 70 |
| nenhum 6 em 3 tentativas | $(5/6)^3$ | -30 |

### a)

$$
E(G)=90\frac{1}{6}
+80\frac{5}{36}
+70\frac{25}{216}
-30\frac{125}{216}
=16{,}85.
$$

A expectativa é positiva: aproximadamente R$ 16,85.

### b)

Se o prêmio é $P$, os ganhos líquidos são $P-10$, $P-20$, $P-30$ e $-30$.

Impondo $E(G)=0$, obtém-se:

$$
P=60.
$$

O prêmio deveria ser R$ 60,00.

### c)

Com prêmio de R$ 60,00, os ganhos líquidos são 50, 40, 30 e -30. Como $E(G)=0$:

$$
Var(G)=50^2\frac{1}{6}
+40^2\frac{5}{36}
+30^2\frac{25}{216}
+(-30)^2\frac{125}{216}
=1263{,}89.
$$

$$
DP(G)=\sqrt{1263{,}89}=35{,}55.
$$

## Exercício 4.3_P

### a)

A árvore de probabilidades leva à distribuição:

| $x$ | 0 | 1 | 2 | 3 |
| ---: | ---: | ---: | ---: | ---: |
| $P(X=x)$ | 0,060 | 0,156 | 0,280 | 0,504 |

### b)

Média:

$$
E(X)=0(0{,}060)+1(0{,}156)+2(0{,}280)+3(0{,}504)=2{,}228.
$$

Variância:

$$
Var(X)=\sum_x (x-2{,}228)^2P(X=x)=0{,}8480.
$$

Desvio-padrão:

$$
DP(X)=\sqrt{0{,}8480}=0{,}921.
$$

## Exercício 4.4_P

### a)

Alternativa A:

$$
E(A)=15\%.
$$

Alternativa B:

$$
E(B)=16(0{,}6)+13(0{,}4)=14{,}8\%.
$$

O retorno esperado é maior na alternativa A.

### b)

Alternativa A:

$$
Var(A)=2^2=4.
$$

Alternativa B:

$$
Var(B)=0{,}6(16-14{,}8)^2+0{,}4(13-14{,}8)^2=2{,}16.
$$

A variância é maior na alternativa A.

### c)

Para $C$ assumir $j$ e $k$ com probabilidade $0{,}5$ cada, precisamos:

$$
\frac{j+k}{2}=15
$$

e:

$$
\frac{(j-15)^2+(k-15)^2}{2}=4.
$$

Uma solução simétrica é:

$$
j=13,\qquad k=17.
$$

## Exercício 4.5_P

Se $X$ é o número de acertos em 10 tiros:

$$
X\sim Binomial(10,0{,}7).
$$

Queremos:

$$
P(X\ge 8)=P(X=8)+P(X=9)+P(X=10).
$$

$$
P(X\ge 8)
=\sum_{k=8}^{10}\binom{10}{k}0{,}7^k0{,}3^{10-k}
=0{,}3828.
$$

Logo, a probabilidade de ganhar a aposta é aproximadamente 38,28%.

## Exercício 4.6_P

A variável binomial é $Y$.

Pelo primeiro valor:

$$
P(Y=0)=0{,}07776=(0{,}6)^5.
$$

Logo:

$$
1-p=0{,}6
\Rightarrow p=0{,}4.
$$

De fato, para $n=5$ e $p=0{,}4$:

$$
P(Y=k)=\binom{5}{k}0{,}4^k0{,}6^{5-k}.
$$

## Exercício 4.7_P

Seja $\mu$ o número médio diário de chegadas.

O enunciado informa:

$$
P(X\le 1\mid X\le 2)=0{,}60.
$$

Para $X\sim Poisson(\mu)$:

$$
\frac{P(X\le 1)}{P(X\le 2)}
=
\frac{e^{-\mu}(1+\mu)}
{e^{-\mu}(1+\mu+\mu^2/2)}
=0{,}60.
$$

Cancelando $e^{-\mu}$:

$$
\frac{1+\mu}{1+\mu+\mu^2/2}=0{,}60.
$$

Daí:

$$
\mu=2.
$$

### b)

Queremos:

$$
P(X\ge 3\mid X\ge 2)
=
\frac{P(X\ge 3)}{P(X\ge 2)}.
$$

Com $\mu=2$:

$$
P(X\ge 3)=1-P(X\le 2)
=1-e^{-2}\left(1+2+\frac{2^2}{2}\right).
$$

$$
P(X\ge 2)=1-P(X\le 1)
=1-e^{-2}(1+2).
$$

Logo:

$$
P(X\ge 3\mid X\ge 2)=0{,}5443.
$$

Ou seja, aproximadamente 54,43%.

## Exercício 4.8_P

Como a média da exponencial é 15:

$$
\lambda=\frac{1}{15}.
$$

### a)

Pelo enunciado extraído do PDF, a pergunta é "pelo menos 30 minutos":

$$
P(X\ge 30)=e^{-\lambda 30}
=e^{-2}
=0{,}1353.
$$

Portanto, a resposta ao enunciado como transcrito é 13,53%.

Observação de conferência: o gabarito do livro informa 86,47%, que corresponde a:

$$
P(X\le 30)=1-e^{-2}=0{,}8647.
$$

Isso indica provável erro de enunciado ou de gabarito. A resolução conceitualmente correta depende de qual desigualdade se pretende usar.

### b)

Queremos:

$$
P(X\le c)=0{,}98.
$$

Então:

$$
1-e^{-c/15}=0{,}98
\Rightarrow e^{-c/15}=0{,}02.
$$

$$
c=-15\ln(0{,}02)=58{,}68.
$$

Logo, $c\approx 58{,}68$ minutos.

## Exercício 4.9_P

Se $X$ é a altura em cm:

$$
X\sim N(\mu,20^2).
$$

Sabe-se que:

$$
P(X>200)=0{,}40.
$$

Logo:

$$
P(X\le 200)=0{,}60.
$$

Na Normal padrão, $\Phi(0{,}253)\approx 0{,}60$. Assim:

$$
\frac{200-\mu}{20}=0{,}253.
$$

$$
\mu=200-20(0{,}253)=194{,}9\text{ cm}.
$$

### b)

$$
P(X<180)
=P\left(Z<\frac{180-194{,}9}{20}\right)
=P(Z<-0{,}747)
=0{,}2276.
$$

Logo, aproximadamente 22,76% dos jogadores têm menos de 1,80 m.

## Exercício 4.10_P

Se $X$ é o conteúdo de $S$:

$$
X\sim N(87,2^2).
$$

### a)

O barril é comprado se:

$$
82\le X\le 92.
$$

Padronizando:

$$
P(82\le X\le 92)
=P\left(\frac{82-87}{2}\le Z\le \frac{92-87}{2}\right)
=P(-2{,}5\le Z\le 2{,}5).
$$

$$
P(-2{,}5\le Z\le 2{,}5)=0{,}9876.
$$

Logo, a probabilidade de compra é 98,76%.

### b)

A probabilidade de um barril ser comprado é:

$$
p=0{,}9876.
$$

Em 100 barris independentes, a probabilidade de todos serem comprados é:

$$
p^{100}=0{,}9876^{100}.
$$

Logo, a probabilidade de pelo menos um ser rejeitado é:

$$
1-p^{100}
=1-0{,}9876^{100}
=0{,}7134.
$$

Portanto, aproximadamente 71,34%.
