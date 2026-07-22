# Proposta de Dataset — Violência Contra a Mulher (SINAN / DATASUS)

## Problema Proposto

Desenvolver um modelo de Machine Learning capaz de identificar padrões associados à violência contra a mulher, auxiliando profissionais de saúde na triagem, 
classificação e encaminhamento de situações de risco.

A proposta é utilizar dados históricos de notificações registradas no Sistema de Informação de Agravos de Notificação (SINAN) para identificar fatores relacionados à 
reincidência da violência e aos diferentes tipos de agressão sofridos pelas vítimas.

---

## Justificativa

O desafio proposto menciona explicitamente a necessidade de identificar sinais de violência doméstica em registros e prontuários médicos, tornando este tema diretamente alinhado aos objetivos do projeto.

Além disso, a violência contra a mulher representa um importante problema de saúde pública, exigindo mecanismos que auxiliem na identificação precoce de situações de vulnerabilidade e 
apoiem a tomada de decisão por profissionais da área da saúde.

A utilização de dados oficiais do Ministério da Saúde permite que o estudo seja desenvolvido com base em registros reais de notificações realizadas em todo o território nacional.

---

## Dataset

Será utilizado o conjunto de dados **VIOL - Violência doméstica, sexual e/ou outras violências**, disponibilizado pelo DATASUS por meio do Sistema de Informação de Agravos de Notificação (SINAN).

O SINAN é o sistema oficial do Ministério da Saúde responsável pela coleta, transmissão e disseminação de informações relacionadas a agravos e eventos de interesse para a saúde pública.

O conjunto de dados contempla notificações de casos suspeitos ou confirmados de violência registradas por:

- Unidades de saúde;
- Hospitais;
- Pronto-atendimentos;
- Centros especializados de atendimento à mulher;
- Conselhos tutelares;
- Serviços de assistência social;
- Outras instituições habilitadas para notificação.

### Informações disponíveis no conjunto de dados

O dataset contém informações epidemiológicas e sociodemográficas como:

- Idade da vítima;
- Faixa etária;
- Escolaridade;
- Raça/Cor;
- Município e Unidade Federativa;
- Local de ocorrência;
- Tipo de violência;
- Reincidência da violência;
- Sexo do agressor;
- Relação entre vítima e agressor;
- Encaminhamentos realizados;
- Evolução do caso;
- Outras características relacionadas à notificação.

---

## Fonte dos Dados

**Origem:** DATASUS – Ministério da Saúde

**Sistema:** SINAN (Sistema de Informação de Agravos de Notificação)

**Conjunto de dados utilizado:** VIOL – Violência doméstica, sexual e/ou outras violências

**Arquivo obtido:** VIOLBR25

**Abrangência geográfica:** Brasil

**Ano de referência:** 2025

**https://datasus.saude.gov.br/transferencia-de-arquivos/#

---

## Objetivo da Modelagem

Identificar padrões presentes nas notificações de violência contra a mulher que possam auxiliar na classificação de casos com maior risco de reincidência ou maior gravidade.

A solução proposta não tem finalidade diagnóstica, mas sim de apoio à tomada de decisão e à vigilância em saúde.

---

## Variável Alvo

Inicialmente será utilizada a variável relacionada à reincidência da violência.

| Valor | Significado |
|---------|-------------|
| 0 | Não houve reincidência |
| 1 | Houve reincidência |

Dependendo da qualidade e distribuição dos dados, também poderão ser avaliadas classificações relacionadas a:

- Violência física;
- Violência psicológica;
- Violência sexual;
- Violência autoprovocada;
- Encaminhamento para serviços especializados.

---

## Possíveis Técnicas de Machine Learning

O problema será tratado como uma tarefa de classificação supervisionada utilizando algoritmos como:

- Regressão Logística;
- Árvore de Decisão;
- Random Forest;
- K-Nearest Neighbors (KNN).

Os modelos serão comparados utilizando métricas como:

- Accuracy;
- Precision;
- Recall;
- F1-Score.

---

## Benefícios da Solução

- Apoio à triagem de mulheres em situação de vulnerabilidade;
- Auxílio à tomada de decisão por profissionais da saúde;
- Identificação precoce de padrões associados à violência;
- Apoio ao planejamento de políticas públicas;
- Contribuição para ações preventivas e de proteção à mulher;
- Utilização de dados reais provenientes do sistema oficial de vigilância em saúde.

---

## Conclusão

A utilização de dados oficiais do SINAN/DATASUS permite o desenvolvimento de uma solução alinhada aos objetivos do Tech Challenge, 
aplicando conceitos de Inteligência Artificial e Machine Learning em um contexto real de saúde pública.

Além da relevância social do tema, o projeto possibilita a análise de dados epidemiológicos reais, contribuindo para a compreensão 
dos fatores associados à violência contra a mulher e para o desenvolvimento de ferramentas de apoio à vigilância e proteção das vítimas.