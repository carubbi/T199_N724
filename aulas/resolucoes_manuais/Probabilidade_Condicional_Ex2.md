# Probabilidade condicional - Perdido em uma encruzilhada

## Enunciado

Inácio chega a uma encruzilhada com duas estradas: uma leva à cidade desejada e a outra a uma fazenda. Ele não sabe qual estrada seguir. Há quatro camponeses, A, B, C e D, todos conhecedores das estradas. Inácio escolhe um deles ao acaso para perguntar.

As probabilidades de cada camponês dizer a verdade são:

| Camponês | Probabilidade de dizer a verdade |
| --- | ---: |
| A | $1{,}00$ |
| B | $0{,}75$ |
| C | $0{,}40$ |
| D | $0{,}00$ |

Calcule:

<ol type="a">
<li>a probabilidade de Inácio ser enviado pelo caminho certo;</li>
<li>sabendo que ele foi enviado pelo caminho errado, a probabilidade de que B tenha dado a informação;</li>
<li>sabendo que ele foi enviado pelo caminho errado, a probabilidade de que C tenha dado a informação;</li>
<li>sabendo que ele foi enviado pelo caminho errado, a probabilidade de que D tenha dado a informação.</li>
</ol>

## Observação inicial e perguntas orientadoras

- Como Inácio escolhe um camponês ao acaso, $P(A)=P(B)=P(C)=P(D)=1/4$.
- Se o camponês diz a verdade, Inácio é enviado pelo caminho certo.
- Se o camponês não diz a verdade, Inácio é enviado pelo caminho errado.
- O item (a) usa probabilidade total.
- Os itens (b), (c) e (d) usam probabilidade condicional: o universo passa a ser apenas o conjunto de situações em que Inácio foi enviado pelo caminho errado.

## Dados

| Camponês | $P(\text{escolhido})$ | $P(\text{certo}\mid\text{camponês})$ | $P(\text{errado}\mid\text{camponês})$ |
| --- | ---: | ---: | ---: |
| A | $0{,}25$ | $1{,}00$ | $0{,}00$ |
| B | $0{,}25$ | $0{,}75$ | $0{,}25$ |
| C | $0{,}25$ | $0{,}40$ | $0{,}60$ |
| D | $0{,}25$ | $0{,}00$ | $1{,}00$ |

## Estratégia de resolução

A estratégia mais segura é transformar a tabela original em uma tabela de probabilidades conjuntas. Isso evita confundir a probabilidade de o camponês errar com a probabilidade de ele ter sido a fonte da informação errada.

## Desenvolvimento da solução com tabela

| Camponês | $P(\text{escolhido})$ | $P(\text{certo}\mid\text{camponês})$ | $P(\text{errado}\mid\text{camponês})$ | $P(\text{camponês e certo})$ | $P(\text{camponês e errado})$ |
| --- | ---: | ---: | ---: | ---: | ---: |
| A | $0{,}25$ | $1{,}00$ | $0{,}00$ | $0{,}2500$ | $0{,}0000$ |
| B | $0{,}25$ | $0{,}75$ | $0{,}25$ | $0{,}1875$ | $0{,}0625$ |
| C | $0{,}25$ | $0{,}40$ | $0{,}60$ | $0{,}1000$ | $0{,}1500$ |
| D | $0{,}25$ | $0{,}00$ | $1{,}00$ | $0{,}0000$ | $0{,}2500$ |
| **Total** | **1,00** |  |  | **0,5375** | **0,4625** |

Para o item (a):

$$
P(\text{certo})
=
0{,}2500 + 0{,}1875 + 0{,}1000 + 0{,}0000
=
0{,}5375
=
53{,}75\%
$$

Logo:

$$
P(\text{errado}) = 1 - 0{,}5375 = 0{,}4625
$$

Para os itens condicionais:

$$
P(B\mid\text{errado})
=
\frac{P(B\cap\text{errado})}{P(\text{errado})}
=
\frac{0{,}0625}{0{,}4625}
=
0{,}1351
=
13{,}51\%
$$

$$
P(C\mid\text{errado})
=
\frac{P(C\cap\text{errado})}{P(\text{errado})}
=
\frac{0{,}1500}{0{,}4625}
=
0{,}3243
=
32{,}43\%
$$

$$
P(D\mid\text{errado})
=
\frac{P(D\cap\text{errado})}{P(\text{errado})}
=
\frac{0{,}2500}{0{,}4625}
=
0{,}5405
=
54{,}05\%
$$

## Desenvolvimento da solução com árvore de probabilidades

```text
Inácio escolhe um camponês
├── A: 25%
│   ├── Caminho certo: 100% de 25% = 25%
│   └── Caminho errado: 0% de 25% = 0%
│
├── B: 25%
│   ├── Caminho certo: 75% de 25% = 18,75%
│   └── Caminho errado: 25% de 25% = 6,25%
│
├── C: 25%
│   ├── Caminho certo: 40% de 25% = 10%
│   └── Caminho errado: 60% de 25% = 15%
│
└── D: 25%
    ├── Caminho certo: 0% de 25% = 0%
    └── Caminho errado: 100% de 25% = 25%
```

Então:

$$
P(\text{certo}) = 25\% + 18{,}75\% + 10\% + 0\% = 53{,}75\%
$$

e:

$$
P(\text{errado}) = 0\% + 6{,}25\% + 15\% + 25\% = 46{,}25\%
$$

As probabilidades condicionais são obtidas dividindo cada ramo errado pelo total de ramos errados:

$$
P(B\mid\text{errado}) = \frac{6{,}25\%}{46{,}25\%}=13{,}51\%
$$

$$
P(C\mid\text{errado}) = \frac{15\%}{46{,}25\%}=32{,}43\%
$$

$$
P(D\mid\text{errado}) = \frac{25\%}{46{,}25\%}=54{,}05\%
$$

## Fórmulas para planilha

Se a tabela usar as colunas:

| Coluna | Conteúdo |
| --- | --- |
| A | Camponês |
| B | $P(\text{escolhido})$ |
| C | $P(\text{certo}\mid\text{camponês})$ |
| D | $P(\text{errado}\mid\text{camponês})$ |
| E | $P(\text{camponês e certo})$ |
| F | $P(\text{camponês e errado})$ |
| G | $P(\text{camponês}\mid\text{errado})$ |

As fórmulas centrais são:

| Medida | Fórmula conceitual | Fórmula de planilha |
| --- | --- | --- |
| Errado dado o camponês | $1-P(\text{certo}\mid\text{camponês})$ | `=1-C2` |
| Camponês e certo | $P(\text{camponês})P(\text{certo}\mid\text{camponês})$ | `=B2*C2` |
| Camponês e errado | $P(\text{camponês})P(\text{errado}\mid\text{camponês})$ | `=B2*D2` |
| Probabilidade total de acerto | $\sum P(\text{camponês e certo})$ | `=SUM(E2:E5)` |
| Probabilidade total de erro | $\sum P(\text{camponês e errado})$ | `=SUM(F2:F5)` |
| Camponês dado erro | $\frac{P(\text{camponês e errado})}{P(\text{errado})}$ | `=F2/SUM(F2:F5)` |

## Interpretação final

A probabilidade de Inácio ser enviado pelo caminho certo é **53,75%**.

Sabendo que ele foi enviado pelo caminho errado, a origem mais provável da informação é o camponês **D**, com **54,05%**. O camponês C responde por **32,43%** dos erros e o camponês B por **13,51%**.

Esse resultado não depende apenas da tendência individual de mentir. Ele também depende da probabilidade inicial de cada camponês ser escolhido. Como todos têm a mesma chance de serem escolhidos, os ramos errados são proporcionais às probabilidades de erro de cada camponês.

## Erros comuns

| Erro | Por que está errado |
| --- | --- |
| Responder $25\%$, $60\%$ e $100\%$ nos itens condicionais | Esses valores são $P(\text{errado}\mid\text{camponês})$, não $P(\text{camponês}\mid\text{errado})$. |
| Esquecer que cada camponês tem probabilidade $1/4$ de ser escolhido | Sem essa etapa, a tabela conjunta fica incompleta. |
| Calcular apenas $P(\text{errado})$ e não normalizar pelos erros | Os itens (b), (c) e (d) pedem a composição do grupo dos casos errados. |

## Critério de correção sugerido

| Critério | Pontuação sugerida |
| --- | ---: |
| Identifica corretamente $P(\text{escolhido})=1/4$ para cada camponês | 1,5 |
| Calcula corretamente os complementos de acerto/erro | 2,0 |
| Calcula a probabilidade total de acerto | 2,0 |
| Calcula corretamente as probabilidades conjuntas de erro | 2,0 |
| Calcula corretamente as probabilidades condicionais dado erro | 2,0 |
| Interpreta a diferença entre $P(\text{erro}\mid\text{camponês})$ e $P(\text{camponês}\mid\text{erro})$ | 0,5 |
