# Respostas dos exercícios de Barbetta (2010), capítulo 5

Fonte dos enunciados: `exs/und2/barbetta_cap5.md`

Conferência com o gabarito extraído do livro: `exs/und2/respostas/barbetta_livro.md`.

Observação de conferência: as respostas coincidem com o gabarito do livro. As únicas diferenças são de arredondamento/tabela:

- Exercício 7(c): este arquivo usa $0{,}0755$; o livro registra $0{,}0754$.
- Exercício 11(a): este arquivo usa $0{,}0842$; o livro registra $0{,}0843$.
- Exercício 15(c): este arquivo usa $0{,}1887$; o livro registra $0{,}1886$.

## Fórmulas usadas

### Bernoulli

Se $X \sim \operatorname{Bernoulli}(p)$:

$$
P(X=x)=p^x(1-p)^{1-x}, \quad x=0,1
$$

$$
E(X)=p
$$

$$
V(X)=p(1-p)
$$

### Binomial

Se $X \sim \operatorname{Binomial}(n,p)$:

$$
P(X=x)=\binom{n}{x}p^x(1-p)^{n-x}, \quad x=0,1,\ldots,n
$$

$$
E(X)=np
$$

$$
V(X)=np(1-p)
$$

### Hipergeométrica

Se $X \sim \operatorname{Hipergeométrica}(N,r,n)$, em que $N$ é o tamanho do lote, $r$ é o número de itens com a característica de interesse e $n$ é o tamanho da amostra:

$$
P(X=x)=\frac{\binom{r}{x}\binom{N-r}{n-x}}{\binom{N}{n}}
$$

$$
E(X)=np, \quad p=\frac{r}{N}
$$

$$
V(X)=np(1-p)\frac{N-n}{N-1}
$$

### Poisson

Se $X \sim \operatorname{Poisson}(\lambda)$:

$$
P(X=x)=\frac{e^{-\lambda}\lambda^x}{x!}, \quad x=0,1,2,\ldots
$$

$$
E(X)=V(X)=\lambda
$$

### Função acumulada e complementos

$$
F(x)=P(X\le x)
$$

$$
P(X\ge 1)=1-P(X=0)
$$

$$
P(X>a)=1-P(X\le a)
$$

### Valor esperado e variância

Para uma variável aleatória discreta:

$$
E(X)=\sum_i x_i p(x_i)
$$

$$
E(X^2)=\sum_i x_i^2 p(x_i)
$$

$$
V(X)=E(X^2)-[E(X)]^2
$$

Se $Y=aX+b$:

$$
E(Y)=aE(X)+b
$$

$$
V(Y)=a^2V(X)
$$

Se $X$ e $Y$ são independentes:

$$
E(X+Y)=E(X)+E(Y)
$$

$$
V(X+Y)=V(X)+V(Y)
$$

$$
V(X-Y)=V(X)+V(Y)
$$

### Probabilidade condicional

$$
P(A\mid B)=\frac{P(A\cap B)}{P(B)}
$$

## Exercício 1

### a)

Se $X =$ número de caras no lançamento de uma moeda honesta, então $X \sim \operatorname{Bernoulli}(0{,}5)$.

Fórmula:

$$
P(X=x)=p^x(1-p)^{1-x}, \quad x=0,1
$$

| $x$ | $p(x)$ |
| ---: | ---: |
| 0 | 0,5 |
| 1 | 0,5 |

### b)

Se $X =$ número de caras no lançamento de duas moedas honestas, então $X \sim \operatorname{Binomial}(2, 0{,}5)$.

Fórmula:

$$
P(X=x)=\binom{n}{x}p^x(1-p)^{n-x}
$$

| $x$ | $p(x)$ |
| ---: | ---: |
| 0 | 0,25 |
| 1 | 0,50 |
| 2 | 0,25 |

### c)

Se $X =$ número de peças com defeito em duas peças sorteadas de um grande lote com 40% de defeituosas, então $X \sim \operatorname{Binomial}(2, 0{,}4)$.

Fórmula:

$$
P(X=x)=\binom{n}{x}p^x(1-p)^{n-x}
$$

| $x$ | $p(x)$ |
| ---: | ---: |
| 0 | 0,36 |
| 1 | 0,48 |
| 2 | 0,16 |

### d)

Se $X =$ número de peças com defeito em três peças sorteadas de um grande lote com 40% de defeituosas, então $X \sim \operatorname{Binomial}(3, 0{,}4)$.

Fórmula:

$$
P(X=x)=\binom{n}{x}p^x(1-p)^{n-x}
$$

| $x$ | $p(x)$ |
| ---: | ---: |
| 0 | 0,216 |
| 1 | 0,432 |
| 2 | 0,288 |
| 3 | 0,064 |

## Exercício 2

Para o Exercício 1(d), a distribuição de probabilidades é:

Fórmula:

$$
P(X=x)=\binom{3}{x}(0{,}4)^x(0{,}6)^{3-x}
$$

| $x$ | $p(x)$ |
| ---: | ---: |
| 0 | 0,216 |
| 1 | 0,432 |
| 2 | 0,288 |
| 3 | 0,064 |

Uma representação em hastes fica:

```text
x   p(x)
0   0,216  ######################
1   0,432  ###########################################
2   0,288  #############################
3   0,064  ######
```

O maior valor de probabilidade ocorre em $x = 1$.

## Exercício 3

Para o Exercício 1(d):

Fórmula:

$$
F(x)=P(X\le x)=\sum_{t\le x}p(t)
$$

| $x$ | $p(x)$ | $F(x) = P(X \le x)$ |
| ---: | ---: | ---: |
| 0 | 0,216 | 0,216 |
| 1 | 0,432 | 0,648 |
| 2 | 0,288 | 0,936 |
| 3 | 0,064 | 1,000 |

Assim:

$$
F(x) =
\begin{cases}
0, & x < 0 \\
0{,}216, & 0 \le x < 1 \\
0{,}648, & 1 \le x < 2 \\
0{,}936, & 2 \le x < 3 \\
1, & x \ge 3
\end{cases}
$$

## Exercício 4

Usando $E(X)=np$ e $V(X)=np(1-p)$ para as binomiais:

Fórmulas:

$$
E(X)=np
$$

$$
V(X)=np(1-p)
$$

| Caso | Distribuição | $E(X)$ | $V(X)$ |
| --- | --- | ---: | ---: |
| 1(a) | $\operatorname{Binomial}(1, 0{,}5)$ | 0,5 | 0,25 |
| 1(b) | $\operatorname{Binomial}(2, 0{,}5)$ | 1,0 | 0,50 |
| 1(c) | $\operatorname{Binomial}(2, 0{,}4)$ | 0,8 | 0,48 |
| 1(d) | $\operatorname{Binomial}(3, 0{,}4)$ | 1,2 | 0,72 |

## Exercício 5

A distribuição do lucro é:

| Produto | $x$ | $p(x)$ |
| --- | ---: | ---: |
| B | 6 | 0,7 |
| DL | 0 | 0,2 |
| DG | -2 | 0,1 |

### a)

Fórmulas:

$$
E(X)=\sum_i x_i p(x_i)
$$

$$
E(X^2)=\sum_i x_i^2 p(x_i)
$$

$$
V(X)=E(X^2)-[E(X)]^2
$$

$$
E(X) = 6(0{,}7)+0(0{,}2)+(-2)(0{,}1)=4
$$

$$
E(X^2)=6^2(0{,}7)+0^2(0{,}2)+(-2)^2(0{,}1)=25{,}6
$$

$$
V(X)=E(X^2)-[E(X)]^2=25{,}6-16=9{,}6
$$

Resposta: valor esperado $R\$\,4{,}00$ e variância $9{,}6$.

### b)

Se o lucro aumenta uma unidade, a nova variável é $Y=X+1$.

Fórmulas:

$$
E(X+b)=E(X)+b
$$

$$
V(X+b)=V(X)
$$

$$
E(Y)=E(X)+1=5
$$

$$
V(Y)=V(X)=9{,}6
$$

### c)

Se o lucro duplica, a nova variável é $Z=2X$.

Fórmulas:

$$
E(aX)=aE(X)
$$

$$
V(aX)=a^2V(X)
$$

$$
E(Z)=2E(X)=8
$$

$$
V(Z)=2^2V(X)=4(9{,}6)=38{,}4
$$

## Exercício 6

Seja:

$$
B = L + E
$$

em que $B$ é o peso bruto, $L$ é o peso líquido e $E$ é o peso da embalagem.

Como os pesos são independentes:

Fórmulas:

$$
E(L+E)=E(L)+E(E)
$$

$$
V(L+E)=V(L)+V(E)
$$

$$
E(B)=E(L)+E(E)=900+100=1000\text{ g}
$$

$$
V(B)=V(L)+V(E)=10^2+4^2=116
$$

Logo:

$$
DP(B)=\sqrt{116}\approx 10{,}77\text{ g}
$$

Resposta: média $1000\text{ g}$ e desvio-padrão aproximadamente $10{,}77\text{ g}$.

## Exercício 7

Seja $X =$ número de itens defeituosos no lote. Então:

$$
X \sim \operatorname{Binomial}(20, 0{,}05)
$$

### a)

Fórmula:

$$
P(X\ge 1)=1-P(X=0)
$$

$$
P(X \ge 1)=1-P(X=0)=1-(0{,}95)^{20}\approx 0{,}6415
$$

### b)

Fórmula:

$$
P(X=x)=\binom{n}{x}p^x(1-p)^{n-x}
$$

$$
P(X=2)=\binom{20}{2}(0{,}05)^2(0{,}95)^{18}\approx 0{,}1887
$$

### c)

Fórmula:

$$
P(X>2)=1-P(X\le 2)
$$

$$
P(X>2)=1-P(X\le 2)\approx 0{,}0755
$$

### d)

Fórmula:

$$
E(X)=np
$$

$$
E(X)=np=20(0{,}05)=1
$$

### e)

Se $Y =$ número de itens bons:

Fórmula:

$$
E(Y)=n(1-p)
$$

$$
E(Y)=20(0{,}95)=19
$$

## Exercício 8

No Exemplo 5.2, $X \sim \operatorname{Binomial}(10,0{,}7)$.

| $x$ | $p(x)$ |
| ---: | ---: |
| 0 | 0,0000 |
| 1 | 0,0001 |
| 2 | 0,0014 |
| 3 | 0,0090 |
| 4 | 0,0368 |
| 5 | 0,1029 |
| 6 | 0,2001 |
| 7 | 0,2668 |
| 8 | 0,2335 |
| 9 | 0,1211 |
| 10 | 0,0282 |

O valor esperado é:

Fórmula:

$$
E(X)=np
$$

$$
E(X)=np=10(0{,}7)=7
$$

E a área correspondente a $P(X>5)$ é a soma das barras de $x=6,7,8,9,10$:

Fórmula:

$$
P(X>5)=\sum_{x=6}^{10}p(x)
$$

$$
P(X>5)=0{,}2001+0{,}2668+0{,}2335+0{,}1211+0{,}0282\approx 0{,}8497
$$

Representação textual:

```text
x    p(x)
0    0,0000
1    0,0001
2    0,0014
3    0,0090  #
4    0,0368  ####
5    0,1029  ##########
6    0,2001  ####################  <- área de P(X > 5)
7    0,2668  ###########################  <- área de P(X > 5), E(X)=7
8    0,2335  #######################  <- área de P(X > 5)
9    0,1211  ############  <- área de P(X > 5)
10   0,0282  ###  <- área de P(X > 5)
```

## Exercício 9

No Exemplo 5.3:

$$
X \sim \operatorname{Hipergeométrica}(N=30,\ r=3,\ n=5)
$$

Agora a inspeção completa ocorre quando forem encontradas mais de uma placa defeituosa:

Fórmula da hipergeométrica:

$$
P(X=x)=\frac{\binom{r}{x}\binom{N-r}{n-x}}{\binom{N}{n}}
$$

Fórmula do complemento:

$$
P(X>1)=1-P(X=0)-P(X=1)
$$

$$
P(X=0)=\frac{\binom{3}{0}\binom{27}{5}}{\binom{30}{5}}\approx 0{,}5665
$$

$$
P(X=1)=\frac{\binom{3}{1}\binom{27}{4}}{\binom{30}{5}}\approx 0{,}3695
$$

Logo:

$$
P(X>1)\approx 1-0{,}5665-0{,}3695=0{,}0640
$$

## Exercício 10

Para $X \sim \operatorname{Hipergeométrica}(N=30,\ r=3,\ n=5)$:

Fórmula:

$$
p=\frac{r}{N}
$$

$$
p=\frac{r}{N}=\frac{3}{30}=0{,}1
$$

Valor esperado:

Fórmula:

$$
E(X)=np
$$

$$
E(X)=np=5(0{,}1)=0{,}5
$$

Variância:

$$
V(X)=np(1-p)\frac{N-n}{N-1}
$$

$$
V(X)=5(0{,}1)(0{,}9)\frac{25}{29}\approx 0{,}3879
$$

## Exercício 11

As mensagens chegam segundo uma distribuição de Poisson.

### a)

Para um minuto, $\lambda=5$:

Fórmula:

$$
P(X=x)=\frac{e^{-\lambda}\lambda^x}{x!}
$$

$$
P(X=2)=\frac{e^{-5}5^2}{2!}\approx 0{,}0842
$$

### b)

Em 30 segundos, a taxa média é:

$$
\lambda = 5\cdot 0{,}5=2{,}5
$$

Assim:

Fórmula:

$$
P(X=x)=\frac{e^{-\lambda}\lambda^x}{x!}
$$

$$
P(X=1)=\frac{e^{-2{,}5}2{,}5^1}{1!}\approx 0{,}2052
$$

## Exercício 12

Seja $X =$ número de bits recebidos com erro. Como $n=10.000$ e $p=0{,}0002$, temos:

$$
X \sim \operatorname{Binomial}(10000,0{,}0002)
$$

Como $n$ é grande e $p$ é pequeno, podemos usar a aproximação de Poisson:

Fórmula:

$$
\lambda=np
$$

$$
\lambda=np=10000(0{,}0002)=2
$$

Logo:

Fórmula:

$$
P(X>4)=1-\sum_{x=0}^{4}\frac{e^{-\lambda}\lambda^x}{x!}
$$

$$
P(X>4)=1-P(X\le 4)
$$

$$
P(X>4)=1-\sum_{x=0}^{4}\frac{e^{-2}2^x}{x!}\approx 0{,}0527
$$

Pela binomial exata, o valor é aproximadamente $0{,}0526$.

## Exercício 13

Assumindo mês com 30 dias, seja $X$ o excedente diário:

$$
X = A - D
$$

em que $A$ é o abastecimento diário e $D$ é a demanda diária.

Valor esperado diário:

Fórmula:

$$
E(A-D)=E(A)-E(D)
$$

$$
E(X)=E(A)-E(D)=30-25=5
$$

Como abastecimento e demanda são independentes:

Fórmula:

$$
V(A-D)=V(A)+V(D)
$$

$$
V(X)=V(A)+V(D)=3^2+4^2=25
$$

Logo, o desvio-padrão diário é:

$$
DP(X)=5
$$

Para 30 dias:

Fórmulas:

$$
E(S)=mE(X)
$$

$$
DP(S)=\sqrt{m}\,DP(X)
$$

$$
E(S)=30(5)=150
$$

$$
DP(S)=\sqrt{30}\cdot 5\approx 27{,}39
$$

Resposta: excedente esperado de $150$ unidades e desvio-padrão de aproximadamente $27{,}39$ unidades no mês.

## Exercício 14

Seja $X =$ número de clientes que deixam de pagar regularmente. Então:

$$
X \sim \operatorname{Binomial}(10,0{,}1)
$$

Mais de 20% de 10 pessoas significa mais de 2 pessoas, isto é, $X>2$.

Fórmula:

$$
P(X>2)=1-\sum_{x=0}^{2}\binom{n}{x}p^x(1-p)^{n-x}
$$

$$
P(X>2)=1-P(X\le 2)
$$

$$
P(X>2)=1-\sum_{x=0}^{2}\binom{10}{x}(0{,}1)^x(0{,}9)^{10-x}
\approx 0{,}0702
$$

## Exercício 15

### a)

O modelo adequado é a distribuição binomial:

$$
X \sim \operatorname{Binomial}(20,0{,}05)
$$

Justificativa: há 20 transmissões, cada uma pode resultar em erro ou não erro, a probabilidade de erro é constante e assume-se independência entre lotes.

### b)

Interpretando como a probabilidade de haver pelo menos um erro nas 20 transmissões:

Fórmula:

$$
P(X\ge 1)=1-P(X=0)
$$

$$
P(X\ge 1)=1-P(X=0)=1-(0{,}95)^{20}\approx 0{,}6415
$$

### c)

Fórmula:

$$
P(X=x)=\binom{n}{x}p^x(1-p)^{n-x}
$$

$$
P(X=2)=\binom{20}{2}(0{,}05)^2(0{,}95)^{18}\approx 0{,}1887
$$

### d)

Fórmula:

$$
E(X)=np
$$

$$
E(X)=np=20(0{,}05)=1
$$

Resposta: espera-se, em média, 1 erro no teste.

## Exercício 16

Seja $X$ o número de peças defeituosas na amostra. Como a taxa de defeituosas é 3%, usamos distribuição binomial.

### Proposta 1

$$
X_1 \sim \operatorname{Binomial}(80,0{,}03)
$$

O comprador A paga 60 u.m. por peça se $X_1\le 3$; caso contrário, paga 30 u.m. por peça.

Fórmula:

$$
P(X_1\le 3)=\sum_{x=0}^{3}\binom{80}{x}(0{,}03)^x(0{,}97)^{80-x}
$$

$$
P(X_1\le 3)\approx 0{,}7807
$$

Valor esperado por peça:

Fórmula:

$$
E(V)=v_1P(A)+v_2P(A^c)
$$

$$
60(0{,}7807)+30(1-0{,}7807)\approx 53{,}42
$$

Valor esperado da venda:

Fórmula:

$$
E(T)=q\cdot E(V)
$$

$$
4000(53{,}42)\approx 213.680{,}00
$$

### Proposta 2

$$
X_2 \sim \operatorname{Binomial}(40,0{,}03)
$$

O comprador B paga 65 u.m. por peça se $X_2=0$; caso contrário, paga 20 u.m. por peça.

Fórmula:

$$
P(X_2=0)=\binom{40}{0}(0{,}03)^0(0{,}97)^{40}
$$

$$
P(X_2=0)=(0{,}97)^{40}\approx 0{,}2957
$$

Valor esperado por peça:

Fórmula:

$$
E(V)=v_1P(A)+v_2P(A^c)
$$

$$
65(0{,}2957)+20(1-0{,}2957)\approx 33{,}31
$$

Valor esperado da venda:

Fórmula:

$$
E(T)=q\cdot E(V)
$$

$$
4000(33{,}31)\approx 133.228{,}21
$$

Resposta: a melhor proposta é a proposta 1.

## Exercício 17

### a)

Seja $X =$ número de transformadores defeituosos na amostra:

$$
X \sim \operatorname{Binomial}(10,0{,}03)
$$

O lote é aceito se $X=0$.

Fórmula:

$$
P(X=0)=\binom{10}{0}(0{,}03)^0(0{,}97)^{10}
$$

$$
P(X=0)=(0{,}97)^{10}\approx 0{,}7374
$$

### b)

A probabilidade de rejeição de um lote é:

Fórmula:

$$
q=1-P(\text{aceitação})
$$

$$
q=1-0{,}7374=0{,}2626
$$

Se $Y =$ número de lotes rejeitados em 8 lotes, então:

$$
Y \sim \operatorname{Binomial}(8,0{,}2626)
$$

Queremos:

Fórmula:

$$
P(Y\le 1)=P(Y=0)+P(Y=1)
$$

$$
P(Y\le 1)=P(Y=0)+P(Y=1)\approx 0{,}3365
$$

## Exercício 18

Uma mensagem com 20 pacotes é enviada corretamente se o número de pacotes enviados erroneamente não passar de 10% do total. Como 10% de 20 é 2, a mensagem é enviada corretamente se $X\le 2$.

### a)

Usando a distribuição binomial:

$$
X \sim \operatorname{Binomial}(20,0{,}01)
$$

Fórmula:

$$
P(X\le 2)=\sum_{x=0}^{2}\binom{n}{x}p^x(1-p)^{n-x}
$$

$$
P(X\le 2)=\sum_{x=0}^{2}\binom{20}{x}(0{,}01)^x(0{,}99)^{20-x}
\approx 0{,}9990
$$

### b)

Usando a aproximação de Poisson:

Fórmula:

$$
\lambda=np
$$

$$
\lambda=np=20(0{,}01)=0{,}2
$$

Fórmula:

$$
P(X\le 2)=\sum_{x=0}^{2}\frac{e^{-\lambda}\lambda^x}{x!}
$$

$$
P(X\le 2)=\sum_{x=0}^{2}\frac{e^{-0{,}2}0{,}2^x}{x!}
\approx 0{,}9989
$$

## Exercício 19

A central recebe 300 chamadas por hora. Como uma hora tem 60 minutos:

$$
\lambda = \frac{300}{60}=5
$$

Se $X =$ número de chamadas em um minuto:

$$
X \sim \operatorname{Poisson}(5)
$$

A capacidade é ultrapassada se $X>10$.

Fórmula:

$$
P(X>10)=1-\sum_{x=0}^{10}\frac{e^{-\lambda}\lambda^x}{x!}
$$

$$
P(X>10)=1-P(X\le 10)
$$

$$
P(X>10)=1-\sum_{x=0}^{10}\frac{e^{-5}5^x}{x!}\approx 0{,}0137
$$

## Exercício 20

A área é:

Fórmula:

$$
A=\text{comprimento}\times\text{largura}
$$

$$
10\text{ m}\times 10\text{ m}=100\text{ m}^2
$$

Como a taxa média é 0,01 defeito por $m^2$:

$$
\lambda=0{,}01(100)=1
$$

Logo:

Fórmula:

$$
P(X\ge 1)=1-P(X=0)=1-e^{-\lambda}
$$

$$
P(X\ge 1)=1-P(X=0)=1-e^{-1}\approx 0{,}6321
$$

## Exercício 21

### a)

Com reposição:

$$
X \sim \operatorname{Binomial}(5, 4/20)
$$

Queremos $P(X\ge 1)$:

Fórmula:

$$
P(X\ge 1)=1-P(X=0)
$$

$$
P(X\ge 1)=1-P(X=0)=1-(0{,}8)^5\approx 0{,}6723
$$

### b)

Sem reposição:

$$
X \sim \operatorname{Hipergeométrica}(N=20,\ r=4,\ n=5)
$$

Fórmula:

$$
P(X\ge 1)=1-\frac{\binom{r}{0}\binom{N-r}{n}}{\binom{N}{n}}
$$

$$
P(X\ge 1)=1-P(X=0)
=1-\frac{\binom{4}{0}\binom{16}{5}}{\binom{20}{5}}
\approx 0{,}7183
$$

## Exercício 22

A superfície de cada barco é:

Fórmula:

$$
A=\text{comprimento}\times\text{largura}
$$

$$
3\text{ m}\times 2\text{ m}=6\text{ m}^2
$$

Como a taxa média é 0,05 defeito por $m^2$:

$$
\lambda=0{,}05(6)=0{,}3
$$

### a)

Fórmula:

$$
P(X=0)=\frac{e^{-\lambda}\lambda^0}{0!}=e^{-\lambda}
$$

$$
P(X=0)=e^{-0{,}3}\approx 0{,}7408
$$

### b)

Fórmula:

$$
P(X>1)=1-P(X=0)-P(X=1)
$$

$$
P(X>1)=1-P(X=0)-P(X=1)
$$

$$
P(X>1)=1-e^{-0{,}3}-e^{-0{,}3}(0{,}3)\approx 0{,}0369
$$

### c)

Seja $Y =$ número de barcos sem defeito entre 5 barcos. A probabilidade de um barco não apresentar defeito é:

$$
p=P(X=0)\approx 0{,}7408
$$

Então:

$$
Y \sim \operatorname{Binomial}(5,0{,}7408)
$$

Queremos:

Fórmula:

$$
P(Y\ge 4)=P(Y=4)+P(Y=5)
$$

$$
P(Y\ge 4)=P(Y=4)+P(Y=5)\approx 0{,}6135
$$

## Exercício 23

Interpretação: os valores de R\$ 100,00, R\$ 200,00, R\$ 50,00 e R\$ 5,00 são valores por lote.

Na alternativa 1, o valor por lote é certo:

$$
E(V_1)=100
$$

Na alternativa 2, seja $X =$ número de defeituosos na amostra:

$$
X \sim \operatorname{Binomial}(15,0{,}05)
$$

As probabilidades são:

Fórmula:

$$
P(X=x)=\binom{15}{x}(0{,}05)^x(0{,}95)^{15-x}
$$

$$
P(X=0)=(0{,}95)^{15}\approx 0{,}4633
$$

$$
P(X=1)=\binom{15}{1}(0{,}05)(0{,}95)^{14}\approx 0{,}3658
$$

$$
P(X>1)\approx 0{,}1710
$$

O valor esperado da alternativa 2 é:

Fórmula:

$$
E(V)=\sum_i v_iP(V=v_i)
$$

$$
E(V_2)=200P(X=0)+50P(X=1)+5P(X>1)
$$

$$
E(V_2)\approx 200(0{,}4633)+50(0{,}3658)+5(0{,}1710)
\approx 111{,}80
$$

Resposta: em média, a alternativa 2 é mais vantajosa para o fabricante.

## Exercício 24

Seja $X =$ número de rolhas da categoria A na amostra:

$$
X \sim \operatorname{Binomial}(8,0{,}4)
$$

### a)

Fórmula:

$$
P(X>5)=\sum_{x=6}^{8}\binom{8}{x}(0{,}4)^x(0{,}6)^{8-x}
$$

$$
P(X>5)=P(X=6)+P(X=7)+P(X=8)
$$

$$
P(X>5)=\sum_{x=6}^{8}\binom{8}{x}(0{,}4)^x(0{,}6)^{8-x}
\approx 0{,}0498
$$

### b)

Se o fabricante aceitar a proposta, o valor de venda por milhar será:

- R\$ 200,00, com probabilidade $0{,}0498$;
- R\$ 50,00, com probabilidade $0{,}9502$.

Então:

Fórmula:

$$
E(V)=\sum_i v_iP(V=v_i)
$$

$$
E(V)=200(0{,}0498)+50(0{,}9502)\approx 57{,}47
$$

Na venda separada por categoria, o valor esperado por milhar é:

Fórmula:

$$
E(V)=v_A P(A)+v_B P(B)
$$

$$
100(0{,}4)+60(0{,}6)=76
$$

Resposta: pela média, a proposta do comprador não é vantajosa, pois $57{,}47 < 76$.

### c)

Como $V$ assume apenas os valores 200 e 50:

Fórmula:

$$
V(V)=\sum_i [v_i-E(V)]^2P(V=v_i)
$$

$$
V(V)= (200-57{,}47)^2(0{,}0498)+(50-57{,}47)^2(0{,}9502)
$$

$$
V(V)\approx 1064{,}85
$$

## Exercício 25

Seja $X =$ número de requisições no próximo minuto. Então:

$$
X \sim \operatorname{Poisson}(3)
$$

### a)

Fórmula:

$$
P(X>1)=1-P(X=0)-P(X=1)
$$

$$
P(X>1)=1-P(X=0)-P(X=1)
$$

$$
P(X>1)=1-e^{-3}-3e^{-3}\approx 0{,}8009
$$

### b)

Queremos:

$$
P(X>1 \mid X\ge 1)
$$

Então:

Fórmula:

$$
P(A\mid B)=\frac{P(A\cap B)}{P(B)}
$$

$$
P(X>1 \mid X\ge 1)=\frac{P(X>1)}{P(X\ge 1)}
$$

$$
P(X\ge 1)=1-P(X=0)=1-e^{-3}
$$

Logo:

$$
P(X>1 \mid X\ge 1)
=\frac{0{,}8009}{1-e^{-3}}
\approx 0{,}8428
$$
