# Ex 1 - Peso versus altura

## Enunciado

Os dados a seguir se referem a uma amostra de oito pessoas para as quais se dispõe de informações relativas a:

- nome;
- altura, em metros;
- peso, em quilos.

| Nome | Altura | Peso |
| --- | --- | --- |
| Jorge | 1,89 | 73 |
| Diva | 1,74 | 68 |
| André | 1,93 | 82 |
| Lucia | 1,74 | 57 |
| Silvio | 1,78 | 126 |
| Pedro | 1,92 | 90 |
| Maria | 1,61 | 53 |
| Norma | 1,80 | 65 |

**Calcule:**

<ol type="a">
<li>média e desvio-padrão da altura;</li>
<li>média e desvio-padrão do peso;</li>
<li>correlação e reta de regressão para explicar peso pela altura;</li>
<li>repita a correlação e a regressão excluindo Silvio;</li>
<li>interprete o efeito dessa exclusão.</li>
</ol>

## Observação inicial e perguntas orientadoras

- Qual é a variável explicativa? x = altura. Antes dos cálculos, confirme: faz sentido usar altura para explicar peso? Qual é a unidade de x e como ela afeta a interpretação da inclinação da reta?
- Qual é a variável resposta? y = peso. O objetivo é apenas medir associação ou também prever peso a partir da altura? Que tipo de erro de previsão seria esperado nesse contexto?
- O gráfico sugere associação positiva, negativa ou fraca? Compare a leitura visual com r, com o sinal de b e com R2. R2 alto significa bom ajuste? R2 baixo elimina a possibilidade de alguma relação linear?
- Silvio parece valor atípico/outlier? A exclusão não deve ser automática. Analise resíduos, SQReg, SQRes, SQTot e R2 antes e depois de retirar Silvio. Na ANOVA, o que representam gl, QM e F? O F sugere que a regressão explica variação relevante? A decisão estatística muda quando comparamos todos os casos com o cenário sem Silvio?

## Dados

| Caso | x = altura (m) | y = peso (kg) |
| --- | ---: | ---: |
| Jorge | 1.89 | 73 |
| Diva | 1.74 | 68 |
| André | 1.93 | 82 |
| Lucia | 1.74 | 57 |
| Silvio | 1.78 | 126 |
| Pedro | 1.92 | 90 |
| Maria | 1.61 | 53 |
| Norma | 1.8 | 65 |

## Desenvolvimento da solução sem o uso de planilha

Esta seção mostra a resolução pelas fórmulas estatísticas, usando somatórios e substituição numérica. A planilha serve apenas para conferir os resultados.

### 1. Médias

$$
\bar{x} = \frac{\sum x_i}{n} = \frac{14,41}{8} = 1,80125
$$

$$
\bar{y} = \frac{\sum y_i}{n} = \frac{614}{8} = 76,75
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
| Jorge | 1,89 | 73 | 0,08875 | -3,75 | -0,332812 | 0,007877 | 14,0625 |
| Diva | 1,74 | 68 | -0,06125 | -8,75 | 0,535938 | 0,003752 | 76,5625 |
| André | 1,93 | 82 | 0,12875 | 5,25 | 0,675937 | 0,016577 | 27,5625 |
| Lucia | 1,74 | 57 | -0,06125 | -19,75 | 1,209688 | 0,003752 | 390,062 |
| Silvio | 1,78 | 126 | -0,02125 | 49,25 | -1,046562 | 0,000452 | 2425,562 |
| Pedro | 1,92 | 90 | 0,11875 | 13,25 | 1,573437 | 0,014102 | 175,562 |
| Maria | 1,61 | 53 | -0,19125 | -23,75 | 4,542187 | 0,036577 | 564,062 |
| Norma | 1,8 | 65 | -0,00125 | -11,75 | 0,014687 | 0,000002 | 138,062 |
| **Somatório** | $\sum x_i = 14,41$ | $\sum y_i = 614$ |  |  | $\sum d_{x_i}d_{y_i} = 7,1725$ | $\sum d_{x_i}^2 = 0,083087$ | $\sum d_{y_i}^2 = 3811,5$ |

Os somatórios principais são:

| Somatório | Valor |
| --- | ---: |
| $\sum d_{x_i}d_{y_i}$ | 7,1725 |
| $\sum d_{x_i}^2$ | 0,083087 |
| $\sum d_{y_i}^2$ | 3811,5 |

### 3. Correlação de Pearson

$$
r = \frac{\sum d_{x_i}d_{y_i}}{\sqrt{\sum d_{x_i}^2 \sum d_{y_i}^2}}
$$

$$
r = \frac{7,1725}{\sqrt{0,083087\cdot 3811,5}} = 0,403046
$$

### 4. Reta de regressão

A inclinação da reta é:

$$
b = \frac{\sum d_{x_i}d_{y_i}}{\sum d_{x_i}^2}
$$

$$
b = \frac{7,1725}{0,083087} = 86,324658
$$

O intercepto é:

$$
a = \bar{y} - b\bar{x}
$$

$$
a = 76,75 - 86,324658\cdot 1,80125 = -78,74229
$$

Logo, a reta ajustada é:

$$
\hat{y} = -78,74229 + 86,324658x
$$

### 5. Coeficiente de determinação

$$
R^2 = r^2 = (0,403046)^2 = 0,162446
$$

Também é possível calcular $R^2$ pela decomposição da ANOVA:

$$
R^2 = \frac{\mathrm{SQ}_{Reg}}{\mathrm{SQ}_{Tot}} = \frac{619,164}{3811,5} = 0,162446
$$

### 6. ANOVA da regressão

A decomposição da variabilidade é:

$$
\mathrm{SQ}_{Tot} = \mathrm{SQ}_{Reg} + \mathrm{SQ}_{Res} = 619,164 + 3192,336 = 3811,5
$$

Os quadrados médios são:

$$
\mathrm{QM}_{Reg} = \frac{\mathrm{SQ}_{Reg}}{\mathrm{gl}_{Reg}} = \frac{619,164}{1} = 619,164
$$

$$
\mathrm{QM}_{Res} = \frac{\mathrm{SQ}_{Res}}{\mathrm{gl}_{Res}} = \frac{3192,336}{6} = 532,056
$$

A estatística $F$ é:

$$
F = \frac{\mathrm{QM}_{Reg}}{\mathrm{QM}_{Res}} = \frac{619,164}{532,056} = 1,163719
$$

Resumo dos graus de liberdade:

- $\mathrm{gl}_{Reg} = 1$
- $\mathrm{gl}_{Res} = n - 2 = 8 - 2 = 6$
- $\mathrm{gl}_{Tot} = n - 1 = 8 - 1 = 7$

Tabela ANOVA final:

| Fonte | $\mathrm{SQ}$ | $\mathrm{gl}$ | $\mathrm{QM}$ | $F$ |
| --- | ---: | ---: | ---: | ---: |
| Regressão | 619,164 | 1 | 619,164 | 1,163719 |
| Resíduos | 3192,336 | 6 | 532,056 |  |
| Total | 3811,5 | 7 |  |  |

## Desenvolvimento da solução com o uso de planilha

### Definições das variáveis e símbolos

| Símbolo ou termo | Significado |
| --- | --- |
| `x` | Variável explicativa: x = altura (m). |
| `y` | Variável resposta: y = peso (kg). |
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
| `Erro-padrão residual` | Medida da escala típica dos resíduos: `RAIZ(SQRes / glRes)`. |
| `z_resíduo` | Resíduo padronizado: `resíduo / Erro-padrão residual`. |
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
| Erro-padrão residual | `Erro-padrão residual = RAIZ(SQRes / glRes)` | Escala típica dos resíduos. |
| Resíduo padronizado | `z_e = e / Erro-padrão residual` | Ajuda a comparar resíduos em escala comum. |
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
| n | `=COUNT(B10:B17)` | 8 |
| média x | `=SUM(B10:B17)/B20` | 1.80125 |
| média y | `=SUM(C10:C17)/B20` | 76.75 |
| SOMA dx*dy | `=SUM(F10:F17)` | 7.1725 |
| SOMA dx^2 | `=SUM(G10:G17)` | 0.083087 |
| SQTot = SOMA dy^2 | `=SUM(H10:H17)` | 3811.5 |
| r manual | `=B23/SQRT(B24*B25)` | 0.403046 |
| R2 manual = r^2 | `=B26^2` | 0.162446 |
| b manual | `=B23/B24` | 86.324658 |
| a manual | `=B22-B28*B21` | -78.74229 |

### ANOVA da regressão na planilha

| Fonte | SQ | gl | QM | F |
| --- | ---: | ---: | ---: | ---: |
| Regressão | 619.164 | 1 | 619.164 | 1.163719 |
| Resíduos | 3192.336 | 6 | 532.056 |  |
| Total | 3811.5 | 7 |  |  |

- Conferência SQTot - (SQReg + SQRes): -0
- R2 pela ANOVA: 0.162446

### Resíduos padronizados e diagnóstico visual

Além do resíduo bruto, a planilha calcula:

$$
\text{Erro-padrão residual}=\sqrt{\frac{SQRes}{glRes}}
$$

e:

$$
z_{e_i}=\frac{e_i}{\text{Erro-padrão residual}}
$$

Como regra prática inicial, resíduos padronizados com:

$$
|z_{e_i}|>2
$$

devem ser investigados. Isso não implica exclusão automática; indica apenas que a observação merece análise.

A planilha também lista os intervalos-base para construir gráficos diagnósticos:

| Gráfico | Eixo X | Eixo Y | Objetivo |
| --- | --- | --- | --- |
| Dispersão | altura | peso | Ver se altura e peso parecem ter relação aproximadamente linear; observar direção da associação e possíveis pontos isolados. |
| Reta ajustada | altura | valor previsto | Ver se a reta passa pelo centro da nuvem de pontos ou se foi puxada por algum caso específico, como Silvio. |
| Resíduos vs previsto | valor previsto | resíduo | Ver se os erros ficam espalhados ao redor de zero sem padrão; curva ou funil indicam ajuste problemático. |
| Resíduos vs altura | altura | resíduo | Ver se os erros mudam conforme a altura aumenta; padrão sistemático sugere que a reta não capturou bem a relação. |
| Resíduos padronizados | altura | resíduo padronizado | Identificar observações com erro grande em escala comum; valores com `|z| > 2` devem ser investigados, não excluídos automaticamente. |

Conclusões diagnósticas esperadas:

| Gráfico | Conclusão diagnóstica |
| --- | --- |
| Dispersão | A associação é positiva, mas enfraquecida por Silvio, que aparece como ponto isolado; a linearidade melhora quando esse caso é analisado separadamente. |
| Reta ajustada | A reta com todos os casos é puxada por Silvio e representa mal o padrão dos demais; a comparação sem Silvio sugere ajuste mais forte. |
| Resíduos vs previsto | Os resíduos mostram Silvio com erro positivo muito alto; isso indica que o modelo subestima fortemente seu peso. |
| Resíduos vs altura | Não há padrão claro entre altura e resíduos para os demais casos, mas Silvio se destaca como erro extremo. |
| Resíduos padronizados | Silvio tem resíduo padronizado maior que 2 e deve ser investigado como possível valor atípico/outlier, sem exclusão automática. |

Para criar cada gráfico no Google Planilhas:

1. selecione o intervalo do eixo X e, mantendo a tecla de seleção múltipla, selecione o intervalo do eixo Y;
2. use **Inserir > Gráfico**;
3. escolha gráfico de dispersão;
4. no gráfico de dispersão principal, adicione a série dos valores previstos para visualizar a reta ajustada;
5. nos gráficos de resíduos, observe se há padrão sistemático, curvatura, mudança de variância ou pontos isolados.

No gráfico de dispersão principal, também é possível usar a linha de tendência do Google Planilhas:

1. clique no gráfico;
2. abra **Editar gráfico > Personalizar > Série**;
3. marque **Linha de tendência**;
4. em **Rótulo**, escolha **Usar equação**;
5. marque **Mostrar R²**.

Use a equação e o R² exibidos no gráfico apenas como conferência. Eles devem ser compatíveis com os valores calculados na planilha para o intercepto, a inclinação e o coeficiente de determinação.

### Validação com LINEST completo da planilha

A função `LINEST` ajusta a regressão linear aos intervalos informados. O primeiro `TRUE` estima o intercepto da reta e o segundo `TRUE` retorna a matriz completa de estatísticas.

| Modelo da fórmula | Substituição no exercício |
| --- | --- |
| `=LINEST(intervalo_y; intervalo_x; TRUE; TRUE)` | `=LINEST(C10:C17; B10:B17; TRUE; TRUE)` |

| Linha do retorno | Coluna 1 | Resultado | Coluna 2 | Resultado |
| --- | --- | ---: | --- | ---: |
| 1 | inclinação `b` | 86.324658 | intercepto `a` | -78.74229 |
| 2 | erro-padrão de `b` | 80.022268 | erro-padrão de `a` | 144.371 |
| 3 | `R2` | 0.162446 | erro-padrão da estimativa de `y` | 23.066341 |
| 4 | `F` | 1.163719 | graus de liberdade | 6 |
| 5 | `SQReg` | 619.164 | `SQRes` | 3192.336 |

## Interpretação crítica

- Todos os casos: r aproximado 0,403; R2 aproximado 0,162. A reta explica cerca de 16,2% da variação do peso.
- ANOVA: F aproximado 1,164. A variação explicada pela regressão é pequena quando comparada à variação residual.
- Sem Silvio: r aproximado 0,903; R2 aproximado 0,815. A exclusão aumenta muito o ajuste, indicando forte efeito dessa observação atípica/outlier.
- A decisão de excluir Silvio exige justificativa substantiva; não basta melhorar R2, F ou a aparência da reta.
