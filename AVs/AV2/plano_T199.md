# Plano de Elaboração da AV2 - T199

## Resumo

Construir a AV2 da turma **T199 - Ciência da Computação** como uma prova de **7,0 pontos**, seguindo o padrão da AV1: questões objetivas, 5 alternativas, feedback geral, feedback específico e gabarito final. O arquivo final da prova é `AVs/AV2/T199_AV2.md`.

A prova terá **3 problemas-base**, cada um com pequena base de dados explícita, resolvível manualmente e também por planilha ou notebook.

| Problema | Tema | Valor | Subitens |
| --- | ---: | ---: | ---: |
| Problema 1 | Medidas de associação | 2,5 | 5 |
| Problema 2 | Probabilidade condicional, probabilidade total e Bayes | 2,0 | 4 |
| Problema 3 | Variáveis aleatórias discretas por distribuição tabular | 2,5 | 5 |
| **Total** |  | **7,0** | **14** |

Cada subitem vale `0,5` ponto.

## Restrição Didática Central

Na turma T199, **regressão linear simples não foi abordada**. Portanto, o Problema 1 deve permanecer estritamente no escopo de **medidas de associação**, conforme os conceitos trabalhados em `aulas/notebooks/5_MA.ipynb` e nas resoluções manuais em `aulas/resolucoes_manuais`.

Não devem ser avaliados:

- reta ajustada;
- modelo linear;
- previsão por regressão;
- valor ajustado;
- resíduo;
- inclinação;
- intercepto;
- `R2` ou coeficiente de determinação;
- ANOVA;
- diagnóstico de regressão.

O uso de “associação linear” é aceitável apenas no sentido do **coeficiente de Pearson** (`r`), não como modelo de regressão.

## Estratégia Das Questões

- Usar **bases pequenas**, resolvíveis manualmente e reproduzíveis em notebook.
- Cada problema deve apresentar a base bruta no enunciado, com notas da tabela discriminando as variáveis.
- A prova permite consulta, planilha e notebook; portanto, não deve fornecer somatórios intermediários que tornem a resposta mecânica.
- Priorizar **cálculo + interpretação estatística**, com distratores que representem erros plausíveis.
- Usar o padrão `termo ($símbolo$)` nos enunciados, alternativas e feedbacks quando houver variável ou medida estatística, por exemplo: tempo ($x$), BOD ($y$), covariância amostral ($s_{xy}$), coeficiente de Pearson ($r$).
- Incluir seção de fórmulas por tema, com tags contínuas `F1`, `F2`, etc., e **Legenda** explicando o que cada fórmula representa.
- Usar fontes como adaptação quando houver reestruturação didática: `Fonte: Adaptado de Montgomery (2018), Exercício ...`.

## Problema 1: Medidas De Associação

Usar como base o **Exercício 11.2.9** de Montgomery (2018), extraído em `AVs/AV2/montgomery2018_ch11_sec11_2.md`.

Embora o exercício original seja de regressão, na T199 ele deve ser tratado como uma **adaptação para medidas de associação**, usando apenas a base de pares observados:

- tempo ($x$), em dias;
- BOD ($y$), em mg/liter.

Base a utilizar:

| Observação | Tempo ($x$) em dias | BOD ($y$) em mg/liter |
| ---: | ---: | ---: |
| 1 | 1 | 0,6 |
| 2 | 2 | 0,7 |
| 3 | 4 | 1,5 |
| 4 | 6 | 1,9 |
| 5 | 8 | 2,1 |
| 6 | 10 | 2,6 |
| 7 | 12 | 2,9 |
| 8 | 14 | 3,7 |
| 9 | 16 | 3,5 |
| 10 | 18 | 3,7 |
| 11 | 20 | 3,8 |

Sequência dos 5 subitens:

1. Avaliar a etapa inicial por gráfico de dispersão entre tempo ($x$) e BOD ($y$): tipo das variáveis, direção visual, intensidade visual, possíveis pontos discrepantes e ausência de conclusão causal.
2. Calcular e interpretar a covariância amostral ($s_{xy}$), destacando sinal, variação conjunta e dependência das unidades.
3. Calcular e interpretar o coeficiente de Pearson ($r$), destacando direção, intensidade e ausência de causalidade.
4. Comparar covariância amostral ($s_{xy}$) e correlação de Pearson ($r$), enfatizando a padronização por desvios-padrão amostrais ($s_x$ e $s_y$).
5. Avaliar a sensibilidade da associação linear ao remover o ponto $x=14$, $y=3,7$, recalculando apenas o coeficiente de Pearson ($r$).

Implementação avaliativa recomendada:

- Não usar regressão nem termos associados a regressão.
- Não usar `R2`, coeficiente de determinação ou previsão.
- Não transformar a retirada do ponto em regra automática; o foco é a sensibilidade do coeficiente de Pearson ($r$).
- Usar distratores que confundam covariância com correlação, errem o divisor `n` versus `n-1`, invertam o sinal, atribuam causalidade ou confundam valor de covariância com `r`.

## Problema 2: Probabilidade Condicional

Usar como base o **Exercício 2.S26** de Montgomery (2018), catalogado em `AVs/AV2/montgomery2018_ch02_catalogo.md`. O problema envolve visitantes de um site, número de páginas vistas e solicitação de mais informação (`RMI`).

A escolha é adequada para a T199 porque usa tabela pequena, contexto próximo da área de Computação e permite trabalhar eventos, condicionais, probabilidade total e Bayes sem exigir base extensa.

Base a utilizar:

| Páginas vistas | Proporção de visitantes | Probabilidade condicional de solicitar mais informação `P(RMI | grupo)` |
| --- | ---: | ---: |
| 1 | 40% | 10% |
| 2 | 30% | 10% |
| 3 | 20% | 20% |
| 4 ou mais | 10% | 40% |

Sequência dos 4 subitens:

1. Identificar o evento `RMI`, os grupos por páginas vistas e o universo condicionado.
2. Calcular as probabilidades conjuntas `P(grupo e RMI)`.
3. Calcular `P(RMI)` por probabilidade total.
4. Calcular `P(4 ou mais páginas | RMI)` por Bayes e interpretar corretamente o denominador.

Implementação avaliativa recomendada:

- Preservar a ideia de maior propensão a solicitar informação como probabilidade condicional, não como percentual absoluto isolado.
- Incluir distratores que invertam condicionais, usem probabilidade marginal no lugar de condicional, somem condicionais sem ponderação ou confundam complemento.

## Problema 3: Variáveis Aleatórias Discretas

Usar como base o **Exercício 3.S30** de Montgomery (2018), catalogado em `AVs/AV2/montgomery2018_ch03_catalogo.md`. O problema traz uma distribuição discreta tabular pequena:

| `x` | 2 | 3 | 5 | 8 |
| ---: | ---: | ---: | ---: | ---: |
| `P(X = x)` | 0,2 | 0,4 | 0,3 | 0,1 |

A escolha é adequada porque contempla diretamente função de probabilidade, suporte discreto, probabilidades por eventos, função acumulada, esperança e variância.

Sequência dos 5 subitens:

1. Verificar validade da função de probabilidade e reconhecer que o suporte não precisa ser consecutivo.
2. Calcular probabilidades de eventos a partir da tabela.
3. Construir ou interpretar a função acumulada `F(x)`.
4. Calcular e interpretar `E(X)`.
5. Calcular e interpretar `Var(X)` e distinguir variância de desvio-padrão.

Implementação avaliativa recomendada:

- Fornecer apenas a distribuição original, sem tabela auxiliar com acumuladas ou produtos `xP(X=x)` e `x^2P(X=x)`.
- Usar distratores que confundam suporte com intervalo contínuo, média simples com esperança, valor mais provável com esperança, `E(X^2)` com variância e desvio-padrão com variância.

## Critérios De Aceitação

- A AV2 da T199 deve ter exatamente **14 questões objetivas**, cada uma com 5 alternativas.
- A soma deve ser exatamente **7,0 pontos**.
- Cada problema deve ter pequena base de dados explícita.
- Cada problema deve ser resolvível manualmente e reproduzível em planilha ou notebook.
- Cada questão deve conter `Feedback Geral` e `Feedback Específico`.
- O feedback específico deve comentar as alternativas `A` a `E`.
- O arquivo final deve terminar com `## Gabarito`.
- As fontes devem aparecer ao final do enunciado de cada problema, no mesmo parágrafo.
- As fontes adaptadas devem usar o padrão `Fonte: Adaptado de Montgomery (2018), Exercício ...`.
- O Problema 1 deve permanecer como medidas de associação, sem regressão linear simples.
- O gabarito da prova e o arquivo de respostas devem coincidir.
- Todos os cálculos das alternativas e feedbacks devem ser validados numericamente.
- Não deve haver ocorrências avaliativas de regressão, `R2`, coeficiente de determinação, reta ajustada, resíduo, inclinação, intercepto, ANOVA ou modelo linear na T199.
