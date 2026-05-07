# Materiais de Métodos Quantitativos

Repositório de apoio à disciplina **Métodos Quantitativos**, com materiais de aula, exercícios, bases de dados, planilhas e notebooks para estudo de estatística aplicada.

O foco do material é combinar rigor estatístico com leitura didática para estudantes de computação e áreas afins.

## Estrutura

- `aulas/slides/`: slides em PDF usados nas aulas.
- `aulas/notebooks/`: notebooks de aula e recursos visuais.
- `aulas/planilhas/`: planilhas de apoio, revisão e resolução.
- `aulas/planilhas/exports/`: versões Markdown geradas a partir das planilhas, para leitura sem Excel/Google Planilhas.
- `dataset/`: bases de dados utilizadas nas aulas, notebooks e trabalhos.
- `exs/und1/`: exercícios da Unidade 1.
- `exs/und2/`: exercícios da Unidade 2.
- `exs/*/respostas/`: respostas e resoluções quando disponíveis.
- `trabalhos/`: orientações dos trabalhos por turma e unidade.
- `scripts/`: scripts de apoio à geração e manutenção dos materiais.

## Revisão AV2

A revisão da AV2 está organizada em planilha e em versões Markdown.

Fonte operacional:

- [`aulas/planilhas/Revisao_AV2.xlsx`](aulas/planilhas/Revisao_AV2.xlsx)

Versões Markdown para leitura:

- [`Revisao_AV2__revisao_conceitual.md`](aulas/planilhas/exports/Revisao_AV2__revisao_conceitual.md)
- [`Revisao_AV2__ex_1_e_resolucao.md`](aulas/planilhas/exports/Revisao_AV2__ex_1_e_resolucao.md)
- [`Revisao_AV2__ex_2_e_resolucao.md`](aulas/planilhas/exports/Revisao_AV2__ex_2_e_resolucao.md)

Os arquivos Markdown não são uma cópia bruta da planilha. Eles organizam o conteúdo em:

- enunciado;
- observações e perguntas orientadoras;
- desenvolvimento sem uso de planilha;
- desenvolvimento com uso de planilha;
- validação com funções do Google Planilhas;
- interpretação crítica.

Para regenerar os Markdown da revisão AV2:

```bash
/home/carubbi/Documents/REPOS/T199_N724/.venv/bin/python -B scripts/export_revisao_av2_md.py
```

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
/home/carubbi/Documents/REPOS/T199_N724/.venv/bin/python
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
