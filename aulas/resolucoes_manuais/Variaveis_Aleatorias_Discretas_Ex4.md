# Ex 4 - Chegadas de navios a um porto

## Enunciado

O número de chegadas de navios a um porto durante um dia segue distribuição de Poisson. Sabe-se que, considerando apenas os dias em que chegam no máximo 2 navios, em 60% desses dias chega no máximo 1 navio.

Calcule:

<ol type="a">
<li>o número médio diário de chegadas de navios;</li>
<li>considerando apenas os dias em que chegam pelo menos 2 navios, em que percentual desses dias chegam pelo menos 3 navios.</li>
</ol>

## Observação inicial e perguntas orientadoras

- A variável aleatória é $X=$ número de chegadas de navios em um dia.
- O enunciado informa que $X$ segue distribuição de Poisson.
- O item (a) não dá diretamente o parâmetro da Poisson; ele precisa ser obtido a partir de uma probabilidade condicional.
- O item (b) também é uma probabilidade condicional.

## Modelo

Se:

$$
X\sim Poisson(\mu)
$$

então:

$$
P(X=k)=\frac{e^{-\mu}\mu^k}{k!}
$$

e:

$$
E(X)=Var(X)=\mu
$$

## Item a: determinação de $\mu$

O enunciado informa:

$$
P(X\le 1\mid X\le 2)=0{,}60
$$

Pela definição de probabilidade condicional:

$$
P(X\le 1\mid X\le 2)=\frac{P(X\le 1)}{P(X\le 2)}
$$

Para a distribuição de Poisson:

$$
P(X\le 1)=e^{-\mu}(1+\mu)
$$

e:

$$
P(X\le 2)=e^{-\mu}\left(1+\mu+\frac{\mu^2}{2}\right)
$$

Logo:

$$
\frac{1+\mu}{1+\mu+\mu^2/2}=0{,}60
$$

Resolvendo:

$$
\mu=2
$$

Portanto, o número médio diário de chegadas é **2 navios por dia**.

## Item b: probabilidade condicional

Queremos:

$$
P(X\ge 3\mid X\ge 2)
$$

Pela definição de probabilidade condicional:

$$
P(X\ge 3\mid X\ge 2)
=
\frac{P(X\ge 3)}{P(X\ge 2)}
$$

Como $\mu=2$:

$$
P(X\ge 3)=1-P(X\le 2)
$$

e:

$$
P(X\ge 2)=1-P(X\le 1)
$$

Assim:

$$
P(X\ge 3\mid X\ge 2)
=
\frac{1-P(X\le 2)}{1-P(X\le 1)}
$$

Usando a Poisson com $\mu=2$:

$$
P(X\ge 3\mid X\ge 2)=0{,}5443
$$

Logo, aproximadamente **54,43%** dos dias com pelo menos 2 navios têm pelo menos 3 navios.

## Fórmulas para planilha

Com $\mu$ em uma célula, as fórmulas centrais no Google Planilhas são:

| Medida | Fórmula |
| --- | --- |
| $P(X\le 1)$ | `=POISSON(1;mu;TRUE)` |
| $P(X\le 2)$ | `=POISSON(2;mu;TRUE)` |
| $P(X\le 1\mid X\le 2)$ | `=P(X<=1)/P(X<=2)` |
| $P(X\ge 2)$ | `=1-POISSON(1;mu;TRUE)` |
| $P(X\ge 3)$ | `=1-POISSON(2;mu;TRUE)` |
| $P(X\ge 3\mid X\ge 2)$ | `=P(X>=3)/P(X>=2)` |

## Erro comum

O erro principal é tentar usar diretamente uma média arbitrária para a Poisson. O parâmetro $\mu$ precisa ser determinado a partir da condição:

$$
P(X\le 1\mid X\le 2)=0{,}60
$$
