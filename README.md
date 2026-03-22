# Materiais de Métodos Quantitativos

## Objetivo
Este repositório reúne materiais da disciplina **Métodos Quantitativos para Computação**, com foco em estatística descritiva, análise exploratória de dados, exercícios comentados e notebooks de apoio.

## Estrutura do projeto
- `aulas/notebooks/`: notebooks de aula e os respectivos recursos visuais (`imgs/` e `figs/`).
- `aulas/planilhas/`: planilhas de apoio usadas em exemplos e atividades.
- `dataset/`: bases de dados utilizadas nas atividades e trabalhos.
- `exs/und1/`: listas de exercícios da Unidade 1, extraídas de diferentes referências.
- `exs/und1/respostas/`: respostas elaboradas e revisadas para as listas.
- `trabalhos/und1/notebooks/`: notebooks e artefatos de apoio ao trabalho da Unidade 1.
- `T1/`: documentos de orientação do trabalho.

## Materiais atualmente destacados
- [barbetta2010_exercicios_cap_1_2_3.md](/Users/carubbi/Documents/aulas/T199/exs/und1/barbetta2010_exercicios_cap_1_2_3.md): enunciados transcritos de Barbetta.
- [barbetta2010_exercicios_cap_1_2_3_respostas.md](/Users/carubbi/Documents/aulas/T199/exs/und1/respostas/barbetta2010_exercicios_cap_1_2_3_respostas.md): respostas revisadas com foco em rigor estatístico e didático.
- [Fundamentos de Estatística.xlsx](/Users/carubbi/Documents/aulas/T199/aulas/planilhas/Fundamentos%20de%20Estati%CC%81stica.xlsx): planilha de apoio com fórmulas, gráficos e tabelas dinâmicas para exemplos de aula.

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
- `openpyxl`: leitura e edição de arquivos `.xlsx`.
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

## Referências bibliográficas
- BARBETTA, Pedro Alberto; REIS, Marcelo Menezes; BORNIA, Antonio Cezar. *Estatística para cursos de engenharia e informática*. 3. ed. São Paulo: Atlas, 2010. Link: [Amazon](https://www.amazon.com.br/s?k=Estat%C3%ADstica+para+cursos+de+engenharia+e+inform%C3%A1tica+Barbetta).
- BRUCE, Peter; BRUCE, Andrew. *Estatística prática para cientistas de dados: 50 conceitos essenciais*. 1. ed. Rio de Janeiro: Alta Books, 2019. Link: [Amazon](https://www.amazon.com.br/s?k=Estat%C3%ADstica+pr%C3%A1tica+para+cientistas+de+dados+Bruce).
- MORETTIN, Pedro Alberto; BUSSAB, Wilton de Oliveira. *Estatística básica*. São Paulo: Saraiva, 2010. Link: [Amazon](https://www.amazon.com.br/s?k=Estat%C3%ADstica+b%C3%A1sica+Morettin+Bussab).
- NAVIDI, William. *Statistics for engineers and scientists*. 6. ed. New York: McGraw-Hill, 2024. Link: [Amazon](https://www.amazon.com.br/s?k=Statistics+for+Engineers+and+Scientists+William+Navidi).
- PINHEIRO, João Ismael D. et al. *Estatística básica: a arte de trabalhar com dados*. Rio de Janeiro: Elsevier, 2009. Link: [Amazon](https://www.amazon.com.br/s?k=Estat%C3%ADstica+b%C3%A1sica+a+arte+de+trabalhar+com+dados+Pinheiro).
