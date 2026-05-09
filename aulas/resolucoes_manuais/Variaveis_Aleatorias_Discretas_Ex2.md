# Ex 2 - Aposta

## Enunciado

Você é convidado a participar de um jogo. Deve lançar um dado até obter o primeiro 6, com no máximo 3 tentativas. Cada lançamento custa R$ 10,00. Se obtiver um 6 em até 3 tentativas, ganha um prêmio de R$ 100,00. O jogo termina quando sai o primeiro 6 ou quando as 3 tentativas acabam sem sucesso.

Calcule:

<ol type="a">
<li>a expectativa de ganho líquido e se ela é positiva;</li>
<li>qual deveria ser o prêmio para que a expectativa de ganho líquido fosse nula;</li>
<li>o desvio-padrão do ganho líquido nas condições do item b.</li>
</ol>

## Observação inicial e perguntas orientadoras

- A variável aleatória de interesse é o ganho líquido, não apenas o número de lançamentos.
- O custo depende do momento em que sai o primeiro 6.
- A expectativa positiva não significa ganho garantido em uma única rodada.

## Distribuição do ganho líquido com prêmio de R$ 100

| Resultado | Probabilidade | Ganho líquido |
| --- | ---: | ---: |
| 6 na 1ª tentativa | $\frac{1}{6}$ | 90 |
| 6 na 2ª tentativa | $\frac{5}{6}\frac{1}{6}$ | 80 |
| 6 na 3ª tentativa | $\left(\frac{5}{6}\right)^2\frac{1}{6}$ | 70 |
| nenhum 6 em 3 tentativas | $\left(\frac{5}{6}\right)^3$ | -30 |

Então:

$$
E(G)=90\frac{1}{6}
+80\frac{5}{36}
+70\frac{25}{216}
-30\frac{125}{216}
=16{,}85
$$

A expectativa de ganho líquido é positiva: aproximadamente R$ 16,85.

## Prêmio justo

Se o prêmio é $P$, os ganhos líquidos possíveis são:

| Resultado | Ganho líquido |
| --- | ---: |
| 6 na 1ª tentativa | $P-10$ |
| 6 na 2ª tentativa | $P-20$ |
| 6 na 3ª tentativa | $P-30$ |
| nenhum 6 em 3 tentativas | -30 |

Impondo $E(G)=0$, obtém-se:

$$
P=60
$$

O prêmio justo é R$ 60,00.

## Desvio-padrão com prêmio justo

Com prêmio de R$ 60,00, os ganhos líquidos são 50, 40, 30 e -30.

Como $E(G)=0$:

$$
Var(G)=50^2\frac{1}{6}
+40^2\frac{5}{36}
+30^2\frac{25}{216}
+(-30)^2\frac{125}{216}
=1263{,}89
$$

Logo:

$$
DP(G)=\sqrt{1263{,}89}=35{,}55
$$

## Fórmulas para planilha

| Medida | Fórmula de planilha |
| --- | --- |
| Probabilidade do resultado | produto das probabilidades do caminho |
| Ganho líquido | prêmio menos custos acumulados |
| Valor esperado | `=SUM(probabilidade*ganho)` |
| Prêmio justo | usar célula de prêmio e resolver para expectativa zero |
| Variância com prêmio justo | `=SUM(probabilidade*(ganho-media)^2)` |
| Desvio-padrão | `=SQRT(variancia)` |

## Erro comum

Um erro frequente é calcular apenas a probabilidade de sair pelo menos um 6 e esquecer que o ganho líquido depende da tentativa em que o 6 aparece.
