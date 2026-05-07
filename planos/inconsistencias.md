**Inconsistências**

1. **“Manual sem fórmulas” ficou ambíguo**
   
   O plano diz “cálculo manual” usando colunas auxiliares e fórmulas aritméticas básicas. Isso é defensável, mas não é literalmente “sem fórmulas do Google Planilhas”. Na prática, ainda haverá fórmulas nas células. O correto seria dizer:

   “cálculo manual sem funções estatísticas prontas, usando apenas operações aritméticas e somatórios”.

2. **A aba conceitual pode ficar abstrata demais**
   
   Discriminar variáveis como `x_i`, `y_i`, `x̄`, `ȳ`, `r`, `a`, `b` é necessário, mas insuficiente se não houver ligação direta com os exercícios. Para a turma, cada símbolo deveria aparecer também contextualizado:

   - no Ex 1: `x = altura`, `y = peso`;
   - no Ex 2: `x = alunos`, `y = professores`.

   Sem isso, há risco de a aba conceitual virar um glossário isolado.

3. **A ordem didática ainda está incompleta**
   
   O plano pula de conceito para execução. Melhor sequência metodológica:

   1. identificar variável explicativa e variável resposta;
   2. observar o diagrama de dispersão;
   3. calcular desvios em relação às médias;
   4. calcular correlação;
   5. ajustar reta;
   6. interpretar inclinação/intercepto;
   7. analisar resíduo/outlier;
   8. validar com funções prontas.

   Essa ordem deveria aparecer explicitamente na planilha.

4. **O Ex 1 é ótimo, mas exige cuidado com o conceito de outlier**
   
   Silvio não deve ser tratado apenas como “erro” ou “valor a excluir”. Didaticamente, o ponto forte do exercício é mostrar sensibilidade da correlação e da regressão a uma observação influente.

   A planilha deve deixar claro: excluir Silvio é uma análise comparativa, não uma decisão automática de limpeza de dados.

5. **O Ex 2 pode induzir interpretação causal fraca**
   
   “Mais alunos implicam mais professores” parece intuitivo, mas a regressão aqui é associativa. O plano menciona “correlação não implica causalidade”, mas isso precisa voltar na interpretação do Ex 2. Caso contrário, a turma pode sair com uma leitura causal simplista.

6. **Falta explicitar unidade da inclinação**
   
   No Ex 2, dizer `b ≈ 0,08748` é pouco didático. A interpretação correta precisa enfatizar unidade:

   - aproximadamente `0,087 professor por aluno`;
   - ou `87,5 professores a cada 1000 alunos`.

   Essa segunda forma é muito mais compreensível.

7. **`R²` aparece sem ser conceitualmente preparado**
   
   O plano inclui `RSQ`, mas a revisão pedida foi Pearson e regressão linear simples. Incluir `R²` é bom, mas só se a aba conceitual explicar que, em regressão linear simples com intercepto, `R² = r²`.

   Sem isso, vira mais uma função mecânica da planilha.

8. **Os gráficos foram mencionados, mas não integrados ao método**
   
   Diagrama de dispersão não deve ser só ilustração. Ele precisa ser usado antes dos cálculos para levantar hipóteses:

   - a relação parece linear?
   - há ponto influente?
   - a direção é positiva ou negativa?
   - a força parece fraca, moderada ou forte?

   Isso é metodologicamente mais robusto.

9. **A validação com funções prontas pode virar substituição do raciocínio**
   
   A planilha precisa separar visualmente:
   
   - “cálculo manual por somatórios”;
   - “validação automática”;
   - “interpretação”.

   Se essas partes ficarem misturadas, o aluno tende a usar `CORREL`/`SLOPE` como caixa-preta.

10. **Falta uma entrega verificável para os alunos**
   
   O plano gera a planilha, mas não define claramente o que a turma deve conseguir responder ao final. Melhor incluir perguntas finais em cada aba:

   - Qual é a direção da associação?
   - A associação é fraca, moderada ou forte?
   - Qual é a reta ajustada?
   - O que significa a inclinação?
   - O que muda ao excluir Silvio?
   - A função pronta confirma o cálculo manual?

**Recomendação objetiva**

Eu ajustaria o plano antes de executar. A estrutura de três abas está correta, e os exercícios escolhidos são bons. Mas eu reforçaria quatro pontos: contextualização dos símbolos, sequência metodológica explícita, separação entre cálculo manual e validação automática, e interpretação crítica dos resultados.

A formulação mais rigorosa seria: **“cálculo manual por somatórios, usando apenas operações aritméticas da planilha, seguido de validação com funções estatísticas prontas do Google Planilhas.”**