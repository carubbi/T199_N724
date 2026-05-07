# AGENTS.md

## Postura de colaboração

Atue como parceiro crítico de decisão, não como executor passivo.

Não valide propostas automaticamente. Analise decisões à luz do objetivo didático, rigor estatístico, manutenção do material, consistência entre arquivos, custo de alteração e risco de confundir alunos.

Quando uma decisão afetar arquitetura do material, escopo, metodologia, planilhas, exportações, nomenclatura estatística, fórmulas ou organização pedagógica, apresente:

1. o que foi entendido;
2. riscos ou fragilidades;
3. alternativas possíveis;
4. recomendação objetiva;
5. confirmação antes de executar quando a alteração for estrutural, difícil de reverter ou puder gerar inconsistência.

Para mudanças simples, como correções pontuais de texto, acentuação, títulos ou regeneração de exportações, execute diretamente e informe o que mudou.

## Regras do projeto

- Priorize clareza didática sem sacrificar rigor estatístico.
- Use português do Brasil com acentuação correta nos materiais finais.
- Em fórmulas matemáticas dentro de Markdown, use `$...$` para expressões inline e `$$...$$` para blocos.
- Em fórmulas do Google Planilhas voltadas ao aluno, use separador `;`, não `,`.
- Preserve o arquivo `.xlsx` como fonte operacional quando a mudança envolver a planilha.
- Sempre que atualizar `aulas/planilhas/Revisao_AV2.xlsx`, regenere os Markdown em `aulas/planilhas/exports/`.
- Não antecipe resultados dos exercícios na revisão conceitual.
- Use o termo `valor atípico/outlier`; não use `ponto influente` nos materiais didáticos deste projeto.
- Ao explicar `LINEST(intervalo_y; intervalo_x; TRUE; TRUE)`, deixe claro que:
  - a função ajusta uma regressão linear aos intervalos informados;
  - o primeiro `TRUE` estima o intercepto;
  - o segundo `TRUE` retorna a matriz completa de estatísticas da regressão.

## Planilhas e exportações

- Use o ambiente virtual do projeto quando precisar manipular planilhas:

```bash
/home/carubbi/Documents/REPOS/T199_N724/.venv/bin/python
```

- Para regenerar os Markdown da revisão AV2:

```bash
/home/carubbi/Documents/REPOS/T199_N724/.venv/bin/python -B scripts/export_revisao_av2_md.py
```

- Os Markdown exportados devem funcionar como material de leitura para alunos que não dominam Excel/Google Planilhas.
- O Markdown não deve ser uma cópia bruta da planilha; ele deve organizar enunciado, resolução sem planilha, resolução com planilha, validação e interpretação crítica.

## Estatística e didática

- Diferencie cálculo, interpretação e validação.
- Ao apresentar ANOVA, defina explicitamente `SQ`, `gl`, `QM` e `F`.
- Ao apresentar regressão, defina `x`, `y`, `r`, `a`, `b`, `R2`, `resíduo`, `SQReg`, `SQRes` e `SQTot`.
- Inclua análise de resíduos e diagnóstico visual quando o tema for regressão.
- Não trate `R2` alto como prova de bom modelo nem como evidência causal.
- Não trate correlação como causalidade.
- Não exclua valor atípico/outlier automaticamente; a exclusão exige justificativa substantiva.

## Cuidados de edição

- Não insira linhas em planilhas com fórmulas e gráficos sem avaliar risco de deslocar referências.
- Prefira alterar células existentes quando isso preservar fórmulas, gráficos e intervalos.
- Se uma alteração no `.xlsx` for feita, confira as células-chave e regenere os `.md`.
- Antes de finalizar, verifique se os arquivos gerados refletem a alteração solicitada.
