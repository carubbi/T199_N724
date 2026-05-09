# Probabilidade condicional - Informatização entre psicólogos

## Enunciado

Em uma grande cidade, os psicólogos se distribuem assim:

- $60\%$ atuam em clínica;
- $20\%$ atuam na área empresarial;
- $20\%$ atuam em outras áreas.

Os percentuais que usam computador regularmente no trabalho são:

- clínicos: $10\%$;
- área empresarial: $70\%$;
- outras áreas: $40\%$.

Calcule:

<ol type="a">
<li>o percentual geral de psicólogos que não usam regularmente computador;</li>
<li>entre os psicólogos não informatizados, o percentual que atua em clínica.</li>
</ol>

## Observação inicial e perguntas orientadoras

- A informação "clínicos: 10% usam computador" significa $P(\text{usa computador}\mid\text{clínica})$, não $P(\text{clínica}\mid\text{usa computador})$.
- O item (a) pede uma probabilidade total: é preciso somar os não informatizados de todas as áreas.
- O item (b) muda o universo de referência: agora o total considerado é apenas o grupo dos não informatizados.
- A pergunta central da questão é distinguir $P(\text{não usa}\mid\text{clínica})$ de $P(\text{clínica}\mid\text{não usa})$.

## Dados

| Área de atuação | Percentual na população | Percentual que usa computador |
| --- | ---: | ---: |
| Clínica | $60\%$ | $10\%$ |
| Empresarial | $20\%$ | $70\%$ |
| Outras áreas | $20\%$ | $40\%$ |

## Estratégia de resolução

A estratégia mais segura é trabalhar com uma base hipotética de 100 psicólogos. Essa escolha não altera as probabilidades e torna visível a composição dos grupos.

## Desenvolvimento da solução com tabela

Base: 100 psicólogos.

| Área de atuação | Total | Usam computador | Não usam computador |
| --- | ---: | ---: | ---: |
| Clínica | 60 | 6 | 54 |
| Empresarial | 20 | 14 | 6 |
| Outras áreas | 20 | 8 | 12 |
| **Total** | **100** | **28** | **72** |

Para o item (a):

$$
P(\text{não usa}) = \frac{72}{100} = 0{,}72 = 72\%
$$

Para o item (b), o universo de referência passa a ser o conjunto dos psicólogos não informatizados:

$$
P(\text{clínica}\mid\text{não usa})
=
\frac{P(\text{clínica e não usa})}{P(\text{não usa})}
=
\frac{54}{72}
=
0{,}75
=
75\%
$$

## Desenvolvimento da solução com árvore de probabilidades

```text
Psicólogo
├── Clínica: 60%
│   ├── Usa computador: 10% de 60% = 6%
│   └── Não usa computador: 90% de 60% = 54%
│
├── Empresarial: 20%
│   ├── Usa computador: 70% de 20% = 14%
│   └── Não usa computador: 30% de 20% = 6%
│
└── Outras áreas: 20%
    ├── Usa computador: 40% de 20% = 8%
    └── Não usa computador: 60% de 20% = 12%
```

Então:

$$
P(\text{não usa})
=
54\% + 6\% + 12\%
=
72\%
$$

e:

$$
P(\text{clínica}\mid\text{não usa})
=
\frac{54\%}{72\%}
=
75\%
$$

## Fórmulas para planilha

Se a tabela usar as colunas:

| Coluna | Conteúdo |
| --- | --- |
| A | Área |
| B | $P(\text{área})$ |
| C | $P(\text{usa}\mid\text{área})$ |
| D | $P(\text{não usa}\mid\text{área})$ |
| E | $P(\text{área e usa})$ |
| F | $P(\text{área e não usa})$ |

As fórmulas centrais são:

| Medida | Fórmula conceitual | Fórmula de planilha |
| --- | --- | --- |
| Não usa dada a área | $1-P(\text{usa}\mid\text{área})$ | `=1-C2` |
| Área e usa | $P(\text{área})P(\text{usa}\mid\text{área})$ | `=B2*C2` |
| Área e não usa | $P(\text{área})P(\text{não usa}\mid\text{área})$ | `=B2*D2` |
| Total que não usa | $\sum P(\text{área e não usa})$ | `=SUM(F2:F4)` |
| Clínica entre não informatizados | $\frac{P(\text{clínica e não usa})}{P(\text{não usa})}$ | `=F2/SUM(F2:F4)` |

## Interpretação final

O percentual geral de psicólogos que não usam computador regularmente é **72%**. Entre os psicólogos não informatizados, **75%** atuam em clínica.

Esse resultado não significa que 75% dos clínicos não usam computador. Essa seria outra probabilidade. No problema, 90% dos clínicos não usam computador, mas 75% dos não informatizados são clínicos.

## Erros comuns

| Erro | Por que está errado |
| --- | --- |
| Responder $90\%$ no item (b) | Confunde $P(\text{não usa}\mid\text{clínica})$ com $P(\text{clínica}\mid\text{não usa})$. |
| Somar apenas os percentuais de uso | O item (a) pede quem não usa, exigindo complemento em cada área. |
| Dividir 54 por 100 no item (b) | O denominador correto é 72, pois o universo condicionado é o grupo dos não informatizados. |

## Critério de correção sugerido

| Critério | Pontuação sugerida |
| --- | ---: |
| Organiza corretamente os dados por área | 2,0 |
| Calcula os complementos de uso em cada área | 2,0 |
| Calcula corretamente o percentual geral de não informatizados | 2,0 |
| Calcula corretamente $P(\text{clínica}\mid\text{não usa})$ | 2,5 |
| Interpreta a diferença entre as probabilidades condicionais | 1,5 |
