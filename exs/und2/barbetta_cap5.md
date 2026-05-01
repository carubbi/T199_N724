# Barbetta (2010) - Capítulo 5: Variáveis Aleatórias Discretas

Fonte: `livros/Barbetta_2010  Estatística  para cursos de engenharia e informática.pdf`

## Exemplos

### Exemplo 5.1 - Lançamento de um dado comum

Seja a variável aleatória $X =$ número obtido no lançamento de um dado comum. Se assumirmos o dado perfeitamente equilibrado e o lançamento imparcial, podemos alocar as seguintes probabilidades aos valores possíveis de $X$:

| Valores possíveis de $X$ | Probabilidade $p(x)$ |
| ---: | ---: |
| 1 | $1/6$ |
| 2 | $1/6$ |
| 3 | $1/6$ |
| 4 | $1/6$ |
| 5 | $1/6$ |
| 6 | $1/6$ |
| **Total** | **1** |

Ou, mais resumidamente:

$$
p(j) = \frac{1}{6}, \quad j = 1,2,3,4,5,6.
$$

### Exemplo 5.2 - Distribuição binomial com carregamentos de laranja

Uma indústria processadora de suco classifica os carregamentos de laranja que chegam a suas instalações em A, B ou C. Suponha independência entre as chegadas dos carregamentos, isto é, a classificação de um não altera a classificação dos demais. Suponha também que a probabilidade $p$ de classificação na classe A é a mesma para todos os carregamentos.

Para os próximos 4 carregamentos, seja $X$ a variável aleatória que representa o número de carregamentos classificados na classe A. Vamos calcular a probabilidade de que $X$ assuma o valor $x$, isto é, a probabilidade de que $x$ carregamentos sejam classificados na classe A, com $x = 0,1,2,3,4$.

Para cada carregamento, seja $S$ sucesso quando este for classificado na classe A; e seja $F$ fracasso quando este for classificado em outra classe.

| Valor de $X$ | Resultados possíveis | Probabilidade |
| ---: | --- | ---: |
| 0 | FFFF | $(1-p)^4$ |
| 1 | SFFF, FSFF, FFSF, FFFS | $4p(1-p)^3$ |
| 2 | SSFF, SFSF, SFFS, FSSF, FSFS, FFSS | $6p^2(1-p)^2$ |
| 3 | SSSF, SSFS, SFSS, FSSS | $4p^3(1-p)$ |
| 4 | SSSS | $p^4$ |

Explicando as probabilidades: o evento $X = 0$ ocorre quando nenhum carregamento é classificado na classe A, isto é, FFFF, cuja probabilidade é $(1-p)^4$. O evento $X = 1$ ocorre quando um carregamento for classificado na classe A, isto é, SFFF, FSFF, FFSF ou FFFS. Como cada um desses resultados tem probabilidade $p(1-p)^3$, a probabilidade do evento $X = 1$ é igual a $4p(1-p)^3$. As outras probabilidades podem ser obtidas de forma análoga.

Historicamente, 30% dos carregamentos são classificados na classe A. Podemos supor que a probabilidade $p$ de um carregamento ser classificado na classe A é $0{,}3$. Entre os quatro próximos carregamentos, calculemos a probabilidade de exatamente dois serem classificados na classe A.

Temos $n = 4$ e $p = 0{,}3$. Assim:

$$
p(x) = \binom{4}{x}(0{,}3)^x(0{,}7)^{4-x},
\quad x = 0,1,2,3,4.
$$

Em particular:

$$
p(2) = \binom{4}{2}(0{,}3)^2(0{,}7)^2
= 6(0{,}09)(0{,}49)
= 0{,}2646.
$$

Dados históricos mostram que 70% das pessoas que acessam a página p23 da internet também acessam a página p24. Obtemos, pela tabela da distribuição binomial, a probabilidade de que, nos dez próximos acessos à p23, a maioria também acesse a p24.

Temos um experimento binomial, com $n = 10$ e $p = 0{,}7$, supondo independência entre os acessos. A probabilidade de ocorrer o evento "a maioria também acessar a p24" corresponde ao evento $\{X > 5\}$:

| $n$ | $x$ | $p(x)$ para $p=0{,}70$ |
| ---: | ---: | ---: |
| 10 | 0 | 0,0000 |
| 10 | 1 | 0,0001 |
| 10 | 2 | 0,0014 |
| 10 | 3 | 0,0090 |
| 10 | 4 | 0,0368 |
| 10 | 5 | 0,1029 |
| 10 | 6 | 0,2001 |
| 10 | 7 | 0,2668 |
| 10 | 8 | 0,2335 |
| 10 | 9 | 0,1211 |
| 10 | 10 | 0,0282 |

Logo:

$$
P(X > 5) = p(6)+p(7)+p(8)+p(9)+p(10)
$$

$$
P(X > 5) = 0{,}2001+0{,}2668+0{,}2335+0{,}1211+0{,}0282 = 0{,}8497.
$$

### Exemplo 5.3 - Inspeção de placas de vídeo

Placas de vídeo são expedidas em lotes de 30 unidades. Antes que a remessa seja aprovada, um inspetor escolhe aleatoriamente cinco placas do lote e as inspeciona. Se nenhuma das placas inspecionadas for defeituosa, o lote é aprovado. Se uma ou mais forem defeituosas, todo o lote é inspecionado.

Supondo que haja três placas defeituosas no lote, qual é a probabilidade de que o controle da qualidade aponte para a inspeção total?

Seja $X$ o número de placas defeituosas na amostra. Desejamos calcular:

$$
P(X \ge 1) = 1 - P(X = 0).
$$

Usando o modelo hipergeométrico:

$$
P(X = 0)
= \frac{\binom{3}{0}\binom{30-3}{5}}{\binom{30}{5}}
= \frac{80.730}{142.506}
= 0{,}5665.
$$

Logo:

$$
P(X \ge 1) = 1 - 0{,}5665 = 0{,}4335.
$$

### Exemplo 5.4 - Consultas a um banco de dados

Supondo que as consultas num banco de dados ocorrem de forma independente e aleatória, com uma taxa média de três consultas por minuto, calculemos a probabilidade de que no próximo minuto ocorram menos do que três consultas.

Seja $X$ o número de consultas por minuto. Então:

$$
P(X < 3) = p(0) + p(1) + p(2)
= \frac{e^{-3}3^0}{0!}
+ \frac{e^{-3}3^1}{1!}
+ \frac{e^{-3}3^2}{2!}
= 0{,}4232.
$$

Usando a tabela da Poisson:

$$
P(X < 3) = P(X \le 2) = F(2) = 0{,}4232.
$$

Calculemos também a probabilidade de que nos próximos dois minutos ocorram mais do que 5 consultas. Observe que a unidade de tempo alterou de um para dois minutos. Mas, se a taxa média é de três ocorrências por minuto, então, em dois minutos, a taxa média é de seis ocorrências. Logo:

$$
P(X > 5) = 1 - P(X \le 5) = 1 - F(5) = 1 - 0{,}4457 = 0{,}5543.
$$

### Exemplo 5.5 - Aproximação da binomial pela Poisson

Seja uma linha de produção em que a taxa de itens defeituosos é de 0,5%. Calculemos a probabilidade de ocorrer mais do que quatro defeituosos, em uma amostra de 500 itens.

$$
\lambda = n \cdot p = 500 \cdot 0{,}005 = 2{,}5.
$$

Então:

$$
P(X > 4) = 1 - P(X \le 4) = 1 - F(4) = 1 - 0{,}8912 = 0{,}1088.
$$

## Exercícios

### Exercícios da seção 5.1

1. Apresente a função de probabilidade para as seguintes variáveis aleatórias:

   a) Número de caras obtido com o lançamento de uma moeda honesta.

   b) Número de caras obtido no lançamento de duas moedas honestas.

   c) Número de peças com defeito em uma amostra de duas peças, sorteadas aleatoriamente de um grande lote, em que 40% das peças são defeituosas.

   d) Número de peças com defeito em uma amostra de três peças, sorteadas aleatoriamente de um grande lote, em que 40% das peças são defeituosas.

2. Apresente, sob forma gráfica, a distribuição de probabilidades do Exercício 1(d).

3. Apresente a função de probabilidade acumulada do Exercício 1(d).

4. Calcule os valores esperados e as variâncias das distribuições de probabilidade do Exercício 1.

5. Considere que um produto pode estar perfeito (B), com defeito leve (DL) ou com defeito grave (DG). Seja a seguinte distribuição do lucro, em R$, por unidade vendida desse produto:

| Produto | $X$ | $p(x)$ |
| --- | ---: | ---: |
| B | 6 | 0,7 |
| DL | 0 | 0,2 |
| DG | -2 | 0,1 |

   a) Calcule o valor esperado e a variância do lucro.

   b) Se, com a redução de desperdícios, foi possível aumentar uma unidade no lucro de cada unidade do produto, qual é o novo valor esperado e a variância do lucro por unidade?

   c) E se o lucro duplicou, qual é o novo valor esperado e variância do lucro por unidade?

6. Certo tipo de conserva tem peso líquido médio de 900 g, com desvio padrão de 10 g. A embalagem tem peso médio de 100 g, com desvio padrão de 4 g. Suponha que o processo de enchimento das embalagens controla o peso líquido, de tal forma que se possa supor independência entre o peso líquido e o peso da embalagem. Qual é a média e o desvio padrão do peso bruto?

### Exercícios da seção 5.2.2

7. Dados históricos mostram que 5% dos itens provenientes de um fornecedor apresentam algum tipo de defeito. Considerando um lote com 20 itens, calcule a probabilidade de:

   a) haver algum item com defeito;

   b) haver exatamente dois itens defeituosos;

   c) haver mais de dois itens defeituosos;

   d) o número esperado de itens defeituosos no lote;

   e) o número esperado de itens bons.

8. Apresente o gráfico da variável aleatória do Exemplo 5.2 sob a forma de um histograma, indique a posição do valor esperado e represente $P(X > 5)$ como uma área na figura.

### Exercícios da seção 5.2.3

9. Qual é a probabilidade do Exemplo 5.3, se a inspeção completa for feita somente quando forem encontradas mais do que uma placa defeituosa na amostra?

10. Calcule o valor esperado e a variância da variável aleatória definida no Exemplo 5.3.

### Exercícios da seção 5.2.4

11. Mensagens chegam a um servidor de acordo com uma distribuição de Poisson, com taxa média de cinco chegadas por minuto.

   a) Qual é a probabilidade de que duas chegadas ocorram em um minuto?

   b) Qual é a probabilidade de que uma chegada ocorra em 30 segundos?

12. Em um canal de comunicação digital, a probabilidade de se receber um bit com erro é de 0,0002. Se 10.000 bits forem transmitidos por esse canal, qual é a probabilidade de que mais de quatro bits sejam recebidos com erro?

### Exercícios complementares

13. Um armazém é abastecido mensalmente, sendo que a taxa média de abastecimento é 30 unidades/dia, com desvio padrão de 3 unidades/dia. A demanda média é de 25 unidades/dia, com desvio padrão de 4 unidades/dia. Suponha que o abastecimento e a demanda sejam independentes e, além disso, a demanda e o abastecimento num dia não alteram o abastecimento e a demanda nos dias seguintes. Qual é o valor esperado e o desvio padrão do excedente de produtos, no período de um mês?

14. Suponha que 10% dos clientes que compram a crédito em uma loja deixam de pagar regularmente suas contas, ou prestações. Se, em um dia particular, a loja vende a crédito para 10 pessoas, qual é a probabilidade de que mais de 20% delas deixem de pagar regularmente as contas? Suponha que as 10 pessoas que fizeram crediário nesse dia correspondam a uma amostra aleatória de clientes potenciais desta loja.

15. Em um sistema de transmissão de dados, existe uma probabilidade igual a 0,05 de um lote de dados ser transmitido erroneamente. Foram transmitidos 20 lotes de dados para a realização de um teste de análise da confiabilidade do sistema.

   a) Qual é o modelo teórico mais adequado para esse caso? Por quê?

   b) Calcule a probabilidade de haver erro na transmissão.

   c) Calcule a probabilidade de que haja erro na transmissão em exatamente 2 dos 20 lotes de dados.

   d) Qual é o número esperado de erros no teste realizado?

16. Numa fábrica, 3% dos artigos produzidos são defeituosos. O fabricante pretende vender 4000 peças e recebeu 2 propostas:

   Proposta 1: o comprador A propõe examinar uma amostra de 80 peças. Se houver 3 ou menos defeituosas, ele paga 60 unidades monetárias (u.m.) por peça; caso contrário, ele paga 30 u.m. por peça.

   Proposta 2: o comprador B propõe examinar 40 peças. Se todas forem perfeitas, ele está disposto a pagar 65 u.m. por peça; caso contrário, ele paga 20 u.m. por peça.

   Qual é a melhor proposta? Calcule o valor esperado da venda em cada proposta.

17. O departamento de qualidade de uma empresa seleciona, aleatoriamente, alguns itens que chegam à empresa e submete-os a testes. Para avaliar um lote de transformadores de pequeno porte, o departamento de qualidade selecionou, aleatoriamente, 10 transformadores. Ele vai recomendar a aceitação do lote se não existir item defeituoso na amostra. Supondo que o processo produtivo desses transformadores gera um percentual de 3% de defeituosos, responda:

   a) Qual é a probabilidade de que o lote venha a ser aceito?

   b) Ao analisar 8 lotes de transformadores, com amostras aleatórias de 10 itens em cada lote, qual é a probabilidade de que, no máximo, um lote seja rejeitado?

18. Na comunicação entre servidores, uma mensagem é dividida em $n$ pacotes, os quais são enviados em forma de códigos. Pelo histórico da rede, sabe-se que cada pacote tem uma pequena probabilidade, igual a 0,01, de não chegar corretamente a seu destino e, além disso, o fato de um pacote não chegar ao destino não altera a probabilidade dos demais chegarem corretamente. Um programa corretivo garante o envio correto da mensagem quando o número de pacotes enviados erroneamente não passar de 10% do total de pacotes da mensagem. Qual é a probabilidade de uma mensagem composta de 20 pacotes ser enviada corretamente? Responder usando:

   a) a distribuição binomial;

   b) a distribuição de Poisson.

19. Uma central telefônica recebe, em média, 300 chamadas na hora de maior movimento, e pode processar, no máximo, 10 ligações por minuto. Utilizando a distribuição de Poisson, calcule a probabilidade de que a capacidade da mesa seja ultrapassada em dado minuto do horário de pico.

20. Um piso cerâmico tem, em média, 0,01 defeito por $m^2$. Em uma área de $10\ \text{m} \times 10\ \text{m}$ desse piso, calcule a probabilidade de ocorrer algum defeito.

21. Placas de circuito integrado são avaliadas após serem preenchidas com chips semicondutores. Considere que foi produzido um lote de 20 placas e selecionadas 5 para avaliação. Calcule a probabilidade de encontrar pelo menos uma placa defeituosa, supondo que o lote tenha 4 defeituosas e que tenha sido realizada:

   a) uma amostragem aleatória com reposição;

   b) uma amostragem aleatória sem reposição.

22. Suponha que o número de falhas em certo tipo de placa plástica tenha distribuição de Poisson, com taxa média de 0,05 defeito por $m^2$. Na construção de um barco, é necessário cobrir uma superfície de $3\ \text{m} \times 2\ \text{m}$ com essa placa.

   a) Qual é a probabilidade de que não haja falhas nessa superfície?

   b) Qual é a probabilidade de que haja mais que uma falha nessa superfície?

   c) Na construção de 5 barcos, qual é a probabilidade de que pelo menos 4 não apresentem defeito na superfície plástica?

23. Um item é vendido em lotes de 200 unidades. Normalmente o processo de fabricação gera 5% de itens defeituosos. Um comprador compra cada lote por R$ 100,00 (alternativa 1). Um outro comprador faz a seguinte proposta: de cada lote, ele escolhe uma amostra de 15 peças; se a amostra tem 0 defeituoso, ele paga R$ 200,00; 1 defeituoso, ele paga R$ 50,00; mais que 1 defeituoso, ele paga R$ 5,00 (alternativa 2). Em média, qual alternativa é mais vantajosa para o fabricante? Calcule os valores esperados das duas alternativas.

24. Na produção de rolhas de cortiça, não é possível garantir qualidade homogênea, devido às variações internas nas placas de cortiça. Em função disso, um equipamento separa as rolhas que saem da linha de produção em duas categorias: A e B. Os dados históricos mostram que 40% são classificadas como A e 60% como B. O fabricante vende por R$ 100,00 o milhar de rolhas da categoria A; e por R$ 60,00 o milhar da categoria B.

   Um comprador propõe comprar a produção diária da fábrica. Ele fará um plano de amostragem, extraindo 8 rolhas aleatoriamente. Se encontrar mais que 5 rolhas da categoria A, ele paga R$ 200,00; caso contrário, ele paga R$ 50,00. Pede-se:

   a) Qual é a probabilidade do comprador encontrar mais que 5 rolhas da classe A?

   b) Qual é o valor esperado da venda do fabricante, por milhar de rolhas vendidas, se ele aceitar a proposta do comprador? Em termos do valor esperado da venda, a proposta do comprador é mais vantajosa do que a venda separada por categoria?

   c) Qual é a variância da venda do fabricante, por milhar de rolhas vendidas, se ele aceitar a proposta do comprador?

25. Suponha que as requisições a um sistema ocorram de forma independente e que a taxa média de ocorrências é três requisições por minuto, constante no período em estudo. Calcule a probabilidade de:

   a) ocorrer mais que uma requisição no próximo minuto;

   b) ocorrer mais que uma requisição no próximo minuto, sabendo-se que é certa a ocorrência de pelo menos uma, pois você mesmo fará uma requisição no próximo minuto.
