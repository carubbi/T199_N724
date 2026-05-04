# Pinheiro et al. (2009) - Capítulo 2: Estudando a Relação entre Duas Variáveis

Fonte: `livros/Pinheiro_2009.pdf`

Observação: os enunciados abaixo foram reorganizados e parafraseados para uso didático. Os exercícios resolvidos são mantidos apenas como referência de padrão de raciocínio; as respostas detalhadas são dadas somente para os exercícios propostos.

## Fórmulas úteis

### Tabelas de contingência

Percentual de linha:

$$
100 \cdot \frac{n_{ij}}{n_{i\cdot}}
$$

Percentual de coluna:

$$
100 \cdot \frac{n_{ij}}{n_{\cdot j}}
$$

em que:

- $n_{ij}$ é a frequência da célula na linha $i$ e coluna $j$;
- $n_{i\cdot}$ é o total da linha $i$;
- $n_{\cdot j}$ é o total da coluna $j$.

### Correlação de Pearson

$$
r_{xy} =
\frac{\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})}
{\sqrt{\sum_{i=1}^{n}(x_i-\bar{x})^2 \sum_{i=1}^{n}(y_i-\bar{y})^2}}
$$

Interpretação:

- $r$ próximo de $1$: associação linear positiva forte;
- $r$ próximo de $-1$: associação linear negativa forte;
- $r$ próximo de $0$: ausência de associação linear forte, não ausência de relação em geral.

### Regressão linear simples

Para explicar $Y$ a partir de $X$:

$$
\hat{y} = a + bx
$$

com:

$$
b = \frac{\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})}
{\sum_{i=1}^{n}(x_i-\bar{x})^2}
$$

$$
a = \bar{y} - b\bar{x}
$$

em que:

- $b$ é a inclinação da reta;
- $a$ é o intercepto;
- $\hat{y}$ é o valor previsto de $Y$ para um dado valor de $X$.

## Exercícios Resolvidos

### 2.1_R - Condições de trabalho por departamento

Analisa uma tabela de contingência com avaliação das condições de trabalho por departamento. O ponto didático central é distinguir percentuais por grupo de contagens absolutas e evitar médias simples de percentuais quando os tamanhos dos grupos são diferentes.

### 2.2_R - Intenção de voto por faixa etária

Combina uma tabela de intenção de voto condicional à idade com a distribuição etária do eleitorado. O padrão usado é ponderar percentuais por faixas etárias e, depois, calcular medidas resumidas para o eleitorado de cada candidato.

### 2.3_R - Segurança pública: policiais e presos

Usa dados por estado para estudar a relação entre número de policiais e número de presos. O exercício aplica transformação logarítmica, diagrama de dispersão e correlação, além de discutir o efeito de São Paulo sobre a associação observada.

## Exercícios Propostos

### 2.1_P - Diagnóstico de psicose e sexo do paciente

Usando a tabela de internações por diagnóstico de psicose e sexo do paciente, construa:

a) percentuais por linha, isto é, a distribuição de sexo dentro de cada diagnóstico;

b) percentuais por coluna, isto é, a distribuição de diagnósticos dentro de cada sexo;

c) uma interpretação da associação entre as variáveis.

### 2.2_P - Área do curso e avaliação da qualidade

Com base na tabela:

| Área | Satisfeito | Insatisfeito | Total |
| --- | ---: | ---: | ---: |
| Biomédica | 22 | 8 | 30 |
| Humanas | 10 | 20 | 30 |
| Tecnológica | 28 | 12 | 40 |
| **Total** | **60** | **40** | **100** |

Calcule:

a) entre os insatisfeitos, o percentual que pertence à área biomédica;

b) entre os alunos que não são da área tecnológica, o percentual satisfeito.

### 2.3_P - Sexo e opinião sobre legalização do aborto

Com base na tabela:

| Sexo | Favoráveis | Contrários | Total |
| --- | ---: | ---: | ---: |
| Masculino | 40 | 10 | 50 |
| Feminino | 30 | 20 | 50 |
| **Total** | **70** | **30** | **100** |

Classifique como verdadeiro ou falso:

a) a proporção de rapazes entre os favoráveis é $0{,}80$;

b) a probabilidade de sortear uma pessoa que seja mulher ou favorável é $0{,}60$;

c) menos de 30% das moças são contrárias.

### 2.4_P - Treinamento visto por gerentes e não gerentes

Avalie afirmações sobre uma pesquisa de clima organizacional que compara gerentes e não gerentes quanto às oportunidades de treinamento. O objetivo é distinguir percentuais por linha, percentuais gerais e a interpretação de grupos com tamanhos muito diferentes.

### 2.5_P - Peso versus altura

Para uma amostra de oito pessoas, calcule:

a) média e desvio-padrão da altura;

b) média e desvio-padrão do peso;

c) correlação e reta de regressão para explicar peso pela altura;

d) repita a correlação e a regressão excluindo Silvio;

e) interprete o efeito dessa exclusão.

### 2.6_P - Alunos e professores em universidades brasileiras

Usando dados de 31 universidades:

a) calcule a correlação entre número de alunos e número de professores;

b) ajuste a reta que expressa professores em função de alunos;

c) interprete os coeficientes da reta.

### 2.7_P - Relação entre regressão e correlação

Julgue afirmações conceituais sobre o coeficiente de correlação $r$ em regressão linear simples.

### 2.8_P - Hemoglobina versus hematócrito

Usando os dados de 37 pacientes:

a) analise a dependência linear entre hematócrito e hemoglobina via correlação;

b) ajuste a reta $\text{Hgb} = a + b\cdot\text{Hct} + erro$;

c) estime a hemoglobina para hematócrito igual a $34{,}7\%$.

### 2.9_P - Segurança revisitada

Retome os dados de policiais e presos do exercício resolvido 2.3_R, mas agora usando as variáveis originais, sem logaritmo:

a) construa o diagrama de dispersão de presos contra policiais;

b) calcule a correlação com e sem São Paulo;

c) compare com os resultados em escala logarítmica;

d) conclua sobre o papel da transformação logarítmica.

### 2.10_P - Argilosidade e tipo de solo

Usando o arquivo `Argilosidade.xls`, conte observações por tipo de solo, faça gráfico de setores e compare box plots da argilosidade por tipo de solo.
