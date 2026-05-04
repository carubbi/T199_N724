# Respostas dos exercícios de Pinheiro et al. (2009), capítulo 2

Fonte dos enunciados: `exs/und2/pinheiro_cap2.md`

Conferência com o gabarito extraído do livro: o livro fornece respostas numéricas resumidas para parte dos exercícios propostos. As respostas abaixo detalham os cálculos e interpretações.

Observação de rigor: no Exercício 2.1_P, o enunciado menciona a Tabela 8.5, mas essa tabela contém frequências esperadas sob independência. Para analisar a associação observada entre diagnóstico e sexo, foi usada a Tabela 8.4, que contém os dados observados.

## Exercício 2.1_P

Tabela observada:

| Diagnóstico | Masculino | Feminino | Total |
| --- | ---: | ---: | ---: |
| Psicoses esquizofrênicas | 68 | 74 | 142 |
| Outras psicoses não-orgânicas | 35 | 61 | 96 |
| Síndrome de dependência do álcool | 85 | 7 | 92 |
| Psicoses afetivas | 25 | 61 | 86 |
| Síndrome de dependência das drogas | 15 | 2 | 17 |
| Outros | 30 | 20 | 50 |
| **Total** | **258** | **225** | **483** |

Percentuais por linha:

| Diagnóstico | Masculino | Feminino |
| --- | ---: | ---: |
| Psicoses esquizofrênicas | 47,89% | 52,11% |
| Outras psicoses não-orgânicas | 36,46% | 63,54% |
| Síndrome de dependência do álcool | 92,39% | 7,61% |
| Psicoses afetivas | 29,07% | 70,93% |
| Síndrome de dependência das drogas | 88,24% | 11,76% |
| Outros | 60,00% | 40,00% |

Percentuais por coluna:

| Diagnóstico | Entre homens | Entre mulheres |
| --- | ---: | ---: |
| Psicoses esquizofrênicas | 26,36% | 32,89% |
| Outras psicoses não-orgânicas | 13,57% | 27,11% |
| Síndrome de dependência do álcool | 32,95% | 3,11% |
| Psicoses afetivas | 9,69% | 27,11% |
| Síndrome de dependência das drogas | 5,81% | 0,89% |
| Outros | 11,63% | 8,89% |

Interpretação: há diferenças fortes entre os perfis. Síndrome de dependência do álcool aparece muito mais entre homens, enquanto psicoses afetivas e outras psicoses não-orgânicas aparecem proporcionalmente mais entre mulheres. Portanto, os dados sugerem associação entre sexo e diagnóstico.

## Exercício 2.2_P

### a)

Entre os insatisfeitos, há 8 alunos da área biomédica em um total de 40 insatisfeitos:

$$
\frac{8}{40}\cdot 100 = 20\%.
$$

### b)

Os alunos que não pertencem à área tecnológica são os das áreas biomédica e humanas:

$$
n = 30 + 30 = 60.
$$

Entre eles, satisfeitos:

$$
22 + 10 = 32.
$$

Logo:

$$
\frac{32}{60}\cdot 100 = 53{,}33\%.
$$

## Exercício 2.3_P

### a)

Falsa. Entre os favoráveis, há 40 homens em um total de 70 favoráveis:

$$
\frac{40}{70} = 0{,}5714.
$$

O valor $0{,}80$ corresponde à proporção de favoráveis entre os homens:

$$
\frac{40}{50} = 0{,}80.
$$

### b)

Falsa. Seja $F$ o evento "ser do sexo feminino" e $A$ o evento "ser favorável". Então:

$$
P(F \cup A) = P(F) + P(A) - P(F \cap A)
$$

$$
P(F \cup A) = \frac{50}{100} + \frac{70}{100} - \frac{30}{100}
= 0{,}90.
$$

### c)

Falsa. Entre as mulheres, 20 de 50 são contrárias:

$$
\frac{20}{50} = 0{,}40 = 40\%.
$$

## Exercício 2.4_P

### a)

Verdadeira. A amostra de gerentes tem apenas 15 pessoas. Percentuais como 60,00% em uma base tão pequena representam poucos casos e devem ser interpretados com cautela.

### b)

Falsa, se a frase for lida como conclusão sobre todos os gerentes da empresa. Na amostra, os gerentes entrevistados tendem a avaliar positivamente o treinamento, mas a base é pequena para generalização forte.

### c)

Falsa. Não se somam percentuais de linhas diferentes. Na amostra, o percentual geral de avaliação ótima é:

$$
\frac{15\cdot 0{,}60 + 335\cdot 0{,}1194}{350}
\approx 0{,}1400 = 14{,}00\%.
$$

### d)

Falsa para a amostra, pois o percentual geral de avaliação péssima é:

$$
\frac{15\cdot 0 + 335\cdot 0{,}2179}{350}
\approx 20{,}86\%.
$$

Se ponderarmos pelo contingente real da empresa, com 223 gerentes em 8000 empregados, o percentual estimado também fica perto de 21%, não de 10%.

### e)

Falsa. Os percentuais foram calculados dentro de cada situação funcional. Portanto, cada linha deve somar aproximadamente 100%, não cada coluna.

## Exercício 2.5_P

### a)

Para altura:

$$
\bar{x} = 1{,}801\text{ m}, \qquad s = 0{,}109\text{ m}.
$$

### b)

Para peso:

$$
\bar{y} = 76{,}75\text{ kg}, \qquad s = 23{,}33\text{ kg}.
$$

### c)

Com todos os oito casos:

$$
r = 0{,}403.
$$

Reta ajustada:

$$
\widehat{\text{peso}} = -78{,}742 + 86{,}325\cdot\text{altura}.
$$

### d)

Excluindo Silvio:

$$
r = 0{,}903.
$$

Reta ajustada:

$$
\widehat{\text{peso}} = -113{,}149 + 101{,}350\cdot\text{altura}.
$$

### e)

Silvio tem peso muito alto em relação à sua altura. Ele enfraquece a relação linear observada entre peso e altura. Ao removê-lo, a correlação passa de moderada para forte, o que mostra a sensibilidade da correlação e da reta de regressão a pontos atípicos.

## Exercício 2.6_P

Dados fornecidos:

$$
n = 31,\quad \bar{x} = 13108,\quad \bar{y} = 1236,
$$

$$
\sum (x_i-\bar{x})(y_i-\bar{y}) = 2{,}443\cdot 10^8,
$$

$$
\sum (x_i-\bar{x})^2 = 2{,}793\cdot 10^9,\quad
\sum (y_i-\bar{y})^2 = 3{,}052\cdot 10^7.
$$

### a)

Correlação:

$$
r =
\frac{2{,}443\cdot 10^8}
{\sqrt{(2{,}793\cdot 10^9)(3{,}052\cdot 10^7)}}
= 0{,}837.
$$

Há associação linear positiva forte entre número de alunos e número de professores.

### b)

Inclinação:

$$
b = \frac{2{,}443\cdot 10^8}{2{,}793\cdot 10^9}
= 0{,}087.
$$

Intercepto:

$$
a = 1236 - 0{,}087\cdot 13108
\approx 89{,}546.
$$

Reta:

$$
\widehat{\text{professores}} =
89{,}546 + 0{,}088\cdot\text{alunos}.
$$

### c)

O coeficiente angular indica que, em média, 1 aluno adicional está associado a aproximadamente 0,088 professor adicional. Equivalentemente, 1000 alunos adicionais estão associados a cerca de 88 professores adicionais. O intercepto é o valor previsto para uma universidade com zero alunos; neste contexto, ele é principalmente um parâmetro técnico da reta, sem interpretação substantiva forte.

## Exercício 2.7_P

### a)

Verdadeira, com ressalva. Quanto mais $r$ se aproxima de $1$, mais forte é a associação linear positiva e mais próximos os pontos tendem a estar de uma reta crescente.

### b)

Falsa. O valor de $r$ mede força e direção da associação linear padronizada. Ele não depende apenas do ângulo da reta; também depende da dispersão dos pontos em torno da reta e é invariável a mudanças de escala linear positiva.

### c)

Falsa. $r$ próximo de zero indica ausência de associação linear forte. Pode haver uma relação não linear entre $x$ e $y$.

### d)

Falsa. O coeficiente de correlação está sempre no intervalo:

$$
-1 \le r \le 1.
$$

## Exercício 2.8_P

### a)

A correlação entre hematócrito e hemoglobina é:

$$
r = 0{,}961.
$$

Isso indica associação linear positiva muito forte.

### b)

A reta ajustada é:

$$
\widehat{\text{Hgb}} = 8{,}546 + 3{,}036\cdot\text{Hct}.
$$

O coeficiente angular $b = 3{,}036$ indica que, no ajuste linear, cada aumento de 1 ponto percentual no hematócrito está associado a aumento médio previsto de aproximadamente 3,036 unidades na hemoglobina.

### c)

Para $\text{Hct} = 34{,}7$:

$$
\widehat{\text{Hgb}}
= 8{,}546 + 3{,}036\cdot 34{,}7
= 113{,}879.
$$

Logo, a hemoglobina esperada pelo modelo é aproximadamente:

$$
113{,}88.
$$

## Exercício 2.9_P

### a)

O diagrama de dispersão de $y$ contra $x$, sem transformação logarítmica, tende a ser fortemente influenciado por São Paulo, que tem valores muito maiores do que os demais estados.

### b)

Usando os somatórios fornecidos:

$$
r_{\text{com SP}} = 0{,}955.
$$

Retirando São Paulo:

$$
r_{\text{sem SP}} = 0{,}902.
$$

### c)

No exercício resolvido com logaritmos, os valores eram aproximadamente:

$$
r_{\log,\text{com SP}} = 0{,}904,\qquad
r_{\log,\text{sem SP}} = 0{,}870.
$$

Na escala original, as correlações são maiores, mas isso ocorre em parte porque São Paulo domina a escala dos dados. Na escala logarítmica, a comparação fica menos concentrada nos estados de maior tamanho.

### d)

A transformação logarítmica foi importante porque reduziu o efeito de escala e permitiu analisar a relação proporcional entre as variáveis. Sem a transformação, estados muito grandes podem induzir uma impressão excessivamente forte de associação linear.

## Exercício 2.10_P

Não foi possível calcular a resposta numérica porque o arquivo `Argilosidade.xls` não está disponível no repositório.

Com o arquivo, a solução adequada seria:

1. contar as observações por tipo de solo (`B`, `D`, `E`, `G`);
2. calcular os percentuais de cada tipo;
3. construir um gráfico de setores para a distribuição dos tipos de solo;
4. construir box plots de argilosidade por tipo de solo;
5. comparar medianas, dispersões, assimetria e possíveis pontos discrepantes entre os quatro grupos.

Sem os dados, qualquer conclusão sobre qual solo tem maior argilosidade, maior variabilidade ou mais outliers seria especulativa.
