# AV2 - Métodos Quantitativos

Curso: Ciência da Computação e Engenharias afins  
Valor total: **7,0 pontos**  
Formato: **14 questões objetivas**, cada uma valendo $0,5$ ponto.  
Temas: **associação e regressão linear simples**, **probabilidade condicional, probabilidade total e Bayes**, **variáveis aleatórias discretas por distribuição tabular**.

## Instruções

- Leia cada problema com atenção.
- Todas as questões são objetivas e possuem **5 alternativas**, com apenas **1 correta**.
- Quando houver cálculo, use as bases de dados dos problemas e os recursos permitidos pela avaliação.
- A prova valoriza a sequência de análise e a interpretação estatística, não apenas a substituição mecânica em fórmulas.

## Fórmulas

As fórmulas estão agrupadas por tema. Nem todas serão necessárias em todas as questões; cabe ao estudante selecionar a ferramenta adequada ao problema.

### Associação, Correlação E Regressão

$$
\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i
\tag{F1}
$$

$$
\bar{y}=\frac{1}{n}\sum_{i=1}^{n}y_i
\tag{F2}
$$

$$
d_{x_i}=x_i-\bar{x}
\tag{F3}
$$

$$
d_{y_i}=y_i-\bar{y}
\tag{F4}
$$

$$
r =
\frac{
\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})
}{
\sqrt{
\sum_{i=1}^{n}(x_i-\bar{x})^2
\sum_{i=1}^{n}(y_i-\bar{y})^2
}
}
\tag{F5}
$$

$$
\hat{y}_i=a+bx_i
\tag{F6}
$$

$$
b =
\frac{
\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})
}{
\sum_{i=1}^{n}(x_i-\bar{x})^2
}
\tag{F7}
$$

$$
a=\bar{y}-b\bar{x}
\tag{F8}
$$

$$
e_i=y_i-\hat{y}_i
\tag{F9}
$$

$$
\theta=(a,b)
$$

$$
f_{\theta}(x)=a+bx
$$

$$
\min_{a,b}\sum_{i=1}^{n}(y_i-(a+bx_i))^2
\tag{F10}
$$

$$
\mathrm{SQ}_{Tot}=\sum_{i=1}^{n}(y_i-\bar{y})^2
\tag{F11}
$$

$$
\mathrm{SQ}_{Reg}=\sum_{i=1}^{n}(\hat{y}_i-\bar{y})^2
\tag{F12}
$$

$$
\mathrm{SQ}_{Res}=\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
\tag{F13}
$$

$$
\mathrm{SQ}_{Tot}=\mathrm{SQ}_{Reg}+\mathrm{SQ}_{Res}
\tag{F14}
$$

$$
R^2=\frac{\mathrm{SQ}_{Reg}}{\mathrm{SQ}_{Tot}}
\tag{F15}
$$

$$
R^2=1-\frac{\mathrm{SQ}_{Res}}{\mathrm{SQ}_{Tot}}
\tag{F16}
$$

$$
R^2=r^2
\tag{F17}
$$

$$
s=\sqrt{\frac{\mathrm{SQ}_{Res}}{n-2}}
\tag{F18}
$$

$$
\mathrm{gl}_{Reg}=1
\tag{F19}
$$

$$
\mathrm{gl}_{Res}=n-2
\tag{F20}
$$

$$
\mathrm{gl}_{Tot}=n-1
\tag{F21}
$$

$$
\mathrm{QM}_{Reg}=\frac{\mathrm{SQ}_{Reg}}{\mathrm{gl}_{Reg}}
\tag{F22}
$$

$$
\mathrm{QM}_{Res}=\frac{\mathrm{SQ}_{Res}}{\mathrm{gl}_{Res}}
\tag{F23}
$$

$$
F=\frac{\mathrm{QM}_{Reg}}{\mathrm{QM}_{Res}}
\tag{F24}
$$

**Legenda**

- $F1$: média amostral de $x$, usada para resumir a variável explicativa.
- $F2$: média amostral de $y$, usada para resumir a variável resposta.
- $F3$: desvio de $x_i$ em relação à média de $x$.
- $F4$: desvio de $y_i$ em relação à média de $y$.
- $F5$: correlação de Pearson, usada para medir força e direção da associação linear entre $x$ e $y$.
- $F6$: reta de regressão ajustada, usada para prever $\hat{y}_i$ a partir de $x_i$.
- $F7$: inclinação da reta, usada para estimar a variação média prevista em $y$ para aumento de uma unidade em $x$.
- $F8$: intercepto da reta, usado para completar a equação ajustada.
- $F9$: resíduo, usado para medir o erro de previsão em cada observação.
- $F10$: critério de mínimos quadrados, usado para definir a reta que minimiza a soma dos erros quadráticos.
- $F11$: soma de quadrados total, usada para medir a variação total observada em $y$.
- $F12$: soma de quadrados da regressão, usada para medir a variação de $y$ explicada pela reta.
- $F13$: soma de quadrados dos resíduos, usada para medir a variação de $y$ não explicada pela reta.
- $F14$: decomposição da soma de quadrados, usada para separar variação total em parte explicada e parte residual.
- $F15$: coeficiente de determinação pela razão entre variação explicada e variação total.
- $F16$: coeficiente de determinação pela proporção complementar da variação residual.
- $F17$: coeficiente de determinação na regressão linear simples com intercepto, calculado como quadrado da correlação.
- $F18$: erro-padrão residual, usado para colocar resíduos em escala comum.
- $F19$: graus de liberdade da regressão.
- $F20$: graus de liberdade dos resíduos.
- $F21$: graus de liberdade totais.
- $F22$: quadrado médio da regressão, usado na ANOVA da regressão.
- $F23$: quadrado médio dos resíduos, usado na ANOVA da regressão.
- $F24$: estatística $F$, usada para comparar variação explicada e variação residual.
- Símbolos gerais do bloco: $x_i$ é o valor da variável explicativa na observação $i$; $y_i$ é o valor observado da variável resposta; $n$ é o número de observações.

### Probabilidade, Probabilidade Condicional E Bayes

$$
P(A)=\frac{n(A)}{n(\Omega)}
\tag{F25}
$$

$$
P(A^c)=1-P(A)
\tag{F26}
$$

$$
P(A\cup B)=P(A)+P(B)-P(A\cap B)
\tag{F27}
$$

$$
A\cap B=\varnothing
$$

$$
P(A\cap B)=0
\quad \text{se } A \text{ e } B \text{ são mutuamente exclusivos}
\tag{F28}
$$

$$
P(A\cup B)=P(A)+P(B)
\quad \text{se } A \text{ e } B \text{ são mutuamente exclusivos}
\tag{F29}
$$

$$
P(A\mid B)=\frac{P(A\cap B)}{P(B)}
\tag{F30}
$$

$$
P(B\mid A)=\frac{P(A\cap B)}{P(A)}
\tag{F31}
$$

$$
P(A\mid B)\ne P(B\mid A)
\quad \text{em geral}
$$

$$
P(A\cap B)=P(A\mid B)P(B)
\tag{F32}
$$

$$
P(A\cap B)=P(B\mid A)P(A)
\tag{F33}
$$

$$
P(A\cap B)=P(A)P(B)
\quad \text{se } A \text{ e } B \text{ são independentes}
\tag{F34}
$$

$$
P(A\mid B)=P(A)
\quad \text{se } A \text{ e } B \text{ são independentes}
\tag{F35}
$$

$$
P(B\mid A)=P(B)
\quad \text{se } A \text{ e } B \text{ são independentes}
\tag{F36}
$$

$$
P(B)=\sum_{i=1}^{m}P(B\mid A_i)P(A_i)
\tag{F37}
$$

$$
P(A_i\mid B)=
\frac{P(B\mid A_i)P(A_i)}
{\sum_{j=1}^{m}P(B\mid A_j)P(A_j)}
\tag{F38}
$$

$$
P(A_i\mid B)=\frac{P(A_i\cap B)}{P(B)}
\tag{F39}
$$

**Legenda**

- $F25$: probabilidade clássica, usada quando os resultados são finitos e equiprováveis.
- $F26$: regra do complementar, usada para calcular a probabilidade de $A$ não ocorrer.
- $F27$: regra geral da união, usada para calcular a probabilidade de ocorrer $A$, $B$ ou ambos.
- $F28$: probabilidade da interseção de eventos mutuamente exclusivos.
- $F29$: regra da união para eventos mutuamente exclusivos.
- $F30$: probabilidade condicional de $A$ dado $B$.
- $F31$: probabilidade condicional de $B$ dado $A$.
- $F32$: regra do produto escrita a partir de $P(A\mid B)$.
- $F33$: regra do produto escrita a partir de $P(B\mid A)$.
- $F34$: regra da multiplicação para eventos independentes.
- $F35$: condição de independência expressa por $P(A\mid B)=P(A)$.
- $F36$: condição de independência expressa por $P(B\mid A)=P(B)$.
- $F37$: probabilidade total, usada quando $B$ pode ocorrer por grupos ou caminhos $A_i$.
- $F38$: Teorema de Bayes, usado para inverter uma probabilidade condicional.
- $F39$: forma de Bayes pela probabilidade conjunta.
- Símbolos gerais do bloco: $\Omega$ é o espaço amostral; $A$, $B$ e $A_i$ são eventos; $A^c$ é o complementar de $A$; $n(A)$ é o número de resultados favoráveis a $A$; $m$ é o número de grupos da partição.

### Variáveis Aleatórias Discretas

$$
p(x)=P(X=x)
\tag{F40}
$$

$$
p(x)\ge 0
\tag{F41}
$$

$$
\sum_x p(x)=1
\tag{F42}
$$

$$
F(x)=P(X\le x)
\tag{F43}
$$

$$
E(X)=\sum_x xP(X=x)
\tag{F44}
$$

$$
E[h(X)]=\sum_x h(x)p(x)
\tag{F45}
$$

$$
\operatorname{Var}(X)=\sum_x [x-E(X)]^2p(x)
\tag{F46}
$$

$$
E(X^2)=\sum_x x^2p(x)
\tag{F47}
$$

$$
\operatorname{Var}(X)=E(X^2)-[E(X)]^2
\tag{F48}
$$

$$
\operatorname{DP}(X)=\sqrt{\operatorname{Var}(X)}
\tag{F49}
$$

$$
\operatorname{CV}(X)=\frac{\operatorname{DP}(X)}{E(X)}, \quad E(X)\ne 0
\tag{F50}
$$

$$
P(X=1)=p,\quad P(X=0)=1-p
\tag{F51}
$$

$$
E(X)=p
\quad \text{para } X\sim Bernoulli(p)
\tag{F52}
$$

$$
\operatorname{Var}(X)=p(1-p)
\quad \text{para } X\sim Bernoulli(p)
\tag{F53}
$$

$$
X\sim Binomial(n,p)
$$

$$
P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}
\tag{F54}
$$

$$
k=0,1,\ldots,n
$$

$$
E(X)=np
\quad \text{para } X\sim Binomial(n,p)
\tag{F55}
$$

$$
\operatorname{Var}(X)=np(1-p)
\quad \text{para } X\sim Binomial(n,p)
\tag{F56}
$$

$$
P(X=k)=
\frac{\binom{K}{k}\binom{N-K}{n-k}}
{\binom{N}{n}}
\tag{F57}
$$

$$
X\sim Poisson(\lambda)
$$

$$
P(X=k)=\frac{e^{-\lambda}\lambda^k}{k!}
\tag{F58}
$$

$$
k=0,1,2,\ldots
$$

$$
E(X)=\lambda,\quad \operatorname{Var}(X)=\lambda
\quad \text{para } X\sim Poisson(\lambda)
\tag{F59}
$$

**Legenda**

- $F40$: função de probabilidade discreta, usada para calcular $P(X=x)$.
- $F41$: condição de não negatividade das probabilidades.
- $F42$: condição de soma total igual a $1$.
- $F43$: função acumulada, usada para calcular $P(X\le x)$.
- $F44$: esperança de $X$, usada como média teórica de longo prazo.
- $F45$: esperança de uma função de $X$, usada quando se transforma a variável aleatória.
- $F46$: variância pela soma dos desvios quadráticos ponderados.
- $F47$: segundo momento, usado no cálculo alternativo da variância.
- $F48$: variância pela diferença entre segundo momento e quadrado da esperança.
- $F49$: desvio-padrão, usado para medir dispersão na unidade original de $X$.
- $F50$: coeficiente de variação, usado para medir dispersão relativa.
- $F51$: função de probabilidade da distribuição Bernoulli.
- $F52$: esperança da distribuição Bernoulli.
- $F53$: variância da distribuição Bernoulli.
- $F54$: função de probabilidade da distribuição binomial.
- $F55$: esperança da distribuição binomial.
- $F56$: variância da distribuição binomial.
- $F57$: função de probabilidade da distribuição hipergeométrica, usada em amostragem sem reposição.
- $F58$: função de probabilidade da distribuição de Poisson.
- $F59$: esperança e variância da distribuição de Poisson.
- Símbolos gerais do bloco: $X$ é uma variável aleatória discreta; $x$ é um valor possível de $X$; $p$ é a probabilidade de sucesso; $k$ é o número de sucessos ou ocorrências; $n$ é o número de tentativas ou o tamanho da amostra; $N$ é o tamanho da população; $K$ é o número de sucessos na população; $\lambda$ é a média da distribuição de Poisson.

## Problema 1 - Associação e regressão

Um artigo publicado no *Journal of the Environmental Engineering Division* [“Least Squares Estimates of BOD Parameters” (1980, Vol. 106, pp. 1197–1202)] coletou uma amostra do rio Holston a jusante de Kingsport, Tennessee, durante agosto de 1977. O teste de demanda bioquímica de oxigênio (BOD) é conduzido ao longo de um período de tempo, medido em dias. Os dados resultantes são apresentados a seguir. Fonte: Adaptado de Montgomery (2018), Exercício 11.2.9.

| Observação | Tempo $x$ (dias) | BOD $y$ (mg/liter) |
| ---: | ---: | ---: |
| 1 | 1 | 0,6 |
| 2 | 2 | 0,7 |
| 3 | 4 | 1,5 |
| 4 | 6 | 1,9 |
| 5 | 8 | 2,1 |
| 6 | 10 | 2,6 |
| 7 | 12 | 2,9 |
| 8 | 14 | 3,7 |
| 9 | 16 | 3,5 |
| 10 | 18 | 3,7 |
| 11 | 20 | 3,8 |

*__Notas da tabela:__ Observação identifica o par de dados; tempo $x$ é o tempo do teste, em dias; BOD $y$ é o BOD observado, em mg/liter.*

### Questão 1 (0,5 ponto)

No Problema 1, considere que o objetivo é ajustar uma reta de regressão linear simples para prever o BOD $y$ a partir do tempo $x$. Usando a base de dados fornecida, calcule a reta ajustada $\hat{y}=a+bx$ e o coeficiente de correlação de Pearson $r$.

Qual alternativa apresenta corretamente a reta ajustada e a direção/intensidade da associação linear entre tempo e BOD?

A. $\hat{y} = 0,658 + 0,178x$ e $r = 0,947$.

B. $\hat{y} = 0,178 + 0,658x$ e $r = 0,973$.

C. $\hat{y} = 0,658 + 0,178x$ e $r = 0,973$.

D. $\hat{y} = 0,658 + 0,178x$ e $r = -0,973$.

E. $\hat{y} = 0,660 + 0,172x$ e $r = 0,984$.

**Feedback Geral**  
Para ajustar a reta, primeiro identificam-se $x$ como variável explicativa e $y$ como variável resposta. A inclinação é calculada por $b=S_{xy}/S_{xx}$, e o intercepto por $a=\bar{y}-b\bar{x}$. O coeficiente $r$ resume a direção e a intensidade da associação linear; como $S_{xy}>0$, a associação é positiva.

**Feedback Específico**  
- A. Incorreta. A reta está correta, mas usa $R^2$ como se fosse $r$.
- B. Incorreta. Troca intercepto e inclinação.
- C. Correta. $b \approx 0,178$, $a \approx 0,658$ e $r \approx 0,973$.
- D. Incorreta. A reta indica associação positiva; o sinal de $r$ deve ser compatível com a inclinação.
- E. Incorreta. Esses valores correspondem ao ajuste sem o ponto $x=14$, $y=3,7$, não ao ajuste com todos os dados.

### Questão 2 (0,5 ponto)

Após ajustar o modelo linear do Problema 1, avalie o coeficiente de determinação $R^2$ associado ao ajuste.

Qual alternativa apresenta corretamente o valor aproximado de $R^2$ e uma conclusão compatível com a análise estatística do problema?

A. $R^2 \approx 0,947$; isso prova que o tempo causa aumento no BOD.

B. $R^2 \approx 0,973$; cerca de 97,3% da variação observada no BOD é explicada linearmente pelo tempo.

C. $R^2 \approx 0,946$; cerca de 94,6% da variação observada no tempo é explicada linearmente pelo BOD.

D. $R^2 \approx 0,947$; cerca de 94,7% da variação observada no BOD é explicada linearmente pelo tempo, sem que isso prove causalidade ou dispense análise dos resíduos.

E. $R^2 \approx 0,795$; cerca de 79,5% da variação observada no BOD é explicada linearmente pelo tempo, pois $R^2$ é obtido subtraindo a inclinação do valor da correlação.

**Feedback Geral**  
Em regressão linear simples com intercepto, $R^2=r^2$. O coeficiente de determinação mede proporção de variação explicada pelo ajuste linear, mas não prova causalidade.

**Feedback Específico**  
- A. Incorreta. $R^2$ não prova causalidade.
- B. Incorreta. Usa $r$ como se fosse $R^2$.
- C. Incorreta. O valor numérico é próximo, mas inverte a interpretação entre variável resposta e variável explicativa.
- D. Correta. $(0,973)^2 \approx 0,947$, ou 94,7%; a interpretação deve continuar descritiva e crítica.
- E. Incorreta. A interpretação geral parece plausível, mas o cálculo de $R^2$ não é feito subtraindo a inclinação de $r$.

### Questão 3 (0,5 ponto)

A partir da reta ajustada no Problema 1, use o modelo para três tarefas: prever o BOD quando $x=15$, interpretar a mudança média prevista no BOD para um aumento de $3$ dias no tempo e calcular o resíduo do ponto observado com $x=6$. Considere que, para $x=6$, o valor observado na base é $y=1,9$.

Qual alternativa apresenta corretamente a previsão, a mudança média prevista e o resíduo?

A. Para $x = 15$, $\hat{y} \approx 3,33$; um aumento de 3 dias está associado a aumento médio previsto de aproximadamente $0,18$ no BOD; em $x = 6$, o resíduo é aproximadamente $0,17$.

B. Para $x = 15$, $\hat{y} \approx 3,33$; um aumento de 3 dias está associado a aumento médio previsto de aproximadamente $0,53$ no BOD; em $x = 6$, o resíduo é aproximadamente $0,17$.

C. Para $x = 15$, $\hat{y} \approx 3,33$; um aumento de 3 dias está associado a aumento médio previsto de aproximadamente $0,53$ no BOD; em $x = 6$, o resíduo é aproximadamente $-0,17$.

D. Para $x = 15$, $\hat{y} \approx 2,67$; um aumento de 3 dias está associado a aumento médio previsto de aproximadamente $0,53$ no BOD; em $x = 6$, o resíduo é aproximadamente $0,17$.

E. Para $x = 15$, $\hat{y} \approx 3,33$; um aumento de 3 dias está associado a aumento médio previsto de aproximadamente $0,53$ no BOD; em $x = 6$, o valor ajustado é aproximadamente $0,17$.

**Feedback Geral**  
A previsão é obtida substituindo $x$ na reta. A mudança esperada para aumento de 3 unidades em $x$ é $3b$. O resíduo em $x = 6$ é $y-\hat{y}$; como o valor observado é $1,9$ e o ajustado é aproximadamente $1,73$, o resíduo é positivo.

**Feedback Específico**  
- A. Incorreta. Usa a inclinação como mudança para 3 dias; a mudança correta é $3b$.
- B. Correta. $0,658 + 0,178\cdot 15 \approx 3,33$; $3\cdot 0,178 \approx 0,53$; resíduo em $x=6$ é aproximadamente $0,17$.
- C. Incorreta. Acerta a previsão e a mudança média, mas inverte o sinal do resíduo.
- D. Incorreta. Calcula a previsão sem o intercepto, embora interprete corretamente a mudança e o resíduo.
- E. Incorreta. Confunde resíduo com valor ajustado; o valor ajustado em $x=6$ é aproximadamente $1,73$.

### Questão 4 (0,5 ponto)

Usando a reta ajustada no Problema 1, calcule os valores ajustados $\hat{y}_i$ para cada valor observado de $x_i$. Em seguida, considere o gráfico de $\hat{y}_i$ no eixo vertical contra os valores observados $y_i$ no eixo horizontal.

Se a relação entre $y$ e $x$ fosse uma reta determinística, sem erro aleatório, como esse gráfico deveria se comportar? E o que o gráfico obtido indica sobre o uso do tempo como variável regressora para prever BOD?

A. Os pontos deveriam ficar próximos de uma reta crescente; no caso determinístico, ficariam exatamente sobre a reta $\hat{y}=y$. Como os pontos observados ficam próximos desse padrão, o tempo parece ser um regressor efetivo para prever BOD.

B. Os pontos deveriam formar uma reta horizontal, pois $\hat{y}_i$ é constante quando o modelo é linear. Como há variação nos valores previstos, o tempo não é um regressor efetivo.

C. Os pontos deveriam ficar exatamente sobre a reta $\hat{y}=y$ em qualquer regressão linear ajustada. Se isso não ocorre, o modelo linear deve ser rejeitado.

D. O gráfico de $\hat{y}_i$ versus $y_i$ deve ser idêntico ao gráfico de dispersão de $y_i$ versus $x_i$, pois ambos usam os mesmos dados. Assim, ele não acrescenta informação diagnóstica.

E. A proximidade dos pontos à reta $\hat{y}=y$ prova que o tempo causa aumento no BOD e elimina a necessidade de analisar resíduos.

**Feedback Geral**  
O gráfico de $\hat{y}_i$ versus $y_i$ compara valores previstos com valores observados. Se a relação fosse determinística e sem erro aleatório, os pontos coincidiriam com a reta $\hat{y}=y$. Quando os pontos ficam próximos dessa referência, há evidência de bom ajuste preditivo, mas isso não prova causalidade nem dispensa análise dos resíduos.

**Feedback Específico**  
- A. Correta. Em uma relação determinística, $\hat{y}_i=y_i$ para todos os pontos; no ajuste obtido, a proximidade entre previsto e observado indica que o tempo é um regressor efetivo para prever BOD.
- B. Incorreta. Em regressão linear, $\hat{y}_i$ varia com $x_i$; os valores ajustados não precisam ser constantes.
- C. Incorreta. Em dados com erro aleatório, não se espera coincidência perfeita entre $\hat{y}_i$ e $y_i$.
- D. Incorreta. O gráfico de $\hat{y}_i$ versus $y_i$ compara previsto e observado; ele não é igual ao gráfico de dispersão de $y_i$ versus $x_i$.
- E. Incorreta. Bom ajuste preditivo não prova causalidade e não elimina a necessidade de análise dos resíduos.

### Questão 5 (0,5 ponto)

Considere que o ponto $x=14$, $y=3,7$ foi identificado como outlier pelo critério $|z|>2$. Para avaliar a sensibilidade do modelo linear, refaça o ajuste da regressão sem esse ponto e compare com o ajuste usando todos os dados.

Qual alternativa apresenta corretamente os resultados sem esse ponto?

A. $\hat{y}=0{,}660+0{,}172x$, $r\approx 0{,}984$, $R^2\approx 0{,}968$. A associação permanece positiva e forte.

B. $\hat{y}=0{,}658+0{,}178x$, $r\approx 0{,}973$, $R^2\approx 0{,}947$. A retirada do ponto não altera o ajuste.

C. $\hat{y}=0{,}172+0{,}660x$, $r\approx 0{,}984$, $R^2\approx 0{,}968$. A associação permanece positiva e forte.

D. $\hat{y}=0{,}660+0{,}172x$, $r\approx 0{,}968$, $R^2\approx 0{,}984$. A associação permanece positiva e forte.

E. $\hat{y}=0{,}660+0{,}172x$, $r\approx 0{,}984$, $R^2\approx 0{,}968$. A inclinação menor mostra que a associação deixa de ser forte.

**Feedback Geral**  
Sem o ponto $x=14$, $y=3,7$, a reta ajustada fica aproximadamente $\hat{y}=0{,}660+0{,}172x$, com $r\approx 0{,}984$ e $R^2\approx 0{,}968$. A associação continua positiva e forte.

**Feedback Específico**  
- A. Correta. Apresenta a reta, $r$ e $R^2$ compatíveis com o ajuste sem o ponto $x=14$, $y=3,7$.
- B. Incorreta. Repete os resultados do ajuste com todos os dados.
- C. Incorreta. Usa $r$ e $R^2$ compatíveis, mas troca intercepto e inclinação.
- D. Incorreta. Usa a reta correta, mas troca os papéis de $r$ e $R^2$.
- E. Incorreta. Os valores estão corretos, mas a interpretação é inadequada: a associação permanece forte.

## Problema 2 - Probabilidade condicional, total e Bayes

Uma empresa que acompanha o uso de seu site observou que, quanto mais páginas um visitante visualiza, maior tende a ser a chance de ele solicitar mais informações, evento indicado por $\mathrm{RMI}$. A tabela mostra a distribuição dos visitantes por número de páginas vistas, tratado como grupo, e a probabilidade condicional de solicitação de mais informação $\mathrm{RMI}$ dentro de cada grupo. Fonte: Adaptado de Montgomery (2018), Exercício 2.S26.

| Páginas vistas (grupo) | Proporção de visitantes $P(\text{grupo})$ | Probabilidade condicional $P(\mathrm{RMI}\mid \text{grupo})$ |
| --- | ---: | ---: |
| 1 | 40% | 10% |
| 2 | 30% | 10% |
| 3 | 20% | 20% |
| 4 ou mais | 10% | 40% |

*__Notas da tabela:__ páginas vistas define o grupo de visitantes; proporção de visitantes $P(\text{grupo})$ representa a probabilidade de um visitante pertencer ao grupo; $\mathrm{RMI}$ significa solicitação de mais informação; probabilidade condicional $P(\mathrm{RMI}\mid \text{grupo})$ representa a probabilidade de solicitação de mais informação dentro do grupo.*

### Questão 6 (0,5 ponto)

No Problema 2, considere o evento $\mathrm{RMI}$ e os grupos definidos pelo número de páginas vistas. Qual alternativa identifica corretamente o evento, os grupos e o universo de referência de $P(4\text{ ou mais páginas}\mid \mathrm{RMI})$?

A. $\mathrm{RMI}$ é o evento “visitante solicita mais informação”; os grupos são definidos por páginas vistas; em $P(4\text{ ou mais páginas}\mid \mathrm{RMI})$, o universo é o conjunto dos visitantes que solicitaram mais informação.

B. $\mathrm{RMI}$ é o grupo “visitantes com 4 ou mais páginas”; em $P(4\text{ ou mais páginas}\mid \mathrm{RMI})$, o universo é o conjunto de todos os visitantes.

C. $\mathrm{RMI}$ é o evento “visitante solicita mais informação”; em $P(4\text{ ou mais páginas}\mid \mathrm{RMI})$, o universo é o conjunto dos visitantes que viram 4 ou mais páginas.

D. Os grupos são definidos por solicitar ou não solicitar informação; em $P(\mathrm{RMI}\mid 4\text{ ou mais páginas})$, o universo é o conjunto dos visitantes que solicitaram mais informação.

E. $P(\mathrm{RMI}\mid 4\text{ ou mais páginas})$ e $P(4\text{ ou mais páginas}\mid \mathrm{RMI})$ têm o mesmo universo de referência, pois envolvem os mesmos dois eventos.

**Feedback Geral**  
Em probabilidade condicional, o evento depois da barra define o universo de referência. Aqui $\mathrm{RMI}$ é o evento de solicitar mais informação, e os grupos são as categorias de páginas vistas.

**Feedback Específico**  
- A. Correta. Define corretamente o evento, os grupos e o universo condicionado.
- B. Incorreta. Troca o evento $\mathrm{RMI}$ com um grupo de páginas vistas e ignora a condição.
- C. Incorreta. O universo de $P(4\text{ ou mais páginas}\mid \mathrm{RMI})$ é quem solicitou mais informação.
- D. Incorreta. Os grupos da tabela são definidos por páginas vistas, não por solicitar informação.
- E. Incorreta. Condicionais invertidas usam universos de referência diferentes.

### Questão 7 (0,5 ponto)

Ao montar a tabela conjunta, os valores de $P(\text{grupo}\cap \mathrm{RMI})$ para os grupos $1$, $2$, $3$ e $4$ ou mais páginas são, respectivamente:

A. $0,40$, $0,30$, $0,20$, $0,10$.

B. $0,10$, $0,10$, $0,20$, $0,40$.

C. $0,04$, $0,03$, $0,04$, $0,04$.

D. $0,36$, $0,27$, $0,16$, $0,06$.

E. $0,04$, $0,03$, $0,04$, $0,40$.

**Feedback Geral**  
A probabilidade conjunta é obtida por $P(\text{grupo}\cap \mathrm{RMI})=P(\text{grupo})\cdot P(\mathrm{RMI}\mid \text{grupo})$. Não se somam probabilidades condicionais de grupos diferentes sem ponderação.

**Feedback Específico**  
- A. Incorreta. Lista apenas as proporções de visitantes por grupo.
- B. Incorreta. Lista apenas as probabilidades condicionais de $\mathrm{RMI}$ dentro dos grupos.
- C. Correta. $0,40\cdot 0,10=0,04$; $0,30\cdot 0,10=0,03$; $0,20\cdot 0,20=0,04$; $0,10\cdot 0,40=0,04$.
- D. Incorreta. Calcula conjuntas com o complemento de $\mathrm{RMI}$, não com $\mathrm{RMI}$.
- E. Incorreta. Calcula corretamente as três primeiras conjuntas, mas usa a probabilidade condicional $0,40$ no último grupo em vez da conjunta $0,10\cdot 0,40$.

### Questão 8 (0,5 ponto)

Calcule a probabilidade total $P(\mathrm{RMI})$ de um visitante solicitar mais informação e assinale a interpretação correta.

A. $0,40$; é a probabilidade total porque é a maior probabilidade condicional da tabela.

B. $1,00$; é a probabilidade total porque os grupos de páginas vistas cobrem todos os visitantes.

C. $0,20$; é a probabilidade total obtida pela média simples das probabilidades condicionais.

D. $0,85$; é a probabilidade total de não solicitar mais informação, portanto deve ser usada como probabilidade de $\mathrm{RMI}$.

E. $0,15$; é a probabilidade total obtida pela soma das probabilidades conjuntas de $\mathrm{RMI}$ em todos os grupos.

**Feedback Geral**  
A probabilidade total de $\mathrm{RMI}$ é a soma das probabilidades conjuntas dos grupos: $0,04 + 0,03 + 0,04 + 0,04 = 0,15$.

**Feedback Específico**  
- A. Incorreta. A maior probabilidade condicional não é a probabilidade total.
- B. Incorreta. Os grupos cobrirem todos os visitantes não significa que todos solicitaram informação.
- C. Incorreta. Probabilidades condicionais de grupos diferentes não devem ser combinadas por média simples sem ponderação.
- D. Incorreta. $0,85$ é a probabilidade total de não solicitar mais informação, não de solicitar.
- E. Correta. A soma das conjuntas é $0,15$, ou 15% dos visitantes.

### Questão 9 (0,5 ponto)

Sabendo que um visitante solicitou mais informação, qual é a probabilidade de que ele tenha visto 4 ou mais páginas?

A. $0,04$.

B. $0,10$.

C. $0,15$.

D. $0,267$, aproximadamente.

E. $0,40$.

**Feedback Geral**  
A probabilidade pedida é $P(4\text{ ou mais páginas}\mid \mathrm{RMI})$. O numerador é $P(4\text{ ou mais páginas}\cap \mathrm{RMI})=0,04$; o denominador é $P(\mathrm{RMI})=0,15$. Logo, $0,04/0,15 \approx 0,267$.

**Feedback Específico**  
- A. Incorreta. É a probabilidade conjunta, não a condicional final.
- B. Incorreta. É a proporção de visitantes que viu 4 ou mais páginas.
- C. Incorreta. É $P(\mathrm{RMI})$, o denominador.
- D. Correta. $0,04/0,15 \approx 0,267$.
- E. Incorreta. É $P(\mathrm{RMI}\mid 4\text{ ou mais páginas})$, a condicional invertida.

## Problema 3 - Variáveis aleatórias discretas

A variável aleatória discreta $X$ tem a seguinte distribuição de probabilidade $P(X=x)$. Fonte: Adaptado de Montgomery (2018), Exercício 3.S30.

| $x$ | 2 | 3 | 5 | 8 |
| ---: | ---: | ---: | ---: | ---: |
| $P(X=x)$ | 0,2 | 0,4 | 0,3 | 0,1 |

*__Notas da tabela:__ $X$ é a variável aleatória discreta; $x$ representa um valor possível de $X$; $P(X=x)$ é a probabilidade de a variável aleatória assumir o valor $x$.*

### Questão 10 (0,5 ponto)

Sobre a validade da função de probabilidade e o suporte da variável aleatória $X$, assinale a alternativa correta.

A. A distribuição é válida apenas se os valores ausentes entre $2$ e $8$ tiverem probabilidade zero explicitamente informada na tabela.

B. A distribuição é inválida, pois os valores possíveis de $X$ não são equiprováveis.

C. A distribuição é válida, pois todas as probabilidades são não negativas e somam $1$; os valores possíveis de $X$ não precisam ser consecutivos.

D. A distribuição é válida, mas somente depois de normalizar as probabilidades para que cada uma seja dividida por $4$.

E. A distribuição é válida, mas os valores não consecutivos impedem o cálculo de probabilidades acumuladas.

**Feedback Geral**  
Uma função de probabilidade discreta é válida quando todas as probabilidades são não negativas e a soma das probabilidades é igual a 1. O suporte de $X$ pode ter valores não consecutivos.

**Feedback Específico**  
- A. Incorreta. Valores não listados simplesmente não pertencem ao suporte informado.
- B. Incorreta. Uma função de probabilidade discreta não precisa ser uniforme.
- C. Correta. $0,2 + 0,4 + 0,3 + 0,1 = 1$, e o suporte pode ser $\{2,3,5,8\}$.
- D. Incorreta. As probabilidades já somam $1$; dividir por $4$ invalidaria a distribuição.
- E. Incorreta. A função acumulada pode ser calculada mesmo quando o suporte não é consecutivo.

### Questão 11 (0,5 ponto)

Com base na distribuição de $X$, assinale a alternativa correta.

A. $P(X\le 3) = 0,6$, $P(X>2,5) = 0,8$ e $P(2,7<X<5,1) = 0,4$.

B. $P(X\le 3) = 0,6$, $P(X>2,5) = 0,8$ e $P(2,7<X<5,1) = 0,3$.

C. $P(X\le 3) = 0,4$, $P(X>2,5) = 0,8$ e $P(2,7<X<5,1) = 0,7$.

D. $P(X\le 3) = 0,6$, $P(X>2,5) = 0,8$ e $P(2,7<X<5,1) = 0,7$.

E. $P(X\le 3) = 0,6$, $P(X>2,5) = 0,4$ e $P(2,7<X<5,1) = 0,7$.

**Feedback Geral**  
Para calcular probabilidades de eventos, somam-se as probabilidades dos valores de $X$ que satisfazem a condição. Em $P(2,7<X<5,1)$, entram $x=3$ e $x=5$.

**Feedback Específico**  
- A. Incorreta. Erra o intervalo aberto, pois $x=5$ também satisfaz $2,7<X<5,1$.
- B. Incorreta. Erra o intervalo aberto ao incluir apenas $x=5$.
- C. Incorreta. Erra $P(X\le 3)$ ao omitir $x=2$.
- D. Correta. $P(X\le 3)=0,2+0,4=0,6$; $P(X>2,5)=0,4+0,3+0,1=0,8$; $P(2,7<X<5,1)=0,4+0,3=0,7$.
- E. Incorreta. Erra $P(X>2,5)$ ao considerar apenas parte dos valores maiores que $2,5$.

### Questão 12 (0,5 ponto)

Qual alternativa apresenta corretamente a função acumulada $F(x)=P(X\le x)$ nos pontos do suporte?

A. $F(2)=0,2$, $F(3)=0,6$, $F(5)=0,8$, $F(8)=1,0$.

B. $F(2)=0,2$, $F(3)=0,6$, $F(5)=0,9$, $F(8)=1,0$.

C. $F(2)=0,2$, $F(3)=0,5$, $F(5)=0,9$, $F(8)=1,0$.

D. $F(2)=0,0$, $F(3)=0,6$, $F(5)=0,9$, $F(8)=1,0$.

E. $F(2)=0,2$, $F(3)=0,6$, $F(5)=1,0$, $F(8)=1,0$.

**Feedback Geral**  
A função acumulada soma as probabilidades até o valor considerado. Ela deve ser não decrescente e chegar a 1 no maior valor possível da variável.

**Feedback Específico**  
- A. Incorreta. Erra apenas o acumulado em $x=5$, pois deveria somar $0,2+0,4+0,3=0,9$.
- B. Correta. Os acumulados são $0,2$, $0,6$, $0,9$ e $1,0$.
- C. Incorreta. Erra o acumulado em $x=3$, pois deveria ser $0,2+0,4=0,6$.
- D. Incorreta. Erra o valor inicial: como $P(X=2)=0,2$, então $F(2)=0,2$.
- E. Incorreta. Erra o acumulado em $x=5$, antecipando o total $1,0$ antes do maior valor do suporte.

### Questão 13 (0,5 ponto)

O valor esperado $E(X)$ de $X$ e sua interpretação correta são:

A. $E(X)=4,5$; é a média simples dos valores possíveis de $X$, sem ponderação pelas probabilidades.

B. $E(X)=3,1$; é obtido usando apenas os valores $x=2$, $x=3$ e $x=5$.

C. $E(X)=3$; é o valor mais provável de $X$.

D. $E(X)=3,9$; é o valor mais provável da distribuição.

E. $E(X)=3,9$; é a média teórica de longo prazo, não necessariamente um valor possível de $X$.

**Feedback Geral**  
A esperança é calculada por $E(X)=\sum_x xP(X=x)$. Ela representa uma média teórica de longo prazo e não precisa ser um valor possível da variável.

**Feedback Específico**  
- A. Incorreta. Usa média não ponderada dos valores possíveis, ignorando probabilidades.
- B. Incorreta. Omite o valor $x=8$ no cálculo da esperança.
- C. Incorreta. $3$ é o valor mais provável, mas não a esperança.
- D. Incorreta. O valor esperado é $3,9$, mas ele não é o valor mais provável nem precisa pertencer ao suporte.
- E. Correta. $2\cdot 0,2 + 3\cdot 0,4 + 5\cdot 0,3 + 8\cdot 0,1 = 3,9$.

### Questão 14 (0,5 ponto)

Com base na distribuição de $X$, calcule $E(X)$, $E(X^2)$ e a variância $\operatorname{Var}(X)$.

Qual alternativa apresenta corretamente a variância $\operatorname{Var}(X)$ e sua interpretação?

A. $\operatorname{Var}(X)=18,3$; ela é obtida pela soma de $x^2P(X=x)$.

B. $\operatorname{Var}(X)=14,4$; ela é obtida por $E(X^2)-E(X)$.

C. $\operatorname{Var}(X)=3,09$; ela mede dispersão em torno da esperança, em unidade ao quadrado.

D. $\operatorname{Var}(X)=3,09$; ela mede dispersão em torno da esperança, na mesma unidade de $X$.

E. $\operatorname{Var}(X)=1,76$; ela mede dispersão em torno da esperança, em unidade ao quadrado.

**Feedback Geral**  
A variância pode ser calculada por $\operatorname{Var}(X)=E(X^2)-[E(X)]^2$. Aqui, $18,3 - 3,9^2 = 18,3 - 15,21 = 3,09$. O desvio-padrão seria a raiz quadrada da variância.

**Feedback Específico**  
- A. Incorreta. Esse é $E(X^2)$, não a variância.
- B. Incorreta. Subtrai $E(X)$ em vez de subtrair $[E(X)]^2$.
- C. Correta. A variância é $3,09$ e mede dispersão em torno da esperança.
- D. Incorreta. O valor da variância está correto, mas sua unidade é quadrática, não a mesma unidade de $X$.
- E. Incorreta. $1,76$ é aproximadamente o desvio-padrão, não a variância.

## Gabarito

| Questão | Alternativa correta |
| ---: | :---: |
| 1 | C |
| 2 | D |
| 3 | B |
| 4 | A |
| 5 | A |
| 6 | A |
| 7 | C |
| 8 | E |
| 9 | D |
| 10 | C |
| 11 | D |
| 12 | B |
| 13 | E |
| 14 | C |
