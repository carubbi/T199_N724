# Respostas dos exercícios de Barbetta (2010), capítulo 11

Fonte dos enunciados: `exs/und2/barbetta_cap11.md`

Conferência com o gabarito extraído do livro: `exs/und2/respostas/barbetta_livro.md`.

Observação de conferência: as respostas coincidem com o gabarito do livro, exceto por um detalhe numérico no Exercício 6(d). O livro registra $p<0{,}0001$, mas, usando $F=76{,}1$ com graus de liberdade $(1,4)$, obtém-se $p \approx 0{,}0010$. A decisão estatística não muda: rejeita-se $H_0$.

## Fórmulas usadas

### Correlação de Pearson

$$
r=
\frac{n\sum x_i y_i-\left(\sum x_i\right)\left(\sum y_i\right)}
{\sqrt{n\sum x_i^2-\left(\sum x_i\right)^2}
\cdot
\sqrt{n\sum y_i^2-\left(\sum y_i\right)^2}}
$$

Teste para correlação:

$$
t=
\frac{r\sqrt{n-2}}{\sqrt{1-r^2}},
\qquad gl=n-2.
$$

### Regressão linear simples

Modelo:

$$
Y_i=\alpha+\beta x_i+\varepsilon_i
$$

Reta ajustada:

$$
\hat y=a+bx
$$

Coeficiente angular:

$$
b=
\frac{n\sum x_i y_i-\left(\sum x_i\right)\left(\sum y_i\right)}
{n\sum x_i^2-\left(\sum x_i\right)^2}
$$

Intercepto:

$$
a=\bar y-b\bar x
$$

Coeficiente de determinação:

$$
R^2=r^2
$$

Desvio padrão dos resíduos:

$$
s_e=\sqrt{\frac{\sum (y_i-\hat y_i)^2}{n-2}}
$$

Teste do coeficiente angular:

$$
t=\frac{b}{s_b},
\qquad
F=t^2.
$$

## Exercício 1

Usando as cinco primeiras observações do Exemplo 11.1:

| Ensaio | Retração linear $x$ | Resistência mecânica $y$ |
| ---: | ---: | ---: |
| 1 | 8,70 | 38,42 |
| 2 | 11,68 | 46,93 |
| 3 | 8,30 | 38,05 |
| 4 | 12,00 | 47,04 |
| 5 | 9,50 | 50,90 |

O coeficiente de correlação de Pearson é:

$$
r \approx 0{,}6353 \approx 0{,}64.
$$

Para testar se a correlação é significativamente diferente de zero:

$$
t=
\frac{0{,}6353\sqrt{5-2}}{\sqrt{1-0{,}6353^2}}
\approx 1{,}425,
\qquad gl=3.
$$

O valor-p bilateral é aproximadamente:

$$
p \approx 0{,}249.
$$

Resposta: $r \approx 0{,}64$. Não há evidência estatística suficiente para concluir que a correlação populacional seja diferente de zero.

## Exercício 2

O coeficiente informado é $r=-0{,}56$, indicando associação linear negativa moderada entre número de faltas e nota final.

### a)

A frase é incorreta. Uma correlação negativa moderada não implica que nenhum aluno com muitas faltas tenha tirado nota alta. Ela indica uma tendência média: em geral, maiores números de faltas estão associados a notas menores, mas podem existir exceções.

### b)

A frase é incorreta. Correlação não implica causalidade nem equivalência entre variáveis. Número de faltas e nota final não medem a mesma coisa, e uma variável não deve substituir automaticamente a outra como critério de avaliação.

### c)

A frase é a interpretação mais adequada, com uma ressalva: a tendência é moderada, não determinística. Os dados sugerem que alunos mais frequentes tenderam a ter melhor desempenho, mas não provam causalidade.

## Exercício 3

Dados:

| $X$ | $Y$ | $X$ | $Y$ | $X$ | $Y$ | $X$ | $Y$ | $X$ | $Y$ |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 39 | 65 | 43 | 78 | 21 | 52 | 64 | 82 | 65 | 88 |
| 57 | 92 | 47 | 89 | 28 | 73 | 75 | 98 | 47 | 71 |
| 34 | 56 | 52 | 75 | 35 | 50 | 30 | 50 | 28 | 52 |
| 40 | 70 | 70 | 50 | 80 | 90 | 32 | 58 | 67 | 88 |

### a)

Com todos os 20 alunos:

$$
r \approx 0{,}6941 \approx 0{,}69.
$$

Interpretação: há correlação positiva moderada entre a nota no vestibular de matemática e a nota final em cálculo. Em geral, notas maiores no vestibular tendem a estar associadas a notas maiores em cálculo.

### b)

O ponto discrepante é:

$$
(X,Y)=(70,50).
$$

Ele tem nota alta no vestibular, mas nota final baixa em cálculo, fugindo do padrão geral positivo.

### c)

Removendo o ponto discrepante $(70,50)$:

$$
r \approx 0{,}8648 \approx 0{,}86.
$$

### d)

A correlação passa a ser positiva forte. O teste bilateral dá:

$$
t \approx 7{,}10,
\qquad gl=17,
\qquad p \approx 0{,}0000018.
$$

Resposta: a correlação é positiva forte e significativamente diferente de zero.

## Exercício 4

A matriz de correlação é:

|  | $X_1$ | $X_2$ | $X_3$ |
| --- | ---: | ---: | ---: |
| $X_1$ | 1,00 | 0,18 | 0,86 |
| $X_2$ | 0,18 | 1,00 | 0,02 |
| $X_3$ | 0,86 | 0,02 | 1,00 |

Com $n=16$, temos $gl=14$.

Para $r=0{,}18$:

$$
t\approx 0{,}685,
\qquad p\approx 0{,}505.
$$

Para $r=0{,}86$:

$$
t\approx 6{,}306,
\qquad p\approx 0{,}000019.
$$

Para $r=0{,}02$:

$$
t\approx 0{,}075,
\qquad p\approx 0{,}941.
$$

Resposta: há forte associação positiva entre processamento de textos ($X_1$) e processamento batch ($X_3$). Não há evidência relevante de associação linear entre $X_1$ e $X_2$, nem entre $X_2$ e $X_3$. Portanto, apenas para $X_1$ e $X_3$ há evidência de que melhor desempenho em um atributo tende a acompanhar melhor desempenho no outro.

## Exercício 5

A equação ajustada é:

$$
\hat y=0{,}5+1{,}8x.
$$

### a)

Para $x=27$:

$$
\hat y=0{,}5+1{,}8(27)=0{,}5+48{,}6=49{,}1.
$$

Resposta: o consumo esperado é $49{,}1$ kg.

### b)

O coeficiente angular é $1{,}8$.

Resposta: a cada aumento de 1°C na temperatura média diária, espera-se aumento de $1{,}8$ kg nas vendas diárias de sorvete.

## Exercício 6

Dados:

| $x$ | 1 | 2 | 3 | 4 | 5 | 6 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| $y$ | 41 | 42 | 50 | 53 | 54 | 60 |

### a)

As estimativas são:

$$
a=36{,}6,
\qquad
b\approx 3{,}8286 \approx 3{,}83.
$$

Logo:

$$
\hat y=36{,}6+3{,}83x.
$$

### b)

O coeficiente de determinação é:

$$
R^2\approx 0{,}9501 \approx 0{,}95.
$$

Interpretação: cerca de 95% da variação observada da resistência mecânica é explicada pela relação linear com o nível de temperatura.

### c)

O desvio padrão dos resíduos é:

$$
s_e\approx 1{,}836.
$$

### d)

Teste:

$$
H_0:\beta=0
\qquad
\text{versus}
\qquad
H_1:\beta\ne 0.
$$

O teste resulta em:

$$
t\approx 8{,}72,
\qquad
F=t^2\approx 76{,}1.
$$

Com $gl=(1,4)$ para o teste $F$, obtém-se $p\approx 0{,}0010$. Portanto, rejeita-se $H_0$.

Resposta: há evidência estatística de que a temperatura do forno está associada linearmente à resistência mecânica.

## Exercício 7

Dados:

| Peso | 12 | 13 | 14 | 14 | 16 | 18 | 19 | 22 | 24 | 26 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Rendimento | 16 | 14 | 14 | 13 | 11 | 12 | 9 | 9 | 8 | 6 |

### a)

O coeficiente de correlação de Pearson é:

$$
r\approx -0{,}9585 \approx -0{,}96.
$$

### b)

Há correlação negativa forte: carros mais pesados tendem a apresentar menor rendimento de combustível.

### c)

A variável dependente deve ser o rendimento de combustível, pois é o desempenho que se deseja explicar ou predizer. A variável independente deve ser o peso, pois é a característica usada para explicar o rendimento.

Assim:

$$
Y=\text{rendimento},
\qquad
X=\text{peso}.
$$

### d)

A reta de regressão é:

$$
\hat y=22{,}25-0{,}6208x.
$$

Usando o arredondamento do livro:

$$
\widehat{\text{consumo}}=22{,}25-0{,}62(\text{peso}).
$$

### e)

O diagrama de dispersão teria os pontos com tendência claramente decrescente. A reta ajustada é a do item (d).

### f)

O ajuste é adequado para os dados observados:

$$
R^2=r^2\approx (-0{,}9585)^2\approx 0{,}9187 \approx 0{,}92.
$$

Interpretação: cerca de 92% da variação do rendimento é explicada pela relação linear com o peso.

### g)

Um carro de 2.000 kg corresponde a $x=20$, pois o peso está em centenas de kg.

Usando a equação arredondada do livro:

$$
\hat y=22{,}25-0{,}62(20)=9{,}85.
$$

Resposta: o rendimento esperado é aproximadamente $9{,}85$ km/l.

### h)

Não. Um veículo de 7.000 kg corresponderia a $x=70$, muito fora da faixa observada, que vai de 1.200 a 2.600 kg. Usar a reta nessa situação seria extrapolação indevida.

## Exercício 8

Dados:

| Carvão (%) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Resistência (MPa) | 38,5 | 40,2 | 42,1 | 37,5 | 41,1 | 36,9 | 38,2 | 36,7 | 39,5 | 35,9 |

### a)

A reta de regressão ajustada é:

$$
\hat y=40{,}2255-0{,}3479x.
$$

Com arredondamento:

$$
\hat y=40{,}22-0{,}35x.
$$

### b)

O coeficiente de determinação é:

$$
R^2\approx 0{,}2698 \approx 0{,}27.
$$

### c)

Teste:

$$
H_0:\beta=0
\qquad
\text{versus}
\qquad
H_1:\beta\ne 0.
$$

O teste resulta em:

$$
t\approx -1{,}72,
\qquad gl=8,
\qquad p\approx 0{,}124.
$$

Como $p>0{,}05$, aceita-se $H_0$ no sentido de não rejeitar a hipótese de coeficiente angular zero.

### d)

Não. Apesar de a inclinação estimada ser negativa, ela não é estatisticamente significativa ao nível de 5%. Assim, os dados não fornecem evidência suficiente de que a cinza de carvão diminui a resistência aos 28 dias.

## Exercício 9

Dados:

| Comprimento do cabo (m) | 8 | 8 | 9 | 9 | 10 | 10 | 11 | 11 | 12 | 12 | 13 | 13 | 14 | 14 | 15 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Taxa de falha | 2,2 | 2,1 | 3,0 | 2,9 | 4,1 | 4,5 | 6,2 | 5,9 | 9,8 | 8,7 | 12,5 | 13,1 | 19,3 | 17,4 | 28,2 |

### a)

Com os dados originais, a reta de regressão é:

$$
\hat y=-25{,}9336+3{,}1296x.
$$

O coeficiente de determinação é:

$$
R^2\approx 0{,}8660.
$$

### b)

Apesar do $R^2$ alto, o modelo linear nos dados originais não é adequado: a taxa de falha cresce de modo acelerado com o comprimento do cabo. Os resíduos tendem a apresentar padrão curvo, indicando violação da suposição de relação linear simples na escala original.

### c)

A transformação sugerida é logarítmica em $Y$:

$$
\log(Y).
$$

Essa resposta coincide com o gabarito do livro.

### d)

Usando logaritmo natural:

$$
\log(\hat y)=-2{,}1878+0{,}3652x.
$$

O coeficiente de determinação passa a ser:

$$
R^2\approx 0{,}9968.
$$

Equivalente em escala original:

$$
\hat y=\exp(-2{,}1878+0{,}3652x).
$$

Se for usado logaritmo na base 10, obtém-se:

$$
\log_{10}(\hat y)=-0{,}9502+0{,}1586x,
$$

com o mesmo $R^2\approx 0{,}9968$.

## Exercício 10

O modelo ajustado foi:

$$
\log_{10}(\text{valor})=
1{,}60+1{,}38\log_{10}(\text{área}),
\qquad R^2=0{,}89.
$$

O valor $R^2=0{,}89$ indica que 89% da variação observada em $\log_{10}(\text{valor})$ é explicada pela relação linear com $\log_{10}(\text{área})$.

O coeficiente $1{,}38$ indica que, para cada aumento de 1 unidade em $\log_{10}(\text{área})$, espera-se aumento de 1,38 unidade em $\log_{10}(\text{valor})$.

Como o modelo está em escala log-log, também há uma interpretação percentual aproximada: um aumento relativo de 1% na área está associado, em média, a um aumento relativo de aproximadamente 1,38% no valor.
