# Trabalho da Unidade 2 - Versão B

## Tema

Neste trabalho, cada dupla deverá aplicar conceitos de **associação estatística** e **probabilidade com variáveis aleatórias discretas** ao dataset completo `dataset/nba_stats_preprocessed.csv`.

O objetivo é investigar, no nível `jogador-temporada`, se há associação observacional entre **desempenho**, **uso em quadra**, **salário** e **não permanência observada no mesmo time** na temporada seguinte.

Diferentemente do T1, esta atividade não deve se limitar à descrição de uma equipe entre duas temporadas. O avanço esperado é usar medidas formais de associação e probabilidades no dataset completo.

## Pergunta de Pesquisa

**Há associação observacional entre baixo desempenho, baixa utilização em quadra e não permanência observada no mesmo time na temporada seguinte?**

## Conceitos Obrigatórios

A análise deve usar apenas o núcleo conceitual abaixo:

- covariância;
- correlação de Pearson;
- matriz ou heatmap de correlação;
- evento probabilístico;
- probabilidade condicional;
- variável aleatória discreta;
- distribuição empírica de probabilidade, incluindo PMF e CDF.

## Unidade de Análise

- Cada linha do dataset deve ser tratada como um caso `jogador-temporada`.
- A análise deve usar o dataset completo `nba_stats_preprocessed.csv`.
- As probabilidades devem ser interpretadas sobre casos `jogador-temporada`, e não sobre jogadores únicos.
- As associações observadas não devem ser interpretadas como causalidade.

## Variável de Resultado: Não Permanência Observada

A dupla deverá construir o evento:

$$
S = \text{jogador não permanece observado no mesmo time na temporada seguinte}
$$

Operacionalmente, para cada caso `jogador-temporada`, verifique se o mesmo `id_jogador` aparece no mesmo `sigla_time` na temporada seguinte.

- Se aparece no mesmo time na temporada seguinte: `nao_permanencia = False`.
- Se não aparece no mesmo time na temporada seguinte: `nao_permanencia = True`.
- Casos da última temporada disponível não devem entrar no cálculo de `nao_permanencia`, porque não há temporada seguinte observável.

Essa variável mede **não permanência observada no mesmo time**, não dispensa, venda, troca, aposentadoria ou fim de contrato.

## Variáveis Obrigatórias

Use obrigatoriamente:

- `pontos`;
- `minutos_totais`;
- `jogos_disputados`;
- `salario_usd`;
- `id_jogador`;
- `sigla_time`;
- temporada.

## Preparação dos Dados

A dupla deve:

- carregar o dataset completo;
- criar uma coluna identificadora `jogador_temporada`, combinando `id_jogador` e temporada;
- construir `nao_permanencia`;
- criar um subconjunto de análise para `nao_permanencia`, removendo apenas os casos sem temporada seguinte observável;
- criar os indicadores baixos usados em $X$;
- criar a variável aleatória discreta $X$;
- criar o evento `baixo_desempenho`, definido por $X \geq 2$.

A coluna `jogador_temporada` é apenas um identificador auxiliar. As análises continuam sendo feitas sobre casos `jogador-temporada`, isto é, sobre linhas do dataset.

## Parte 1: Associação Quantitativa

Usando `pontos`, `minutos_totais`, `jogos_disputados` e `salario_usd`, apresente:

- uma matriz ou heatmap de correlação;
- um gráfico de dispersão para um par de variáveis escolhido;
- a covariância desse par;
- a correlação de Pearson desse par;
- uma interpretação curta do sinal e da intensidade da associação.

A interpretação deve deixar claro que correlação indica associação linear, não causalidade.

## Parte 2: Variável Aleatória Discreta

A dupla deverá construir:

$$
X = \text{número de indicadores baixos observados no caso jogador-temporada}
$$

Use três indicadores:

- `pontos` no quartil inferior do dataset;
- `minutos_totais` no quartil inferior do dataset;
- `jogos_disputados` no quartil inferior do dataset.

Assim:

$$
X \in \{0,1,2,3\}
$$

Defina:

$$
B = (X \geq 2)
$$

em que $B$ representa baixo desempenho ou baixa utilização.

Para $X$, apresente:

- tabela com $P(X = x)$;
- tabela com $P(X \leq x)$;
- média;
- desvio padrão;
- interpretação substantiva dos valores de $X$.

## Parte 3: Associação Entre Eventos

Calcule:

$$
P(S \mid B)
$$

e compare com:

$$
P(S \mid \neg B)
$$

Também apresente a diferença:

$$
P(S \mid B) - P(S \mid \neg B)
$$

A interpretação deve responder diretamente à pergunta de pesquisa:

> A não permanência observada no mesmo time é mais frequente entre casos classificados como baixo desempenho ou baixa utilização?

Use linguagem associativa. Não afirme que o jogador saiu **por causa** do baixo desempenho, da baixa utilização ou do salário.

## Conclusão

A conclusão deve ter de 8 a 12 linhas e integrar:

- o que a correlação sugere sobre desempenho, uso em quadra e salário;
- o que $X$ mostra sobre o perfil de baixo desempenho ou baixa utilização;
- o que $P(S \mid B)$ e $P(S \mid \neg B)$ sugerem sobre não permanência observada;
- as principais limitações da análise.

## Entrega

Cada dupla deverá entregar:

- um notebook documentado, executável e com interpretações curtas;
- um vídeo explicativo com síntese dos resultados e das limitações.

## Estrutura Mínima do Notebook

- identificação da dupla;
- pergunta de pesquisa;
- carregamento do dataset;
- criação de `jogador_temporada`;
- construção de `nao_permanencia`;
- associação quantitativa com correlação/covariância;
- construção e distribuição de $X$;
- cálculo de $P(S \mid B)$ e $P(S \mid \neg B)$;
- conclusão.

## Cronograma

- **04/05/2026 - Apresentação do trabalho e preparação dos dados.** Apresentação do enunciado, da pergunta de pesquisa, das variáveis obrigatórias, da estrutura mínima do notebook e dos critérios de avaliação. Início da preparação dos dados, incluindo carregamento do dataset, criação de `jogador_temporada` e organização das colunas necessárias.
- **06/05/2026 - Associação quantitativa.** A dupla deverá concluir a análise com correlação/covariância, matriz ou heatmap e interpretação da associação entre `pontos`, `minutos_totais`, `jogos_disputados` e `salario_usd`.
- **11/05/2026 - Probabilidade e variável aleatória discreta.** A dupla deverá concluir a construção de $X$, PMF, CDF, média, desvio padrão e comparação entre $P(S \mid B)$ e $P(S \mid \neg B)$.
- **13/05/2026 - Revisão para AV2.** Revisão dos conceitos centrais da Unidade 2 e esclarecimento de dúvidas finais.
- **18/05/2026 - AV2.** Avaliação da Unidade 2.

## Critérios de Avaliação

O trabalho vale **3,0 pontos**.

### Notebook (1,0 ponto)

- **Preparação dos dados (0,20 ponto):** carregamento, `jogador_temporada`, `nao_permanencia` e tratamento da última temporada.
- **Associação quantitativa (0,20 ponto):** matriz ou heatmap, dispersão, covariância, correlação e interpretação.
- **Variável aleatória discreta $X$ (0,20 ponto):** construção dos indicadores baixos, PMF, CDF, média, desvio padrão e interpretação.
- **Probabilidade condicional (0,20 ponto):** cálculo e comparação de $P(S \mid B)$ e $P(S \mid \neg B)$.
- **Clareza e conclusão (0,20 ponto):** código executável, organização, interpretação e conclusão sem causalidade.

### Apresentação (2,0 pontos)

- **Síntese dos resultados (0,60 ponto):** apresentação objetiva dos principais achados.
- **Interpretação estatística (0,80 ponto):** explicação correta de associação, $X$ e probabilidades condicionais.
- **Limitações e rigor conceitual (0,40 ponto):** ausência de causalidade e uso correto de “não permanência observada”.
- **Participação e domínio (0,20 ponto):** todos os integrantes devem participar e demonstrar domínio do notebook.

## Observação Final

O foco do trabalho é aprender a transformar uma pergunta observacional em evidências estatísticas simples: associação entre variáveis quantitativas, construção de uma variável aleatória discreta e comparação de probabilidades condicionais. A análise pode sugerir associação, mas não permite concluir motivo de saída, dispensa, venda ou troca de jogadores.
