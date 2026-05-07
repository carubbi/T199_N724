# Ex 2 - Alunos e professores

## Enunciado

Os dados a seguir relacionam o número de alunos e o número de professores em instituições de ensino superior.

Variáveis observadas:
- nome da instituição;
- número de alunos;
- número de professores.

**Calcule e interprete:**

<ol type="a">
<li>a correlação linear entre número de alunos e número de professores;</li>
<li>a reta de regressão para explicar o número de professores pelo número de alunos;</li>
<li>o coeficiente de determinação R2;</li>
<li>a decomposição da variação em SQReg, SQRes e SQTot;</li>
<li>a ANOVA da regressão, incluindo gl, QM e F;</li>
<li>a existência de instituições com resíduos altos ou comportamento atípico/outlier;</li>
<li>os limites da interpretação: associação não implica causalidade.</li>
</ol>

## Observação inicial e perguntas orientadoras

- Qual é a variável explicativa? x = número de alunos. A escolha de x faz sentido substantivo? A regressão deve ser lida como previsão do número de professores a partir do porte da instituição, não como prova causal.
- Qual é a variável resposta? y = número de professores. O que significa prever professores neste contexto? A unidade de b deve ser interpretada por aluno ou por blocos de 1000 alunos para fazer sentido didático?
- A relação parece aproximadamente linear? Compare o gráfico com r, b e R2. R2 indica a proporção da variação de professores explicada pela reta; ele não prova que alunos causam contratação de professores.
- Há instituições com comportamento atípico/outlier? Use resíduos, SQReg, SQRes, SQTot e R2 para avaliar o ajuste. Na ANOVA, identifique gl, QM e F: a variação explicada pela regressão é grande em relação à variação residual? Quais instituições merecem leitura crítica antes de aceitar a reta como resumo do conjunto?

## Dados

| Caso | x = alunos | y = professores |
| --- | ---: | ---: |
| PUC de Minas Gerais | 13147 | 713 |
| Federal de Juiz de Fora | 6606 | 781 |
| Federal de Minas Gerais | 23759 | 2194 |
| Federal de Ouro Preto | 1106 | 178 |
| Federal de Uberlândia | 6651 | 765 |
| Federal de Viçosa | 5842 | 667 |
| PUC do Rio Grande do Sul | 23045 | 1459 |
| Católica de Pelotas | 5711 | 381 |
| Univ. de Caxias do Sul | 9196 | 497 |
| Federal de Pelotas | 4877 | 903 |
| Federal do Rio Gde. do Sul | 16985 | 2451 |
| Federal de Santa Maria | 9693 | 1362 |
| Univ. de Passo Fundo | 7450 | 530 |
| Univ. do Rio Grande | 3476 | 490 |
| Univ. do Vale do Rio dos Sinos | 21000 | 650 |
| PUC do Rio de Janeiro | 8232 | 788 |
| Católica de Petrópolis | 4200 | 298 |
| Estadual do Rio de Janeiro | 11000 | 1750 |
| Federal Fluminense | 24775 | 2415 |
| Federal do Rio de Janeiro | 30000 | 3580 |
| Federal Rural do RJ | 3686 | 611 |
| Gama Filho | 26000 | 1541 |
| PUC de Campinas | 18132 | 1457 |
| PUC de São Paulo | 15296 | 1526 |
| Estadual de Campinas | 9843 | 1474 |
| UNESP Júlio Mesquita Filho | 14204 | 2395 |
| Federal de São Carlos | 2566 | 463 |
| Univ. Mackenzie | 14022 | 121 |
| Univ. de Mogi das Cruzes | 15088 | 924 |
| Estadual de São Paulo | 44159 | 4461 |
| Metodista de Piracicaba | 6600 | 500 |

## Desenvolvimento da solução sem o uso de planilha

Esta seção mostra a resolução pelas fórmulas estatísticas, usando somatórios e substituição numérica. A planilha serve apenas para conferir os resultados.

### 1. Médias

$$
\bar{x} = \frac{\sum x_i}{n} = \frac{406347}{31} = 13107,968
$$

$$
\bar{y} = \frac{\sum y_i}{n} = \frac{38325}{31} = 1236,29
$$

### 2. Somatórios auxiliares

Depois das médias, calcula-se para cada observação:

$$
d_{x_i} = x_i - \bar{x}
$$

$$
d_{y_i} = y_i - \bar{y}
$$

A tabela a seguir explicita os produtos termo a termo e os somatórios usados nos cálculos.

| Caso | $x_i$ | $y_i$ | $d_{x_i}$ | $d_{y_i}$ | $d_{x_i}d_{y_i}$ | $d_{x_i}^2$ | $d_{y_i}^2$ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| PUC de Minas Gerais | 13147 | 713 | 39,032258 | -523,29 | -20425,203 | 1523,517 | 273832,762 |
| Federal de Juiz de Fora | 6606 | 781 | -6501,968 | -455,29 | 2960282,991 | 42275584,517 | 207289,278 |
| Federal de Minas Gerais | 23759 | 2194 | 10651,032 | 957,71 | 10200596,668 | 113444488,162 | 917207,826 |
| Federal de Ouro Preto | 1106 | 178 | -12001,968 | -1058,29 | 12701566,313 | 144047229,678 | 1119978,407 |
| Federal de Uberlândia | 6651 | 765 | -6456,968 | -471,29 | 3043106,41 | 41692432,42 | 222114,568 |
| Federal de Viçosa | 5842 | 667 | -7265,968 | -569,29 | 4136445,12 | 52794287,227 | 324091,471 |
| PUC do Rio Grande do Sul | 23045 | 1459 | 9937,032 | 222,71 | 2213073,249 | 98744610,098 | 49599,6 |
| Católica de Pelotas | 5711 | 381 | -7396,968 | -855,29 | 6326554,926 | 54715131,775 | 731521,536 |
| Univ. de Caxias do Sul | 9196 | 497 | -3911,968 | -739,29 | 2892079,894 | 15303491,614 | 546550,181 |
| Federal de Pelotas | 4877 | 903 | -8230,968 | -333,29 | 2743301,894 | 67748829,969 | 111082,439 |
| Federal do Rio Gde. do Sul | 16985 | 2451 | 3877,032 | 1214,71 | 4709468,604 | 15031379,13 | 1475519,6 |
| Federal de Santa Maria | 9693 | 1362 | -3414,968 | 125,71 | -429294,493 | 11662004,678 | 15802,923 |
| Univ. de Passo Fundo | 7450 | 530 | -5657,968 | -706,29 | 3996167,862 | 32012598,969 | 498846,02 |
| Univ. do Rio Grande | 3476 | 490 | -9631,968 | -746,29 | 7188244,313 | 92774802,582 | 556949,246 |
| Univ. do Vale do Rio dos Sinos | 21000 | 650 | 7892,032 | -586,29 | -4627022,138 | 62284173,162 | 343736,342 |
| PUC do Rio de Janeiro | 8232 | 788 | -4875,968 | -448,29 | 2185849,152 | 23775061,42 | 200964,213 |
| Católica de Petrópolis | 4200 | 298 | -8907,968 | -938,29 | 8358259,926 | 79351889,291 | 880388,729 |
| Estadual do Rio de Janeiro | 11000 | 1750 | -2107,968 | 513,71 | -1082883,429 | 4443528,001 | 263897,633 |
| Federal Fluminense | 24775 | 2415 | 11667,032 | 1178,71 | 13752043,829 | 136119641,711 | 1389356,504 |
| Federal do Rio de Janeiro | 30000 | 3580 | 16892,032 | 2343,71 | 39590019,475 | 285340753,807 | 5492975,052 |
| Federal Rural do RJ | 3686 | 611 | -9421,968 | -625,29 | 5891465,249 | 88773476,13 | 390987,988 |
| Gama Filho | 26000 | 1541 | 12892,032 | 304,71 | 3928326,991 | 166204495,743 | 92847,988 |
| PUC de Campinas | 18132 | 1457 | 5024,032 | 220,71 | 1108852,539 | 25240900,13 | 48712,762 |
| PUC de São Paulo | 15296 | 1526 | 2188,032 | 289,71 | 633894,12 | 4787485,162 | 83931,697 |
| Estadual de Campinas | 9843 | 1474 | -3264,968 | 237,71 | -776114,429 | 10660014,356 | 56505,891 |
| UNESP Júlio Mesquita Filho | 14204 | 2395 | 1096,032 | 1158,71 | 1269983,184 | 1201286,711 | 1342608,117 |
| Federal de São Carlos | 2566 | 463 | -10541,968 | -773,29 | 8152001,636 | 111133083,872 | 597977,923 |
| Univ. Mackenzie | 14022 | 121 | 914,032 | -1115,29 | -1019411,332 | 835454,969 | 1243872,504 |
| Univ. de Mogi das Cruzes | 15088 | 924 | 1980,032 | -312,29 | -618344,913 | 3920527,743 | 97525,246 |
| Estadual de São Paulo | 44159 | 4461 | 31051,032 | 3224,71 | 100130564,216 | 964166604,291 | 10398752,504 |
| Metodista de Piracicaba | 6600 | 500 | -6507,968 | -736,29 | 4791753,668 | 42353644,13 | 542123,439 |
| **Somatório** | $\sum x_i = 406347$ | $\sum y_i = 38325$ |  |  | $\sum d_{x_i}d_{y_i} = 244330406,29$ | $\sum d_{x_i}^2 = 2792840414,968$ | $\sum d_{y_i}^2 = 30517550,387$ |

Os somatórios principais são:

| Somatório | Valor |
| --- | ---: |
| $\sum d_{x_i}d_{y_i}$ | 244330406,29 |
| $\sum d_{x_i}^2$ | 2792840414,968 |
| $\sum d_{y_i}^2$ | 30517550,387 |

### 3. Correlação de Pearson

$$
r = \frac{\sum d_{x_i}d_{y_i}}{\sqrt{\sum d_{x_i}^2 \sum d_{y_i}^2}}
$$

$$
r = \frac{244330406,29}{\sqrt{2792840414,968\cdot 30517550,387}} = 0,836912
$$

### 4. Reta de regressão

A inclinação da reta é:

$$
b = \frac{\sum d_{x_i}d_{y_i}}{\sum d_{x_i}^2}
$$

$$
b = \frac{244330406,29}{2792840414,968} = 0,087485
$$

O intercepto é:

$$
a = \bar{y} - b\bar{x}
$$

$$
a = 1236,29 - 0,087485\cdot 13107,968 = 89,545572
$$

Logo, a reta ajustada é:

$$
\hat{y} = 89,545572 + 0,087485x
$$

### 5. Coeficiente de determinação

$$
R^2 = r^2 = (0,836912)^2 = 0,700421
$$

Também é possível calcular $R^2$ pela decomposição da ANOVA:

$$
R^2 = \frac{\mathrm{SQ}_{Reg}}{\mathrm{SQ}_{Tot}} = \frac{21375137,34}{30517550,387} = 0,700421
$$

### 6. ANOVA da regressão

A decomposição da variabilidade é:

$$
\mathrm{SQ}_{Tot} = \mathrm{SQ}_{Reg} + \mathrm{SQ}_{Res} = 21375137,34 + 9142413,047 = 30517550,387
$$

Os quadrados médios são:

$$
\mathrm{QM}_{Reg} = \frac{\mathrm{SQ}_{Reg}}{\mathrm{gl}_{Reg}} = \frac{21375137,34}{1} = 21375137,34
$$

$$
\mathrm{QM}_{Res} = \frac{\mathrm{SQ}_{Res}}{\mathrm{gl}_{Res}} = \frac{9142413,047}{29} = 315255,622
$$

A estatística $F$ é:

$$
F = \frac{\mathrm{QM}_{Reg}}{\mathrm{QM}_{Res}} = \frac{21375137,34}{315255,622} = 67,802557
$$

Resumo dos graus de liberdade:

- $\mathrm{gl}_{Reg} = 1$
- $\mathrm{gl}_{Res} = n - 2 = 31 - 2 = 29$
- $\mathrm{gl}_{Tot} = n - 1 = 31 - 1 = 30$

Tabela ANOVA final:

| Fonte | $\mathrm{SQ}$ | $\mathrm{gl}$ | $\mathrm{QM}$ | $F$ |
| --- | ---: | ---: | ---: | ---: |
| Regressão | 21375137,34 | 1 | 21375137,34 | 67,802557 |
| Resíduos | 9142413,047 | 29 | 315255,622 |  |
| Total | 30517550,387 | 30 |  |  |

## Desenvolvimento da solução com o uso de planilha

### Definições das variáveis e símbolos

| Símbolo ou termo | Significado |
| --- | --- |
| `x` | Variável explicativa: x = alunos. |
| `y` | Variável resposta: y = professores. |
| `n` | Número de observações usadas no cálculo. |
| `x̄` | Média dos valores de `x`. |
| `ȳ` | Média dos valores de `y`. |
| `dx` | Desvio de cada valor de `x` em relação à média: `x - x̄`. |
| `dy` | Desvio de cada valor de `y` em relação à média: `y - ȳ`. |
| `dx*dy` | Produto dos desvios; mostra como `x` e `y` variam em conjunto. |
| `dx^2` | Quadrado do desvio de `x`; mede a variação de `x`. |
| `dy^2` | Quadrado do desvio de `y`; soma essas parcelas para obter `SQTot`. |
| `r` | Correlação linear de Pearson; mede força e direção da associação linear. |
| `R2` | Coeficiente de determinação; proporção da variação de `y` explicada pela regressão. |
| `a` | Intercepto da reta; valor previsto de `y` quando `x = 0`. |
| `b` | Inclinação da reta; variação prevista em `y` para aumento de 1 unidade em `x`. |
| `ŷ` | Valor previsto pela reta de regressão. |
| `resíduo` | Erro de previsão: valor observado menos valor previsto, isto é, `y - ŷ`. |
| `SQ` | Soma de quadrados; medida de variação acumulada. |
| `SQReg` | Soma de quadrados da regressão; parte da variação de `y` explicada pela reta. |
| `SQRes` | Soma de quadrados dos resíduos; parte da variação de `y` não explicada pela reta. |
| `SQTot` | Soma de quadrados total; variação total observada em `y`. |
| `gl` | Graus de liberdade; quantidade de informação independente usada em cada fonte da ANOVA. |
| `QM` | Quadrado médio; calculado por `SQ / gl`. |
| `F` | Estatística da ANOVA; compara `QMReg` com `QMRes`. |

### Fórmulas estatísticas e funções da planilha

#### Fórmulas estatísticas

| Medida | Fórmula | Leitura didática |
| --- | --- | --- |
| Média de `x` | `x̄ = SOMA(x) / n` | Valor médio da variável explicativa. |
| Média de `y` | `ȳ = SOMA(y) / n` | Valor médio da variável resposta. |
| Desvio de `x` | `dx = x - x̄` | Distância de cada `x` até sua média. |
| Desvio de `y` | `dy = y - ȳ` | Distância de cada `y` até sua média. |
| Correlação | `r = SOMA(dx*dy) / RAIZ(SOMA(dx^2) * SOMA(dy^2))` | Mede associação linear entre `x` e `y`. |
| Inclinação | `b = SOMA(dx*dy) / SOMA(dx^2)` | Mostra quanto `y` tende a variar quando `x` aumenta 1 unidade. |
| Intercepto | `a = ȳ - b*x̄` | Completa a equação da reta. |
| Reta de regressão | `ŷ = a + b*x` | Gera o valor previsto de `y`. |
| Resíduo | `e = y - ŷ` | Diferença entre valor observado e valor previsto. |
| SQTotal | `SQTot = SOMA((y - ȳ)^2)` | Variação total de `y`. |
| SQResíduos | `SQRes = SOMA((y - ŷ)^2)` | Variação que a reta não explicou. |
| SQRegressão | `SQReg = SOMA((ŷ - ȳ)^2)` | Variação explicada pela reta. |
| R2 pela ANOVA | `R2 = SQReg / SQTot` | Proporção explicada pela regressão. |
| Quadrado médio | `QM = SQ / gl` | Variação média por grau de liberdade. |
| Estatística F | `F = QMReg / QMRes` | Compara variação explicada com variação residual. |

#### Funções estatísticas do Google Planilhas

| Função | Para que serve | Modelo da fórmula |
| --- | --- | --- |
| `CORREL` | Calcula a correlação linear de Pearson. | `=CORREL(intervalo_y; intervalo_x)` |
| `SLOPE` | Calcula a inclinação `b` da reta. | `=SLOPE(intervalo_y; intervalo_x)` |
| `INTERCEPT` | Calcula o intercepto `a` da reta. | `=INTERCEPT(intervalo_y; intervalo_x)` |
| `RSQ` | Calcula `R2`. | `=RSQ(intervalo_y; intervalo_x)` |
| `LINEST` | Ajusta a regressão linear aos intervalos informados; o primeiro `TRUE` estima o intercepto e o segundo `TRUE` retorna a matriz completa de estatísticas. | `=LINEST(intervalo_y; intervalo_x; TRUE; TRUE)` |

### Cálculo na planilha por somatórios

| Medida | Fórmula na planilha | Resultado |
| --- | --- | ---: |
| n | `=COUNT(B10:B40)` | 31 |
| média x | `=SUM(B10:B40)/B43` | 13107.968 |
| média y | `=SUM(C10:C40)/B43` | 1236.29 |
| SOMA dx*dy | `=SUM(F10:F40)` | 244330406.29 |
| SOMA dx^2 | `=SUM(G10:G40)` | 2792840414.968 |
| SQTot = SOMA dy^2 | `=SUM(H10:H40)` | 30517550.387 |
| r manual | `=B46/SQRT(B47*B48)` | 0.836912 |
| R2 manual = r^2 | `=B49^2` | 0.700421 |
| b manual | `=B46/B47` | 0.087485 |
| a manual | `=B45-B51*B44` | 89.545572 |

### ANOVA da regressão na planilha

| Fonte | SQ | gl | QM | F |
| --- | ---: | ---: | ---: | ---: |
| Regressão | 21375137.34 | 1 | 21375137.34 | 67.802557 |
| Resíduos | 9142413.047 | 29 | 315255.622 |  |
| Total | 30517550.387 | 30 |  |  |

- Conferência SQTot - (SQReg + SQRes): -0
- R2 pela ANOVA: 0.700421

### Validação com LINEST completo da planilha

A função `LINEST` ajusta a regressão linear aos intervalos informados. O primeiro `TRUE` estima o intercepto da reta e o segundo `TRUE` retorna a matriz completa de estatísticas.

| Modelo da fórmula | Substituição no exercício |
| --- | --- |
| `=LINEST(intervalo_y; intervalo_x; TRUE; TRUE)` | `=LINEST(C10:C40; B10:B40; TRUE; TRUE)` |

| Linha do retorno | Coluna 1 | Resultado | Coluna 2 | Resultado |
| --- | --- | ---: | --- | ---: |
| 1 | inclinação `b` | 0.087485 | intercepto `a` | 89.545572 |
| 2 | erro-padrão de `b` | 0.010624 | erro-padrão de `a` | 171.943 |
| 3 | `R2` | 0.700421 | erro-padrão da estimativa de `y` | 561.476 |
| 4 | `F` | 67.802557 | graus de liberdade | 29 |
| 5 | `SQReg` | 21375137.34 | `SQRes` | 9142413.047 |

## Interpretação crítica

- r aproximado 0,837 e R2 aproximado 0,700: associação linear positiva forte, com cerca de 70,0% da variação de professores explicada pela regressão.
- ANOVA: F aproximado 67,803. A variação explicada pela reta é grande em relação à variação residual.
- Reta: professores = 89,546 + 0,08748*alunos; cada 1000 alunos adicionais estão associados a cerca de 87,5 professores previstos.
- O intercepto é parâmetro técnico; x=0 não tem interpretação substantiva forte nesse contexto.
- Mesmo com R2 alto e F elevado, associação não deve ser lida como prova causal.
