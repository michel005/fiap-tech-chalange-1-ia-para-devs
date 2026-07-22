# Dicionário de Dados - Projeto de Machine Learning

## Objetivo

Este documento descreve as variáveis utilizadas no projeto de predição de recorrência de violência contra a mulher utilizando dados do SINAN (Sistema de Informação de Agravos de Notificação).

---

# Variáveis Utilizadas

| Coluna | Descrição |
|---------|-----------|
| NU_IDADE_N | Idade da vítima codificada pelo SINAN. A idade é armazenada em formato numérico que combina a unidade de tempo (anos, meses, dias) com o valor correspondente. |
| CS_RACA | Raça/Cor da vítima. |
| CS_ESCOL_N | Escolaridade da vítima. |
| SIT_CONJUG | Situação conjugal da vítima. |
| CS_GESTANT | Situação gestacional da vítima no momento da notificação. |
| DEF_TRANS | Possui algum tipo de deficiência ou transtorno. |
| DEF_FISICA | Possui deficiência física. |
| DEF_MENTAL | Possui deficiência mental ou intelectual. |
| DEF_VISUAL | Possui deficiência visual. |
| DEF_AUDITI | Possui deficiência auditiva. |
| TRAN_MENT | Possui transtorno mental. |
| SG_UF | Unidade Federativa (Estado) onde ocorreu a notificação. |
| LOCAL_OCOR | Local onde ocorreu a violência (residência, via pública, escola, etc.). |
| VIOL_FISIC | Indica ocorrência de violência física. |
| VIOL_PSICO | Indica ocorrência de violência psicológica ou moral. |
| VIOL_SEXU | Indica ocorrência de violência sexual. |
| VIOL_NEGLI | Indica ocorrência de negligência ou abandono. |
| VIOL_FINAN | Indica ocorrência de violência financeira ou econômica. |
| VIOL_TORT | Indica ocorrência de tortura. |
| LES_AUTOP | Indica lesão autoprovocada. |
| AG_FORCA | Meio de agressão por força corporal ou espancamento. |
| AG_CORTE | Meio de agressão por objeto perfurocortante. |
| AG_FOGO | Meio de agressão por arma de fogo. |
| AG_AMEACA | Meio de agressão por ameaça. |
| REL_CONJ | O agressor é o cônjuge da vítima. |
| REL_EXCON | O agressor é ex-cônjuge da vítima. |
| REL_NAMO | O agressor é namorado(a) da vítima. |
| REL_PAI | O agressor é o pai da vítima. |
| REL_MAE | O agressor é a mãe da vítima. |
| AUTOR_SEXO | Sexo do provável agressor. |
| AUTOR_ALCO | Indica suspeita de uso de álcool pelo agressor. |
| NUM_ENVOLV | Quantidade de pessoas envolvidas na agressão. |
| OUT_VEZES | **Variável alvo do projeto.** Indica se a violência ocorreu outras vezes (recorrência). |

---

# Variável Alvo

A variável utilizada para treinamento do modelo é:

```
OUT_VEZES
```

Ela representa se a vítima já sofreu violência anteriormente.

O objetivo do modelo é prever a probabilidade de recorrência da violência com base nas características da vítima, do agressor e do evento.

---

# Observações

- Os valores armazenados no dataset seguem a codificação oficial do SINAN.
- Os códigos numéricos representam categorias descritas no dicionário oficial do Ministério da Saúde.
- Durante a etapa de preparação para Machine Learning, algumas variáveis categóricas poderão ser transformadas utilizando técnicas como One-Hot Encoding.
- A coluna **NU_IDADE_N** utiliza um formato codificado e poderá ser convertida para idade em anos para facilitar a interpretação dos modelos.

---

# Classificação das Variáveis

## Perfil da vítima

- NU_IDADE_N
- CS_RACA
- CS_ESCOL_N
- SIT_CONJUG
- CS_GESTANT

## Deficiência ou transtornos

- DEF_TRANS
- DEF_FISICA
- DEF_MENTAL
- DEF_VISUAL
- DEF_AUDITI
- TRAN_MENT

## Local da ocorrência

- SG_UF
- LOCAL_OCOR

## Tipos de violência

- VIOL_FISIC
- VIOL_PSICO
- VIOL_SEXU
- VIOL_NEGLI
- VIOL_FINAN
- VIOL_TORT
- LES_AUTOP

## Meio utilizado na agressão

- AG_FORCA
- AG_CORTE
- AG_FOGO
- AG_AMEACA

## Relação entre vítima e agressor

- REL_CONJ
- REL_EXCON
- REL_NAMO
- REL_PAI
- REL_MAE

## Características do agressor

- AUTOR_SEXO
- AUTOR_ALCO
- NUM_ENVOLV

## Variável alvo

- OUT_VEZES