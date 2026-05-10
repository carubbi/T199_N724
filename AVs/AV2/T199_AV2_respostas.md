# Respostas - T199 AV2

Este arquivo apresenta a resolução manual da AV2, seguindo a lógica das revisões em `aulas/resolucoes_manuais`: identificar variáveis, organizar os dados, escolher a fórmula adequada, calcular e interpretar. Para a turma T199, o Problema 1 fica restrito a medidas de associação, sem regressão linear simples.

## Gabarito

| Questão | Alternativa correta |
| ---: | :---: |
| 1 | B |
| 2 | D |
| 3 | A |
| 4 | A |
| 5 | A |
| 6 | A |
| 7 | C |
| 8 | E |
| 9 | D |
| 10 | C |
| 11 | D |
| 12 | B |
| 13 | E |
| 14 | C |

## Problema 1 - Medidas de associação

### Variáveis

| Símbolo | Significado |
| --- | --- |
| $x$ | tempo do teste de BOD, em dias |
| $y$ | BOD observado, em mg/liter |
| $\bar{x}$ | média amostral do tempo |
| $\bar{y}$ | média amostral do BOD |
| $s_{xy}$ | covariância amostral entre tempo ($x$) e BOD ($y$) |
| $s_x$ | desvio-padrão amostral do tempo |
| $s_y$ | desvio-padrão amostral do BOD |
| $r$ | coeficiente de correlação de Pearson |

A análise é de associação entre duas variáveis quantitativas: tempo ($x$) e BOD ($y$). O gráfico de dispersão é a primeira verificação, pois ajuda a observar direção, intensidade visual, possíveis pontos discrepantes e limitações de um resumo numérico único. O coeficiente de Pearson ($r$) mede associação linear, mas não prova causalidade.

### Cálculos principais com todos os dados

Com os 11 pares observados:

| Quantidade | Valor |
| --- | ---: |
| $n$ | 11 |
| $\bar{x}$ | 10,0909 |
| $\bar{y}$ | 2,4545 |
| $\sum (x_i-\bar{x})^2$ | 420,9091 |
| $\sum (y_i-\bar{y})^2$ | 14,0873 |
| $\sum (x_i-\bar{x})(y_i-\bar{y})$ | 74,9455 |

A covariância amostral ($s_{xy}$) é:

$$
s_{xy}
=
\frac{\sum (x_i-\bar{x})(y_i-\bar{y})}{n-1}
=
\frac{74,9455}{10}
=
7,4945
$$

Como $s_{xy}>0$, tempo ($x$) e BOD ($y$) tendem a variar na mesma direção: valores maiores de tempo tendem a estar associados a valores maiores de BOD. A magnitude da covariância amostral ($s_{xy}$) depende das unidades de medida, por isso não deve ser comparada diretamente com covariâncias de variáveis em outras escalas.

Os desvios-padrão amostrais ($s_x$ e $s_y$) são:

$$
s_x
=
\sqrt{\frac{\sum (x_i-\bar{x})^2}{n-1}}
=
\sqrt{\frac{420,9091}{10}}
=
6,4878
$$

$$
s_y
=
\sqrt{\frac{\sum (y_i-\bar{y})^2}{n-1}}
=
\sqrt{\frac{14,0873}{10}}
=
1,1869
$$

O coeficiente de Pearson ($r$) é a covariância padronizada:

$$
r
=
\frac{s_{xy}}{s_xs_y}
=
\frac{7,4945}{6,4878\cdot 1,1869}
=
0,9733
$$

Interpretação: a associação linear entre tempo ($x$) e BOD ($y$) é forte e positiva. Isso significa que, no conjunto observado, maiores tempos tendem a estar associados a maiores valores de BOD. Essa leitura é associativa, não causal.

### Sensibilidade sem o ponto $x=14$, $y=3,7$

Retirando o ponto $x=14$, $y=3,7$:

| Quantidade | Valor |
| --- | ---: |
| $n$ | 10 |
| $\bar{x}$ | 9,7000 |
| $\bar{y}$ | 2,3300 |
| $\sum (x_i-\bar{x})^2$ | 404,1000 |
| $\sum (y_i-\bar{y})^2$ | 12,3810 |
| $\sum (x_i-\bar{x})(y_i-\bar{y})$ | 69,5900 |
| $s_{xy}$ | 7,7322 |
| $s_x$ | 6,7007 |
| $s_y$ | 1,1729 |
| $r$ | 0,9838 |

Assim, sem esse ponto:

$$
r\approx 0,984
$$

A associação permanece positiva e forte, com leve aumento da intensidade linear. Isso ilustra que o coeficiente de Pearson ($r$) pode ser sensível à presença ou retirada de pontos discrepantes.

### Respostas do Problema 1

**Questão 1: B.** Tempo ($x$) e BOD ($y$) são variáveis quantitativas, e o gráfico de dispersão permite avaliar visualmente direção, intensidade e possíveis pontos discrepantes da associação.

**Questão 2: D.** A covariância amostral ($s_{xy}$) é $s_{xy}=74,9455/(11-1)=7,4945$. O sinal positivo indica variação conjunta na mesma direção, mas a magnitude depende das unidades.

**Questão 3: A.** O coeficiente de Pearson ($r$) é $r\approx 0,973$, indicando associação linear forte e positiva entre tempo ($x$) e BOD ($y$).

**Questão 4: A.** A relação correta é $r=s_{xy}/(s_xs_y)$: o coeficiente de Pearson ($r$) padroniza a covariância amostral ($s_{xy}$) pelos desvios-padrão amostrais ($s_x$ e $s_y$), ficando sem unidade e limitado entre $-1$ e $1$.

**Questão 5: A.** Sem o ponto $x=14$, $y=3,7$, o coeficiente de Pearson ($r$) fica $r\approx 0,984$; a associação permanece positiva e forte.

## Problema 2 - Probabilidade condicional, total e Bayes

### Organização dos eventos

| Símbolo | Significado |
| --- | --- |
| $\mathrm{RMI}$ | visitante solicita mais informação |
| $\text{grupo}$ | categoria definida pelo número de páginas vistas |
| $P(\text{grupo})$ | probabilidade de um visitante pertencer ao grupo |
| $P(\mathrm{RMI}\mid \text{grupo})$ | probabilidade condicional de solicitar mais informação dentro do grupo |

A informação depois da barra vertical define o universo condicionado. Portanto, $P(\mathrm{RMI}\mid 4\text{ ou mais páginas})$ não é o mesmo que $P(4\text{ ou mais páginas}\mid \mathrm{RMI})$.

### Tabela conjunta

A probabilidade conjunta é:

$$
P(\text{grupo}\cap \mathrm{RMI})
=
P(\text{grupo})P(\mathrm{RMI}\mid \text{grupo})
$$

| Páginas vistas | $P(\text{grupo})$ | $P(\mathrm{RMI}\mid \text{grupo})$ | $P(\text{grupo}\cap \mathrm{RMI})$ | $P(\text{grupo}\cap \mathrm{RMI}^c)$ |
| --- | ---: | ---: | ---: | ---: |
| 1 | 0,40 | 0,10 | 0,040 | 0,360 |
| 2 | 0,30 | 0,10 | 0,030 | 0,270 |
| 3 | 0,20 | 0,20 | 0,040 | 0,160 |
| 4 ou mais | 0,10 | 0,40 | 0,040 | 0,060 |
| **Total** | **1,00** |  | **0,150** | **0,850** |

Assim:

$$
P(\mathrm{RMI})
=0,040+0,030+0,040+0,040
=0,150
$$

Logo, 15% dos visitantes solicitam mais informação.

### Bayes

A probabilidade pedida é:

$$
P(4\text{ ou mais páginas}\mid \mathrm{RMI})
=
\frac{P(4\text{ ou mais páginas}\cap \mathrm{RMI})}{P(\mathrm{RMI})}
$$

Substituindo:

$$
P(4\text{ ou mais páginas}\mid \mathrm{RMI})
=
\frac{0,040}{0,150}
=0,2667
\approx 0,267
$$

Interpretação: entre os visitantes que solicitaram mais informação, cerca de 26,7% visualizaram 4 ou mais páginas.

### Respostas do Problema 2

**Questão 6: A.** $\mathrm{RMI}$ é o evento “visitante solicita mais informação”; os grupos são definidos por páginas vistas; em $P(4\text{ ou mais páginas}\mid \mathrm{RMI})$, o universo é o conjunto dos visitantes que solicitaram mais informação.

**Questão 7: C.** As probabilidades conjuntas $P(\text{grupo}\cap \mathrm{RMI})$ são $0,04$, $0,03$, $0,04$ e $0,04$.

**Questão 8: E.** $P(\mathrm{RMI})=0,15$, obtida pela soma das probabilidades conjuntas de $\mathrm{RMI}$ em todos os grupos.

**Questão 9: D.**

$$
P(4\text{ ou mais páginas}\mid \mathrm{RMI})
=
\frac{0,04}{0,15}
\approx 0,267
$$

## Problema 3 - Variáveis aleatórias discretas

### Distribuição

| $x$ | 2 | 3 | 5 | 8 |
| ---: | ---: | ---: | ---: | ---: |
| $P(X=x)$ | 0,2 | 0,4 | 0,3 | 0,1 |

### Validade da função de probabilidade

Todas as probabilidades são não negativas e:

$$
0,2+0,4+0,3+0,1=1
$$

Logo, a função de probabilidade é válida. Os valores possíveis de $X$ não precisam ser consecutivos; o suporte pode ser $\{2,3,5,8\}$.

### Probabilidades de eventos

Para $P(X\le 3)$, entram $x=2$ e $x=3$:

$$
P(X\le 3)=0,2+0,4=0,6
$$

Para $P(X>2,5)$, entram $x=3$, $x=5$ e $x=8$:

$$
P(X>2,5)=0,4+0,3+0,1=0,8
$$

Para $P(2,7<X<5,1)$, entram $x=3$ e $x=5$:

$$
P(2,7<X<5,1)=0,4+0,3=0,7
$$

### Função acumulada

A função acumulada é $F(x)=P(X\le x)$.

| $x$ | $P(X=x)$ | $F(x)$ |
| ---: | ---: | ---: |
| 2 | 0,2 | 0,2 |
| 3 | 0,4 | 0,6 |
| 5 | 0,3 | 0,9 |
| 8 | 0,1 | 1,0 |

### Esperança

$$
E(X)=\sum_x xP(X=x)
$$

$$
E(X)
=2\cdot 0,2+3\cdot 0,4+5\cdot 0,3+8\cdot 0,1
$$

$$
E(X)=0,4+1,2+1,5+0,8=3,9
$$

Interpretação: $3,9$ é a média teórica de longo prazo. Não precisa ser um valor possível de $X$.

### Variância

Primeiro:

$$
E(X^2)=\sum_x x^2P(X=x)
$$

$$
E(X^2)
=2^2\cdot 0,2+3^2\cdot 0,4+5^2\cdot 0,3+8^2\cdot 0,1
$$

$$
E(X^2)
=4\cdot 0,2+9\cdot 0,4+25\cdot 0,3+64\cdot 0,1
$$

$$
E(X^2)=0,8+3,6+7,5+6,4=18,3
$$

A variância é:

$$
\operatorname{Var}(X)=E(X^2)-[E(X)]^2
$$

$$
\operatorname{Var}(X)=18,3-(3,9)^2
=18,3-15,21
=3,09
$$

O desvio-padrão, se necessário, é:

$$
DP(X)=\sqrt{3,09}=1,76
$$

Interpretação: a variância mede dispersão em torno da esperança e fica em unidade ao quadrado. O desvio-padrão volta à unidade original de $X$.

### Respostas do Problema 3

**Questão 10: C.** A distribuição é válida porque todas as probabilidades são não negativas e somam 1. Os valores de $X$ não precisam ser consecutivos.

**Questão 11: D.**

$$
P(X\le 3)=0,6,\quad
P(X>2,5)=0,8,\quad
P(2,7<X<5,1)=0,7
$$

**Questão 12: B.** A função acumulada nos pontos do suporte é:

$$
F(2)=0,2,\quad F(3)=0,6,\quad F(5)=0,9,\quad F(8)=1,0
$$

**Questão 13: E.** $E(X)=3,9$, interpretado como média teórica de longo prazo, não necessariamente como valor possível de $X$.

**Questão 14: C.**

$$
\operatorname{Var}(X)=3,09
$$

A variância mede dispersão em torno da esperança, em unidade ao quadrado.
