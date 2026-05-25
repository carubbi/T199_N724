# Barbetta (2010) - Capítulo 7: Distribuições Amostrais e Estimação de Parâmetros

Fonte: `livros/Barbetta_2010  Estatística  para cursos de engenharia e informática.pdf`

## Exemplos

### Exemplo 7.1 - Proporção amostral de ônibus fora do padrão

Uma população é formada por quatro ônibus. Um deles apresenta alto índice de emissão de CO2 e os outros três estão dentro do padrão. Assim, a população pode ser representada por:

$$
\{1,0,0,0\}.
$$

O parâmetro de interesse é a proporção populacional de veículos fora do padrão.

Perguntas:

a) Calcular a proporção populacional $p$.

b) Se for retirada uma amostra aleatória simples, com reposição, de tamanho $n=2$, qual será a proporção amostral $P$?

c) Construir a distribuição de probabilidades da proporção amostral $P$.

### Exemplo 7.2 - Distribuição amostral da média

Considere novamente uma população de quatro ônibus, agora descrita pela variável:

$$
X = \text{número de defeitos graves}.
$$

Os valores populacionais são:

$$
\{2,3,4,5\}.
$$

O exemplo calcula:

- a média populacional $\mu$;
- a variância populacional $\sigma^2$;
- a distribuição da média amostral $\bar X$ para amostras de tamanho $n=2$, retiradas com reposição.

### Exemplo 7.3 - Intervalo de confiança para proporção

Na avaliação de dois sistemas computacionais, A e B, foram selecionadas 400 cargas de trabalho. O sistema A foi melhor que o sistema B em 60% dos casos.

Construir intervalos de confiança para:

$$
p = \text{proporção de vezes em que o sistema A é melhor que o sistema B}.
$$

Usar níveis de confiança de 95% e 99%.

### Exemplo 7.4 - Intervalo de confiança para média com desvio padrão conhecido

Em uma indústria de cerveja, a quantidade inserida em latas tinha média histórica de 350 ml e desvio padrão de 3 ml. Após problemas na linha de produção, suspeita-se de alteração na média.

Uma amostra de 20 latas apresentou:

$$
\bar x = 346 \text{ ml}.
$$

Construir um intervalo de confiança de 95% para a nova média $\mu$, supondo que o desvio padrão populacional permaneça $\sigma=3$ ml.

### Exemplo 7.5 - Intervalo de confiança para média com desvio padrão desconhecido

Deseja-se avaliar a dureza esperada do aço produzido sob um novo processo de têmpera. Uma amostra de dez corpos de prova apresentou, em HRc:

```text
36,4 35,7 37,2 36,5 34,9 35,2 36,3 35,8 36,6 36,9
```

Construir um intervalo de confiança para $\mu$, com nível de confiança de 95%.

## Exercícios

### Exercícios da seção 7.1

1. Refaça o Exemplo 7.1(c), considerando que a amostra seja retirada sem reposição.

2. Em um estudo sobre consumo de combustível, uma população é composta por quatro ônibus. Os consumos, em km/l, são:

```text
3,8 3,9 4,0 4,1
```

Uma amostra de dois elementos será sorteada com reposição. Verifique todas as amostras possíveis, construa a distribuição amostral do consumo médio e calcule o valor esperado e a variância.

3. Refaça o exercício anterior considerando amostragem sem reposição.

### Exercícios da seção 7.2

4. Uma fundição produz blocos para motor de caminhões. Os furos devem ter diâmetro de 100 mm, com tolerância de 5 mm. Para verificar o diâmetro médio do processo, serão medidos 36 furos, um por bloco. Suponha que o desvio padrão populacional seja conhecido e igual a 3 mm.

   a) Qual é o desvio padrão da distribuição da média amostral?

   b) Qual é a probabilidade de a média amostral diferir da média populacional em mais de 0,5 mm?

   c) Qual é a probabilidade de a média amostral diferir da média populacional em mais de 1 mm?

   d) Se alguém afirmar que a média amostral não se distanciará da média populacional em mais de 0,98 mm, qual é a probabilidade de essa pessoa acertar?

   e) Se alguém afirmar que a média amostral não se distanciará da média populacional em mais de 1,085 mm, qual é a probabilidade de essa pessoa errar?

5. Uma empresa fabricante de pastilhas para freios sabe que 1% das pastilhas do processo atual apresenta desempenho deficiente quanto ao desgaste. Em uma amostra aleatória simples de 10.000 pastilhas, qual é a probabilidade de serem encontradas 85 ou menos pastilhas com problema?

6. Sabe-se que 50% dos edifícios construídos em uma grande cidade apresentam problemas estéticos relevantes em menos de cinco anos. Em uma amostra aleatória simples de 200 edifícios com cinco anos, qual é a probabilidade de menos de 90 apresentarem problemas estéticos relevantes?

7. Algoritmos computacionais podem gerar números pseudoaleatórios uniformes no intervalo $[0,1]$. Considere a geração de 100 números $X_1,X_2,\ldots,X_{100}$ e seja $\bar X$ a média desses números.

   a) Qual é o valor esperado e a variância de $X_i$?

   b) Qual é a probabilidade de $X_i$ assumir valor no intervalo $[0{,}47,0{,}53]$?

   c) Qual é o valor esperado e a variância de $\bar X$?

   d) Qual é a distribuição de probabilidade aproximada de $\bar X$?

   e) Qual é a probabilidade de $\bar X$ assumir valor no intervalo $[0{,}47,0{,}53]$?

8. Um sistema gasta entre 20 e 24 segundos para realizar determinada tarefa. O tempo $X$ pode ser representado pela densidade:

$$
f(x)=
\begin{cases}
\dfrac{x}{4}-5, & 20<x<22,\\
6-\dfrac{x}{4}, & 22<x<24,\\
0, & \text{caso contrário.}
\end{cases}
$$

   a) Em uma rodada, qual é a probabilidade de o sistema gastar mais que 22,4 segundos?

   b) Em 30 rodadas, qual é a probabilidade de o sistema gastar, em média, mais que 22,4 segundos por rodada?

### Exercícios da seção 7.3

9. Sejam $X_1,X_2,\ldots,X_7$ uma amostra aleatória simples de uma população com média $\mu$ e desvio padrão $\sigma$. Considere os estimadores:

$$
T_1=\frac{X_1+X_2+X_3+X_4+X_5+X_6+X_7}{7},
$$

$$
T_2=\frac{X_2+X_3+X_4+X_5+X_6}{5},
$$

$$
T_3=\frac{X_2+X_3+X_4+X_5+X_6}{7}.
$$

   a) Quais estimadores são não viciados? Justifique.

   b) Qual estimador é mais eficiente entre $T_1$ e $T_2$? Justifique.

10. Em uma amostra aleatória simples com 200 edifícios com cinco anos, 55% apresentaram problemas estéticos relevantes após a entrega da obra. Construir um intervalo de confiança de 95% para a proporção populacional.

11. Uma empresa fabricante de pastilhas para freios selecionou 600 pastilhas; 18 apresentaram nível de desgaste acima do tolerado. Construir um intervalo de confiança de 95% para a proporção de pastilhas com desgaste acima do tolerado e interpretar o resultado.

12. Uma fundição retirou uma amostra de 36 blocos e mediu os diâmetros de 36 furos. A amostra apresentou média de 98,0 mm e desvio padrão de 4,0 mm. Construir um intervalo de confiança de 99% para a média do processo. Interpretar o resultado e avaliar se há evidência de que a média não está no valor ideal de 100 mm.

### Exercícios da seção 7.4

13. Um pesquisador precisa determinar o tempo médio gasto para perfurar três orifícios em uma peça de metal. Qual deve ser o tamanho da amostra para que a média amostral esteja a menos de 15 s da média populacional? Suponha desvio padrão de 40 s e nível de confiança de 95%.

14. Em caixas com 100 parafusos, deseja-se controlar o comprimento médio. Quantos parafusos devem ser examinados por caixa para garantir que a média amostral não difira da média da caixa em mais de 0,8 mm? Use nível de confiança de 95% e variância aproximada de 2 mm2.

15. Refaça o Exercício 14 supondo caixas com 1.000 parafusos.

16. Para avaliar a confiabilidade de um novo sistema de transmissão de dados, deseja-se estimar a proporção de bits transmitidos com erro em cada lote de 100 Mb. Tolera-se erro amostral máximo de 2% e, em sistemas similares, a taxa de erro é de 10%. Qual deve ser o tamanho da amostra?

   a) Use $y=0{,}95$.

   b) Use $y=0{,}99$.

## Exercícios complementares

17. Sob condições normais, foram observados os seguintes tempos de resposta, em segundos, de uma consulta a um banco de dados:

```text
28 35 43 23 62 38 34 27 32 37
```

Construa um intervalo de confiança de 99% para o tempo médio de uma consulta.

18. Fixados certos parâmetros de entrada, o tempo de execução de um algoritmo foi medido 12 vezes, em minutos:

```text
15 12 14 15 16 14 16 13 14 11 15 13
```

   a) Apresente um intervalo de confiança de 95% para o tempo médio de execução.

   b) Usando as 12 mensurações como amostra piloto, avalie o tamanho da amostra necessário para garantir erro máximo de 15 segundos, isto é, 0,25 minuto. Use $y=0{,}95$.

19. Uma empresa tem 2.400 empregados. Deseja-se extrair uma amostra para verificar o grau de satisfação com a qualidade da comida no refeitório. Em uma amostra piloto, em escala de 0 a 10, a satisfação teve média 6,5 e desvio padrão 2,0.

   a) Determine o tamanho mínimo da amostra, com erro máximo de 0,5 unidade e nível de confiança de 99%.

   b) Suponha que a amostra planejada tenha sido realizada e apresentado média 5,3 e desvio padrão 1,8. Construa um intervalo de confiança de 99% para a média populacional.

   c) Com base no item anterior, é possível afirmar, com 99% de confiança, que a nota média seria superior a cinco se a pesquisa fosse aplicada aos 2.400 funcionários?

   d) Na amostra planejada, suponha que 70 empregados atribuíram notas iguais ou superiores a cinco. Apresente um intervalo de confiança de 90% para a porcentagem populacional nessa condição.

20. Dados históricos sobre a temperatura do pasteurizador de um laticínio indicam variância aproximada de 1,8 $(^\circ C)^2$. Qual deve ser o tamanho da amostra para garantir erro máximo de 0,3°C, com nível de confiança de 95%?

21. Planeja-se extrair uma amostra aleatória simples dos 2.000 funcionários de uma empresa para avaliar satisfação com o trabalho em vários itens de uma escala de 1 a 5. Qual deve ser o tamanho da amostra para garantir erro máximo de 0,2 unidade, com nível de confiança de 95%? Use a variância teórica obtida ao supor probabilidade igual para os cinco níveis da escala.

22. Em uma pesquisa eleitoral realizada uma semana antes da eleição presidencial, qual deve ser o tamanho de uma amostra aleatória simples para garantir, com 95% de confiança, erro amostral não superior a 2%?

23. Um analista de sistemas está avaliando o desempenho de um novo programa de análise numérica. Foram fornecidas 14 operações similares, com os seguintes tempos de processamento, em milissegundos:

```text
12,0 13,5 16,0 15,7 15,8 16,5 15,0 13,1
15,2 18,1 18,5 12,3 17,5 17,0
```

   a) Calcule a média e o desvio padrão amostral do tempo de processamento.

   b) Construa um intervalo de confiança de 95% para o tempo médio de processamento.

   c) Qual deve ser o tamanho da amostra para garantir erro amostral máximo de 0,5 milissegundo, com nível de confiança de 99%?

24. Uma unidade fabril da Intel produziu 500.000 chips Pentium IV em certo período. Foram selecionados aleatoriamente 400 chips para testes.

   a) Supondo que 20 chips não tenham velocidade de processamento adequada, construa o intervalo de confiança de 95% para a proporção de chips adequados.

   b) Verifique se essa amostra é suficiente para obter um intervalo de confiança de 99%, com erro amostral máximo de 0,5%, para a proporção de chips adequados. Caso contrário, qual deveria ser o tamanho da amostra?
