# Análise Exploratória dos Dados (EDA)

## Objetivo

Este script realiza a Análise Exploratória dos Dados (Exploratory Data Analysis - EDA) do dataset previamente selecionado.

O objetivo é compreender o perfil das vítimas, identificar padrões nos dados e gerar gráficos que auxiliem na interpretação das informações antes das etapas de limpeza e modelagem.

---

# Arquivo

```
scripts/02_analise_exploratoria.py
```

---

# Arquivo de Entrada

```
data/processed/VIOLBR25_SELECIONADO.xlsx
```

---

# Gráficos Gerados

O script gera automaticamente gráficos para as principais variáveis do projeto.

## 1. Distribuição por Raça

Variável:

```
CS_RACA
```

Permite identificar a distribuição das notificações entre os diferentes grupos raciais.

---

## 2. Estado Civil

Variável:

```
SIT_CONJUG
```

Mostra a quantidade de vítimas por situação conjugal.

---

## 3. Gestantes

Variável:

```
CS_GESTANT
```

Apresenta a distribuição entre:

- Não gestantes
- Gestantes no 1º trimestre
- Gestantes no 2º trimestre
- Gestantes no 3º trimestre
- Idade gestacional ignorada
- Não se aplica
- Ignorado

---

## 4. Casos por Estado

Variável:

```
SG_UF
```

Os códigos IBGE são convertidos automaticamente para as respectivas siglas dos estados brasileiros, permitindo melhor visualização da distribuição geográfica das notificações.

---

## 5. Deficiências

Variáveis utilizadas:

- DEF_FISICA
- DEF_MENTAL
- DEF_VISUAL
- DEF_AUDITI
- TRAN_MENT

O gráfico apresenta a quantidade de vítimas com cada tipo de deficiência ou transtorno.

---

## 6. Tipos de Violência

Variáveis utilizadas:

- VIOL_FISIC
- VIOL_PSICO
- VIOL_SEXU
- VIOL_NEGLI
- VIOL_FINAN
- VIOL_TORT

Permite visualizar quais tipos de violência são mais frequentes na base analisada.

---

# Tradução dos Códigos

Durante a geração dos gráficos, os códigos do SINAN são convertidos para descrições compreensíveis, como:

- Raça
- Estado civil
- Situação gestacional
- Unidade da Federação (UF)

Essa conversão facilita a interpretação dos resultados.

---

# Arquivos Gerados

Todos os gráficos são armazenados em:

```
graficos/
```

Arquivos produzidos:

```
01_raca.png
02_estado_civil.png
03_gestantes.png
04_estados.png
05_deficiencias.png
06_tipos_violencia.png
```

---

# Como Executar

```powershell
python scripts/03_analise_exploratoria.py
```

---

# Objetivo da EDA

A análise exploratória permite:

- compreender o perfil das vítimas;
- identificar possíveis inconsistências nos dados;
- conhecer a distribuição das variáveis;
- orientar as próximas etapas de limpeza e preparação dos dados;
- apoiar a seleção das variáveis mais relevantes para o treinamento dos modelos de Machine Learning.

---

# Próxima Etapa

Após a análise exploratória será realizada a limpeza do conjunto de dados, tratando valores ausentes, inconsistências e preparando a base para a etapa de modelagem preditiva.