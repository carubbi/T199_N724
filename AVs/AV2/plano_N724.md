# Plano de Elaboração da AV2

## Resumo

Construir a AV2 como uma prova de **7,0 pontos**, seguindo o padrão da AV1: questões objetivas, 5 alternativas, feedback geral, feedback específico e gabarito final. O arquivo final da prova é `AVs/AV2/NT24_AV2.md`. A prova terá **3 problemas-base**, cada um com uma pequena base de dados e uma sequência de subitens que conduz da leitura do problema até a interpretação final.

A estrutura recomendada é:

| Problema | Tema | Valor | Subitens |
| --- | ---: | ---: | ---: |
| Problema 1 | Associação e regressão linear simples | 2,5 | 5 |
| Problema 2 | Probabilidade condicional, total e Bayes | 2,0 | 4 |
| Problema 3 | Variáveis aleatórias discretas por distribuição tabular | 2,5 | 5 |
| **Total** |  | **7,0** | **14** |

Cada subitem vale `0,5` ponto.

## Estratégia Das Questões

- Usar **bases pequenas**, resolvíveis manualmente e também reproduzíveis em notebook.
- Cada problema deve trazer a base bruta no enunciado, com notas da tabela discriminando as variáveis. Como a AV2 permite consulta ao material didático, planilha e notebook, a prova não deve fornecer somatórios intermediários que entreguem o procedimento.
- Priorizar **cálculo + interpretação estatística**. A prova não deve premiar resistência a álgebra longa; deve avaliar se o estudante escolhe o procedimento correto, organiza a informação, calcula e interpreta o resultado.
- Usar distratores rigorosos: cada alternativa incorreta deve representar um erro estatístico plausível, como troca entre `r` e `R2`, inversão de condicionais, uso de probabilidade marginal no lugar de conjunta, erro de suporte discreto, confusão entre variância e desvio-padrão ou interpretação causal indevida.
- Incluir uma seção de fórmulas por tema antes dos problemas, com fórmulas enumeradas por tags `F1`, `F2`, etc., sem lacunas, e com **Legenda** discriminando o que cada fórmula representa e o significado das variáveis.
- Cada sequência deve avaliar:
  - identificação do tipo de problema;
  - escolha da ferramenta estatística;
  - organização intermediária dos dados;
  - cálculo;
  - interpretação;
  - erro conceitual comum.

## Problema 1: Associação E Regressão

Usar como base o **Exercício 11.2.9** de Montgomery (2018), extraído em `AVs/AV2/montgomery2018_ch11_sec11_2.md`. O problema relaciona:

- `x = tempo (dias)`;
- `y = BOD (mg/liter)`.

A escolha é tecnicamente adequada para a AV2 porque a base tem `n = 11`, e é pequena o suficiente para resolução manual e notebook. O problema será uma **adaptação controlada** do exercício `11.2.9`: preserva ajuste da regressão linear simples, previsão para `x = 15`, interpretação da mudança média para aumento de `3` dias, valor ajustado e resíduo para `x = 6`, cálculo dos valores ajustados e avaliação se tempo é um regressor efetivo; remove a estimativa de `sigma^2` do item (a) e acrescenta `r`, `R2` e diagnóstico de ponto discrepante por resíduo padronizado.

Observação crítica: esta versão já não é reprodução literal do `11.2.9`. A alteração é didaticamente defensável porque `r`, `R2` e o diagnóstico de regressão reforçam a interpretação do ajuste. Dentro do escopo da AV2, o critério adotado para investigar ponto discrepante no ajuste será o resíduo padronizado. A prova não deve transformar esse diagnóstico em exclusão automática de observações.

Base a utilizar:

| Observação | `x` tempo (dias) | `y` BOD (mg/liter) |
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

1. Interpretar por que a ordem entre `x` e `y` importa na regressão, distinguindo correlação simétrica de reta ajustada, resíduos e interpretação da inclinação.
2. Ajustar ou interpretar a reta de regressão e estimar a correlação de Pearson `r`.
3. Calcular `R2` e interpretar a proporção da variação de BOD explicada pelo tempo.
4. Usar a reta para estimar o BOD em `x = 15`, interpretar a mudança esperada para aumento de `3` dias e calcular o resíduo em `x = 6`.
5. Avaliar a sensibilidade do modelo linear após a retirada do ponto `x = 14`, `y = 3,7`, identificado pelo critério `|z| > 2`, comparando reta ajustada, `r`, `R2` e interpretação da associação.

A prova deve deixar os dados brutos explícitos e permitir que os estudantes calculem manualmente, por planilha ou por notebook. O notebook pode validar os resultados com `pandas`, `numpy`, `statsmodels` ou equivalente.

Implementação avaliativa recomendada:

- Não fornecer somatórios como `Sxx`, `Syy` e `Sxy` no enunciado, pois a avaliação permite consulta, planilha e notebook.
- Informar no enunciado da questão de sensibilidade que o ponto `x = 14`, `y = 3,7` foi identificado como outlier pelo critério `|z| > 2`, sem exigir que o estudante refaça o diagnóstico formal.
- Usar a regra prática apenas como critério de investigação e sensibilidade do modelo: `|z| > 2` sugere ponto verticalmente discrepante. O foco avaliativo é comparar os resultados com e sem o ponto.
- Evitar ANOVA, testes de hipótese e gráficos diagnósticos adicionais, pois extrapolam o escopo definido para a AV2.

## Problema 2: Probabilidade Condicional

Usar como base o **Exercício 2.S26** de Montgomery (2018), catalogado em `AVs/AV2/montgomery2018_ch02_catalogo.md`. O problema envolve visitantes de um site, número de páginas vistas e solicitação de mais informação (`RMI`).

A escolha é tecnicamente melhor do que exercícios apenas com probabilidades dadas, porque traz uma base pequena tabulada, permite resolução manual e notebook, e contempla a sequência da revisão: eventos, probabilidade condicional, regra do produto, probabilidade total, Bayes, tabela de probabilidades conjuntas e erro de denominador. O enunciado deve preservar a ideia qualitativa de “maior propensão” e tratar a coluna `P(RMI | grupo)` como probabilidade condicional, não como mera tradução de “more likely”.

Base a utilizar:

| Páginas vistas | Proporção de visitantes | Probabilidade condicional de solicitar mais informação `P(RMI | grupo)` |
| --- | ---: | ---: |
| 1 | 40% | 10% |
| 2 | 30% | 10% |
| 3 | 20% | 20% |
| 4 ou mais | 10% | 40% |

Sequência dos 4 subitens:

1. Identificar o evento `RMI`, os grupos por páginas vistas e o universo de referência.
2. Montar ou completar a tabela de probabilidades conjuntas, calculando `P(grupo e RMI) = P(grupo) * P(RMI | grupo)`.
3. Calcular `P(RMI)` por probabilidade total, somando as probabilidades conjuntas dos grupos.
4. Aplicar Bayes para calcular `P(4 ou mais páginas | RMI)` e interpretar corretamente o denominador.

A questão deve combater explicitamente os erros de confundir `P(RMI | 4 ou mais páginas)` com `P(4 ou mais páginas | RMI)` e de combinar probabilidades condicionais sem ponderação pelos tamanhos dos grupos.

Implementação avaliativa recomendada:

- Apresentar a tabela original com `P(grupo)` e `P(RMI | grupo)`.
- Pedir que o estudante complete ou reconheça `P(grupo e RMI)`, `P(RMI)` e `P(4 ou mais páginas | RMI)`.
- Incluir distratores que usem denominador errado, confundam probabilidade condicional com conjunta, usem o complemento de `RMI` ou façam média simples das probabilidades condicionais.

## Problema 3: Variáveis Aleatórias Discretas

Usar como base o **Exercício 3.S30** de Montgomery (2018), catalogado em `AVs/AV2/montgomery2018_ch03_catalogo.md`. O problema traz uma distribuição discreta tabular pequena:

| `x` | 2 | 3 | 5 | 8 |
| ---: | ---: | ---: | ---: | ---: |
| `P(X = x)` | 0,2 | 0,4 | 0,3 | 0,1 |

A escolha é adequada para a AV2 porque tem base pequena, é resolvível manualmente e em notebook, e contempla diretamente função de probabilidade, probabilidades por intervalos, função acumulada, esperança e variância.

Sequência dos 5 subitens:

1. Reconhecer `X` como variável aleatória discreta e verificar que a função de probabilidade é válida.
2. Calcular probabilidades a partir da tabela, por exemplo `P(X <= 3)`, `P(X > 2,5)` ou `P(2,7 < X < 5,1)`.
3. Construir ou interpretar a função acumulada `F(x)`.
4. Calcular e interpretar `E(X)`.
5. Calcular e interpretar `Var(X)` e, se necessário, o desvio-padrão.

A prova deve fornecer a tabela da distribuição e exigir que o estudante calcule as quantidades necessárias manualmente, por planilha ou por notebook.

Implementação avaliativa recomendada:

- Fornecer a distribuição original, sem tabela auxiliar preenchida com `F(x)`, `xP(X=x)` ou `x^2P(X=x)`.
- Cobrar a validade da função de probabilidade antes dos cálculos de esperança e variância.
- Separar cálculo e interpretação: por exemplo, uma alternativa pode trazer o valor correto de `E(X)` mas interpretação incorreta como valor mais provável; outra pode trazer a variância correta, mas com unidade interpretada incorretamente.

## Critérios De Aceitação

- A AV2 deve ter exatamente **14 subitens objetivos**, cada um com 5 alternativas.
- A soma deve ser exatamente **7,0 pontos**.
- Cada problema deve ter uma pequena base de dados explícita.
- Cada problema deve ser resolvível manualmente e reproduzível em notebook.
- Cada subitem deve corresponder a uma etapa da sequência de análise.
- Cada questão deve conter `Feedback Geral` e `Feedback Específico`.
- O feedback específico deve comentar as alternativas `A` a `E`.
- O arquivo final deve terminar com `## Gabarito`.
- A prova deve conter seção de fórmulas por tema, com enumeração contínua das tags e legenda dos símbolos.
- A prova deve ser compatível com resolução manual, planilha e notebook, sem fornecer resultados intermediários que tornem a resposta mecânica.
- A AV2 deve avaliar variável aleatória discreta tabular no Problema 3, incluindo validade da função de probabilidade, função acumulada, esperança e variância.
- O Problema 1 deve usar resíduos padronizados para identificar ponto discrepante e avaliar a sensibilidade do modelo linear após a retirada do ponto informado.
- O Problema 2 deve usar tabela conjunta como estrutura central da resolução.
- As fontes dos exercícios devem aparecer ao final do enunciado de cada problema, no mesmo parágrafo.
- Todos os cálculos das alternativas e feedbacks devem ser validados numericamente antes da versão final.
