# Plano Atualizado Para Geração AVA/XML Da AV2

## Resumo

Gerar `AVs/AV2/plano_AVA.md` como plano técnico para converter as provas Markdown da AV2 em XML Moodle/AVA, seguindo o padrão estrutural de `AVs/AV1/av1.xml`.

Arquivos de entrada:

- Engenharia/N724: `AVs/AV2/NT24_AV2.md`
- Ciência da Computação/T199: `AVs/AV2/T199_AV2.md`

Arquivos de saída:

- `AVs/AV2/N724_AV2_AVA.xml`
- `AVs/AV2/T199_AV2_AVA.xml`

Execução prevista:

- Executar o processo **uma vez para cada prova**.
- Primeiro gerar e validar `N724_AV2_AVA.xml`.
- Depois gerar e validar `T199_AV2_AVA.xml`.
- Cada XML será importado na respectiva disciplina no AVA; portanto, a categoria comum `$course$/AV2` é adequada e não deve ser subdividida por turma.

## Estrutura XML

- Usar `<quiz>` como raiz.
- Criar categoria do banco de questões:
  - `<question type="category">`
  - `<text>$course$/AV2</text>`
- Manter a categoria `$course$/AV2` nos dois XMLs, pois cada arquivo será importado separadamente na disciplina correspondente.
- Criar uma questão inicial do tipo `description` em cada XML:
  - nome: `00 - Fórmulas`
  - conteúdo: apenas o bloco de fórmulas da respectiva prova.
- Usar título HTML interno `<h2>Fórmulas da AV2</h2>` na página inicial.
- Converter como página inicial da avaliação o trecho:
  - de `## Fórmulas`
  - até imediatamente antes de `## Problema 1`
- Criar uma questão `description` para cada problema:
  - `01 - Problema 1`
  - `02 - Problema 2`
  - `03 - Problema 3`
- Cada descrição de problema deve conter o enunciado completo do problema, a fonte, a tabela/base de dados e as notas da tabela.
- Cada descrição de problema deve ser inserida imediatamente antes das questões correspondentes.
- Estrutura esperada no XML:
  - `00 - Fórmulas`
  - `01 - Problema 1`
  - `N724 Q01` a `N724 Q05` ou `T199 Q01` a `T199 Q05`
  - `02 - Problema 2`
  - `N724 Q06` a `N724 Q09` ou `T199 Q06` a `T199 Q09`
  - `03 - Problema 3`
  - `N724 Q10` a `N724 Q14` ou `T199 Q10` a `T199 Q14`
- Não incluir o gabarito na página inicial.
- Não incluir respostas comentadas no XML da prova.

## Conversão Das Questões

- Converter cada `### Questão N (0,5 ponto)` em `<question type="multichoice">`.
- Nomear as questões com prefixo da turma:
  - `N724 Q01`, `N724 Q02`, ...
  - `T199 Q01`, `T199 Q02`, ...
- Converter enunciado, tabelas e expressões matemáticas para HTML dentro de `<questiontext format="html">`.
- Converter `Feedback Geral` para `<generalfeedback format="html">`.
- Converter alternativas `A` a `E` em `<answer>`.
- Permitir que o AVA randomize as posições das alternativas usando configuração de embaralhamento no XML.
- Remover os prefixos `A.`, `B.`, `C.`, `D.` e `E.` do texto das alternativas no XML, pois o AVA gerará a numeração/letra das alternativas após o embaralhamento.
- Usar as letras `A` a `E` apenas internamente para mapear alternativa, gabarito e feedback específico.
- Cada questão deve ter exatamente uma alternativa correta:
  - alternativa correta com `fraction="100"`;
  - alternativas incorretas com `fraction="0"`.
- Cada questão deve valer `0,5` ponto.
- A prova deve totalizar `7,0` pontos com `14` questões objetivas.
- Converter o feedback específico de cada alternativa para o `<feedback>` da respectiva alternativa.
- O feedback específico deve acompanhar a alternativa original mesmo após a remoção da letra e o embaralhamento no AVA.
- As questões não devem repetir o enunciado completo do problema nem a tabela/base de dados, pois esses elementos ficarão na questão `description` imediatamente anterior ao bloco.
- As questões devem conter apenas o enunciado específico da questão, alternativas, feedback geral e feedback específico.
- A ordem das questões no AVA deve permanecer fixa para preservar a relação entre cada descrição de problema e suas questões.
- Apenas as alternativas devem ser embaralhadas.

## Tags Moodle Obrigatórias

Cada questão do tipo `description` deve conter:

- `<defaultgrade>0.0000000</defaultgrade>`
- `<penalty>0.0000000</penalty>`
- `<hidden>0</hidden>`
- `<idnumber />`

Cada questão de múltipla escolha deve conter:

- `<defaultgrade>0.5000000</defaultgrade>`
- `<penalty>0.3333333</penalty>`
- `<hidden>0</hidden>`
- `<single>true</single>`
- `<shuffleanswers>true</shuffleanswers>`
- `<answernumbering>abc</answernumbering>`
- `<showstandardinstruction>0</showstandardinstruction>`
- `<correctfeedback format="html"><text>Resposta correta.</text></correctfeedback>`
- `<partiallycorrectfeedback format="html"><text /></partiallycorrectfeedback>`
- `<incorrectfeedback format="html"><text>Resposta incorreta.</text></incorrectfeedback>`

## Regras De Renderização E Conversão Segura

- Converter LaTeX inline delimitado por `$...$` para `\(...\)` antes de inserir no XML.
- Converter LaTeX em bloco delimitado por `$$...$$` para `\[...\]` antes de inserir no XML.
- Preservar comandos LaTeX usados nas provas, como `\frac`, `\sum`, `\operatorname`, `\binom`, `\lambda`, `\le`, `\mid`, `\cap`, `\cup` e `\tag`.
- Manter `\tag{F1}`, `\tag{F2}`, etc. nas fórmulas, mas validar visualmente a renderização da página de fórmulas após importação no AVA.
- Gerar o XML com serializador XML, por exemplo `xml.etree.ElementTree`, e não por concatenação manual de strings.
- Garantir escape correto de caracteres especiais em XML, especialmente `<`, `>`, `&`, aspas e expressões como `2,7<X<5,1`.
- Converter tabelas Markdown para HTML com `<table>`, `<thead>`, `<tbody>`, `<tr>`, `<th>` e `<td>`, preservando alinhamento e conteúdo matemático.
- Preservar negrito, itálico, listas e parágrafos em HTML.
- Não usar CDATA como substituto para escape sistemático; o XML final deve ser bem formado e compatível com importação Moodle.

## Regras Específicas Por Turma

- `N724_AV2_AVA.xml` pode conter regressão linear simples, reta ajustada, resíduos, \(R^2\) e análise de sensibilidade do modelo.
- `T199_AV2_AVA.xml` deve permanecer restrito a medidas de associação no Problema 1.
- No XML da T199, não deve haver uso avaliativo de:
  - regressão;
  - \(R^2\);
  - coeficiente de determinação;
  - reta ajustada;
  - resíduos;
  - inclinação;
  - intercepto;
  - ANOVA;
  - modelo linear.

## Implementação Recomendada

- Criar um script de conversão, por exemplo `AVs/AV2/gerar_xml_ava.py`.
- O script deve receber uma configuração por prova:
  - arquivo Markdown de entrada;
  - arquivo XML de saída;
  - prefixo das questões;
  - categoria Moodle `$course$/AV2`.
- O parser deve identificar:
  - bloco de fórmulas;
  - problemas;
  - questões;
  - alternativas;
  - feedback geral;
  - feedback específico;
  - gabarito.
- O parser deve separar cada problema em duas partes:
  - descrição do problema: de `## Problema N` até antes da primeira `### Questão`;
  - questões do problema: de cada `### Questão` até antes da próxima questão ou próximo problema.
- O script deve gerar questões `description` para o bloco de fórmulas e para cada um dos três problemas.
- O script deve validar antes de gerar o XML final:
  - 14 questões objetivas;
  - 4 questões do tipo `description`: fórmulas, Problema 1, Problema 2 e Problema 3;
  - 5 alternativas por questão;
  - exatamente 1 correta por questão;
  - alternativa correta com fração `100%`;
  - alternativas incorretas com fração `0%`;
  - pontuação `0,5` por questão;
  - total da prova igual a `7,0` pontos;
  - embaralhamento de alternativas habilitado;
  - feedback geral presente em todas as questões;
  - feedback específico para alternativas `A` a `E`;
  - gabarito do XML igual ao gabarito do Markdown.
- O script deve falhar com erro explícito se:
  - uma questão tiver menos ou mais de 5 alternativas;
  - uma questão tiver mais de uma alternativa com `fraction="100"`;
  - alguma alternativa não tiver feedback específico;
  - algum bloco LaTeX estiver com delimitador aberto;
  - o gabarito final não contiver exatamente 14 entradas;
  - houver texto de alternativa ainda iniciado por `A.`, `B.`, `C.`, `D.` ou `E.` no XML.
  - uma questão depender de tabela/base de dados sem haver uma descrição de problema imediatamente anterior no XML.
- Usar `AVs/AV1/av1.xml` como referência de tags Moodle, não como fonte de conteúdo.

## Testes E Aceitação

- Validar que ambos os XMLs são bem formados.
- Confirmar que a categoria dos dois XMLs é `$course$/AV2`.
- Confirmar que a primeira questão de cada XML é `description` com o bloco de fórmulas da prova correspondente.
- Confirmar que cada XML contém quatro questões do tipo `description`: fórmulas, Problema 1, Problema 2 e Problema 3.
- Confirmar que cada descrição de problema aparece imediatamente antes das questões correspondentes.
- Confirmar a ordem dos blocos:
  - fórmulas;
  - Problema 1 + Q01 a Q05;
  - Problema 2 + Q06 a Q09;
  - Problema 3 + Q10 a Q14.
- Confirmar que `N724_AV2_AVA.xml` contém 14 questões de múltipla escolha após a página de fórmulas.
- Confirmar que `T199_AV2_AVA.xml` contém 14 questões de múltipla escolha após a página de fórmulas.
- Confirmar que cada questão tem pontuação `0,5`.
- Confirmar que a soma das questões é `7,0`.
- Confirmar que cada questão possui apenas uma alternativa verdadeira, com fração `100%`.
- Confirmar que todas as demais alternativas possuem fração `0%`.
- Confirmar que o embaralhamento das alternativas está habilitado.
- Confirmar que a ordem das questões deve ser mantida fixa na configuração do quiz no AVA.
- Confirmar que apenas as alternativas são embaralhadas.
- Confirmar que os textos das alternativas no XML não contêm prefixos fixos `A.`, `B.`, `C.`, `D.` ou `E.`.
- Confirmar que expressões LaTeX inline usam `\(...\)` e expressões em bloco usam `\[...\]`.
- Confirmar visualmente no AVA que as fórmulas com `\tag{F...}` renderizam corretamente na página inicial.
- Confirmar que tabelas renderizam corretamente no AVA.
- Confirmar que os gabaritos importados coincidem com:
  - `NT24_AV2.md`
  - `T199_AV2.md`
- Confirmar que o XML da T199 não contém termos avaliativos proibidos ligados a regressão.

## Premissas

- A categoria comum no banco de questões será `$course$/AV2`, seguindo o padrão da AV1 (`$course$/AV1`), porque cada XML será importado em sua disciplina correspondente.
- A página inicial da avaliação será apenas o conjunto de fórmulas da primeira parte de cada prova, não as instruções completas.
- O AVA será configurado com uma página para cada problema: a descrição do problema e suas questões correspondentes no mesmo bloco/página.
- A ordem das questões não será embaralhada no quiz; apenas as alternativas serão embaralhadas.
- Os arquivos de respostas (`*_respostas.md`) não serão usados para gerar o XML da prova; eles servem apenas para validação.
