# Materiais de Métodos Quantitativos

## Objetivo
Este repositório reúne materiais da disciplina **Métodos Quantitativos para Computação**, com foco em estatística descritiva, análise exploratória de dados, exercícios comentados e notebooks de apoio.

## Estrutura do projeto
- `aulas/`: notebooks e figuras usadas em aula.
- `dataset/`: bases de dados utilizadas nas atividades e trabalhos.
- `exs/und1/`: listas de exercícios da Unidade 1, extraídas de diferentes referências.
- `exs/und1/respostas/`: respostas elaboradas e revisadas para as listas.
- `trabalhos/und1/`: notebooks e artefatos de apoio ao trabalho da Unidade 1.
- `T1/`: documentos de orientação do trabalho.

## Materiais atualmente destacados
- [barbetta2010_exercicios_cap_1_2_3.md](/Users/carubbi/Documents/aulas/T199/exs/und1/barbetta2010_exercicios_cap_1_2_3.md): enunciados transcritos de Barbetta.
- [barbetta2010_exercicios_cap_1_2_3_respostas.md](/Users/carubbi/Documents/aulas/T199/exs/und1/respostas/barbetta2010_exercicios_cap_1_2_3_respostas.md): respostas revisadas com foco em rigor estatístico e didático.

## Como executar
1. Criar e ativar um ambiente virtual.
2. Instalar as dependências:
```bash
pip install -r requirements.txt
```
3. Abrir os notebooks:
```bash
jupyter notebook
```

## Dependências
As dependências estão em [requirements.txt](/Users/carubbi/Documents/aulas/T199/requirements.txt). As bibliotecas mais relevantes para análise estatística e exploração de dados são:

- `numpy`: operações numéricas e vetorização.
- `pandas`: manipulação tabular e sumarização de dados.
- `scipy`: rotinas estatísticas e funções científicas.
- `statsmodels`: apoio a modelagem e procedimentos estatísticos.
- `matplotlib`: visualizações básicas.
- `seaborn`: visualizações estatísticas de mais alto nível.
- `ipykernel`: execução dos notebooks no ambiente Jupyter.

O projeto também inclui bibliotecas de apoio para leitura e extração de conteúdo de PDFs:

- `PyMuPDF`
- `pdfplumber`
- `pypdf`
- `rapidfuzz`
- `ocrmypdf`
