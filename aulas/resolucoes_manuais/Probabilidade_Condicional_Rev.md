# Revisão conceitual: probabilidade, probabilidade condicional, probabilidade total e Bayes

Este material resume os conceitos necessários para resolver problemas de probabilidade do capítulo 3 de Pinheiro et al. (2009), com ênfase em eventos, complemento, união, interseção, independência, probabilidade condicional, probabilidade total, Teorema de Bayes, tabelas e árvores de probabilidades.

## 1. Experimento aleatório, espaço amostral e evento

Um experimento aleatório é uma situação cujo resultado não pode ser previsto com certeza antes de ocorrer, embora os resultados possíveis possam ser descritos.

| Termo | Significado |
| --- | --- |
| Experimento aleatório | Processo com resultado incerto |
| Espaço amostral $\Omega$ | Conjunto de todos os resultados possíveis |
| Evento $A$ | Subconjunto de $\Omega$ |
| Evento complementar $A^c$ | Evento formado pelos resultados em que $A$ não ocorre |

Exemplo: no lançamento de um dado comum,

$$
\Omega = \{1,2,3,4,5,6\}
$$

Se $A$ é o evento "resultado par", então:

$$
A = \{2,4,6\}
$$

e:

$$
A^c = \{1,3,5\}
$$

## 2. Probabilidade clássica

Quando os resultados são finitos e equiprováveis, a probabilidade de um evento é:

$$
P(A)=\frac{n(A)}{n(\Omega)}
$$

onde:

| Símbolo | Significado |
| --- | --- |
| $n(A)$ | Número de resultados favoráveis ao evento $A$ |
| $n(\Omega)$ | Número total de resultados possíveis |

Exemplo: ao lançar um dado equilibrado, a probabilidade de obter número par é:

$$
P(A)=\frac{3}{6}=0{,}5
$$

## 3. Complemento

O evento complementar representa a não ocorrência de um evento.

$$
P(A^c)=1-P(A)
$$

Essa regra é útil quando é mais fácil calcular a probabilidade de o evento não ocorrer.

Exemplo: se a probabilidade de uma pessoa comparecer a uma consulta é $0{,}90$, então a probabilidade de não comparecer é:

$$
P(\text{não comparece})=1-0{,}90=0{,}10
$$

## 4. União e interseção

A união $A\cup B$ representa a ocorrência de pelo menos um dos eventos.

$$
A\cup B = \text{ocorre A, ou B, ou ambos}
$$

A interseção $A\cap B$ representa a ocorrência simultânea dos dois eventos.

$$
A\cap B = \text{ocorrem A e B ao mesmo tempo}
$$

A regra geral da união é:

$$
P(A\cup B)=P(A)+P(B)-P(A\cap B)
$$

O termo $P(A\cap B)$ é subtraído porque os casos em que $A$ e $B$ ocorrem juntos foram contados duas vezes na soma $P(A)+P(B)$.

## 5. Eventos mutuamente exclusivos

Dois eventos são mutuamente exclusivos quando não podem ocorrer ao mesmo tempo.

$$
A\cap B=\varnothing
$$

Nesse caso:

$$
P(A\cap B)=0
$$

e a regra da união fica:

$$
P(A\cup B)=P(A)+P(B)
$$

Ponto crítico: eventos mutuamente exclusivos não são o mesmo que eventos independentes. Se dois eventos não podem ocorrer juntos, a ocorrência de um elimina a possibilidade de ocorrência do outro.

## 6. Probabilidade condicional

A probabilidade condicional mede a chance de um evento ocorrer quando já se sabe que outro evento ocorreu.

$$
P(B\mid A)=\frac{P(A\cap B)}{P(A)}, \quad P(A)>0
$$

Leitura:

$$
P(B\mid A) = \text{probabilidade de B dado que A ocorreu}
$$

O evento informado depois da barra vertical define o novo universo de referência.

| Expressão | Leitura | Universo de referência |
| --- | --- | --- |
| $P(B\mid A)$ | Probabilidade de $B$ dado $A$ | Apenas os casos em que $A$ ocorreu |
| $P(A\mid B)$ | Probabilidade de $A$ dado $B$ | Apenas os casos em que $B$ ocorreu |

Ponto crítico:

$$
P(B\mid A) \neq P(A\mid B)
$$

em geral.

## 7. Regra do produto

A fórmula da probabilidade condicional pode ser reorganizada para calcular a probabilidade conjunta:

$$
P(A\cap B)=P(B\mid A)P(A)
$$

Também vale:

$$
P(A\cap B)=P(A\mid B)P(B)
$$

Essa regra é a base das árvores de probabilidades. Em uma árvore, a probabilidade de um caminho completo é obtida multiplicando as probabilidades dos ramos.

## 8. Independência

Dois eventos são independentes quando a ocorrência de um não altera a probabilidade do outro.

Formalmente:

$$
P(A\cap B)=P(A)P(B)
$$

Equivalente a:

$$
P(A\mid B)=P(A)
$$

e:

$$
P(B\mid A)=P(B)
$$

Ponto crítico: independência não deve ser assumida automaticamente. Ela precisa vir do enunciado, do desenho do experimento ou de uma justificativa substantiva.

## 9. Probabilidade total

A probabilidade total é usada quando um evento pode ocorrer por diferentes caminhos ou grupos.

Se $A_1,A_2,\ldots,A_m$ formam uma partição do espaço amostral, então:

$$
P(B)=P(B\mid A_1)P(A_1)+P(B\mid A_2)P(A_2)+\cdots+P(B\mid A_m)P(A_m)
$$

Uma partição significa que os eventos:

- cobrem todas as possibilidades relevantes;
- não se sobrepõem;
- têm probabilidades que somam 1.

Exemplo de estrutura:

| Grupo | $P(\text{grupo})$ | $P(B\mid\text{grupo})$ | $P(\text{grupo e }B)$ |
| --- | ---: | ---: | ---: |
| $A_1$ | $P(A_1)$ | $P(B\mid A_1)$ | $P(A_1)P(B\mid A_1)$ |
| $A_2$ | $P(A_2)$ | $P(B\mid A_2)$ | $P(A_2)P(B\mid A_2)$ |
| $A_m$ | $P(A_m)$ | $P(B\mid A_m)$ | $P(A_m)P(B\mid A_m)$ |
| **Total** | **1** |  | **$P(B)$** |

## 10. Teorema de Bayes

O Teorema de Bayes permite inverter uma probabilidade condicional.

Se $A_1,A_2,\ldots,A_m$ formam uma partição, então:

$$
P(A_i\mid B)=
\frac{P(B\mid A_i)P(A_i)}
{P(B\mid A_1)P(A_1)+P(B\mid A_2)P(A_2)+\cdots+P(B\mid A_m)P(A_m)}
$$

Como o denominador é $P(B)$, a fórmula também pode ser escrita como:

$$
P(A_i\mid B)=
\frac{P(A_i\cap B)}{P(B)}
$$

Leitura:

- antes de observar $B$, a probabilidade de $A_i$ é $P(A_i)$;
- depois de observar $B$, a probabilidade é atualizada para $P(A_i\mid B)$;
- a atualização depende de quão provável era observar $B$ dentro de cada grupo $A_i$.

## 11. Tabela de probabilidades conjuntas

Uma tabela de probabilidades conjuntas mostra a decomposição do problema em partes que podem ser somadas ou condicionadas.

Modelo geral:

| Grupo | $P(\text{grupo})$ | $P(\text{evento}\mid\text{grupo})$ | $P(\text{grupo e evento})$ |
| --- | ---: | ---: | ---: |
| Grupo 1 |  |  |  |
| Grupo 2 |  |  |  |
| Grupo 3 |  |  |  |
| **Total** | **1** |  | **$P(\text{evento})$** |

Depois de montar a coluna conjunta, duas operações ficam claras:

1. Para obter a probabilidade total do evento, somam-se as probabilidades conjuntas.
2. Para obter a composição dos casos em que o evento ocorreu, divide-se cada probabilidade conjunta pelo total do evento.

## 12. Árvore de probabilidades

A árvore de probabilidades organiza o problema em etapas.

Modelo:

```text
Início
├── Grupo 1: P(Grupo 1)
│   ├── Evento: P(Evento | Grupo 1)
│   └── Não evento: P(Não evento | Grupo 1)
│
├── Grupo 2: P(Grupo 2)
│   ├── Evento: P(Evento | Grupo 2)
│   └── Não evento: P(Não evento | Grupo 2)
│
└── Grupo 3: P(Grupo 3)
    ├── Evento: P(Evento | Grupo 3)
    └── Não evento: P(Não evento | Grupo 3)
```

Em uma árvore:

- multiplica-se ao longo dos ramos;
- soma-se entre caminhos alternativos;
- condiciona-se dividindo o ramo de interesse pelo total dos ramos compatíveis com a informação observada.

## 13. Fórmulas para planilha

Para problemas com grupos e probabilidades condicionais, uma estrutura eficiente é:

| Coluna | Conteúdo | Fórmula típica |
| --- | --- | --- |
| A | Grupo | preenchimento manual |
| B | $P(\text{grupo})$ | preenchimento manual |
| C | $P(\text{evento}\mid\text{grupo})$ | preenchimento manual |
| D | $P(\text{não evento}\mid\text{grupo})$ | `=1-C2` |
| E | $P(\text{grupo e evento})$ | `=B2*C2` |
| F | $P(\text{grupo e não evento})$ | `=B2*D2` |
| G | $P(\text{grupo}\mid\text{evento})$ | `=E2/SUM(E:E)` |
| H | $P(\text{grupo}\mid\text{não evento})$ | `=F2/SUM(F:F)` |

Em planilhas de avaliação, é melhor evitar apenas a resposta final. A tabela obriga o estudante a mostrar:

- quais são os grupos;
- quais são as probabilidades condicionais dadas;
- quais complementos foram calculados;
- quais probabilidades conjuntas foram formadas;
- qual denominador foi usado na probabilidade condicional final.

## 14. Erros comuns

| Erro | Por que é problemático |
| --- | --- |
| Confundir $P(A\mid B)$ com $P(B\mid A)$ | São probabilidades condicionais com universos de referência diferentes. |
| Somar probabilidades condicionais de grupos diferentes | Percentuais condicionais não podem ser somados sem ponderação pelos tamanhos dos grupos. |
| Ignorar a probabilidade inicial do grupo | Bayes exige combinar a chance do grupo com a chance do evento dentro do grupo. |
| Assumir independência sem justificativa | Independência é uma condição forte e deve vir do problema ou de uma hipótese explícita. |
| Usar o denominador errado | Em probabilidade condicional, o denominador é sempre a probabilidade do evento que aparece depois da barra vertical. |
| Tratar eventos mutuamente exclusivos como independentes | Eventos mutuamente exclusivos com probabilidades positivas não são independentes. |

## 15. Checklist de resolução

Antes de calcular:

- identifique o evento pedido;
- identifique se há condição dada;
- defina o universo de referência;
- verifique se há grupos ou caminhos alternativos;
- monte tabela ou árvore quando houver probabilidades condicionais por grupo.

Durante o cálculo:

- use complemento quando for mais simples calcular a não ocorrência;
- multiplique ao longo dos ramos;
- some caminhos alternativos;
- divida pelo total observado quando a pergunta for "dado que".

Depois do cálculo:

- interprete o resultado em linguagem comum;
- confira se a probabilidade está entre 0 e 1;
- verifique se probabilidades de categorias exaustivas somam 1;
- confirme se o denominador usado corresponde ao evento condicionado.

## 16. Síntese

| Situação | Ferramenta adequada |
| --- | --- |
| Resultados equiprováveis | Probabilidade clássica |
| Evento "não ocorre" | Complemento |
| "A ou B" | União |
| "A e B" | Interseção |
| Informação adicional já ocorreu | Probabilidade condicional |
| Evento pode ocorrer por vários grupos | Probabilidade total |
| Quer inverter a condição | Teorema de Bayes |
| Problema com etapas sucessivas | Árvore de probabilidades |
| Problema com grupos e percentuais condicionais | Tabela de probabilidades conjuntas |
