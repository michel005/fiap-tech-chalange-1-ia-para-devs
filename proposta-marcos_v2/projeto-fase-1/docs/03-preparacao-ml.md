# 03 - Preparacao dos Dados para Machine Learning

## Objetivo

Transformar o dataset limpo em conjuntos prontos para treinamento e avaliacao de modelos de Machine Learning.

---

## Entrada

Arquivo utilizado:

```
data/processed/VIOLBR25_LIMPO.xlsx
```

---

## Transformacoes Realizadas

Durante esta etapa sao aplicadas as seguintes transformacoes:

- Identificacao da variavel alvo `OUT_VEZES`.
- Conversao da variavel alvo para formato binario.
- Separacao entre atributos (`X`) e alvo (`y`).
- Conversao de variaveis categoricas para formato numerico.
- Aplicacao de One-Hot Encoding nas colunas categoricas.
- Divisao dos dados em treino e teste.

### Conversao da Variavel Alvo

A coluna `OUT_VEZES` e convertida para binario com a seguinte regra:

| Valor original | Valor final |
|---------|--------|
| Sim | 1 |
| 1 | 1 |
| Nao | 0 |
| Não | 0 |
| 2 | 0 |

---

## Saidas Geradas

Os seguintes arquivos sao produzidos em:

```
data/processed/
```

- `X_train.xlsx`
- `X_test.xlsx`
- `y_train.xlsx`
- `y_test.xlsx`

---

## Script Responsavel

```
scripts/03_preparacao_ml.py
```

---

## Execucao

Com Python 3.12 e as dependencias instaladas, execute:

```bash
python scripts/03_preparacao_ml.py
```

O script le `data/processed/VIOLBR25_LIMPO.xlsx`, aplica as transformacoes de codificacao e separacao dos dados e salva os conjuntos finais em `data/processed/`.
