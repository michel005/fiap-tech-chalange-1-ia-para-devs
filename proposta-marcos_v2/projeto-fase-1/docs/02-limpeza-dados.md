# 02 - Limpeza e Preparação dos Dados

## Objetivo

Preparar o conjunto de dados do SINAN para utilização em algoritmos de Machine Learning, removendo informações desnecessárias, tratando valores ausentes e selecionando apenas as variáveis relevantes para o problema proposto.

---

# Entrada

Arquivo de origem:

```
data/raw/VIOLBR25.xlsx
```

Saída esperada:

```
data/processed/VIOLBR25_LIMPO.xlsx
```

---

# Objetivos da Limpeza

Durante esta etapa serão realizadas as seguintes transformações:

- Filtrar apenas notificações referentes a mulheres.
- Remover colunas administrativas do SINAN.
- Selecionar apenas variáveis relevantes para o problema.
- Remover registros inconsistentes.
- Identificar valores ausentes.
- Tratar valores ignorados.
- Gerar um dataset preparado para Machine Learning.

---

# Regras de Limpeza

## 1. Filtrar apenas mulheres

A proposta deste trabalho é analisar notificações de violência contra a mulher.

Será mantido apenas:

| Coluna | Valor |
|---------|-------|
| CS_SEXO | F |

Registros com sexo masculino, ignorado ou não informado serão removidos.

---

## 2. Remover colunas administrativas

As seguintes informações não possuem valor preditivo para o modelo e serão removidas.

Exemplos:

- TP_NOT
- ID_AGRAVO
- ID_UNIDADE
- DT_DIGITA
- DT_TRANSUS
- DT_TRANSDM
- DT_TRANSRS
- DT_TRANSRM
- DT_ENCERRA
- NDUPLIC

Essas colunas são utilizadas apenas para controle interno do SINAN.

---

## 3. Selecionar variáveis relevantes

Serão mantidas apenas variáveis relacionadas ao perfil da vítima, características da violência e do agressor.

### Perfil da vítima

- NU_IDADE_N
- CS_RACA
- CS_ESCOL_N
- SIT_CONJUG
- CS_GESTANT

### Deficiências

- DEF_TRANS
- DEF_FISICA
- DEF_MENTAL
- DEF_VISUAL
- DEF_AUDITI
- TRAN_MENT

### Local

- SG_UF
- LOCAL_OCOR

### Tipo de violência

- VIOL_FISIC
- VIOL_PSICO
- VIOL_SEXU
- VIOL_NEGLI
- VIOL_FINAN
- VIOL_TORT
- LES_AUTOP

### Meio de agressão

- AG_FORCA
- AG_CORTE
- AG_FOGO
- AG_AMEACA

### Relação com o agressor

- REL_CONJ
- REL_EXCON
- REL_NAMO
- REL_PAI
- REL_MAE

### Autor

- AUTOR_SEXO
- AUTOR_ALCO
- NUM_ENVOLV

### Evolução

- EVOLUCAO

---

# Variável Alvo

A variável alvo do modelo será:

```
OUT_VEZES
```

Significado:

| Valor | Classe |
|---------|--------|
| Sim | 1 |
| Não | 0 |

Registros com valor ignorado ou em branco serão removidos da base de treinamento.

---

# Tratamento de Valores Ausentes

Será calculado o percentual de valores ausentes para todas as colunas.

Critério inicial:

- até 30% → manter
- entre 30% e 70% → avaliar
- acima de 70% → remover

Caso alguma variável seja considerada importante para o domínio do problema, poderá ser mantida mesmo apresentando percentual elevado de valores ausentes, desde que essa decisão seja justificada.

---

# Tratamento de Categorias

Durante a preparação para Machine Learning:

- Sim → 1
- Não → 0
- Ignorado → valor ausente (NaN)

Posteriormente as variáveis categóricas serão codificadas utilizando técnicas apropriadas, como One-Hot Encoding ou Label Encoding, conforme a natureza de cada atributo.

---

# Produto Gerado

Ao final desta etapa será produzido o arquivo:

```
data/processed/VIOLBR25_LIMPO.xlsx
```

Esse conjunto de dados será utilizado na etapa de preparação para Machine Learning.

---

# Script Responsável

```
scripts/02_limpeza_dataset.py
```

---

# Próxima Etapa

Na próxima etapa será realizada a preparação dos dados para Machine Learning, incluindo:

- tratamento final dos valores ausentes;
- codificação das variáveis categóricas;
- normalização, quando aplicável;
- divisão entre conjuntos de treinamento e teste.

---

# Execução

Com Python 3.12 e as dependências instaladas, execute:

```bash
python scripts/02_limpeza_dataset.py
```

O script lê `data/raw/VIOLBR25.xlsx`, gera `data/processed/VIOLBR25_LIMPO.xlsx` e cria o relatório `relatorios/04_relatorio_limpeza.xlsx`.
