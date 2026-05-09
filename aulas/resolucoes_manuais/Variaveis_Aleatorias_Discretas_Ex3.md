# Ex 3 - Placas de circuito integrado: binomial versus hipergeométrica

## Enunciado

Placas de circuito integrado são avaliadas após serem preenchidas com chips semicondutores. Considere que foi produzido um lote de 20 placas e selecionadas 5 para avaliação.

Calcule a probabilidade de encontrar pelo menos uma placa defeituosa, supondo que o lote tenha 4 defeituosas e que tenha sido realizada:

<ol type="a">
<li>uma amostragem aleatória com reposição;</li>
<li>uma amostragem aleatória sem reposição.</li>
</ol>

Fonte: Barbetta, capítulo 5.

## Observação inicial e perguntas orientadoras

- Com reposição, a probabilidade de defeito permanece constante em cada retirada. O modelo é binomial.
- Sem reposição, a composição do lote muda a cada retirada. O modelo é hipergeométrico.
- Como a pergunta pede pelo menos uma defeituosa, é mais simples calcular o complemento: nenhuma defeituosa.

## Dados

| Quantidade | Valor |
| --- | ---: |
| Tamanho do lote $N$ | 20 |
| Defeituosas no lote $K$ | 4 |
| Não defeituosas no lote $N-K$ | 16 |
| Tamanho da amostra $n$ | 5 |

## Item a: com reposição

Com reposição:

$$
X\sim Binomial\left(5,\frac{4}{20}\right)
$$

Logo:

$$
P(X\ge 1)=1-P(X=0)
$$

$$
P(X\ge 1)=1-\left(\frac{16}{20}\right)^5
$$

$$
P(X\ge 1)=1-(0{,}8)^5=0{,}6723
$$

## Item b: sem reposição

Sem reposição:

$$
X\sim Hipergeométrica(N=20,K=4,n=5)
$$

Logo:

$$
P(X\ge 1)=1-P(X=0)
$$

$$
P(X\ge 1)
=
1-
\frac{\binom{4}{0}\binom{16}{5}}
{\binom{20}{5}}
$$

$$
P(X\ge 1)=0{,}7183
$$

## Comparação

| Situação | Modelo | Probabilidade de pelo menos uma defeituosa |
| --- | --- | ---: |
| Com reposição | Binomial | 0,6723 |
| Sem reposição | Hipergeométrica | 0,7183 |

A diferença ocorre porque, sem reposição, retirar placas boas reduz o número de boas restantes no lote, aumentando a chance relativa de encontrar defeituosa nas retiradas seguintes.

## Fórmulas para planilha

| Medida | Fórmula de planilha |
| --- | --- |
| Com reposição, forma conceitual | `=1-(1-K/N)^n` |
| Com reposição, função nativa | `=1-BINOMDIST(0;n;K/N;TRUE)` |
| Sem reposição, forma conceitual | `=1-COMBIN(N-K;n)/COMBIN(N;n)` |
| Sem reposição, função nativa | `=1-HYPGEOMDIST(0;n;K;N)` |

No arquivo `.xlsx`, o Ex3 usa as funções nativas `BINOMDIST` e `HYPGEOMDIST` do Google Planilhas para explicitar os modelos estatísticos.

## Erro comum

O erro central é usar binomial nos dois itens. A binomial é adequada com reposição; sem reposição, a formulação tecnicamente correta é hipergeométrica.
