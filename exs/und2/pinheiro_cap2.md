# Pinheiro et al. (2009) - Capítulo 2: Estudando a Relação entre Duas Variáveis

Fonte: `livros/Pinheiro_2009.pdf`

Observação: os enunciados abaixo foram reorganizados e parafraseados para uso didático. Os exemplos têm respostas sintéticas no arquivo de respostas. Os exercícios resolvidos são mantidos apenas como referência de padrão de raciocínio; as respostas detalhadas são dadas somente para os exercícios propostos.

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

## Exemplos

### 2.1 - Categoria versus classe de IMC

Usa dados antropométricos de uma amostra de idosas para cruzar duas variáveis qualitativas: categoria de atividade física, ativa ou sedentária, e classe do índice de massa corporal, normal ou sobrepeso.

Tabela de contingência:

| Categoria | IMC normal | Sobrepeso | Total |
| --- | ---: | ---: | ---: |
| Ativa | 18 | 4 | 22 |
| Sedentária | 9 | 14 | 23 |
| **Total** | **27** | **18** | **45** |

O objetivo é calcular percentuais por linha e por coluna e interpretar a associação entre atividade física e classe de IMC.

### 2.2 - Consumo cultural por faixa etária

Analisa uma pesquisa com $n=499$ pessoas sobre faixa etária e programa cultural preferido. A tabela original tinha as opções cinema, exposições, teatro, dança e shows musicais. Como a coluna de exposições tinha poucas observações, o exemplo funde dança e exposições para obter uma tabela mais estável.

Tabela após a fusão:

| Faixa etária | Cinema | Teatro | Shows musicais | Dança/Exposições | Total |
| --- | ---: | ---: | ---: | ---: | ---: |
| 18 a 21 | 68 | 15 | 45 | 10 | 138 |
| 22 a 25 | 66 | 21 | 42 | 15 | 144 |
| 26 a 30 | 66 | 24 | 25 | 19 | 134 |
| 31 a 40 | 39 | 16 | 17 | 11 | 83 |
| **Total** | **239** | **76** | **129** | **55** | **499** |

O objetivo é comparar percentuais por linha e por coluna e discutir a relação entre idade e preferência cultural.

### 2.3 - Telefonia fixa per capita versus renda per capita

Usa dados de 2001 dos estados brasileiros para estudar a relação entre:

- $x$: renda per capita, em milhares de reais;
- $y$: telefonia fixa per capita.

O exemplo constrói o diagrama de dispersão, calcula a correlação e interpreta a associação linear entre renda e telefonia fixa.

Dados de entrada:

| Estado | População | Telefonia fixa | $y$ = telefonia fixa per capita | $x$ = renda per capita (R$ mil) |
| --- | ---: | ---: | ---: | ---: |
| Acre | 557.226 | 102,4 | 0,183767448 | 1,841 |
| Alagoas | 2.819.172 | 353,6 | 0,125426898 | 1,482 |
| Amapá | 475.843 | 92,0 | 0,193341081 | 1,789 |
| Amazonas | 2.813.085 | 455,7 | 0,161992972 | 2,350 |
| Bahia | 13.066.910 | 1.858,8 | 0,142252453 | 1,590 |
| Ceará | 7.418.476 | 1.042,8 | 0,140567955 | 1,187 |
| Distrito Federal | 2.043.169 | 933,3 | 0,456790407 | 6,259 |
| Espírito Santo | 3.094.390 | 707,8 | 0,228736520 | 2,403 |
| Goiás | 4.996.439 | 1.156,3 | 0,231424821 | 1,904 |
| Maranhão | 5.642.960 | 485,6 | 0,086054128 | 0,837 |
| Mato Grosso | 2.502.260 | 499,4 | 0,199579580 | 2,147 |
| Mato Grosso do Sul | 2.074.877 | 488,2 | 0,235291056 | 3,285 |
| Minas Gerais | 17.866.402 | 3.905,0 | 0,218566671 | 2,647 |
| Pará | 6.189.550 | 792,2 | 0,127989918 | 1,687 |
| Paraíba | 3.439.344 | 431,3 | 0,125401821 | 0,964 |
| Paraná | 9.558.454 | 2.333,8 | 0,244160823 | 2,870 |
| Pernambuco | 7.911.937 | 1.169,1 | 0,147764068 | 1,437 |
| Piauí | 2.841.202 | 335,8 | 0,118189414 | 0,792 |
| Rio de Janeiro | 14.367.083 | 4.991,9 | 0,347453968 | 3,820 |
| Rio Grande do Norte | 2.771.538 | 416,1 | 0,150133247 | 1,575 |
| Rio Grande do Sul | 10.181.749 | 2.411,6 | 0,236855181 | 3,399 |
| Rondônia | 1.377.792 | 295,7 | 0,214618752 | 2,421 |
| Roraima | 324.152 | 69,4 | 0,214097090 | 2,250 |
| Santa Catarina | 5.349.580 | 1.376,4 | 0,257291227 | 3,031 |
| São Paulo | 36.969.476 | 13.413,6 | 0,362829054 | 4,859 |
| Sergipe | 1.781.714 | 250,6 | 0,140651081 | 1,498 |
| Tocantins | 1.155.913 | 131,6 | 0,113849399 | 0,600 |

### 2.4 - Hotelaria no estado do Rio de Janeiro

Usa dados municipais de hotelaria do estado do Rio de Janeiro em 2001, comparando:

- $x$: número de estabelecimentos hoteleiros;
- $y$: número de acomodações.

Dados de entrada:

| Município/localidade | $x$ = estabelecimentos | $y$ = acomodações |
| --- | ---: | ---: |
| Areal | 3 | 88 |
| Barra Mansa | 22 | 1.718 |
| Barra do Piraí | 18 | 1.199 |
| Eng. Paulo de Frontin | 8 | 684 |
| Itatiaia | 121 | 4.214 |
| Maringá | 17 | 484 |
| Maromba | 20 | 468 |
| Penedo | 55 | 2.289 |
| Mendes | 5 | 148 |
| Paraíba do Sul | 12 | 639 |
| Piraí | 7 | 701 |
| Porto Real | 4 | 115 |
| Quatis | 5 | 267 |
| Resende | 36 | 2.124 |
| Engenheiro Passos | 4 | 368 |
| Visconde de Mauá | 12 | 247 |
| Rio Claro | 10 | 160 |
| Rio das Flores | 2 | 40 |
| Sapucaia | 5 | 228 |
| S. J. Vale do Rio Preto | 5 | 197 |
| Silva Jardim | 6 | 439 |
| Teresópolis | 44 | 2.876 |
| Vassouras | 9 | 504 |
| Aperibé | 2 | 60 |
| B. J. do Itabapoana | 4 | 249 |
| Cambuci | 3 | 85 |
| Campos dos Goytacazes | 49 | 2.792 |
| Cardoso Moreira | 2 | 70 |
| Italva | 3 | 118 |
| Itaocara | 7 | 283 |
| Itaperuna | 25 | 2.619 |
| Raposo | 10 | 1.592 |
| Miracema | 6 | 193 |
| Natividade | 2 | 100 |
| Porciúncula | 3 | 111 |
| Santa Maria Madalena | 2 | 85 |
| Sto. Antônio de Pádua | 11 | 548 |
| São Fidélis | 5 | 262 |
| São Sebastião do Alto | 3 | 53 |
| Sumidouro | 1 | 59 |
| Trajano de Morais | 2 | 62 |
| Araruama | 17 | 1.157 |
| Armação dos Búzios | 149 | 7.248 |
| Arraial do Cabo | 33 | 1.564 |
| Cabo Frio | 74 | 5.549 |
| Casimiro de Abreu | 18 | 679 |
| Iguaba Grande | 4 | 239 |
| Maricá | 17 | 441 |
| São Pedro da Aldeia | 21 | 1.082 |
| Saquarema | 25 | 1.283 |
| Angra dos Reis | 160 | 8.693 |
| Ilha Grande | 90 | 3.034 |
| Mangaratiba | 17 | 2.034 |
| Paraty | 149 | 5.315 |
| Trindade | 27 | 632 |
| Belford Roxo | 4 | 338 |
| Duque de Caxias | 24 | 2.227 |
| Três Rios | 15 | 826 |
| Valença | 34 | 1.859 |
| Conservatória | 20 | 1.289 |
| Volta Redonda | 14 | 1.463 |
| Cachoeiras de Macacu | 14 | 700 |
| Guapimirim | 7 | 430 |
| Miguel Pereira | 12 | 1.060 |
| Nova Friburgo | 84 | 3.853 |
| Lumiar | 16 | 312 |
| São Pedro da Serra | 14 | 319 |
| Paty do Alferes | 8 | 697 |
| Petrópolis | 83 | 3.203 |
| Petrópolis/arredores | 58 | 1.837 |
| Rio Bonito | 6 | 478 |
| S. Fco. Itabapoana | 11 | 421 |
| São João da Barra | 12 | 2.622 |
| São José de Ubá | 1 | 16 |
| Varre-Sai | 2 | 65 |
| Bom Jardim | 4 | 245 |
| Cantagalo | 7 | 450 |
| Carapebus | 1 | 32 |
| Carmo | 3 | 112 |
| Conceição de Macabu | 4 | 258 |
| Cordeiro | 5 | 158 |
| Duas Barras | 5 | 65 |
| Macaé | 46 | 2.688 |
| Sana | 13 | 321 |
| Quissamã | 4 | 201 |
| Itaboraí | 5 | 366 |
| Itaguaí | 11 | 895 |
| Magé | 8 | 249 |
| Nilópolis | 7 | 724 |
| Niterói | 40 | 2.861 |
| Nova Iguaçu | 22 | 1.979 |
| Paracambi | 1 | 48 |
| Queimados | 1 | 84 |
| Rio de Janeiro | 397 | 50.910 |
| São Gonçalo | 25 | 2.215 |
| São João de Meriti | 22 | 2.182 |
| Seropédica | 2 | 153 |
| Tanguá | 1 | 22 |

Como há forte assimetria à direita e o município do Rio de Janeiro destoa muito dos demais, o exemplo aplica a transformação:

$$
u=\ln(x), \qquad v=\ln(y).
$$

O objetivo é analisar a correlação entre $u$ e $v$ e discutir o papel da transformação logarítmica.

### 2.5 - Regressão para telefonia fixa

Retoma os dados de telefonia fixa e renda per capita do Exemplo 2.3. O objetivo é ajustar a reta:

$$
y = a + bx + erro
$$

em que $y$ é telefonia fixa per capita e $x$ é renda per capita, em milhares de reais. Depois, usa a reta ajustada para estimar a telefonia fixa per capita quando a renda per capita é de R$ 2.000.

### 2.6 - Regressão logarítmica para hotelaria

Retoma os dados de hotelaria do Exemplo 2.4. O objetivo é ajustar a reta:

$$
v = a + bu + erro
$$

em que:

$$
u=\ln(x), \qquad v=\ln(y).
$$

Depois, usa a reta ajustada para estimar o número de acomodações em um município com 30 estabelecimentos hoteleiros.

## Exercícios Resolvidos

### 2.1_R - Condições de trabalho por departamento

Analisa uma tabela de contingência com avaliação das condições de trabalho por departamento. O ponto didático central é distinguir percentuais por grupo de contagens absolutas e evitar médias simples de percentuais quando os tamanhos dos grupos são diferentes.

Avaliação das condições de trabalho:

| Departamento | Nº de entrevistas | Insatisfeitos | Parcialmente satisfeitos | Satisfeitos |
| --- | ---: | ---: | ---: | ---: |
| Comercial | 75 | 84,00% | 10,67% | 5,33% |
| Pessoal | 75 | 53,33% | 40,00% | 6,67% |
| Produção | 200 | 42,00% | 36,00% | 22,00% |

Nível de satisfação com o plano de saúde:

| Departamento | Nº de entrevistas | Média | Desvio-padrão |
| --- | ---: | ---: | ---: |
| Comercial | 75 | 2,76 | 1,32 |
| Pessoal | 75 | 2,85 | 2,43 |
| Produção | 200 | 3,71 | 2,78 |

A pontuação usada para o plano de saúde foi: 1 = péssimo, 2 = ruim, 3 = regular, 4 = bom e 5 = ótimo.

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

Foi realizada uma pesquisa de opinião com 100 alunos de uma universidade. A tabela de contingência cruza a área de conhecimento do curso com a avaliação da qualidade do curso.

Avaliação da Qualidade do Curso:

| Área de conhecimento do curso | Satisfeito | Insatisfeito | Total |
| --- | ---: | ---: | ---: |
| Biomédica | 22 | 8 | 30 |
| Humanas | 10 | 20 | 30 |
| Tecnológica | 28 | 12 | 40 |
| **Total** | **60** | **40** | **100** |

Calcule:

a) entre os insatisfeitos, o percentual que pertence à área biomédica;

b) entre os alunos que não são da área tecnológica, o percentual satisfeito.

### 2.3_P - Sexo e opinião sobre legalização do aborto

Foi realizada uma pesquisa por amostragem entre jovens de uma certa região do país para conhecer suas posições sobre a legalização do aborto.

Posicionamento quanto à legalização do aborto:

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

Foi realizada uma pesquisa de clima organizacional com 350 empregados da empresa X. A empresa tem cerca de 8.000 empregados, dos quais 223 ocupam cargos gerenciais. A tabela compara gerentes e não gerentes quanto à avaliação das oportunidades de treinamento oferecidas pela empresa.

Avaliação das Oportunidades de Treinamento:

| Situação funcional | Número de entrevistas | Péssimas | Ruins | Médias | Boas | Ótimas |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Gerentes | 15 | 0,00% | 6,67% | 0,00% | 33,33% | 60,00% |
| Não gerentes | 335 | 21,79% | 24,18% | 22,39% | 19,07% | 11,94% |

Classifique como verdadeiro ou falso e justifique:

a) como nesta amostra o contingente de empregados que ocupam cargos de gerência é excessivamente reduzido, os percentuais da linha dos gerentes não são estatisticamente significativos;

b) de forma geral, os gerentes da empresa X tendem a estar muito satisfeitos com as oportunidades de treinamento;

c) considerando a empresa como um todo, 71,94% dos empregados entrevistados avaliaram como ótimas as oportunidades de treinamento;

d) considerando a empresa como um todo, cerca de 10% dos empregados consideram péssimas as oportunidades de treinamento;

e) os resultados não são coerentes porque a soma dos dois percentuais em cada uma das cinco últimas colunas deveria ser 100%.

### 2.5_P - Peso versus altura

Os dados a seguir se referem a uma amostra de oito pessoas para as quais se dispõe de informações relativas a:

- nome;
- altura, em metros;
- peso, em quilos.

| Nome | Altura | Peso |
| --- | ---: | ---: |
| Jorge | 1,89 | 73 |
| Diva | 1,74 | 68 |
| André | 1,93 | 82 |
| Lucia | 1,74 | 57 |
| Silvio | 1,78 | 126 |
| Pedro | 1,92 | 90 |
| Maria | 1,61 | 53 |
| Norma | 1,80 | 65 |

Calcule:

a) média e desvio-padrão da altura;

b) média e desvio-padrão do peso;

c) correlação e reta de regressão para explicar peso pela altura;

d) repita a correlação e a regressão excluindo Silvio;

e) interprete o efeito dessa exclusão.

### 2.6_P - Alunos e professores em universidades brasileiras

A tabela a seguir fornece o número total de alunos e o número total de professores em 1982 para as principais universidades dos quatro estados mais ricos do Brasil: MG, RJ, RS e SP.

| Universidade | Alunos | Professores |
| --- | ---: | ---: |
| PUC de Minas Gerais | 13.147 | 713 |
| Federal de Juiz de Fora | 6.606 | 781 |
| Federal de Minas Gerais | 23.759 | 2.194 |
| Federal de Ouro Preto | 1.106 | 178 |
| Federal de Uberlândia | 6.651 | 765 |
| Federal de Viçosa | 5.842 | 667 |
| PUC do Rio Grande do Sul | 23.045 | 1.459 |
| Católica de Pelotas | 5.711 | 381 |
| Univ. de Caxias do Sul | 9.196 | 497 |
| Federal de Pelotas | 4.877 | 903 |
| Federal do Rio Gde. do Sul | 16.985 | 2.451 |
| Federal de Santa Maria | 9.693 | 1.362 |
| Univ. de Passo Fundo | 7.450 | 530 |
| Univ. do Rio Grande | 3.476 | 490 |
| Univ. do Vale do Rio dos Sinos | 21.000 | 650 |
| PUC do Rio de Janeiro | 8.232 | 788 |
| Católica de Petrópolis | 4.200 | 298 |
| Estadual do Rio de Janeiro | 11.000 | 1.750 |
| Federal Fluminense | 24.775 | 2.415 |
| Federal do Rio de Janeiro | 30.000 | 3.580 |
| Federal Rural do RJ | 3.686 | 611 |
| Gama Filho | 26.000 | 1.541 |
| PUC de Campinas | 18.132 | 1.457 |
| PUC de São Paulo | 15.296 | 1.526 |
| Estadual de Campinas | 9.843 | 1.474 |
| UNESP Julio Mesquita Filho | 14.204 | 2.395 |
| Federal de São Carlos | 2.566 | 463 |
| Univ. Mackenzie | 14.022 | 121 |
| Univ. de Mogi das Cruzes | 15.088 | 924 |
| Estadual de São Paulo | 44.159 | 4.461 |
| Metodista de Piracicaba | 6.600 | 500 |

Com base nos dados:

a) calcule a correlação entre número de alunos e número de professores;

b) ajuste a reta que expressa professores em função de alunos;

c) interprete os coeficientes da reta.

### 2.7_P - Relação entre regressão e correlação

Julgue afirmações conceituais sobre o coeficiente de correlação $r$ em regressão linear simples.

### 2.8_P - Hemoglobina versus hematócrito

Na Unidade de Pesquisa sobre Choque da Universidade de Southern California, Los Angeles, foram coletados dados sobre variáveis fisiológicas no momento em que cada paciente foi admitido. Os dados se referem a uma amostra com $n=37$ pacientes.

TABELA - Dados da pesquisa sobre choque:

| Hgb | Hct |
| ---: | ---: |
| 134 | 41,0 |
| 103 | 31,0 |
| 122 | 43,0 |
| 157 | 47,0 |
| 93 | 28,0 |
| 85 | 28,0 |
| 119 | 32,0 |
| 121 | 38,0 |
| 130 | 39,0 |
| 97 | 29,0 |
| 97 | 31,0 |
| 133 | 41,0 |
| 100 | 31,0 |
| 152 | 48,0 |
| 79 | 24,0 |
| 106 | 32,0 |
| 133 | 41,0 |
| 100 | 30,0 |
| 100 | 30,0 |
| 143 | 43,0 |
| 133 | 42,0 |
| 99 | 30,0 |
| 96 | 29,0 |
| 136 | 39,0 |
| 105 | 27,0 |
| 123 | 36,5 |
| 67 | 20,0 |
| 90 | 27,0 |
| 136 | 38,0 |
| 125 | 42,5 |
| 91 | 27,0 |
| 98 | 30,0 |
| 130 | 40,3 |
| 105 | 31,5 |
| 77 | 25,0 |
| 137 | 41,5 |
| 99 | 30,0 |

Com base nos dados:

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
