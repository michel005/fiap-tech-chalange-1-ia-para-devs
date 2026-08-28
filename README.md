# FIAP — IA para Devs — Grupo 21

## Tech Challenge — Fase 1 (Módulo de Machine Learning)

Detecção da **Síndrome dos Ovários Policísticos (SOP / PCOS)** com Machine Learning:
um modelo de classificação que, a partir de exames e características clínicas, estima a
probabilidade de uma paciente ter SOP e funciona como ferramenta de **apoio à triagem**
(não substitui o diagnóstico médico).

## Membros

- Marcos de Lima (marcoslima237@outlook.com)
- Michel Douglas Grigoli (mdgrigoli@hotmail.com.br)
- Fabricio Geraldo Araujo (fabaraujo23@gmail.com)

## Entregáveis

- **Notebook principal:** [`notebooks/pcos_tech_challenge.ipynb`](notebooks/pcos_tech_challenge.ipynb)
- **Modelo treinado:** [`notebooks/modelo_pcos_final.pkl`](notebooks/modelo_pcos_final.pkl)
- **Relatório técnico (PDF):** [`docs/Tech_Challenge_Fase1_SOP_PCOS.pdf`](docs/Tech_Challenge_Fase1_SOP_PCOS.pdf)
- **Enunciado do desafio:** [`docs/IADT-tech-challenge-fase-1.pdf`](docs/IADT-tech-challenge-fase-1.pdf)
- **Vídeo de apresentação (até 15 min):** https://www.youtube.com/watch?v=Du_KeZ0IGjA&list=PLdZIFpQTvlLM

## Dataset

- **Fonte:** [Polycystic Ovary Syndrome (PCOS) — Kaggle](https://www.kaggle.com/datasets/prasoonkottarathil/polycystic-ovary-syndrome-pcos/data)
- **Arquivo:** [`datasets/PCOS_data_without_infertility.xlsx`](datasets/PCOS_data_without_infertility.xlsx), aba `Full_new`
- **Dimensões:** 541 pacientes × 45 colunas originais (exames hormonais, medidas físicas,
  ultrassom e sintomas/hábitos).
- **Variável-alvo:** `PCOS (Y/N)` — `1` = tem SOP, `0` = não tem. Distribuição: 67,3% sem SOP,
  32,7% com SOP (desbalanceamento moderado).

O arquivo do dataset já está versionado no repositório, então não é necessário baixá-lo do Kaggle
para executar o notebook.

## Como executar

Requisitos: **Python 3.10+** e Git.

```bash
# 1. Clonar o repositório
git clone https://github.com/michel005/fiap-tech-chalange-1-ia-para-devs.git
cd fiap-tech-chalange-1-ia-para-devs

# 2. Criar e ativar um ambiente virtual
python -m venv venv
# Windows (PowerShell):
venv\Scripts\Activate.ps1
# Linux / macOS:
source venv/bin/activate

# 3. Instalar as dependências
pip install -r requirements.txt

# 4. Abrir o Jupyter e executar o notebook principal
jupyter notebook notebooks/pcos_tech_challenge.ipynb
```

No Jupyter, use **Kernel → Restart & Run All** para rodar o notebook do início ao fim.
A semente aleatória é fixada em `RANDOM_STATE = 42`, portanto os resultados são reproduzíveis.

### Dependências

`pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`, `shap`, `openpyxl`, `jupyter`
(todas em [`requirements.txt`](requirements.txt)).

## Estrutura do projeto

```
datasets/    bases de dados (inclui o .xlsx do PCOS)
docs/        enunciado do desafio e relatório técnico em PDF
notebooks/   notebook principal e modelo treinado (.pkl)
prompts/     prompts de apoio usados no desenvolvimento
requirements.txt
```

## Pipeline e resultados

1. **Carga** dos dados (aba `Full_new` do Excel).
2. **EDA** — estrutura, distribuição do alvo e correlações (nº de folículos, ganho de peso,
   irregularidade do ciclo e hirsutismo lideram — coerente com os critérios clínicos da SOP).
3. **Pré-processamento** — limpeza dos nomes das colunas, remoção de identificadores e da coluna
   vazia, conversão de colunas de exame lidas como texto (`pd.to_numeric(errors="coerce")`),
   imputação de ausentes pela mediana e `StandardScaler` dentro de um `Pipeline` (evita *data leakage*).
4. **Modelagem** — `train_test_split` estratificado (80/20) e três classificadores:
   Regressão Logística, Random Forest e KNN.
5. **Avaliação** — métrica principal: **Recall** da classe positiva (o pior erro é o falso negativo),
   com F1 como equilíbrio.
6. **Explicabilidade** — Feature Importance (coeficientes) e SHAP.
7. **Discussão crítica** — uso como ferramenta de triagem, limitações e próximos passos.

| Modelo | Accuracy | Precision | Recall | F1 | AUC |
|---|---|---|---|---|---|
| **Regressão Logística** (final) | 0,890 | 0,816 | **0,861** | **0,838** | **0,951** |
| Random Forest | 0,899 | 0,903 | 0,778 | 0,836 | 0,948 |
| KNN | 0,899 | 0,963 | 0,722 | 0,825 | 0,937 |

**Modelo final:** Regressão Logística, por apresentar o maior Recall (menor número de falsos
negativos: 5 em 109 pacientes de teste).

## Fontes

- [Kaggle](https://www.kaggle.com)
