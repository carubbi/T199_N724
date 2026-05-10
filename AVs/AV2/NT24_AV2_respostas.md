# Respostas - NT24 AV2

Este arquivo apresenta a resolução manual da AV2, seguindo a lógica das revisões em `aulas/resolucoes_manuais`: identificar variáveis, organizar os dados, escolher a fórmula adequada, calcular e interpretar.

## Gabarito

| Questão | Alternativa correta |
| ---: | :---: |
| 1 | C |
| 2 | D |
| 3 | B |
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

## Problema 1 - Associação e regressão

### Variáveis

| Símbolo | Significado |
| --- | --- |
| $x$ | tempo do teste de BOD, em dias |
| $y$ | BOD observado, em mg/liter |
| $\hat{y}$ | BOD previsto pela reta ajustada |
| $e$ | resíduo, dado por $e=y-\hat{y}$ |

A regressão é formulada para explicar ou prever $y$ a partir de $x$. A correlação de Pearson é simétrica, mas a reta ajustada, os resíduos e a interpretação da inclinação dependem da escolha de variável explicativa e variável resposta.

### Cálculos principais com todos os dados

Com os 11 pares observados:

| Quantidade | Valor |
| --- | ---: |
| $n$ | 11 |
| $\bar{x}$ | 10,0909 |
| $\bar{y}$ | 2,4545 |
| $S_{xx}=\sum (x_i-\bar{x})^2$ | 420,9091 |
| $S_{yy}=\sum (y_i-\bar{y})^2$ | 14,0873 |
| $S_{xy}=\sum (x_i-\bar{x})(y_i-\bar{y})$ | 74,9455 |

A inclinação é:

$$
b=\frac{S_{xy}}{S_{xx}}
=\frac{74,9455}{420,9091}
=0,1781
$$

O intercepto é:

$$
a=\bar{y}-b\bar{x}
=2,4545-0,1781\cdot 10,0909
=0,6578
$$

Logo:

$$
\hat{y}=0,6578+0,1781x
$$

A correlação é:

$$
r=
\frac{S_{xy}}{\sqrt{S_{xx}S_{yy}}}
=
\frac{74,9455}{\sqrt{420,9091\cdot 14,0873}}
=0,9733
$$

O coeficiente de determinação é:

$$
R^2=r^2=(0,9733)^2=0,9473
$$

Interpretação: aproximadamente 94,7% da variação observada no BOD é explicada linearmente pelo tempo no modelo ajustado. Isso não prova causalidade e não dispensa a análise dos resíduos.

### Previsão, mudança média e resíduo

Para $x=15$:

$$
\hat{y}=0,6578+0,1781\cdot 15=3,3286\approx 3,33
$$

Para aumento de 3 dias:

$$
3b=3\cdot 0,1781=0,5342\approx 0,53
$$

Em $x=6$:

$$
\hat{y}=0,6578+0,1781\cdot 6=1,7261
$$

Como o valor observado é $y=1,9$:

$$
e=y-\hat{y}=1,9-1,7261=0,1739\approx 0,17
$$

O resíduo é positivo; o valor observado ficou acima do previsto.

### Valores ajustados e comparação com valores observados

Usando $\hat{y}=0,6578+0,1781x$, os valores ajustados são:

| Observação | $x_i$ | $y_i$ | $\hat{y}_i$ | $e_i=y_i-\hat{y}_i$ |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 1 | 0,6 | 0,8359 | -0,2359 |
| 2 | 2 | 0,7 | 1,0139 | -0,3139 |
| 3 | 4 | 1,5 | 1,3700 | 0,1300 |
| 4 | 6 | 1,9 | 1,7261 | 0,1739 |
| 5 | 8 | 2,1 | 2,0822 | 0,0178 |
| 6 | 10 | 2,6 | 2,4384 | 0,1616 |
| 7 | 12 | 2,9 | 2,7945 | 0,1055 |
| 8 | 14 | 3,7 | 3,1506 | 0,5494 |
| 9 | 16 | 3,5 | 3,5067 | -0,0067 |
| 10 | 18 | 3,7 | 3,8628 | -0,1628 |
| 11 | 20 | 3,8 | 4,2189 | -0,4189 |

No gráfico de $\hat{y}_i$ versus $y_i$, uma relação determinística sem erro aleatório produziria pontos exatamente sobre a reta $\hat{y}=y$. No ajuste obtido, os pontos ficam próximos dessa referência, indicando que o tempo é um regressor efetivo para prever BOD no conjunto observado. Essa conclusão é preditiva e associativa; não prova causalidade e não dispensa a análise dos resíduos.

### Sensibilidade sem o ponto $x=14$, $y=3,7$

O ponto $x=14$, $y=3,7$ foi identificado como outlier pelo critério $|z|>2$. Reajustando a regressão sem esse ponto:

| Quantidade | Valor |
| --- | ---: |
| $\bar{x}$ | 9,7000 |
| $\bar{y}$ | 2,3300 |
| $S_{xx}$ | 404,1000 |
| $S_{yy}$ | 12,3810 |
| $S_{xy}$ | 69,5900 |
| $a$ | 0,6596 |
| $b$ | 0,1722 |
| $r$ | 0,9838 |
| $R^2$ | 0,9679 |

Assim:

$$
\hat{y}=0,6596+0,1722x
$$

Arredondando:

$$
\hat{y}=0,660+0,172x,\quad r\approx 0,984,\quad R^2\approx 0,968
$$

A associação permanece positiva e forte. A retirada do ponto altera pouco a inclinação, mas aumenta $r$ e $R^2$, indicando maior ajuste linear no conjunto sem esse ponto.

### Respostas do Problema 1

**Questão 1: C.** A reta ajustada com todos os dados é $\hat{y}=0,658+0,178x$ e $r\approx 0,973$, indicando associação linear positiva e forte.

**Questão 2: D.** Como $R^2=r^2$, tem-se $R^2\approx 0,947$. A interpretação correta é descritiva: cerca de 94,7% da variação do BOD é explicada linearmente pelo tempo, sem concluir causalidade.

**Questão 3: B.** Para $x=15$, $\hat{y}\approx 3,33$; para aumento de 3 dias, a mudança média prevista é aproximadamente $0,53$; em $x=6$, o resíduo é aproximadamente $0,17$.

**Questão 4: A.** No gráfico de $\hat{y}_i$ versus $y_i$, uma relação determinística sem erro aleatório colocaria todos os pontos sobre a reta $\hat{y}=y$. Como os pontos obtidos ficam próximos desse padrão, o tempo parece ser um regressor efetivo para prever BOD.

**Questão 5: A.** Sem o ponto $x=14$, $y=3,7$, a reta é aproximadamente $\hat{y}=0,660+0,172x$, com $r\approx 0,984$ e $R^2\approx 0,968$.

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

| Páginas vistas | $P(\text{grupo})$ | $P(\mathrm{RMI}\mid \text{grupo})$ | $P(\text{grupo}\cap \mathrm{RMI})$ |
| --- | ---: | ---: | ---: |
| 1 | 0,40 | 0,10 | 0,040 |
| 2 | 0,30 | 0,10 | 0,030 |
| 3 | 0,20 | 0,20 | 0,040 |
| 4 ou mais | 0,10 | 0,40 | 0,040 |
| **Total** | **1,00** |  | **0,150** |

Assim:

$$
P(\mathrm{RMI})
=0,040+0,030+0,040+0,040
=0,150
$$

Logo, 15% dos visitantes solicitam mais informação.

### Bayes

A probabilidade pedida na última etapa é:

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

**Questão 6: A.** $\mathrm{RMI}$ é o evento “visitante solicita mais informação”; os grupos são definidos pelas páginas vistas; em $P(4\text{ ou mais páginas}\mid \mathrm{RMI})$, o universo é o conjunto dos visitantes que solicitaram mais informação.

**Questão 7: C.** As conjuntas são $0,04$, $0,03$, $0,04$ e $0,04$.

**Questão 8: E.** $P(\mathrm{RMI})=0,15$, obtida pela soma das probabilidades conjuntas de $\mathrm{RMI}$ em todos os grupos.

**Questão 9: D.** 

$$
P(4\text{ ou mais páginas}\mid \mathrm{RMI})
=\frac{0,04}{0,15}
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

**Questão 10: C.** A distribuição é válida porque as probabilidades são não negativas e somam 1. Os valores de $X$ não precisam ser consecutivos.

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
