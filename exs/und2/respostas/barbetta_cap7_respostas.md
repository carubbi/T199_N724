# Respostas dos exercícios de Barbetta (2010), capítulo 7

Fonte dos enunciados: `exs/und2/barbetta_cap7.md`

Conferência com o gabarito extraído do livro: `livros/Barbetta_2010  Estatística  para cursos de engenharia e informática.pdf`.

Observação de conferência: os resultados coincidem com o gabarito do livro. Em alguns itens, mantive casas decimais extras no desenvolvimento e arredondei a resposta final para o padrão do gabarito.

## Fórmulas usadas

### Média amostral

Se $\bar X$ é a média de uma amostra aleatória simples:

$$
E(\bar X)=\mu.
$$

Com reposição, população muito grande ou população infinita:

$$
V(\bar X)=\frac{\sigma^2}{n},
\qquad
\sigma_{\bar X}=\frac{\sigma}{\sqrt n}.
$$

Sem reposição em população finita:

$$
V(\bar X)=\frac{\sigma^2}{n}\cdot\frac{N-n}{N-1}.
$$

### Proporção amostral

Se $\hat p$ é a proporção amostral:

$$
E(\hat p)=p.
$$

Com reposição, população muito grande ou população infinita:

$$
V(\hat p)=\frac{p(1-p)}{n}.
$$

Sem reposição em população finita:

$$
V(\hat p)=\frac{p(1-p)}{n}\cdot\frac{N-n}{N-1}.
$$

### Intervalo de confiança para proporção

$$
IC(p,\gamma)=\hat p\pm z_\gamma\sqrt{\frac{\hat p(1-\hat p)}{n}}.
$$

Quando a população finita for relevante, usa-se a correção:

$$
\sqrt{\frac{N-n}{N-1}}.
$$

### Intervalo de confiança para média

Com desvio padrão populacional conhecido:

$$
IC(\mu,\gamma)=\bar x\pm z_\gamma\frac{\sigma}{\sqrt n}.
$$

Com desvio padrão populacional desconhecido:

$$
IC(\mu,\gamma)=\bar x\pm t_\gamma\frac{s}{\sqrt n}.
$$

### Tamanho de amostra

Para estimar média:

$$
n_0=\frac{z_\gamma^2\sigma^2}{E_0^2}.
$$

Para estimar proporção:

$$
n_0=\frac{z_\gamma^2p(1-p)}{E_0^2}.
$$

Quando não há informação prévia sobre $p$, usa-se $p(1-p)\le 1/4$:

$$
n_0=\frac{z_\gamma^2}{4E_0^2}.
$$

Correção para população finita:

$$
n=\frac{Nn_0}{N+n_0-1}.
$$

## Exercício 1

Na população $\{1,0,0,0\}$ há $N=4$ ônibus e apenas um fora do padrão. A amostra tem tamanho $n=2$ e é retirada sem reposição.

Se $X$ é o número de ônibus fora do padrão na amostra:

$$
P(X=0)=\frac{\binom{3}{2}}{\binom{4}{2}}=\frac{3}{6}=\frac12,
$$

$$
P(X=1)=\frac{\binom{1}{1}\binom{3}{1}}{\binom{4}{2}}=\frac{3}{6}=\frac12.
$$

Como $\hat p=X/2$, a distribuição da proporção amostral é:

| $\hat p$ | $P(\hat p)$ |
| ---: | ---: |
| 0 | $1/2$ |
| $1/2$ | $1/2$ |

## Exercício 2

População:

$$
\{3{,}8,\ 3{,}9,\ 4{,}0,\ 4{,}1\}.
$$

Com reposição e amostras ordenadas de tamanho 2, há $4^2=16$ amostras possíveis.

| $\bar x$ | Frequência | $P(\bar X=\bar x)$ |
| ---: | ---: | ---: |
| 3,80 | 1 | $1/16$ |
| 3,85 | 2 | $2/16$ |
| 3,90 | 3 | $3/16$ |
| 3,95 | 4 | $4/16$ |
| 4,00 | 3 | $3/16$ |
| 4,05 | 2 | $2/16$ |
| 4,10 | 1 | $1/16$ |

Assim:

$$
E(\bar X)=3{,}95.
$$

A variância populacional é:

$$
\sigma^2=\frac{(3{,}8-3{,}95)^2+(3{,}9-3{,}95)^2+(4{,}0-3{,}95)^2+(4{,}1-3{,}95)^2}{4}=0{,}0125.
$$

Como a amostragem é com reposição:

$$
V(\bar X)=\frac{\sigma^2}{n}=\frac{0{,}0125}{2}=0{,}00625.
$$

## Exercício 3

Sem reposição, há $4\cdot 3=12$ amostras ordenadas possíveis.

| $\bar x$ | Frequência | $P(\bar X=\bar x)$ |
| ---: | ---: | ---: |
| 3,85 | 2 | $2/12$ |
| 3,90 | 2 | $2/12$ |
| 3,95 | 4 | $4/12$ |
| 4,00 | 2 | $2/12$ |
| 4,05 | 2 | $2/12$ |

Logo:

$$
E(\bar X)=3{,}95.
$$

Com correção para população finita:

$$
V(\bar X)=\frac{0{,}0125}{2}\cdot\frac{4-2}{4-1}
=0{,}00417.
$$

## Exercício 4

Dados:

$$
n=36,\qquad \sigma=3.
$$

O erro padrão da média é:

$$
\sigma_{\bar X}=\frac{3}{\sqrt{36}}=0{,}5.
$$

### a)

Resposta: $0{,}5$ mm.

### b)

Queremos:

$$
P(|\bar X-\mu|>0{,}5).
$$

Padronizando:

$$
z=\frac{0{,}5}{0{,}5}=1.
$$

Logo:

$$
P(|Z|>1)=0{,}3174.
$$

### c)

$$
z=\frac{1}{0{,}5}=2.
$$

$$
P(|Z|>2)=0{,}0456.
$$

### d)

$$
z=\frac{0{,}98}{0{,}5}=1{,}96.
$$

$$
P(|Z|\le 1{,}96)=0{,}95.
$$

Resposta: a probabilidade de acertar é $0{,}95$.

### e)

$$
z=\frac{1{,}085}{0{,}5}=2{,}17.
$$

$$
P(|Z|>2{,}17)\approx 0{,}03.
$$

Resposta: a probabilidade de errar é aproximadamente $0{,}03$.

## Exercício 5

Se $X$ é o número de pastilhas com problema:

$$
X\sim \operatorname{Binomial}(10000,0{,}01).
$$

Como $n$ é grande, usamos aproximação normal:

$$
\mu=np=100,
\qquad
\sigma=\sqrt{np(1-p)}=\sqrt{99}.
$$

Com correção de continuidade:

$$
P(X\le 85)\approx P(X\le 85{,}5).
$$

Padronizando:

$$
z=\frac{85{,}5-100}{\sqrt{99}}\approx -1{,}46.
$$

Logo:

$$
P(X\le 85)\approx 0{,}0722.
$$

## Exercício 6

Se $X$ é o número de edifícios com problemas:

$$
X\sim \operatorname{Binomial}(200,0{,}5).
$$

Queremos $P(X<90)=P(X\le 89)$. Com aproximação normal e correção de continuidade:

$$
\mu=100,
\qquad
\sigma=\sqrt{200(0{,}5)(0{,}5)}=\sqrt{50}.
$$

$$
P(X\le 89)\approx P(X\le 89{,}5).
$$

$$
z=\frac{89{,}5-100}{\sqrt{50}}\approx -1{,}48.
$$

Logo:

$$
P(X<90)\approx 0{,}0694.
$$

## Exercício 7

Para $X_i\sim U(0,1)$:

$$
E(X_i)=\frac12,
\qquad
V(X_i)=\frac{1}{12}.
$$

### a)

Resposta: $E(X_i)=1/2$ e $V(X_i)=1/12$.

### b)

Como a distribuição é uniforme:

$$
P(0{,}47\le X_i\le 0{,}53)=0{,}53-0{,}47=0{,}06.
$$

### c)

Para $\bar X$ com $n=100$:

$$
E(\bar X)=\frac12,
\qquad
V(\bar X)=\frac{1/12}{100}=\frac{1}{1200}.
$$

### d)

Pelo teorema do limite central:

$$
\bar X\approx N\left(\frac12,\frac{1}{1200}\right).
$$

### e)

O desvio padrão de $\bar X$ é:

$$
\sigma_{\bar X}=\sqrt{\frac{1}{1200}}\approx 0{,}02887.
$$

Padronizando o limite superior:

$$
z=\frac{0{,}53-0{,}50}{0{,}02887}\approx 1{,}04.
$$

Por simetria:

$$
P(0{,}47\le \bar X\le 0{,}53)
=P(-1{,}04\le Z\le 1{,}04)
\approx 0{,}7016.
$$

## Exercício 8

A densidade é triangular entre 20 e 24, simétrica em torno de 22.

### a)

Para $22{,}4<x<24$:

$$
f(x)=6-\frac{x}{4}.
$$

Então:

$$
P(X>22{,}4)=\int_{22{,}4}^{24}\left(6-\frac{x}{4}\right)\,dx=0{,}32.
$$

### b)

Para essa distribuição:

$$
E(X)=22,
\qquad
V(X)=\frac23.
$$

Com $n=30$:

$$
\bar X\approx N\left(22,\frac{2/3}{30}\right).
$$

Padronizando:

$$
z=\frac{22{,}4-22}{\sqrt{(2/3)/30}}\approx 2{,}68.
$$

Logo:

$$
P(\bar X>22{,}4)\approx 0{,}0037.
$$

## Exercício 9

### a)

Para $T_1$:

$$
E(T_1)=\frac{7\mu}{7}=\mu.
$$

Para $T_2$:

$$
E(T_2)=\frac{5\mu}{5}=\mu.
$$

Para $T_3$:

$$
E(T_3)=\frac{5\mu}{7}\ne \mu.
$$

Resposta: $T_1$ e $T_2$ são não viciados; $T_3$ é viciado.

### b)

Entre estimadores não viciados, o mais eficiente é o de menor variância.

$$
V(T_1)=\frac{\sigma^2}{7},
\qquad
V(T_2)=\frac{\sigma^2}{5}.
$$

Como:

$$
\frac{\sigma^2}{7}<\frac{\sigma^2}{5},
$$

$T_1$ é mais eficiente.

## Exercício 10

Dados:

$$
\hat p=0{,}55,
\qquad
n=200,
\qquad
z_{95\%}=1{,}96.
$$

Margem de erro:

$$
E=1{,}96\sqrt{\frac{0{,}55(0{,}45)}{200}}\approx 0{,}069.
$$

Logo:

$$
IC(p,95\%)=0{,}55\pm 0{,}069.
$$

Resposta: $55\%\pm 6{,}9\%$.

## Exercício 11

Dados:

$$
\hat p=\frac{18}{600}=0{,}03,
\qquad
n=600.
$$

Margem de erro:

$$
E=1{,}96\sqrt{\frac{0{,}03(0{,}97)}{600}}\approx 0{,}0136.
$$

Logo:

$$
IC(p,95\%)=0{,}0300\pm 0{,}0136.
$$

Resposta: $3{,}00\%\pm 1{,}36\%$.

Interpretação: com 95% de confiança, a proporção de pastilhas com desgaste acima do tolerado está aproximadamente entre 1,64% e 4,36%.

## Exercício 12

Dados:

$$
n=36,
\qquad
\bar x=98{,}0,
\qquad
s=4{,}0.
$$

Como $\sigma$ é desconhecido, usa-se a distribuição $t$ com $gl=35$. Para 99% de confiança:

$$
t\approx 2{,}724.
$$

Margem de erro:

$$
E=2{,}724\frac{4}{\sqrt{36}}\approx 1{,}8.
$$

Logo:

$$
IC(\mu,99\%)=98{,}0\pm 1{,}8.
$$

Intervalo:

$$
(96{,}2;\ 99{,}8).
$$

Como 100 mm não pertence ao intervalo, há evidência, com 99% de confiança, de que a média do processo está abaixo do valor ideal.

## Exercício 13

Dados:

$$
\sigma=40,
\qquad
E_0=15,
\qquad
z_{95\%}=1{,}96.
$$

$$
n_0=\frac{1{,}96^2(40)^2}{15^2}\approx 27{,}32.
$$

Arredondando para cima:

$$
n=28.
$$

## Exercício 14

Dados:

$$
N=100,
\qquad
\sigma^2=2,
\qquad
E_0=0{,}8,
\qquad
z_{95\%}=1{,}96.
$$

Tamanho inicial:

$$
n_0=\frac{1{,}96^2(2)}{0{,}8^2}\approx 12{,}005.
$$

Com correção para população finita:

$$
n=\frac{100(12{,}005)}{100+12{,}005-1}\approx 10{,}81.
$$

Resposta:

$$
n=11.
$$

## Exercício 15

Agora:

$$
N=1000.
$$

Usando o mesmo $n_0\approx 12{,}005$:

$$
n=\frac{1000(12{,}005)}{1000+12{,}005-1}\approx 11{,}87.
$$

Resposta:

$$
n=12.
$$

## Exercício 16

Dados:

$$
p=0{,}10,
\qquad
1-p=0{,}90,
\qquad
E_0=0{,}02.
$$

### a)

Para 95%:

$$
n_0=\frac{1{,}96^2(0{,}10)(0{,}90)}{0{,}02^2}\approx 864{,}36.
$$

Resposta:

$$
n=865.
$$

### b)

Para 99%:

$$
n_0=\frac{2{,}576^2(0{,}10)(0{,}90)}{0{,}02^2}\approx 1493{,}20.
$$

Resposta:

$$
n=1494.
$$

## Exercício 17

Dados:

```text
28 35 43 23 62 38 34 27 32 37
```

Estatísticas amostrais:

$$
\bar x=35{,}9,
\qquad
s\approx 10{,}88,
\qquad
n=10.
$$

Para 99% de confiança e $gl=9$:

$$
t\approx 3{,}250.
$$

Margem de erro:

$$
E=3{,}250\frac{10{,}88}{\sqrt{10}}\approx 11{,}2.
$$

Resposta:

$$
IC(\mu,99\%)=35{,}9\pm 11{,}2.
$$

## Exercício 18

Dados:

```text
15 12 14 15 16 14 16 13 14 11 15 13
```

Estatísticas amostrais:

$$
\bar x=14{,}00,
\qquad
s\approx 1{,}537,
\qquad
n=12.
$$

### a)

Para 95% de confiança e $gl=11$:

$$
t\approx 2{,}201.
$$

Margem de erro:

$$
E=2{,}201\frac{1{,}537}{\sqrt{12}}\approx 0{,}98.
$$

Resposta:

$$
IC(\mu,95\%)=14{,}00\pm 0{,}98.
$$

### b)

Usando a amostra piloto e $t\approx 2{,}201$:

$$
n_0=\left(\frac{2{,}201(1{,}537)}{0{,}25}\right)^2\approx 183{,}2.
$$

Resposta:

$$
n=184.
$$

## Exercício 19

### a)

Dados:

$$
N=2400,
\qquad
s=2{,}0,
\qquad
E_0=0{,}5,
\qquad
z_{99\%}=2{,}576.
$$

Tamanho inicial:

$$
n_0=\frac{2{,}576^2(2)^2}{0{,}5^2}\approx 106{,}17.
$$

Com correção para população finita:

$$
n=\frac{2400(106{,}17)}{2400+106{,}17-1}\approx 101{,}69.
$$

Resposta:

$$
n=102.
$$

### b)

Com a amostra planejada:

$$
n=102,
\qquad
\bar x=5{,}30,
\qquad
s=1{,}8.
$$

Usando 99% de confiança e correção para população finita, a margem fica aproximadamente:

$$
E\approx 0{,}45.
$$

Resposta:

$$
IC(\mu,99\%)=5{,}30\pm 0{,}45.
$$

### c)

O intervalo do item anterior é aproximadamente:

$$
(4{,}85;\ 5{,}75).
$$

Resposta: não. Como o intervalo inclui valores menores do que 5, não há base para afirmar, com 99% de confiança, que a média populacional seja superior a 5.

### d)

Temos:

$$
\hat p=\frac{70}{102}\approx 0{,}686.
$$

Com 90% de confiança, a margem de erro é aproximadamente:

$$
E\approx 0{,}074.
$$

Resposta:

$$
IC(p,90\%)=68{,}6\%\pm 7{,}4\%.
$$

## Exercício 20

Dados:

$$
\sigma^2=1{,}8,
\qquad
E_0=0{,}3,
\qquad
z_{95\%}=1{,}96.
$$

$$
n_0=\frac{1{,}96^2(1{,}8)}{0{,}3^2}\approx 76{,}83.
$$

Resposta:

$$
n=77.
$$

## Exercício 21

Com níveis igualmente prováveis de 1 a 5:

$$
\mu=3.
$$

Variância:

$$
\sigma^2=\frac{(1-3)^2+(2-3)^2+(3-3)^2+(4-3)^2+(5-3)^2}{5}=2.
$$

Dados:

$$
N=2000,
\qquad
E_0=0{,}2,
\qquad
z_{95\%}=1{,}96.
$$

Tamanho inicial:

$$
n_0=\frac{1{,}96^2(2)}{0{,}2^2}\approx 192{,}08.
$$

Com correção para população finita:

$$
n=\frac{2000(192{,}08)}{2000+192{,}08-1}\approx 175{,}33.
$$

Resposta:

$$
n=176.
$$

## Exercício 22

Sem informação prévia sobre a proporção, usa-se:

$$
p(1-p)\le \frac14.
$$

Com nível de confiança de 95%, o livro adota $z\approx 2$. Para erro máximo de 2%:

$$
n_0=\frac{2^2}{4(0{,}02)^2}=2500.
$$

Resposta:

$$
n=2500.
$$

## Exercício 23

Dados:

```text
12,0 13,5 16,0 15,7 15,8 16,5 15,0 13,1
15,2 18,1 18,5 12,3 17,5 17,0
```

### a)

As estatísticas amostrais são:

$$
\bar x\approx 15{,}443,
\qquad
s\approx 2{,}074.
$$

### b)

Para 95% de confiança e $gl=13$:

$$
t\approx 2{,}160.
$$

Margem de erro:

$$
E=2{,}160\frac{2{,}074}{\sqrt{14}}\approx 1{,}20.
$$

Resposta:

$$
IC(\mu,95\%)=15{,}44\pm 1{,}20.
$$

### c)

Usando 99% de confiança, $t\approx 3{,}012$ e a amostra piloto:

$$
n_0=\left(\frac{3{,}012(2{,}074)}{0{,}5}\right)^2\approx 156{,}1.
$$

Resposta:

$$
n=157.
$$

## Exercício 24

### a)

Foram testados 400 chips, dos quais 20 não tinham velocidade adequada. Logo:

$$
\hat p=\frac{380}{400}=0{,}95.
$$

Margem de erro:

$$
E=1{,}96\sqrt{\frac{0{,}95(0{,}05)}{400}}\approx 0{,}021.
$$

Resposta:

$$
IC(p,95\%)=95\%\pm 2{,}1\%.
$$

### b)

Para 99% de confiança, erro máximo de 0,5% e estimativa preliminar $\hat p=0{,}95$:

$$
n_0=\frac{2{,}576^2(0{,}95)(0{,}05)}{0{,}005^2}\approx 12611{,}6.
$$

Com correção para população finita, $N=500000$:

$$
n=\frac{500000(12611{,}6)}{500000+12611{,}6-1}\approx 12297{,}1.
$$

Resposta: a amostra de 400 chips não é suficiente. O tamanho necessário é:

$$
n=12298.
$$
