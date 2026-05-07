# Revisão Pearson, Regressão Linear Simples e ANOVA - N724

## Resumo
Gerar `aulas/planilhas/revisao_pearson_regressao_N724.xlsx`, compatível com Google Planilhas, usando `.venv/bin/python` e `openpyxl`.

A planilha terá 3 abas e seguirá uma sequência didática completa: conceito, cálculo manual por somatórios, validação com funções prontas, interpretação crítica e ANOVA da regressão.

Exercícios selecionados:
- **Ex 1: `2.5_P - Peso versus altura`**: correlação, regressão e efeito de ponto influente.
- **Ex 2: `2.6_P - Alunos e professores em universidades brasileiras`**: regressão em escala real, interpretação da inclinação, `R²` e ANOVA.

## Estrutura Da Planilha
- **`Revisao conceitual`**
  - Explicar a sequência metodológica:
    1. definir variável explicativa `x` e variável resposta `y`;
    2. observar o diagrama de dispersão;
    3. calcular médias;
    4. calcular desvios;
    5. calcular somatórios;
    6. calcular correlação de Pearson;
    7. ajustar a reta;
    8. calcular valores previstos e resíduos;
    9. decompor a variabilidade via ANOVA;
    10. validar com funções prontas;
    11. interpretar criticamente.
  - Discriminar os símbolos das fórmulas:
    - `x_i`, `y_i`, `n`, `x̄`, `ȳ`, `x_i - x̄`, `y_i - ȳ`;
    - `r`: correlação de Pearson;
    - `a`: intercepto;
    - `b`: inclinação;
    - `ŷ_i`: valor previsto;
    - `e_i = y_i - ŷ_i`: resíduo;
    - `R²`: coeficiente de determinação.
  - Contextualizar:
    - Ex 1: `x = altura`, `y = peso`;
    - Ex 2: `x = alunos`, `y = professores`.
  - Incluir fórmulas:
    - Pearson: `r = Σ[(x_i-x̄)(y_i-ȳ)] / sqrt(Σ(x_i-x̄)² * Σ(y_i-ȳ)²)`;
    - Regressão: `ŷ = a + bx`;
    - Inclinação: `b = Σ[(x_i-x̄)(y_i-ȳ)] / Σ(x_i-x̄)²`;
    - Intercepto: `a = ȳ - bx̄`;
    - Resíduo: `e_i = y_i - ŷ_i`;
    - `R² = r²` em regressão linear simples com intercepto.
  - Incluir ANOVA da regressão:
    - `SQTot = Σ(y_i - ȳ)²`;
    - `SQReg = Σ(ŷ_i - ȳ)²`;
    - `SQRes = Σ(y_i - ŷ_i)²`;
    - `SQTot = SQReg + SQRes`;
    - `R² = SQReg / SQTot = 1 - SQRes / SQTot`;
    - `glReg = 1`, `glRes = n - 2`, `glTot = n - 1`;
    - `QMReg = SQReg / glReg`;
    - `QMRes = SQRes / glRes`;
    - `F = QMReg / QMRes`;
    - `p-valor = F.DIST.RT(F; glReg; glRes)`.
  - Alertas:
    - correlação não implica causalidade;
    - `r` mede associação linear;
    - `R²` alto não garante modelo adequado;
    - ANOVA testa evidência de inclinação diferente de zero, não prova causalidade;
    - ponto influente não deve ser excluído automaticamente;
    - intercepto pode não ter interpretação substantiva quando `x = 0` não faz sentido.

- **`Ex 1 e resolucao`**
  - Inserir dados de altura e peso do exercício `2.5_P`.
  - Incluir perguntas orientadoras sobre variável explicativa, variável resposta, direção da associação e influência de Silvio.
  - Cálculo manual com todos os casos:
    - médias;
    - desvios;
    - produto dos desvios;
    - quadrados dos desvios;
    - somatórios;
    - `r`, `b`, `a`, `ŷ`, resíduos, `R²`;
    - tabela ANOVA com `SQReg`, `SQRes`, `SQTot`, graus de liberdade, quadrados médios, `F` e p-valor.
  - Repetir o núcleo do cálculo sem Silvio:
    - `r`, `b`, `a`, `R²` e interpretação comparativa.
  - Validação com funções prontas:
    - `CORREL`, `SLOPE`, `INTERCEPT`, `RSQ`, `F.DIST.RT`.
  - Valores de referência:
    - todos: `r ≈ 0,403`, `peso = -78,742 + 86,325*altura`;
    - sem Silvio: `r ≈ 0,903`, `peso = -113,149 + 101,350*altura`.
  - Incluir gráfico de dispersão com Silvio destacado.

- **`Ex 2 e resolucao`**
  - Inserir dados de alunos e professores do exercício `2.6_P`.
  - Incluir perguntas orientadoras sobre linearidade, escala, pontos influentes e interpretação da inclinação.
  - Cálculo manual:
    - médias;
    - desvios;
    - produto dos desvios;
    - quadrados dos desvios;
    - somatórios;
    - `r`, `b`, `a`, `ŷ`, resíduos, `R²`;
    - tabela ANOVA completa.
  - Validação com funções prontas:
    - `CORREL`, `SLOPE`, `INTERCEPT`, `RSQ`, `F.DIST.RT`.
  - Valores de referência:
    - `r ≈ 0,837`;
    - `professores = 89,546 + 0,08748*alunos`;
    - interpretação: cada `1000` alunos adicionais estão associados a cerca de `87,5` professores adicionais.
  - Incluir gráfico de dispersão com reta de tendência.

## Implementação
- Usar fórmulas aritméticas nas seções manuais, sem funções estatísticas prontas.
- Usar funções prontas apenas nos blocos de validação.
- Separar visualmente: dados, observação inicial, cálculo manual, ANOVA, validação e interpretação.
- Aplicar formatação básica: títulos, cabeçalhos, larguras ajustadas, congelamento de linha, casas decimais coerentes e cores distintas para cálculo manual, ANOVA e validação.

## Testes
- Confirmar criação de `aulas/planilhas/revisao_pearson_regressao_N724.xlsx`.
- Confirmar exatamente 3 abas:
  - `Revisao conceitual`;
  - `Ex 1 e resolucao`;
  - `Ex 2 e resolucao`.
- Confirmar número de observações:
  - Ex 1: 8;
  - Ex 2: 31.
- Conferir se os cálculos manuais batem com as funções prontas.
- Conferir se `SQTot = SQReg + SQRes`, salvo diferenças pequenas de arredondamento.
- Conferir se `R² = r²` nos dois exercícios.
- Abrir o arquivo com `openpyxl` após salvar para verificar integridade.

## Assumptions
- “Cálculo manual” significa cálculo por somatórios e operações aritméticas básicas, não ausência total de fórmulas de célula.
- ANOVA será incluída de forma enxuta, vinculada a variabilidade explicada, resíduos, `R²` e teste global da regressão.
- A revisão deve ensinar processo estatístico e interpretação, não apenas gerar respostas numéricas.
