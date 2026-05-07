# Plano de Extração de Exercícios de Livro em PDF

## 1. Modelo de pedido para executar o plano

```md
Execute o plano para `livros/NOME.pdf`, capítulo `N`, unidade `exs/undX`.

Gere `exs/undX/NOME_capN.md` com exemplos, exercícios resolvidos e exercícios propostos em paráfrase fiel e didática, sem perda de informações.

Gere `exs/undX/respostas/NOME_capN_respostas.md` com respostas sintéticas ou extraídas dos exemplos e com as respostas detalhadas dos exercícios propostos.

Use apenas conceitos do capítulo correspondente.
```

## 2. Definir escopo

- Livro em PDF: `livros/NOME_DO_LIVRO.pdf`
- Capítulo: número e título.
- Unidade de destino: `exs/undX/`
- Arquivo de exercícios: `exs/undX/livro_capN.md`
- Arquivo de respostas: `exs/undX/respostas/livro_capN_respostas.md`

## 3. Localizar o capítulo no PDF

- Identificar início e fim do capítulo.
- Localizar:
  - exemplos;
  - exercícios resolvidos;
  - exercícios propostos;
  - gabarito do livro, se existir.

## 4. Extrair o conteúdo

- Extrair exemplos, exercícios resolvidos e exercícios propostos.
- Usar **paráfrase fiel e didática, sem perda de informações**: reescrever com palavras próprias, preservando todos os dados, hipóteses, variáveis, unidades, tabelas, itens e conceitos estatísticos necessários para resolver exatamente o mesmo exercício.
- Preservar dados numéricos, tabelas, fórmulas e unidades.
- Não simplificar o problema a ponto de alterar dificuldade, escopo ou conceito avaliado.
- Se o exercício depender de dados, tabelas ou valores disponíveis em apêndices do próprio livro, copiar esses dados para o enunciado do exercício em paráfrase fiel, de modo que o exercício fique autocontido e não dependa de consulta externa.

## 5. Gerar o Markdown de exercícios

- Criar `exs/undX/livro_capN.md`.
- Estrutura:

```md
# Livro (ano) - Capítulo N: Título

Fonte: `livros/NOME_DO_LIVRO.pdf`

## Fórmulas úteis

## Exemplos

## Exercícios Resolvidos

## Exercícios Propostos
```

- Nos exercícios resolvidos, incluir paráfrase fiel do enunciado e objetivo didático.
- Não incluir resposta detalhada no arquivo de exercícios.
- Quando o exercício fizer referência a apêndices, tabelas auxiliares ou bases apresentadas em outra parte do livro, incorporar no próprio exercício os dados necessários para sua resolução.

## 6. Resolver os exercícios propostos

- Para os exemplos listados no arquivo de exercícios, incluir no arquivo de respostas uma seção com respostas sintéticas ou extraídas do próprio capítulo, preservando os resultados centrais, fórmulas e interpretações necessárias para que o exemplo fique verificável.
- As respostas dos exemplos não precisam repetir toda a resolução do livro; devem registrar o resultado essencial e o padrão de raciocínio.
- Usar os exercícios resolvidos como padrão de raciocínio.
- Usar apenas conceitos apresentados no capítulo correspondente.
- Não introduzir métodos externos ao capítulo como solução principal.
- Aplicar as fórmulas e interpretações do próprio capítulo.
- Conferir resultados com gabarito do livro, quando houver.
- Sinalizar limitações quando faltar dado externo, tabela, planilha ou imagem.
- Não deixar a resolução depender de dados localizados apenas em apêndices: quando os dados existirem no PDF, trazê-los para o arquivo de exercícios.
- Se houver solução mais avançada possível, mas fora do escopo do capítulo, registrar no máximo como observação opcional, sem usá-la como resposta principal.

## 7. Gerar o Markdown de respostas

- Criar `exs/undX/respostas/livro_capN_respostas.md`.
- Estrutura:

```md
# Respostas dos exercícios de Livro (ano), capítulo N

Fonte dos enunciados: `exs/undX/livro_capN.md`

Observações de conferência: ...

## Respostas dos Exemplos

### Exemplo N.1

### Exemplo N.2

## Exercício N.1_P

## Exercício N.2_P
```

- Incluir respostas sintéticas ou extraídas dos exemplos sempre que houver seção `## Exemplos` no arquivo de exercícios.
- Separar subitens por letras.
- Incluir cálculos, fórmulas e interpretações.
- Não inventar resposta quando os dados não estiverem disponíveis.

## 8. Validar consistência

- Conferir se todo exercício proposto tem resposta correspondente.
- Conferir se todo exemplo listado tem resposta sintética ou extraída correspondente, quando o exemplo tiver resultado calculável no capítulo.
- Conferir numeração e nomes dos arquivos.
- Procurar `TODO`, `??`, dados ausentes não sinalizados e links quebrados.
- Verificar se as soluções usam apenas conceitos do capítulo.
- Comparar com:
  - `exs/und2/pinheiro_cap2.md`
  - `exs/und2/respostas/pinheiro_cap2_respostas.md`

## 9. Critérios de qualidade

- Preservar rigor estatístico.
- Separar enunciados e respostas.
- Usar LaTeX no Markdown para fórmulas.
- Explicar interpretações, não só resultados numéricos.
- Registrar limitações explicitamente.
- Não misturar arquivos de unidades diferentes.
- Manter o nível técnico compatível com o ponto do livro: a resolução deve equivaler à forma dos exercícios resolvidos ou ao conhecimento apresentado no capítulo correspondente.
