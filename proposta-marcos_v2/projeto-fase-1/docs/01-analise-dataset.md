# 01 - Análise Exploratória do Dataset

## Objetivo

Realizar uma análise inicial do conjunto de dados do SINAN para compreender sua estrutura, qualidade e distribuição das informações antes da etapa de limpeza e preparação para Machine Learning.

---

## Dataset

Arquivo utilizado:

```
data/raw/VIOLBR25.xlsx
```

---

## Objetivos da análise

- Identificar a quantidade de registros.
- Identificar a quantidade de colunas.
- Listar todas as variáveis disponíveis.
- Identificar valores ausentes.
- Calcular o percentual de valores ausentes.
- Identificar valores distintos de cada coluna.
- Verificar a distribuição por sexo.
- Verificar a distribuição da variável alvo.

---

## Saídas esperadas

Os seguintes relatórios serão gerados:

- 01_colunas.xlsx
- 02_relatorio_colunas.xlsx
- 03_valores_unicos.xlsx

Todos serão gravados em:

```
relatorios/
```

---

## Script responsável

```
scripts/01_analise_dataset.py
```

---

## Próxima etapa

Após concluir a análise exploratória será realizada a limpeza do dataset.

---

## Como executar

Com Python 3.12 e as dependências instaladas, execute:

```bash
python scripts/01_analise_dataset.py
```

O script lê `data/raw/VIOLBR25.xlsx`, exibe o resumo inicial no console e gera os relatórios na pasta `relatorios/`.
