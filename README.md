# Proposta de Dataset — Violência Doméstica Contra a Mulher

## Problema Proposto

Desenvolver um modelo de Machine Learning capaz de identificar mulheres com maior risco de sofrer violência doméstica a partir de informações sociodemográficas e de saúde.

A proposta é utilizar dados históricos para identificar padrões que possam auxiliar profissionais de saúde na triagem e no encaminhamento de casos que apresentem sinais de vulnerabilidade.

---

## Justificativa

O próprio desafio menciona a necessidade de identificar sinais de violência doméstica em prontuários médicos, tornando este tema diretamente alinhado aos objetivos do projeto.

Além disso, trata-se de um problema de grande relevância social, que pode contribuir para ações preventivas e para a proteção de mulheres em situação de risco.


---

## Dataset

Será utilizado um dataset público relacionado à violência contra a mulher contendo informações como:

- Idade
- Estado civil
- Escolaridade
- Quantidade de filhos
- Condição econômica
- Localização
- Histórico de violência
- Outros fatores sociais e demográficos

Fonte sugerida:

- Kaggle – Violence Against Women Dataset
- Kaggle – Domestic Violence Against Women Dataset
- DATASUS / SINAN (casos notificados de violência)

---

## Variável Alvo

Exemplo de classificação:

| Valor | Significado |
|---------|-------------|
| 0 | Não sofreu violência |
| 1 | Sofreu violência |

Dependendo do dataset escolhido, também poderão ser utilizadas classificações mais detalhadas:

- Violência física
- Violência psicológica
- Violência sexual
- Violência patrimonial

---

## Possíveis Técnicas de Machine Learning

O problema pode ser tratado como uma tarefa de classificação supervisionada utilizando algoritmos como:

- Regressão Logística
- Árvore de Decisão
- Random Forest
- KNN

Os modelos serão comparados utilizando métricas como:

- Accuracy
- Recall
- F1-Score

---

## Benefícios da Solução

- Auxílio à triagem de pacientes em situação de risco.
- Apoio à tomada de decisão dos profissionais de saúde.
- Identificação precoce de padrões de violência.
- Contribuição para ações preventivas e de proteção à mulher.

---

## Conclusão

A utilização de dados relacionados à violência doméstica está diretamente alinhada ao objetivo do Tech Challenge, 
que busca soluções de IA voltadas à saúde e segurança da mulher. A proposta apresenta relevância social,
potencial impacto prático e oferece uma alternativa diferenciada em relação aos temas mais tradicionais, 
como o diagnóstico de câncer de mama.