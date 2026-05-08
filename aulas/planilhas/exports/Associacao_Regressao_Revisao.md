# Revisão conceitual: correlação, regressão linear simples, $R^2$ e ANOVA

Este material resume os conceitos necessários para analisar a relação entre duas variáveis quantitativas. A ideia central é estudar se uma variável quantitativa $x$ ajuda a explicar ou prever uma variável quantitativa $y$, usando correlação de Pearson, regressão linear simples, resíduos, $R^2$ e ANOVA da regressão.

## 1. Variáveis do problema

Em problemas desse tipo, trabalhamos com pares observados:

$$
(x_i, y_i), \quad i = 1, 2, \ldots, n
$$

onde:

| Símbolo | Significado |
| --- | --- |
| $x_i$ | Valor da variável explicativa no caso $i$ |
| $y_i$ | Valor da variável resposta no caso $i$ |
| $n$ | Número de observações |
| $\bar{x}$ | Média dos valores de $x$ |
| $\bar{y}$ | Média dos valores de $y$ |

Em termos computacionais, os dados podem ser vistos como dois vetores:

$$
\mathbf{x} = (x_1, x_2, \ldots, x_n)
$$

$$
\mathbf{y} = (y_1, y_2, \ldots, y_n)
$$

O objetivo é investigar a relação entre esses vetores.

## 2. Médias e desvios

A média de $x$ é:

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^{n}x_i
$$

A média de $y$ é:

$$
\bar{y} = \frac{1}{n}\sum_{i=1}^{n}y_i
$$

Os desvios em relação às médias são:

$$
d_{x_i} = x_i - \bar{x}
$$

$$
d_{y_i} = y_i - \bar{y}
$$

Esses desvios indicam quanto cada observação está acima ou abaixo da média.

## 3. Correlação de Pearson

A correlação de Pearson mede a força e a direção da associação linear entre $x$ e $y$.

$$
r =
\frac{
\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})
}{
\sqrt{
\sum_{i=1}^{n}(x_i-\bar{x})^2
\sum_{i=1}^{n}(y_i-\bar{y})^2
}
}
$$

Leitura:

| Valor de $r$ | Interpretação |
| ---: | --- |
| Próximo de $1$ | Associação linear positiva forte |
| Próximo de $-1$ | Associação linear negativa forte |
| Próximo de $0$ | Ausência de associação linear forte |

Ponto crítico: $r$ mede apenas associação **linear**. Uma relação não linear pode produzir $r$ baixo mesmo quando existe padrão nos dados.

No Google Planilhas:

```text
=CORREL(intervalo_y; intervalo_x)
```

## 4. Regressão linear simples

A regressão linear simples ajusta uma reta para prever $y$ a partir de $x$:

$$
\hat{y}_i = a + bx_i
$$

onde:

| Símbolo | Significado |
| --- | --- |
| $\hat{y}_i$ | Valor previsto de $y_i$ |
| $a$ | Intercepto da reta |
| $b$ | Inclinação da reta |

A inclinação é calculada por:

$$
b =
\frac{
\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})
}{
\sum_{i=1}^{n}(x_i-\bar{x})^2
}
$$

O intercepto é:

$$
a = \bar{y} - b\bar{x}
$$

Interpretação de $b$:

- $b$ indica a variação prevista em $y$ para aumento de 1 unidade em $x$;
- a unidade de $b$ depende das unidades originais das variáveis;
- quando a unidade de $x$ é muito pequena ou pouco intuitiva, pode ser mais didático interpretar múltiplos de $b$, como $10b$, $100b$ ou $1000b$.

No Google Planilhas:

```text
=SLOPE(intervalo_y; intervalo_x)
=INTERCEPT(intervalo_y; intervalo_x)
```

## 5. Valores previstos e resíduos

Depois de ajustar a reta, cada observação tem um valor previsto:

$$
\hat{y}_i = a + bx_i
$$

O resíduo é o erro de previsão:

$$
e_i = y_i - \hat{y}_i
$$

Leitura:

| Situação | Interpretação |
| --- | --- |
| $e_i > 0$ | O valor observado ficou acima do previsto |
| $e_i < 0$ | O valor observado ficou abaixo do previsto |
| $e_i \approx 0$ | A reta previu bem aquele caso |

Os resíduos são essenciais para avaliar a qualidade do ajuste. Um modelo pode ter boa correlação e ainda assim apresentar resíduos problemáticos ou valores atípicos/outliers.

## 6. Diagnóstico visual e análise de resíduos

Antes de aceitar a regressão como boa representação dos dados, é necessário analisar gráficos e resíduos. Essa etapa é tão importante quanto calcular $r$, $R^2$ ou $F$.

### 6.1 Gráfico de dispersão

O primeiro gráfico deve mostrar os pares observados:

$$
(x_i, y_i)
$$

Esse gráfico responde perguntas básicas:

- existe tendência aproximadamente linear?
- a associação parece positiva, negativa ou fraca?
- há curvatura ou padrão não linear?
- há observações isoladas ou visualmente atípicas?
- a variabilidade de $y$ parece mudar conforme $x$ aumenta?

Se o gráfico não sugere relação aproximadamente linear, a correlação de Pearson e a regressão linear simples podem ser resumos pobres do fenômeno.

### 6.2 Gráfico com reta ajustada

Depois de calcular a reta,

$$
\hat{y}_i = a + bx_i
$$

o gráfico de dispersão deve ser observado junto com a reta ajustada. A leitura principal é verificar se a reta passa pelo centro da nuvem de pontos ou se é puxada por poucos casos.

Esse gráfico ajuda a avaliar:

- direção da tendência;
- qualidade visual do ajuste;
- presença de pontos extremos;
- distância vertical entre observações e reta.

### 6.3 Resíduos versus valores previstos

Um gráfico importante é:

$$
(\hat{y}_i, e_i)
$$

Nesse gráfico, o eixo horizontal mostra os valores previstos e o eixo vertical mostra os resíduos.

Em um ajuste linear razoável, espera-se:

- resíduos distribuídos em torno de zero;
- ausência de curva clara;
- ausência de padrão crescente ou decrescente;
- variabilidade aproximadamente semelhante ao longo dos valores previstos.

Sinais de alerta:

| Padrão no gráfico | Possível interpretação |
| --- | --- |
| Curvatura nos resíduos | Relação não linear não capturada pela reta |
| Forma de funil | Variância dos erros muda com o nível de previsão |
| Muitos resíduos positivos em uma região e negativos em outra | Modelo sistematicamente enviesado |
| Um resíduo muito distante dos demais | Possível valor atípico ou caso anômalo |

### 6.4 Resíduos versus variável explicativa

Também é útil observar:

$$
(x_i, e_i)
$$

Esse gráfico verifica se os erros do modelo ainda têm relação com $x$. Se houver padrão claro, a reta não capturou completamente a estrutura dos dados.

### 6.5 Resíduos padronizados

Para comparar resíduos em escala comum, pode-se usar o resíduo padronizado:

$$
z_{e_i} = \frac{e_i}{s_e}
$$

em que $s_e$ é o erro-padrão da estimativa:

$$
s_e = \sqrt{\frac{\mathrm{SQ}_{Res}}{n-2}}
$$

Valores de $z_{e_i}$ com magnitude alta indicam observações que merecem inspeção. Em aplicações introdutórias, uma regra prática é investigar resíduos padronizados com:

$$
|z_{e_i}| > 2
$$

Essa regra não é uma sentença automática de exclusão. Ela apenas sinaliza pontos que precisam ser examinados.

### 6.6 Valores atípicos ou outliers

Um **valor atípico**, ou **outlier**, é uma observação incomum em relação ao padrão dos dados. Ele pode aparecer como:

- valor extremo em $x$;
- valor extremo em $y$;
- resíduo muito alto;
- combinação incomum entre $x$ e $y$.

Neste material, adotaremos o termo **valor atípico/outlier** para observações que merecem inspeção cuidadosa. Um valor atípico/outlier pode afetar:

- a inclinação $b$;
- o intercepto $a$;
- a correlação $r$;
- o $R^2$;
- a estatística $F$;
- a interpretação substantiva do modelo.

Um valor atípico/outlier não deve ser excluído automaticamente. A decisão deve considerar se há erro de medição, erro de digitação, caso fora da população de interesse ou condição especial documentada.

### 6.7 Checklist mínimo de diagnóstico

Antes de concluir a análise, verifique:

1. O gráfico de dispersão sugere relação aproximadamente linear?
2. A reta ajustada representa o centro da nuvem de pontos?
3. Os resíduos estão distribuídos ao redor de zero?
4. Há padrão sistemático nos resíduos?
5. Há resíduos muito grandes?
6. Algum valor atípico/outlier parece alterar a leitura da reta?
7. A interpretação de $R^2$ é compatível com os gráficos?
8. A ANOVA confirma que a variação explicada é relevante frente à variação residual?

## 7. Soma de quadrados

A ANOVA da regressão decompõe a variação total de $y$ em duas partes:

$$
\mathrm{SQ}_{Tot} = \mathrm{SQ}_{Reg} + \mathrm{SQ}_{Res}
$$

### 7.1 Soma de quadrados total

Mede a variação total observada em $y$:

$$
\mathrm{SQ}_{Tot} = \sum_{i=1}^{n}(y_i-\bar{y})^2
$$

### 7.2 Soma de quadrados da regressão

Mede a parte da variação de $y$ explicada pela reta:

$$
\mathrm{SQ}_{Reg} = \sum_{i=1}^{n}(\hat{y}_i-\bar{y})^2
$$

### 7.3 Soma de quadrados dos resíduos

Mede a parte da variação de $y$ que a reta não explicou:

$$
\mathrm{SQ}_{Res} = \sum_{i=1}^{n}(y_i-\hat{y}_i)^2
$$

Em termos de modelagem, queremos que $\mathrm{SQ}_{Reg}$ seja grande em relação a $\mathrm{SQ}_{Res}$, mas isso deve ser interpretado junto com o gráfico e os resíduos.

## 8. Coeficiente de determinação $R^2$

O coeficiente de determinação mede a proporção da variação de $y$ explicada pela regressão.

$$
R^2 = \frac{\mathrm{SQ}_{Reg}}{\mathrm{SQ}_{Tot}}
$$

Forma equivalente:

$$
R^2 = 1 - \frac{\mathrm{SQ}_{Res}}{\mathrm{SQ}_{Tot}}
$$

Na regressão linear simples com intercepto:

$$
R^2 = r^2
$$

Leitura:

| Valor de $R^2$ | Interpretação |
| ---: | --- |
| Próximo de 0 | A reta explica pouca variação de $y$ |
| Próximo de 1 | A reta explica grande parte da variação de $y$ |

Ponto crítico: $R^2$ alto não prova causalidade, não garante ausência de outliers e não substitui o gráfico de dispersão.

No Google Planilhas:

```text
=RSQ(intervalo_y; intervalo_x)
```

## 9. ANOVA da regressão

A ANOVA organiza a decomposição da variabilidade em uma tabela:

| Fonte | $\mathrm{SQ}$ | $\mathrm{gl}$ | $\mathrm{QM}$ | $F$ |
| --- | ---: | ---: | ---: | ---: |
| Regressão | $\mathrm{SQ}_{Reg}$ | $1$ | $\mathrm{QM}_{Reg} = \mathrm{SQ}_{Reg}/1$ | $F = \mathrm{QM}_{Reg}/\mathrm{QM}_{Res}$ |
| Resíduos | $\mathrm{SQ}_{Res}$ | $n-2$ | $\mathrm{QM}_{Res} = \mathrm{SQ}_{Res}/(n-2)$ |  |
| Total | $\mathrm{SQ}_{Tot}$ | $n-1$ |  |  |

Os graus de liberdade são:

$$
\mathrm{gl}_{Reg} = 1
$$

$$
\mathrm{gl}_{Res} = n - 2
$$

$$
\mathrm{gl}_{Tot} = n - 1
$$

Os quadrados médios são:

$$
\mathrm{QM}_{Reg} = \frac{\mathrm{SQ}_{Reg}}{\mathrm{gl}_{Reg}}
$$

$$
\mathrm{QM}_{Res} = \frac{\mathrm{SQ}_{Res}}{\mathrm{gl}_{Res}}
$$

A estatística $F$ é:

$$
F = \frac{\mathrm{QM}_{Reg}}{\mathrm{QM}_{Res}}
$$

Interpretação didática:

- $\mathrm{QM}_{Reg}$ representa a variação média explicada pela regressão;
- $\mathrm{QM}_{Res}$ representa a variação média não explicada;
- $F$ compara essas duas quantidades.

Se $F$ é grande, a variação explicada pela reta é grande em relação à variação residual. Neste material, a ANOVA está sendo usada principalmente para decompor a variabilidade e interpretar o ajuste, sem aprofundar teste formal de significância.

No Google Planilhas, a estatística $F$ pode ser obtida com:

```text
=INDEX(LINEST(intervalo_y; intervalo_x; TRUE; TRUE); 4; 1)
```

## 10. Funções estatísticas do Google Planilhas

| Função | O que calcula | Modelo |
| --- | --- | --- |
| `CORREL` | Correlação de Pearson $r$ | `=CORREL(intervalo_y; intervalo_x)` |
| `SLOPE` | Inclinação $b$ | `=SLOPE(intervalo_y; intervalo_x)` |
| `INTERCEPT` | Intercepto $a$ | `=INTERCEPT(intervalo_y; intervalo_x)` |
| `RSQ` | Coeficiente $R^2$ | `=RSQ(intervalo_y; intervalo_x)` |
| `LINEST` | Ajusta a regressão linear aos intervalos informados; o primeiro `TRUE` estima o intercepto e o segundo `TRUE` retorna a matriz completa de estatísticas da regressão. | `=LINEST(intervalo_y; intervalo_x; TRUE; TRUE)` |
| `INDEX` | Extrai um elemento de uma matriz | `=INDEX(matriz; linha; coluna)` |

Assim, a fórmula:

```text
=LINEST(intervalo_y; intervalo_x; TRUE; TRUE)
```

deve ser lida como: ajuste uma regressão linear usando todos os pares de dados presentes em `intervalo_y` e `intervalo_x`, estime a reta com intercepto e retorne a tabela completa de resultados da regressão.

Para obter $F$ via `LINEST`:

```text
=INDEX(LINEST(intervalo_y; intervalo_x; TRUE; TRUE); 4; 1)
```

## 11. Leitura computacional do modelo

Para estudantes de Ciência da Computação, a regressão linear simples pode ser entendida como um modelo paramétrico com dois parâmetros:

$$
\theta = (a, b)
$$

A função de predição é:

$$
f_\theta(x) = a + bx
$$

O erro de cada observação é:

$$
e_i = y_i - f_\theta(x_i)
$$

O ajuste por mínimos quadrados procura minimizar a soma dos erros quadráticos:

$$
\min_{a,b} \sum_{i=1}^{n}(y_i - (a + bx_i))^2
$$

Essa função objetivo é exatamente $\mathrm{SQ}_{Res}$. Portanto, a reta de regressão é aquela que minimiza a soma dos quadrados dos resíduos.

## 12. Valores atípicos/outliers

Um valor atípico/outlier é uma observação que foge do padrão geral dos dados e exige análise cuidadosa. Ele pode alterar fortemente:

- a correlação $r$;
- a inclinação $b$;
- o intercepto $a$;
- o $R^2$;
- a estatística $F$;
- a interpretação substantiva do modelo.

Regra importante: não se exclui um valor atípico/outlier apenas porque a remoção melhora o modelo. A exclusão precisa de justificativa substantiva, por exemplo erro de medição, erro de digitação, caso fora da população de interesse ou condição especial documentada.

## 13. Alertas metodológicos

- Correlação não implica causalidade.
- Regressão linear simples descreve associação média, não prova mecanismo causal.
- $R^2$ alto não garante que o modelo seja adequado.
- $R^2$ baixo não prova ausência de relação; pode haver relação não linear.
- A ANOVA ajuda a decompor a variabilidade, mas deve ser interpretada junto com gráfico e resíduos.
- O intercepto pode não ter interpretação prática quando $x=0$ está fora do domínio observado.
- A escala importa: em alguns problemas, interpretar $b$ por blocos de 10, 100 ou 1000 unidades de $x$ é mais claro do que interpretar por apenas 1 unidade.

## 14. Sequência recomendada de análise

1. Definir $x$ e $y$.
2. Observar o gráfico de dispersão.
3. Calcular $\bar{x}$, $\bar{y}$, $d_{x_i}$, $d_{y_i}$, $d_{x_i}^2$, $d_{y_i}^2$ e $d_{x_i}d_{y_i}$.
4. Calcular $r$.
5. Ajustar a reta $\hat{y}=a+bx$.
6. Calcular valores previstos $\hat{y}_i$.
7. Calcular resíduos $e_i$.
8. Fazer gráficos de diagnóstico: dispersão, reta ajustada, resíduos versus $\hat{y}$ e resíduos versus $x$.
9. Investigar valores atípicos/outliers.
10. Calcular $\mathrm{SQ}_{Tot}$, $\mathrm{SQ}_{Reg}$ e $\mathrm{SQ}_{Res}$.
11. Calcular $R^2$.
12. Montar a ANOVA com $\mathrm{SQ}$, $\mathrm{gl}$, $\mathrm{QM}$ e $F$.
13. Validar com funções do Google Planilhas.
14. Interpretar criticamente associação, ajuste, resíduos, $R^2$, ANOVA e valores atípicos/outliers.
