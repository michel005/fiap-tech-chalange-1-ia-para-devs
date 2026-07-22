# Seleção das Variáveis do Projeto (VIOLBR25)

## Objetivo

Este script realiza a primeira etapa de preparação do dataset **VIOLBR25 (SINAN)**.

O objetivo é reduzir a quantidade de informações do banco original, mantendo apenas os registros e variáveis que serão utilizados durante todo o projeto de Ciência de Dados.

---

# Arquivo

```
scripts/02_selecionar_variaveis.py
```

---

# Arquivo de Entrada

O script procura automaticamente um dos arquivos abaixo:

```
data/raw/VIOLBR25.xlsx
```

ou

```
data/raw/VIOLBR25_ptbr.csv
```

---

# Regras Aplicadas

## 1. Leitura do Dataset

O script identifica automaticamente o formato do arquivo.

Formatos suportados:

- Excel (.xlsx)
- CSV (.csv)

---

## 2. Filtro por Sexo

Como o projeto analisa apenas casos de violência contra a mulher, são mantidos somente registros onde:

```
CS_SEXO = F
```

Todos os demais registros são descartados.

---

## 3. Seleção das Variáveis

Após o filtro, são mantidas apenas as variáveis relevantes para o projeto.

As variáveis contemplam informações sobre:

- Perfil da vítima
- Escolaridade
- Estado civil
- Gestação
- Deficiências
- Estado da ocorrência
- Local da ocorrência
- Tipos de violência
- Meio utilizado na agressão
- Relação entre vítima e agressor
- Características do agressor
- Variável alvo do projeto

---

## Variável Alvo

A variável utilizada para previsão é:

```
OUT_VEZES
```

Essa variável indica se a vítima sofreu violência anteriormente.

---

## Arquivo Gerado

Ao final é criado:

```
data/processed/VIOLBR25_SELECIONADO.xlsx
```

Esse arquivo será utilizado nas próximas etapas do projeto.

---

# Como Executar

```powershell
python scripts/02_selecionar_variaveis.py
```

---

# Próxima Etapa

Após a seleção das variáveis será realizada a Análise Exploratória dos Dados (EDA), permitindo compreender o perfil das vítimas e identificar padrões antes da etapa de limpeza e preparação para Machine Learning.