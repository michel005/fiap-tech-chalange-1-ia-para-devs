# 📘 Análise de Dataset com Regressão Logística

## 📌 Descrição
Este projeto aplica **regressão logística** para analisar dados relacionados à **Síndrome dos Ovários Policísticos (PCOS)**.  
O objetivo é treinar um modelo de classificação capaz de prever a presença de PCOS com base em variáveis clínicas.

---

## ⚙️ Tecnologias utilizadas
- **Python**
- **Pandas** → manipulação de dados  
- **Scikit-learn** → modelagem e métricas  
- **KaggleHub** → download do dataset  

---

## 📂 Dataset
- Fonte: Kaggle – *Polycystic Ovary Syndrome (PCOS)*  
- Arquivo utilizado: `PCOS_infertility.csv`  
- Coluna alvo: **`PCOS (Y/N)`**  

---

## 🚀 Como executar

Para rodar o projeto localmente, siga os passos:

1. Clone o repositório:
```bash
git clone https://github.com/seuusuario/seuprojeto.git
```
2. Crie e ative um ambiente virtual (opcional, mas recomendado):
```sh
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
```

3. Instale as dependências:
```sh
pip install pandas scikit-learn kagglehub
```

4. Execute o script principal:
```sh
python logistic_regression_example.py
```

---

## ⚙️ Parâmetros do projeto

No início do arquivo principal, alguns parâmetros podem ser ajustados para controlar o comportamento do modelo:

- **`kaggleHubDatasetName`** → Nome do dataset no Kaggle que será baixado.  
- **`datasetFileName`** → Nome do arquivo CSV dentro da pasta do dataset.  
- **`resultColumnName`** → Nome da coluna alvo (variável dependente) que indica se há PCOS (`PCOS (Y/N)`).  
- **`testSize`** → Proporção dos dados reservados para teste (ex.: `0.25` significa 25%).  
- **`maximumIteractions`** → Número máximo de iterações permitidas para o algoritmo de regressão logística.  
- **`lineExample`** → Índice da linha usada para teste individual de previsão.  

Esses parâmetros podem ser modificados conforme necessário para explorar diferentes cenários, ajustar o tamanho do conjunto de teste ou escolher outra linha para validação manual.

---

## 📊 Resultados
O modelo calcula:
- **Acurácia** → proporção de previsões corretas em relação ao total de casos.  
- **Precisão (Precision)** → entre os casos previstos como positivos, quantos realmente eram positivos.  
- **Recall (Sensibilidade)** → entre os casos que realmente eram positivos, quantos o modelo conseguiu identificar corretamente.  
- **F1-score** → média harmônica entre precisão e recall, útil para avaliar o equilíbrio entre os dois.  
- **Support** → número de ocorrências reais de cada classe no conjunto de teste.

Exemplo de saída:
```txt
Acurácia do modelo: 65.44%

Relatório de classificação:
precision    recall  f1-score   support
Não       0.69      0.90      0.78        92
Sim       0.40      0.14      0.20        44
```

---

## 🔎 Pipeline do projeto
1. **Download** do dataset via KaggleHub  
2. **Carregamento** com Pandas  
3. **Exploração inicial** (`describe()`)  
4. **Separação** em treino e teste  
5. **Normalização** com StandardScaler  
6. **Treinamento** com regressão logística  
7. **Avaliação** com métricas  
8. **Teste individual** de previsão  

---

## 🔮 Próximos passos
- Aplicar **balanceamento de classes** (`class_weight="balanced"` ou SMOTE).  
- Explorar **outros algoritmos** como Random Forest ou XGBoost.  
- Realizar **análise exploratória** mais detalhada com gráficos.  
- Adicionar **probabilidades de previsão** para enriquecer os resultados.  

---

## 👤 Autor
Projeto desenvolvido por **Michel** como parte do **Tech Challenge – Fase 1**.
