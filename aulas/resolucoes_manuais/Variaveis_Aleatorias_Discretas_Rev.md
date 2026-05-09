# Revisão conceitual: variáveis aleatórias discretas

Este material resume os conceitos necessários para resolver exercícios de variáveis aleatórias discretas, com base no capítulo 4 de Pinheiro et al. (2009) e, para a distribuição hipergeométrica, no capítulo 5 de Barbetta.

## 1. Variável aleatória discreta

Uma variável aleatória discreta associa valores numéricos aos resultados de um experimento aleatório e assume valores finitos ou enumeráveis.

Exemplos:

| Situação | Variável aleatória |
| --- | --- |
| Três cobranças de pênalti | $X=$ número de gols |
| Lançar dado até sair 6, com máximo de 3 tentativas | $G=$ ganho líquido do jogo |
| Amostra de placas de um lote | $X=$ número de placas defeituosas |

## 2. Função de probabilidade

Para uma variável aleatória discreta $X$:

$$
p(x)=P(X=x)
$$

Ela deve satisfazer:

$$
p(x)\ge 0
$$

e:

$$
\sum_x p(x)=1
$$

## 3. Função acumulada

A função acumulada é:

$$
F(x)=P(X\le x)
$$

Ela soma as probabilidades até determinado valor.

Exemplo:

| $x$ | 0 | 1 | 2 | 3 |
| ---: | ---: | ---: | ---: | ---: |
| $P(X=x)$ | 0,06 | 0,156 | 0,280 | 0,504 |
| $F(x)$ | 0,06 | 0,216 | 0,496 | 1,000 |

## 4. Esperança

A esperança ou valor esperado é:

$$
E(X)=\sum_x x\,p(x)
$$

Interpretação: é a média teórica de longo prazo, não necessariamente um valor possível da variável.

## 5. Esperança de uma função

Se $Y=h(X)$, então:

$$
E(Y)=E[h(X)]=\sum_x h(x)p(x)
$$

Essa ideia é importante em exercícios de ganho líquido, custo, prêmio ou transformação monetária.

## 6. Variância e desvio-padrão

A variância mede dispersão em torno da esperança:

$$
Var(X)=\sum_x (x-E(X))^2p(x)
$$

Forma equivalente:

$$
Var(X)=E(X^2)-[E(X)]^2
$$

O desvio-padrão é:

$$
DP(X)=\sqrt{Var(X)}
$$

## 7. Coeficiente de variação

Quando $E(X)\ne 0$:

$$
CV(X)=\frac{DP(X)}{E(X)}
$$

Ele mede dispersão relativa. Não deve ser usado quando a média é zero ou muito próxima de zero.

## 8. Bernoulli

Uma variável Bernoulli assume apenas 0 e 1:

$$
P(X=1)=p
$$

$$
P(X=0)=1-p
$$

Então:

$$
E(X)=p
$$

$$
Var(X)=p(1-p)
$$

## 9. Binomial

Se $X$ conta sucessos em $n$ ensaios independentes, com probabilidade constante $p$ de sucesso:

$$
X\sim Binomial(n,p)
$$

e:

$$
P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}
$$

com:

$$
k=0,1,\ldots,n
$$

Além disso:

$$
E(X)=np
$$

$$
Var(X)=np(1-p)
$$

Use binomial quando houver:

- número fixo de tentativas;
- duas categorias por tentativa, sucesso ou fracasso;
- independência entre tentativas;
- probabilidade de sucesso constante.

## 10. Hipergeométrica

A distribuição hipergeométrica é usada em amostragem sem reposição de uma população finita.

Se:

| Símbolo | Significado |
| --- | --- |
| $N$ | tamanho da população |
| $K$ | número de sucessos na população |
| $n$ | tamanho da amostra |
| $k$ | sucessos observados na amostra |

então:

$$
P(X=k)=
\frac{\binom{K}{k}\binom{N-K}{n-k}}
{\binom{N}{n}}
$$

Use hipergeométrica quando:

- a população é finita;
- a amostra é retirada sem reposição;
- o número de sucessos na população é conhecido;
- as probabilidades mudam depois de cada retirada.

## 11. Poisson

A distribuição de Poisson modela contagens em intervalos de tempo, espaço ou área.

Se $X$ conta ocorrências em um intervalo com média $\lambda$:

$$
X\sim Poisson(\lambda)
$$

e:

$$
P(X=k)=\frac{e^{-\lambda}\lambda^k}{k!}
$$

com:

$$
k=0,1,2,\ldots
$$

Além disso:

$$
E(X)=\lambda
$$

$$
Var(X)=\lambda
$$

## 12. Quando usar cada distribuição

| Situação | Distribuição recomendada |
| --- | --- |
| Uma tentativa com sucesso/fracasso | Bernoulli |
| Número de sucessos em $n$ tentativas independentes | Binomial |
| Amostra sem reposição de população finita | Hipergeométrica |
| Contagem em intervalo com taxa média | Poisson |
| Probabilidades dependem do histórico | Construir tabela de sequências |
| Ganho monetário com poucos resultados possíveis | Construir distribuição de $G$ |

## 13. Diferença entre binomial e hipergeométrica

| Aspecto | Binomial | Hipergeométrica |
| --- | --- | --- |
| Reposição | Com reposição ou população muito grande | Sem reposição |
| Independência | Sim | Não |
| Probabilidade de sucesso | Constante | Muda a cada retirada |
| Parâmetros | $n,p$ | $N,K,n$ |

Ponto crítico: se a amostra é retirada sem reposição de um lote pequeno, a hipergeométrica é mais rigorosa que a binomial.

## 14. Organização em planilha

Para uma distribuição discreta por tabela:

| Coluna | Conteúdo | Fórmula típica |
| --- | --- | --- |
| A | Valor $x$ | preenchimento manual |
| B | $P(X=x)$ | preenchimento manual ou soma de sequências |
| C | $F(x)$ | soma acumulada |
| D | $xP(X=x)$ | `=A2*B2` |
| E | $x^2P(X=x)$ | `=A2^2*B2` |

Resultados:

| Medida | Fórmula de planilha |
| --- | --- |
| Soma das probabilidades | `=SUM(B2:B5)` |
| $E(X)$ | `=SUM(D2:D5)` |
| $E(X^2)$ | `=SUM(E2:E5)` |
| $Var(X)$ | `=E(X^2)-E(X)^2` |
| $DP(X)$ | `=SQRT(Var(X))` |

Funções nativas úteis no Google Planilhas:

| Modelo | Função | Uso |
| --- | --- | --- |
| Binomial | `BINOMDIST(k; n; p; cumulativo)` | Probabilidade exata ou acumulada para número de sucessos em ensaios independentes |
| Hipergeométrica | `HYPGEOMDIST(k; n; K; N)` | Probabilidade exata em amostragem sem reposição |
| Poisson | `POISSON(k; lambda; cumulativo)` | Probabilidade exata ou acumulada para contagens em intervalo |

Observação: neste material, as fórmulas de planilha usam a sintaxe do Google Planilhas em localidade brasileira, com `;` como separador de argumentos.

## 15. Erros comuns

| Erro | Por que é problemático |
| --- | --- |
| Aplicar binomial quando as probabilidades mudam | Viola a hipótese de probabilidade constante e independência |
| Esquecer que as probabilidades devem somar 1 | A função de probabilidade fica inválida |
| Interpretar esperança como resultado garantido | Esperança é média de longo prazo |
| Usar variância sem unidade adequada | A variância fica na unidade ao quadrado; o desvio-padrão volta à unidade original |
| Usar binomial em amostragem sem reposição de lote pequeno | A hipergeométrica é o modelo correto |
