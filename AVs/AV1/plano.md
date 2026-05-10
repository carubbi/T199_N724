# Prova Modelo ENADE de Métodos Quantitativos

## Resumo

Elaborar e manter a prova em [av1.md](/Users/carubbi/Documents/aulas/T199_prof/AVs/av1/av1.md) com **10 questões objetivas**, totalizando **7,0 pontos**, para turmas de **Ciência da Computação e Engenharias afins**, em nível próximo ao **ENADE padrão**.

O foco permanece em **estatística descritiva**, com **análise visual bivariada não formal** permitida, como leitura de gráficos de dispersão. Continuam fora de escopo **correlações formais**, como **Pearson**, além de regressão e inferência estatística.

## Fontes e Critério de Uso

- Adotar como **fontes principais** os documentos nas pastas:
  - `exs/und1/`
  - `apostilas/`
- Usar `exs/und1/` como base principal estruturada para:
  - seleção de exercícios;
  - identificação de tópicos;
  - reaproveitamento de tabelas;
  - reaproveitamento de imagens existentes.
- Usar `apostilas/` como base principal complementar para:
  - seleção de questões e exemplos;
  - OCR de trechos ainda não estruturados;
  - recorte de imagens;
  - validação didática e temática.
- Usar `livros/` apenas como apoio secundário de conferência.
- Assumir que os pacotes para OCR e manipulação de imagem já estão instalados no ambiente **`.venv`**.

## Estrutura da Prova

- Manter **10 itens de múltipla escolha**, com **5 alternativas** por questão.
- Manter pontuação em incrementos de **0,5 ponto**, totalizando **7,0 pontos**.
- Preservar contextos compatíveis com Computação e Engenharias, com explicações curtas de termos técnicos quando necessário.
- Manter tabelas em **Markdown**.
- Manter inserção obrigatória de imagens associadas aos itens selecionados.
- Usar e armazenar imagens em [imgs](/Users/carubbi/Documents/aulas/T199_prof/AVs/av1/imgs).

## Estrutura de Feedback e Gabarito

- Cada questão deve conter suas próprias seções:
  - `Feedback Geral`
  - `Feedback Específico`
- O `Feedback Geral` de cada questão deve concentrar:
  - explicação conceitual;
  - interpretação estatística;
  - orientação teórica e prática para resolver o item.
- O `Feedback Específico` de cada questão deve explicar, de forma **curta e objetiva**, cada alternativa `A` a `E`.
- Incluir ao final uma seção única `Gabarito` com a alternativa correta de cada questão.
- Não usar mais seções globais de `Feedback Geral` e `Feedback Específico` para a prova inteira.

## Ajustes Específicos Já Incorporados

- Q6: manter a imagem sem os rótulos que entregavam diretamente a resposta.
- Q3: incluir o **desvio-padrão** entre os elementos cobrados na alternativa correta e nos distratores.
- Q3: remover o termo `aproximado` das alternativas referentes ao desvio-padrão.
- Q1: manter coerência entre o enunciado e a imagem usada.

## Teste de Aceitação

- Confirmar que há exatamente **10 questões objetivas** com **5 alternativas** cada.
- Confirmar que a soma da pontuação é **7,0 pontos**.
- Confirmar que cada questão possui:
  - `Feedback Geral`
  - `Feedback Específico`
- Confirmar que o `Feedback Específico` explica todas as alternativas `A` a `E`.
- Confirmar presença de `## Gabarito` ao final.
- Confirmar que todas as tabelas estão em Markdown.
- Confirmar que as imagens usadas estão corretamente referenciadas em [imgs](/Users/carubbi/Documents/aulas/T199_prof/AVs/av1/imgs).
- Confirmar ausência de correlação formal, regressão e inferência estatística.
- Confirmar que a análise bivariada, quando presente, é apenas visual e descritiva.

## Premissas Adotadas

- O arquivo principal permanece [av1.md](/Users/carubbi/Documents/aulas/T199_prof/AVs/av1/av1.md).
- As pastas `exs/und1/` e `apostilas/` seguem como base principal.
- O estilo ENADE é aproximado por contextualização, interpretação e qualidade dos distratores, não por reprodução literal de prova oficial.
