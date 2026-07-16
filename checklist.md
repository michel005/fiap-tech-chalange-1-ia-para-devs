# Checklist — Tech Challenge Fase 1

Projeto de IA para suporte ao diagnóstico e detecção de riscos na saúde e segurança da mulher.

> Marque cada item com `[x]` conforme for concluindo.

---

## 1. Planejamento e definição do problema

- [ ] Definir o problema a ser resolvido (ex.: classificação de risco materno, câncer de mama, SOP)
- [ ] Escolher e documentar o(s) dataset(s) público(s) a utilizar
- [ ] Registrar no README a fonte dos dados e o link de download
- [ ] Descrever a variável alvo e o que significa cada classe de risco/diagnóstico

---

## 2. Estrutura do projeto

- [ ] Organizar o repositório com pastas claras (`datasets/`, `notebooks/` ou `src/`, `docs/`, `outputs/`)
- [ ] Criar `README.md` com instruções de execução (ambiente, dependências, como rodar)
- [ ] Manter `requirements.txt` atualizado com todas as dependências
- [ ] (Opcional) Criar `Dockerfile` para reproduzir o ambiente
- [ ] Garantir que o dataset esteja no repositório ou com link de download documentado

---

## 3. Exploração de dados (EDA)

- [ ] Carregar a base de dados em Python (Pandas)
- [ ] Inspecionar estrutura: dimensões, tipos de colunas, valores ausentes
- [ ] Gerar estatísticas descritivas (`describe`, contagens por classe)
- [ ] Criar visualizações relevantes (distribuições, histogramas, boxplots, correlações)
- [ ] Identificar padrões relacionados à saúde e segurança feminina
- [ ] Documentar os achados da EDA no relatório técnico

---

## 4. Pré-processamento de dados

- [ ] Tratar valores ausentes e inconsistentes (se houver)
- [ ] Montar pipeline de pré-processamento em Python
- [ ] Converter variáveis categóricas (encoding: one-hot, label encoding etc.)
- [ ] Normalizar/escalar variáveis numéricas quando necessário
- [ ] Realizar análise de correlação entre variáveis
- [ ] Separar features (`X`) e variável alvo (`y`)

---

## 5. Modelagem

- [ ] Definir separação clara entre conjunto de treino e teste (`train_test_split`)
- [ ] Implementar **pelo menos 2 algoritmos de classificação**, por exemplo:
  - [ ] Regressão Logística
  - [ ] Árvore de Decisão
  - [ ] KNN
  - [ ] Random Forest / outros à escolha
- [ ] Treinar cada modelo com o conjunto de treinamento
- [ ] Comparar desempenho entre os modelos

---

## 6. Treinamento, avaliação e interpretação

- [ ] Avaliar modelos no conjunto de teste
- [ ] Calcular métricas adequadas:
  - [ ] Accuracy
  - [ ] Recall
  - [ ] F1-score
- [ ] Justificar a escolha da métrica principal considerando o contexto médico
- [ ] Gerar matriz de confusão e relatório de classificação
- [ ] Aplicar técnicas de explicabilidade:
  - [ ] Feature importance
  - [ ] SHAP values
- [ ] Discutir criticamente: o modelo pode ser usado na prática? Como? (médico tem a palavra final)

---

## 7. Extra — Visão computacional (opcional)

- [ ] Escolher dataset de imagens (ex.: mamografias CBIS-DDSM)
- [ ] Pré-processar imagens (redimensionamento, normalização)
- [ ] Construir e treinar uma CNN para classificação
- [ ] Avaliar o modelo de imagem com métricas adequadas
- [ ] Documentar resultados no relatório

---

## 8. Código e documentação

- [ ] Refatorar código em notebooks Jupyter e/ou scripts Python organizados
- [ ] Adicionar comentários e docstrings onde necessário
- [ ] Salvar gráficos e resultados em pasta de saída (`outputs/` ou similar)
- [ ] Garantir que o projeto rode do zero seguindo o README

---

## 9. Relatório técnico (PDF)

- [ ] Link do repositório Git
- [ ] Discussão da análise exploratória
- [ ] Estratégias de pré-processamento adotadas
- [ ] Modelos utilizados e justificativa da escolha
- [ ] Resultados com prints, gráficos e análises
- [ ] Interpretação dos dados e conclusões críticas
- [ ] Exportar tudo em um arquivo PDF

---

## 10. Vídeo de demonstração

- [ ] Gravar vídeo de até 15 minutos (YouTube ou Vimeo — público ou não listado)
- [ ] Demonstrar o sistema em execução
- [ ] Explicar brevemente o fluxo: dados → pré-processamento → modelo → resultado
- [ ] Incluir o link do vídeo no PDF e no README

---

## 11. Entrega final

- [ ] Revisar todos os itens obrigatórios do desafio
- [ ] Verificar prazo de entrega da Fase 1
- [ ] Submeter o PDF com todos os entregáveis
- [ ] Confirmar que o repositório está acessível e completo
