# Materiais de Métodos Quantitativos

Repositório de apoio à disciplina **Métodos Quantitativos**, com materiais de aula, exercícios, bases de dados, planilhas e notebooks para estudo de estatística aplicada.

O foco do material é combinar rigor estatístico com leitura didática para estudantes de computação e áreas afins.

## Estrutura

- `aulas/slides/`: slides em PDF usados nas aulas.
- `aulas/notebooks/`: notebooks de aula e recursos visuais.
- `aulas/planilhas/`: planilhas de apoio, revisão e resolução.
- `aulas/resolucoes_manuais/`: versões Markdown com resoluções manuais e leituras didáticas das planilhas.
- `dataset/`: bases de dados utilizadas nas aulas, notebooks e trabalhos.
- `exs/und1/`: exercícios da Unidade 1.
- `exs/und2/`: exercícios da Unidade 2.
- `exs/*/respostas/`: respostas e resoluções quando disponíveis.
- `trabalhos/`: orientações dos trabalhos por turma e unidade.

## Planilhas e resoluções manuais

Os materiais de planilha estão organizados em arquivos `.xlsx`, com versões Markdown em `aulas/resolucoes_manuais/` para leitura, resolução manual e acompanhamento didático.

Planilhas principais:

- [`aulas/planilhas/Fundamentos_de_Estatistica.xlsx`](aulas/planilhas/Fundamentos_de_Estatistica.xlsx)
- [`aulas/planilhas/Probabilidade_Condicional.xlsx`](aulas/planilhas/Probabilidade_Condicional.xlsx)
- [`aulas/planilhas/Variaveis_Aleatorias_Discretas.xlsx`](aulas/planilhas/Variaveis_Aleatorias_Discretas.xlsx)
- [`aulas/planilhas/Associacao_Regressao.xlsx`](aulas/planilhas/Associacao_Regressao.xlsx)

Resoluções e revisões manuais:

- [`Probabilidade_Condicional_Rev.md`](aulas/resolucoes_manuais/Probabilidade_Condicional_Rev.md)
- [`Probabilidade_Condicional_Ex1.md`](aulas/resolucoes_manuais/Probabilidade_Condicional_Ex1.md)
- [`Probabilidade_Condicional_Ex2.md`](aulas/resolucoes_manuais/Probabilidade_Condicional_Ex2.md)
- [`Variaveis_Aleatorias_Discretas_Rev.md`](aulas/resolucoes_manuais/Variaveis_Aleatorias_Discretas_Rev.md)
- [`Variaveis_Aleatorias_Discretas_Ex1.md`](aulas/resolucoes_manuais/Variaveis_Aleatorias_Discretas_Ex1.md)
- [`Variaveis_Aleatorias_Discretas_Ex2.md`](aulas/resolucoes_manuais/Variaveis_Aleatorias_Discretas_Ex2.md)
- [`Variaveis_Aleatorias_Discretas_Ex3.md`](aulas/resolucoes_manuais/Variaveis_Aleatorias_Discretas_Ex3.md)
- [`Variaveis_Aleatorias_Discretas_Ex4.md`](aulas/resolucoes_manuais/Variaveis_Aleatorias_Discretas_Ex4.md)
- [`Associacao_Regressao_Rev.md`](aulas/resolucoes_manuais/Associacao_Regressao_Rev.md)
- [`Associacao_Regressao_Ex1.md`](aulas/resolucoes_manuais/Associacao_Regressao_Ex1.md)
- [`Associacao_Regressao_Ex2.md`](aulas/resolucoes_manuais/Associacao_Regressao_Ex2.md)

Os arquivos Markdown não são uma cópia bruta da planilha. Eles organizam o conteúdo em:

- enunciado;
- observações e perguntas orientadoras;
- desenvolvimento sem uso de planilha;
- desenvolvimento com uso de planilha;
- validação com funções nativas do Google Planilhas;
- interpretação crítica.

## Ambiente

O projeto usa Python para notebooks, leitura de dados e manipulação de planilhas.

Criação do ambiente:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Também há um roteiro simples em:

```bash
venv.sh
```

Neste ambiente local, o interpretador usado nos scripts está em:

```bash
.venv/bin/python
```

## Notebooks

Para abrir os notebooks:

```bash
source .venv/bin/activate
jupyter notebook
```

Os notebooks estão em [`aulas/notebooks/`](aulas/notebooks/).

## Dependências

As dependências estão em [`requirements.txt`](requirements.txt).

Bibliotecas principais:

- `numpy`: operações numéricas.
- `pandas`: manipulação de dados tabulares.
- `openpyxl`: leitura e edição de arquivos `.xlsx`.
- `scipy`: rotinas científicas e estatísticas.
- `statsmodels`: modelagem estatística.
- `matplotlib`: visualização de dados.
- `seaborn`: visualização estatística.
- `ipykernel`: execução dos notebooks.

Bibliotecas de apoio para extração de conteúdo de PDFs:

- `PyMuPDF`
- `pdfplumber`
- `pypdf`
- `rapidfuzz`
- `ocrmypdf`

## Convenções dos materiais

- Textos finais devem usar português do Brasil com acentuação.
- Fórmulas matemáticas em Markdown devem usar `$...$` para expressões inline e `$$...$$` para blocos.
- Fórmulas do Google Planilhas devem usar separador `;`.
- A revisão conceitual não deve antecipar resultados dos exercícios.
- Em regressão, usar o termo **valor atípico/outlier** no material didático.
- Em planilhas com fórmulas e gráficos, evitar inserir linhas sem revisar referências e gráficos.

## Referências bibliográficas

- BARBETTA, Pedro Alberto; REIS, Marcelo Menezes; BORNIA, Antonio Cezar. *Estatística para cursos de engenharia e informática*. 3. ed. São Paulo: Atlas, 2010.
- BRUCE, Peter; BRUCE, Andrew. *Estatística prática para cientistas de dados: 50 conceitos essenciais*. Rio de Janeiro: Alta Books, 2019.
- MORETTIN, Pedro Alberto; BUSSAB, Wilton de Oliveira. *Estatística básica*. São Paulo: Saraiva, 2010.
- NAVIDI, William. *Statistics for engineers and scientists*. 6. ed. New York: McGraw-Hill, 2024.
- PINHEIRO, João Ismael D. et al. *Estatística básica: a arte de trabalhar com dados*. Rio de Janeiro: Elsevier, 2009.
