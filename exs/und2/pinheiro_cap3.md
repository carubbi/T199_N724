# Pinheiro et al. (2009) - Capítulo 3: Introdução ao Cálculo de Probabilidades

Fonte: `livros/Pinheiro_2009.pdf`

Observação: os enunciados abaixo foram reorganizados e parafraseados para uso didático, preservando dados, hipóteses e itens necessários. Os exercícios resolvidos são mantidos como referência de padrão de raciocínio; as respostas detalhadas são dadas somente para os exercícios propostos.

## Fórmulas úteis

### Probabilidade clássica

Para um espaço amostral finito e equiprovável:

$$
P(A)=\frac{n(A)}{n(\Omega)}
$$

em que $n(A)$ é o número de casos favoráveis ao evento $A$ e $n(\Omega)$ é o número de resultados possíveis.

### Complemento e união

$$
P(A^c)=1-P(A)
$$

$$
P(A\cup B)=P(A)+P(B)-P(A\cap B)
$$

Se $A$ e $B$ são mutuamente exclusivos:

$$
P(A\cup B)=P(A)+P(B)
$$

### Probabilidade condicional

$$
P(B\mid A)=\frac{P(A\cap B)}{P(A)}, \quad P(A)>0
$$

Logo:

$$
P(A\cap B)=P(B\mid A)P(A)=P(A\mid B)P(B)
$$

### Probabilidade total

Se $A_1,A_2,\ldots,A_m$ formam uma partição de $\Omega$, então:

$$
P(B)=P(B\mid A_1)P(A_1)+\cdots+P(B\mid A_m)P(A_m)
$$

### Teorema de Bayes

Se $A_1,A_2,\ldots,A_m$ formam uma partição de $\Omega$, então:

$$
P(A_i\mid B)=
\frac{P(B\mid A_i)P(A_i)}
{P(B\mid A_1)P(A_1)+\cdots+P(B\mid A_m)P(A_m)}
$$

### Independência

Eventos $A$ e $B$ são independentes quando:

$$
P(A\cap B)=P(A)P(B)
$$

Nesse caso:

$$
P(A\mid B)=P(A)
$$

e

$$
P(B\mid A)=P(B)
$$

## Exemplos

### 3.1 - Moedas, dados e baralho

Aplica o conceito clássico de probabilidade a espaços amostrais simples: lançamento de moeda, lançamento de dado e retirada de carta de um baralho completo sem coringas. O objetivo é distinguir experimento aleatório, espaço amostral e evento, e calcular probabilidades como $1/2$, $1/6$, $3/6$, $1/52$ e $4/52$.

### 3.2 - Simulação de lançamentos de moeda

Usa uma simulação de 100 lançamentos de uma moeda equilibrada para mostrar que a proporção acumulada de caras varia bastante no início, mas tende a se estabilizar perto de $0{,}5$ quando o número de lançamentos aumenta. O objetivo é introduzir a ideia de estabilidade estatística da frequência relativa.

### 3.3 - Propriedades da probabilidade

Ilustra regras de união e complemento. Em um baralho, calcula a probabilidade de retirar uma carta que seja rei ou de paus, descontando a interseção. Em um dado, calcula a probabilidade complementar de obter quatro pontos ou menos a partir do evento de obter cinco pontos ou mais.

### 3.4 - Probabilidade condicional no lançamento de um dado

Usa o lançamento de um dado com os eventos $A=\{1,3,5\}$, resultado ímpar, e $B=\{3,4,5,6\}$, resultado de pelo menos 3 pontos. O objetivo é calcular $P(A\mid B)$ e $P(B\mid A)$, mostrando que a informação de que um evento ocorreu altera o espaço de referência usado no cálculo.

### 3.5 - Duas cartas sem reposição

Analisa a retirada sequencial de duas cartas de um baralho sem reposição. O ponto didático é que a probabilidade da segunda carta depende do resultado da primeira, como em $P(D_2\mid D_1)$ e $P(D_2\mid D_1^c)$.

### 3.6 - Peça defeituosa e fornecedor

Uma empresa compra peças de três fornecedores nas proporções $50\%$, $30\%$ e $20\%$. As taxas de defeito são $5\%$, $2\%$ e $1\%$, respectivamente. O exemplo calcula a probabilidade total de defeito e, depois, usa Bayes para revisar a probabilidade de origem da peça dado que ela é defeituosa.

### 3.7 - Independência em cartas de baralho

Em uma retirada de uma carta de baralho, compara os eventos "ser valete" e "ser de copas". O exemplo mostra independência quando $P(A\cap B)=P(A)P(B)$ e discute que a inclusão de coringas altera o espaço amostral e pode destruir essa independência.

### 3.8 - Quatro situações com dois dados

Com dois dados, compara quatro situações:

- $C=A\cup B$ com $A$ e $B$ mutuamente exclusivos;
- $C=A\cap B$ com $A$ e $B$ independentes;
- $C=A\cup B$ com $A$ e $B$ não mutuamente exclusivos;
- $C=A\cap B$ com $A$ e $B$ dependentes.

O objetivo é distinguir união, interseção, eventos mutuamente exclusivos, independência e uso de probabilidade condicional.

### 3.9 - Vistoria de automóveis

Um carro é aprovado apenas se passar simultaneamente em três condições: emissão de poluentes, lanternas e validade do extintor. As probabilidades de falha são $10\%$, $15\%$ e $20\%$. O exemplo calcula a probabilidade de aprovação e probabilidades condicionais associadas à reprovação.

### 3.10 - Tentativa de contato telefônico

Um executivo só consegue falar com uma pessoa se três eventos ocorrerem conjuntamente: a ligação completa, a pessoa está presente e o executivo permanece na sala. As probabilidades são $0{,}5$, $0{,}8$ e $0{,}9$. O exemplo calcula a probabilidade de sucesso e decompõe as razões de insucesso.

## Exercícios Resolvidos

### 3.1_R - Suspeita de cola em concurso público

Em uma prova com 80 questões de múltipla escolha e cinco alternativas por questão, dois candidatos marcaram a mesma alternativa em 70 questões. Dessas coincidências, 60 eram respostas corretas e 10 eram respostas erradas iguais. Sob a hipótese de que, sem cola, um candidato que não sabe a questão escolhe uma alternativa ao acaso, o exercício calcula a probabilidade de coincidência nas 10 respostas erradas e discute se a ocorrência observada é compatível com ausência de fraude.

Objetivo didático: usar produto de probabilidades independentes para avaliar a plausibilidade de uma sequência de coincidências.

### 3.2_R - Torneio de voleibol

Oito países disputam um torneio eliminatório. Na primeira rodada, alguns jogam em casa e outros fora; nas rodadas seguintes, os jogos são em campo neutro. A chance de vitória é $60\%$ em casa, $40\%$ fora e $50\%$ em campo neutro. O exercício calcula probabilidades de diferentes composições da final, como final entre países específicos, final entre um estreante em casa e um estreante fora, e conferência de que as alternativas possíveis somam probabilidade 1.

Objetivo didático: combinar eventos independentes ao longo de etapas sucessivas e verificar a soma das probabilidades de casos mutuamente exclusivos.

### 3.3_R - Detecção de infecção por HIV

Considera um teste diagnóstico em uma população de doadores de sangue, na qual a prevalência da infecção é $1/1000$. O teste tem sensibilidade $0{,}85$ e especificidade $0{,}99$. O exercício calcula $P(D+\mid T+)$, $P(D-\mid T-)$ e mostra a aplicação da regra do produto no contexto de teste diagnóstico.

Objetivo didático: aplicar probabilidade total e Bayes, mostrando que a prevalência altera fortemente a interpretação de um resultado positivo.

## Exercícios Propostos

### 3.1_P - Probabilidades em um conjunto de números inteiros

Considere o espaço amostral $\Omega$ formado pelos 100 primeiros números naturais, com todos os resultados equiprováveis e probabilidade $1/100$ para cada número.

Defina:

- $A$: números divisíveis por 2;
- $B$: números divisíveis por 3;
- $C$: números divisíveis por 5.

Responda:

a) interprete os eventos $A\cap B$, $A\cap C$, $B\cap C$ e $A\cap B\cap C$;

b) calcule $P(A)$, $P(B)$, $P(C)$, $P(A\cap B)$, $P(A\cap C)$, $P(B\cap C)$ e $P(A\cap B\cap C)$.

### 3.2_P - Código de acesso em caixa eletrônico

Para acessar uma conta em um caixa eletrônico, além da senha correta, é preciso digitar um código de três letras na ordem certa. O acesso é bloqueado se três tentativas consecutivas falharem.

Igor sabe a senha e sabe que o código é formado pelas letras B, C e S, mas não sabe a ordem correta. Ele escolhe uma ordem ao acaso; se errar, tenta outra ordem ainda não usada.

Determine a probabilidade de o acesso ser:

a) bloqueado;

b) autorizado na segunda tentativa;

c) autorizado na terceira e última tentativa;

d) autorizado em alguma das três tentativas.

### 3.3_P - Consulta médica

Um paciente tem consulta marcada. A probabilidade de ele comparecer no dia e horário marcados é $0{,}90$. A probabilidade de o médico receber um chamado urgente que o obrigue a desmarcar a consulta é $0{,}05$.

Admita que:

- os eventos "paciente não comparece" e "médico recebe chamado urgente" são independentes;
- esses são os únicos motivos que podem impedir a consulta.

Calcule a probabilidade de a consulta não ocorrer no dia e horário marcados.

### 3.4_P - Eventos independentes

Dois eventos independentes têm probabilidades de ocorrência iguais a $p$ e $q$.

Calcule:

a) a probabilidade de exatamente um dos dois eventos ocorrer;

b) a probabilidade de nenhum dos dois eventos ocorrer.

### 3.5_P - Seleção de candidatos para entrevista

Uma lista de candidatos a emprego tem cinco homens e três mulheres. Entre as oito pessoas, duas serão escolhidas ao acaso para entrevista.

Calcule a probabilidade de os dois entrevistados serem um homem e uma mulher.

### 3.6_P - Mistura de frações de óleo diesel

Há 11 frações de óleo diesel, das quais cinco são do tipo LCO (*light cycle oil*). Três frações são sorteadas ao acaso e sem reposição para retirada de amostras que comporão uma mistura.

Calcule:

a) a probabilidade de a mistura ter pelo menos uma fração LCO;

b) se esse experimento for repetido 20 vezes, em média em quantos experimentos se espera obter pelo menos uma fração LCO.

### 3.7_P - Decisão sobre investimento em ação

Um investidor avalia a compra de uma ação. Ele considera três cenários para o mercado:

| Cenário | Probabilidade |
| --- | ---: |
| Otimista ($O$) | $0{,}4$ |
| Neutro ($N$) | $0{,}2$ |
| Pessimista ($P$) | $0{,}4$ |

Em cada cenário, a performance da ação pode ser boa ($B$), regular ($R$) ou fraca ($F$), com as probabilidades condicionais:

| Cenário | $P(B\mid\text{cenário})$ | $P(R\mid\text{cenário})$ | $P(F\mid\text{cenário})$ |
| --- | ---: | ---: | ---: |
| Otimista ($O$) | $0{,}6$ | $0{,}3$ | $0{,}1$ |
| Neutro ($N$) | $0{,}3$ | $0{,}4$ | $0{,}3$ |
| Pessimista ($P$) | $0{,}2$ | $0{,}3$ | $0{,}5$ |

Responda:

a) calcule as probabilidades de a performance da ação ser boa, regular ou fraca;

b) com base nessas probabilidades, discuta se a ação deveria ser incorporada à carteira.

### 3.8_P - Informatização entre psicólogos

Em uma grande cidade, os psicólogos se distribuem assim:

- $60\%$ atuam em clínica;
- $20\%$ atuam na área empresarial;
- $20\%$ atuam em outras áreas.

Os percentuais que usam computador regularmente no trabalho são:

- clínicos: $10\%$;
- área empresarial: $70\%$;
- outras áreas: $40\%$.

Calcule:

a) o percentual geral de psicólogos que não usam regularmente computador;

b) entre os psicólogos não informatizados, o percentual que atua em clínica.

### 3.9_P - Teste de gravidez

Um teste de gravidez tem:

- sensibilidade de $98\%$, isto é, probabilidade de teste positivo quando a mulher está grávida;
- especificidade de $95\%$, isto é, probabilidade de teste negativo quando a mulher não está grávida.

Antes do teste, uma mulher estima em $20\%$ a probabilidade de estar grávida.

Calcule:

a) a probabilidade de ela estar grávida dado que o teste deu positivo;

b) a probabilidade de ela não estar grávida dado que o teste deu negativo.

### 3.10_P - Perdido em uma encruzilhada

Inácio chega a uma encruzilhada com duas estradas: uma leva à cidade desejada e a outra a uma fazenda. Ele não sabe qual estrada seguir. Há quatro camponeses, A, B, C e D, todos conhecedores das estradas. Inácio escolhe um deles ao acaso para perguntar.

As probabilidades de cada camponês dizer a verdade são:

| Camponês | Probabilidade de dizer a verdade |
| --- | ---: |
| A | $1{,}00$ |
| B | $0{,}75$ |
| C | $0{,}40$ |
| D | $0{,}00$ |

Calcule:

a) a probabilidade de Inácio ser enviado pelo caminho certo;

b) sabendo que ele foi enviado pelo caminho errado, a probabilidade de que B tenha dado a informação;

c) sabendo que ele foi enviado pelo caminho errado, a probabilidade de que C tenha dado a informação;

d) sabendo que ele foi enviado pelo caminho errado, a probabilidade de que D tenha dado a informação.
