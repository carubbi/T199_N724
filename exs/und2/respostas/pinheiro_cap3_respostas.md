# Respostas dos exercícios de Pinheiro et al. (2009), capítulo 3

Fonte dos enunciados: `exs/und2/pinheiro_cap3.md`

Conferência com o gabarito extraído do livro: o livro fornece respostas numéricas resumidas para os exercícios 3.2_P a 3.10_P. As respostas abaixo detalham os cálculos e interpretações usando apenas o núcleo conceitual do capítulo 3: probabilidade clássica, complemento, união, interseção, independência, probabilidade condicional, probabilidade total e Bayes.

## Respostas dos Exemplos

### Exemplo 3.1

Moeda:

$$
P(\text{cara})=\frac{1}{2}.
$$

Dado:

$$
P(6)=\frac{1}{6},
\qquad
P(\text{par})=\frac{3}{6}=\frac{1}{2}.
$$

Baralho completo sem coringas:

$$
P(\text{rei de paus})=\frac{1}{52},
\qquad
P(\text{rei})=\frac{4}{52}=\frac{1}{13}.
$$

### Exemplo 3.2

Como se trata de uma simulação de 100 lançamentos, o resultado numérico exato depende da sequência simulada. O ponto do exemplo é que a frequência relativa acumulada de caras tende a se estabilizar perto de:

$$
0{,}5.
$$

### Exemplo 3.3

Para carta que seja rei ou de paus:

$$
P(A\cup B)=P(A)+P(B)-P(A\cap B)
=\frac{4}{52}+\frac{13}{52}-\frac{1}{52}
=\frac{16}{52}.
$$

Para o dado, se $A$ é obter 5 ou mais pontos:

$$
P(A)=\frac{2}{6}.
$$

Logo:

$$
P(A^c)=1-P(A)=1-\frac{2}{6}=\frac{4}{6}.
$$

### Exemplo 3.4

Com:

$$
A=\{1,3,5\}, \qquad B=\{3,4,5,6\},
$$

temos:

$$
A\cap B=\{3,5\}.
$$

Assim:

$$
P(A\mid B)=\frac{2}{4}=\frac{1}{2}.
$$

E:

$$
P(B\mid A)=\frac{2}{3}.
$$

### Exemplo 3.5

Para duas cartas retiradas sem reposição, sendo $D_1$ o evento "primeira carta é dama" e $D_2$ o evento "segunda carta é dama":

$$
P(D_1)=\frac{4}{52}.
$$

Se a primeira carta foi dama:

$$
P(D_2\mid D_1)=\frac{3}{51}.
$$

Se a primeira carta não foi dama:

$$
P(D_2\mid D_1^c)=\frac{4}{51}.
$$

Pela probabilidade total:

$$
P(D_2)=\frac{3}{51}\cdot\frac{4}{52}
+\frac{4}{51}\cdot\frac{48}{52}
=\frac{4}{52}.
$$

### Exemplo 3.6

Fornecedores:

$$
P(A_1)=0{,}50,\quad P(A_2)=0{,}30,\quad P(A_3)=0{,}20.
$$

Taxas de defeito:

$$
P(D\mid A_1)=0{,}05,\quad P(D\mid A_2)=0{,}02,\quad P(D\mid A_3)=0{,}01.
$$

Probabilidade total de defeito:

$$
P(D)=0{,}05\cdot0{,}50+0{,}02\cdot0{,}30+0{,}01\cdot0{,}20
=0{,}033.
$$

Pelo Teorema de Bayes:

$$
P(A_1\mid D)=\frac{0{,}05\cdot0{,}50}{0{,}033}\approx0{,}76,
$$

$$
P(A_2\mid D)=\frac{0{,}02\cdot0{,}30}{0{,}033}\approx0{,}18,
$$

$$
P(A_3\mid D)=\frac{0{,}01\cdot0{,}20}{0{,}033}\approx0{,}06.
$$

### Exemplo 3.7

Em um baralho sem coringas:

$$
P(\text{valete})=\frac{4}{52},
\qquad
P(\text{copas})=\frac{13}{52},
$$

e:

$$
P(\text{valete}\cap\text{copas})=\frac{1}{52}.
$$

Como:

$$
\frac{1}{52}=\frac{4}{52}\cdot\frac{13}{52},
$$

os eventos são independentes. Também:

$$
P(\text{valete}\mid\text{copas})=\frac{1}{13}=\frac{4}{52},
$$

e:

$$
P(\text{copas}\mid\text{valete})=\frac{1}{4}=\frac{13}{52}.
$$

### Exemplo 3.8

Situação 1:

$$
P(A)=\frac{21}{36},\quad P(B)=\frac{9}{36},\quad P(A\cap B)=0.
$$

Logo:

$$
P(C)=P(A\cup B)=\frac{30}{36}.
$$

Situação 2:

$$
P(A)=\frac{1}{6},\quad P(B)=\frac{1}{6}.
$$

Como os eventos são independentes:

$$
P(C)=P(A\cap B)=\frac{1}{6}\cdot\frac{1}{6}=\frac{1}{36}.
$$

Situação 3:

$$
P(C)=P(A\cup B)=P(A)+P(B)-P(A\cap B)
=\frac{1}{6}+\frac{1}{6}-\frac{1}{36}
=\frac{11}{36}.
$$

Situação 4:

$$
P(A)=\frac{21}{36},\quad P(B)=\frac{16}{36},\quad P(A\cap B)=\frac{3}{36}.
$$

Assim:

$$
P(A\mid B)=\frac{3}{16},
\qquad
P(B\mid A)=\frac{3}{21}.
$$

E:

$$
P(A\cup B)=\frac{21}{36}+\frac{16}{36}-\frac{3}{36}
=\frac{34}{36}.
$$

### Exemplo 3.9

A aprovação exige que as três condições estejam simultaneamente em ordem:

$$
P(A)=0{,}90\cdot0{,}85\cdot0{,}80=0{,}612.
$$

Logo:

$$
P(A^c)=1-0{,}612=0{,}388.
$$

A probabilidade de exatamente uma falha é:

$$
0{,}10\cdot0{,}85\cdot0{,}80
+0{,}90\cdot0{,}15\cdot0{,}80
+0{,}90\cdot0{,}85\cdot0{,}20
=0{,}329.
$$

Portanto:

$$
P(\text{exatamente uma falha}\mid\text{reprovação})
=\frac{0{,}329}{0{,}388}
\approx0{,}848.
$$

### Exemplo 3.10

A probabilidade de sucesso é:

$$
P(S)=0{,}5\cdot0{,}8\cdot0{,}9=0{,}36.
$$

Logo:

$$
P(S^c)=0{,}64.
$$

Se houve fracasso, as probabilidades condicionais das razões são:

$$
P(\text{ligação não completada}\mid S^c)
=\frac{0{,}50}{0{,}64}
\approx0{,}781.
$$

$$
P(\text{ligação completada e Sr. X ausente}\mid S^c)
=\frac{0{,}5\cdot0{,}2}{0{,}64}
\approx0{,}156.
$$

$$
P(\text{ligação completada, Sr. X presente e executivo ausente}\mid S^c)
=\frac{0{,}5\cdot0{,}8\cdot0{,}1}{0{,}64}
\approx0{,}063.
$$

## Exercício 3.1_P

O espaço amostral é:

$$
\Omega=\{1,2,\ldots,100\}.
$$

Como todos os números são equiprováveis:

$$
P(E)=\frac{n(E)}{100}.
$$

### a)

$A\cap B$ representa os números divisíveis por 2 e por 3 ao mesmo tempo. Portanto, são os múltiplos de 6.

$A\cap C$ representa os números divisíveis por 2 e por 5 ao mesmo tempo. Portanto, são os múltiplos de 10.

$B\cap C$ representa os números divisíveis por 3 e por 5 ao mesmo tempo. Portanto, são os múltiplos de 15.

$A\cap B\cap C$ representa os números divisíveis por 2, por 3 e por 5 ao mesmo tempo. Portanto, são os múltiplos de 30.

### b)

Números divisíveis por 2:

$$
n(A)=50
$$

Logo:

$$
P(A)=\frac{50}{100}=0{,}50.
$$

Números divisíveis por 3:

$$
n(B)=33
$$

Logo:

$$
P(B)=\frac{33}{100}=0{,}33.
$$

Números divisíveis por 5:

$$
n(C)=20
$$

Logo:

$$
P(C)=\frac{20}{100}=0{,}20.
$$

Interseções:

$$
n(A\cap B)=16,\quad
n(A\cap C)=10,\quad
n(B\cap C)=6,\quad
n(A\cap B\cap C)=3.
$$

Portanto:

$$
P(A\cap B)=\frac{16}{100}=0{,}16,
$$

$$
P(A\cap C)=\frac{10}{100}=0{,}10,
$$

$$
P(B\cap C)=\frac{6}{100}=0{,}06,
$$

$$
P(A\cap B\cap C)=\frac{3}{100}=0{,}03.
$$

## Exercício 3.2_P

As três letras B, C e S podem ser ordenadas de:

$$
3\cdot 2\cdot 1=6
$$

formas diferentes. Igor tenta ordens distintas, sem repetir tentativa.

### a)

O acesso é bloqueado se a ordem correta não estiver entre as três primeiras tentativas. Como há 6 ordens possíveis e apenas 3 são testadas antes do bloqueio:

$$
P(\text{bloqueio})=\frac{3}{6}=0{,}50=50\%.
$$

### b)

Para ser autorizado na segunda tentativa, a primeira tentativa deve falhar e a segunda deve acertar:

$$
P(\text{autorizado na 2a})=
\frac{5}{6}\cdot\frac{1}{5}
=\frac{1}{6}
=0{,}1667.
$$

Logo:

$$
P(\text{autorizado na 2a})=16{,}67\%.
$$

### c)

Para ser autorizado na terceira tentativa, as duas primeiras devem falhar e a terceira deve acertar:

$$
P(\text{autorizado na 3a})=
\frac{5}{6}\cdot\frac{4}{5}\cdot\frac{1}{4}
=\frac{1}{6}
=0{,}1667.
$$

Logo:

$$
P(\text{autorizado na 3a})=16{,}67\%.
$$

### d)

O acesso é autorizado se a ordem correta estiver entre as três tentativas permitidas:

$$
P(\text{autorizado})=\frac{3}{6}=0{,}50=50\%.
$$

Equivalente:

$$
P(\text{autorizado})=1-P(\text{bloqueio})=1-0{,}50=0{,}50.
$$

## Exercício 3.3_P

Defina:

- $C$: paciente comparece;
- $U$: médico recebe chamado urgente.

Temos:

$$
P(C)=0{,}90,\quad P(C^c)=0{,}10,\quad P(U)=0{,}05.
$$

A consulta ocorre somente se o paciente comparece e o médico não recebe chamado urgente:

$$
P(\text{consulta ocorre})=P(C\cap U^c).
$$

Como os eventos relevantes são independentes:

$$
P(C\cap U^c)=P(C)P(U^c)=0{,}90\cdot 0{,}95=0{,}855.
$$

Logo, a probabilidade de a consulta não ocorrer é:

$$
P(\text{consulta não ocorre})=1-0{,}855=0{,}145.
$$

Resposta:

$$
0{,}145=14{,}5\%.
$$

## Exercício 3.4_P

Sejam $A$ e $B$ os dois eventos, com:

$$
P(A)=p,\quad P(B)=q.
$$

Como são independentes:

$$
P(A\cap B)=pq.
$$

### a)

Exatamente um evento ocorre quando ocorre $A$ sem $B$ ou ocorre $B$ sem $A$:

$$
P(\text{exatamente um})=P(A\cap B^c)+P(B\cap A^c).
$$

Pela independência:

$$
P(A\cap B^c)=p(1-q)
$$

e

$$
P(B\cap A^c)=q(1-p).
$$

Portanto:

$$
P(\text{exatamente um})=p(1-q)+q(1-p).
$$

### b)

Nenhum dos dois ocorre quando ocorrem simultaneamente $A^c$ e $B^c$:

$$
P(A^c\cap B^c)=(1-p)(1-q).
$$

## Exercício 3.5_P

Há 5 homens e 3 mulheres, totalizando 8 pessoas.

O número total de pares possíveis é:

$$
\binom{8}{2}=28.
$$

O número de pares com um homem e uma mulher é:

$$
5\cdot 3=15.
$$

Logo:

$$
P(\text{um homem e uma mulher})=\frac{15}{28}=0{,}5357.
$$

Resposta:

$$
53{,}57\%.
$$

## Exercício 3.6_P

Há 11 frações no total, sendo 5 LCO e 6 não LCO. São sorteadas 3 frações sem reposição.

### a)

É mais simples usar o complemento:

$$
P(\text{pelo menos uma LCO})=1-P(\text{nenhuma LCO}).
$$

A probabilidade de nenhuma das três frações ser LCO é:

$$
P(\text{nenhuma LCO})=
\frac{6}{11}\cdot\frac{5}{10}\cdot\frac{4}{9}
=\frac{120}{990}
=0{,}1212.
$$

Portanto:

$$
P(\text{pelo menos uma LCO})=1-0{,}1212=0{,}8788.
$$

Resposta:

$$
0{,}879.
$$

### b)

Em 20 repetições, a média esperada de experimentos com pelo menos uma LCO é:

$$
20\cdot 0{,}8788=17{,}576.
$$

Resposta:

$$
17{,}576 \text{ experimentos, em média.}
$$

## Exercício 3.7_P

Os cenários formam uma partição do espaço amostral:

$$
P(O)=0{,}4,\quad P(N)=0{,}2,\quad P(P)=0{,}4.
$$

### a)

Pela probabilidade total:

$$
P(B)=P(B\mid O)P(O)+P(B\mid N)P(N)+P(B\mid P)P(P).
$$

Assim:

$$
P(B)=0{,}6\cdot0{,}4+0{,}3\cdot0{,}2+0{,}2\cdot0{,}4
=0{,}24+0{,}06+0{,}08
=0{,}38.
$$

Para performance regular:

$$
P(R)=0{,}3\cdot0{,}4+0{,}4\cdot0{,}2+0{,}3\cdot0{,}4
=0{,}12+0{,}08+0{,}12
=0{,}32.
$$

Para performance fraca:

$$
P(F)=0{,}1\cdot0{,}4+0{,}3\cdot0{,}2+0{,}5\cdot0{,}4
=0{,}04+0{,}06+0{,}20
=0{,}30.
$$

Resposta:

$$
P(B)=0{,}38,\quad P(R)=0{,}32,\quad P(F)=0{,}30.
$$

### b)

Com base apenas nessas probabilidades, a performance boa é a categoria individual mais provável, com $38\%$. Porém, a soma das probabilidades de performance regular ou fraca é:

$$
P(R\cup F)=0{,}32+0{,}30=0{,}62.
$$

Portanto, os dados probabilísticos isolados não obrigam a decisão de compra. Eles indicam que a chance de desempenho bom é maior que a de desempenho fraco, mas a decisão de incorporar a ação à carteira depende do critério de risco do investidor e do retorno esperado, informações que não aparecem no enunciado.

## Exercício 3.8_P

Defina as áreas:

- $C$: clínica;
- $E$: empresarial;
- $O$: outras áreas;
- $I$: usa computador regularmente.

Temos:

$$
P(C)=0{,}60,\quad P(E)=0{,}20,\quad P(O)=0{,}20.
$$

E:

$$
P(I\mid C)=0{,}10,\quad P(I\mid E)=0{,}70,\quad P(I\mid O)=0{,}40.
$$

Logo:

$$
P(I^c\mid C)=0{,}90,\quad P(I^c\mid E)=0{,}30,\quad P(I^c\mid O)=0{,}60.
$$

### a)

Pela probabilidade total:

$$
P(I^c)=P(I^c\mid C)P(C)+P(I^c\mid E)P(E)+P(I^c\mid O)P(O).
$$

Substituindo:

$$
P(I^c)=0{,}90\cdot0{,}60+0{,}30\cdot0{,}20+0{,}60\cdot0{,}20
=0{,}54+0{,}06+0{,}12
=0{,}72.
$$

Resposta:

$$
72\%.
$$

### b)

Queremos:

$$
P(C\mid I^c).
$$

Pelo Teorema de Bayes:

$$
P(C\mid I^c)=\frac{P(I^c\mid C)P(C)}{P(I^c)}
=\frac{0{,}90\cdot0{,}60}{0{,}72}
=\frac{0{,}54}{0{,}72}
=0{,}75.
$$

Resposta:

$$
75\%.
$$

## Exercício 3.9_P

Defina:

- $G$: mulher está grávida;
- $T+$: teste positivo;
- $T-$: teste negativo.

Dados:

$$
P(G)=0{,}20,\quad P(G^c)=0{,}80.
$$

Sensibilidade:

$$
P(T+\mid G)=0{,}98.
$$

Especificidade:

$$
P(T-\mid G^c)=0{,}95.
$$

Assim:

$$
P(T+\mid G^c)=0{,}05
$$

e

$$
P(T-\mid G)=0{,}02.
$$

### a)

Queremos:

$$
P(G\mid T+).
$$

Pelo Teorema de Bayes:

$$
P(G\mid T+)=
\frac{P(T+\mid G)P(G)}
{P(T+\mid G)P(G)+P(T+\mid G^c)P(G^c)}.
$$

Substituindo:

$$
P(G\mid T+)=
\frac{0{,}98\cdot0{,}20}
{0{,}98\cdot0{,}20+0{,}05\cdot0{,}80}
=\frac{0{,}196}{0{,}236}
=0{,}8305.
$$

Resposta:

$$
83{,}05\%.
$$

### b)

Queremos:

$$
P(G^c\mid T-).
$$

Pelo Teorema de Bayes:

$$
P(G^c\mid T-)=
\frac{P(T-\mid G^c)P(G^c)}
{P(T-\mid G)P(G)+P(T-\mid G^c)P(G^c)}.
$$

Substituindo:

$$
P(G^c\mid T-)=
\frac{0{,}95\cdot0{,}80}
{0{,}02\cdot0{,}20+0{,}95\cdot0{,}80}
=\frac{0{,}76}{0{,}764}
=0{,}9948.
$$

Resposta:

$$
99{,}47\%.
$$

## Exercício 3.10_P

Cada camponês é escolhido com probabilidade:

$$
\frac{1}{4}=0{,}25.
$$

Se o camponês diz a verdade, Inácio segue o caminho certo. Se mente, segue o caminho errado.

### a)

Pela probabilidade total:

$$
P(\text{certo})=
P(\text{certo}\mid A)P(A)+
P(\text{certo}\mid B)P(B)+
P(\text{certo}\mid C)P(C)+
P(\text{certo}\mid D)P(D).
$$

Substituindo:

$$
P(\text{certo})=
1{,}00\cdot0{,}25+
0{,}75\cdot0{,}25+
0{,}40\cdot0{,}25+
0{,}00\cdot0{,}25.
$$

Logo:

$$
P(\text{certo})=0{,}25+0{,}1875+0{,}10+0=0{,}5375.
$$

Resposta:

$$
53{,}75\%.
$$

Também:

$$
P(\text{errado})=1-0{,}5375=0{,}4625.
$$

### b)

Queremos:

$$
P(B\mid \text{errado}).
$$

Pelo Teorema de Bayes:

$$
P(B\mid \text{errado})=
\frac{P(\text{errado}\mid B)P(B)}{P(\text{errado})}.
$$

Como B mente em $25\%$ das vezes:

$$
P(B\mid \text{errado})=
\frac{0{,}25\cdot0{,}25}{0{,}4625}
=0{,}1351.
$$

Resposta:

$$
13{,}51\%.
$$

### c)

Como C mente em $60\%$ das vezes:

$$
P(C\mid \text{errado})=
\frac{0{,}60\cdot0{,}25}{0{,}4625}
=0{,}3243.
$$

Resposta:

$$
32{,}43\%.
$$

### d)

Como D sempre mente:

$$
P(D\mid \text{errado})=
\frac{1{,}00\cdot0{,}25}{0{,}4625}
=0{,}5405.
$$

Resposta:

$$
54{,}06\%.
$$
