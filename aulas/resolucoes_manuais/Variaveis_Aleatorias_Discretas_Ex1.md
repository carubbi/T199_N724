# Ex 1 - Futebol: cobrando pênaltis

## Enunciado

Um jogador cobra 3 pênaltis seguidos. Admita:

- a probabilidade de converter o primeiro é $0{,}70$;
- a probabilidade de converter o segundo é $0{,}80$ se converteu o primeiro e $0{,}60$ caso contrário;
- a probabilidade de converter o terceiro é $0{,}90$ se converteu os dois primeiros, $0{,}70$ se converteu exatamente um dos dois primeiros e $0{,}50$ se não converteu nenhum dos dois primeiros.

Seja $X$ o número total de gols feitos.

Calcule:

<ol type="a">
<li>a função de probabilidade de $X$;</li>
<li>a média e o desvio-padrão de $X$.</li>
</ol>

## Observação inicial e perguntas orientadoras

- Este problema não deve ser tratado como binomial, pois as probabilidades mudam conforme o histórico das cobranças.
- A melhor estrutura para planilha é uma tabela com as 8 sequências possíveis.
- Depois de calcular a probabilidade de cada sequência, agregam-se as sequências pelo número de gols $X$.

## Tabela de sequências

| Sequência | $X$ | $P(1ª)$ | $P(2ª\mid 1ª)$ | $P(3ª\mid 1ª,2ª)$ | Probabilidade da sequência |
| --- | ---: | ---: | ---: | ---: | ---: |
| GGG | 3 | 0,70 | 0,80 | 0,90 | 0,504 |
| GGE | 2 | 0,70 | 0,80 | 0,10 | 0,056 |
| GEG | 2 | 0,70 | 0,20 | 0,70 | 0,098 |
| GEE | 1 | 0,70 | 0,20 | 0,30 | 0,042 |
| EGG | 2 | 0,30 | 0,60 | 0,70 | 0,126 |
| EGE | 1 | 0,30 | 0,60 | 0,30 | 0,054 |
| EEG | 1 | 0,30 | 0,40 | 0,50 | 0,060 |
| EEE | 0 | 0,30 | 0,40 | 0,50 | 0,060 |
| **Total** |  |  |  |  | **1,000** |

## Função de probabilidade

| $x$ | Sequências | $P(X=x)$ |
| ---: | --- | ---: |
| 0 | EEE | 0,060 |
| 1 | GEE, EGE, EEG | 0,156 |
| 2 | GGE, GEG, EGG | 0,280 |
| 3 | GGG | 0,504 |
| **Total** |  | **1,000** |

## Média, variância e desvio-padrão

| $x$ | $P(X=x)$ | $xP(X=x)$ | $x^2P(X=x)$ |
| ---: | ---: | ---: | ---: |
| 0 | 0,060 | 0,000 | 0,000 |
| 1 | 0,156 | 0,156 | 0,156 |
| 2 | 0,280 | 0,560 | 1,120 |
| 3 | 0,504 | 1,512 | 4,536 |
| **Total** | **1,000** | **2,228** | **5,812** |

Logo:

$$
E(X)=2{,}228
$$

$$
Var(X)=E(X^2)-[E(X)]^2=5{,}812-(2{,}228)^2=0{,}848016
$$

$$
DP(X)=\sqrt{0{,}848016}=0{,}921
$$

## Fórmulas para planilha

| Medida | Fórmula de planilha |
| --- | --- |
| Probabilidade da sequência | produto das três probabilidades condicionais |
| $P(X=x)$ | soma das probabilidades das sequências com mesmo $x$ |
| $E(X)$ | `=SUM(xP(X=x))` |
| $E(X^2)$ | `=SUM(x^2P(X=x))` |
| $Var(X)$ | `=E(X^2)-E(X)^2` |
| $DP(X)$ | `=SQRT(Var(X))` |

## Erro comum

O erro mais importante é aplicar binomial com $n=3$ e algum valor fixo de $p$. Isso é tecnicamente inadequado, porque as cobranças não têm probabilidade constante de sucesso.
