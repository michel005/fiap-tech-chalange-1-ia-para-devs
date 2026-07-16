import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Importa o arquivo CSV
df = pd.read_csv("datasets/Maternal_Risk.csv")

# Mostra as primeiras linhas
# print(df.head())

# print(df.info())

# print(df.describe())

# Conta registros de acordo com a coluna
# print(df['DiastolicBP'].value_counts())

# Removemos RiskLevel do dataframe pois ela vai ser a coluna de resultado
X = df.drop('RiskLevel', axis=1) 
y = df['RiskLevel'] 

# Separa os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.5, stratify=y, random_state=42
)

# Algoritimo de ML: Classificação
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Fazer previsões
y_pred = model.predict(X_test)

print("Treino:", X_train.shape)
print("Teste:", X_test.shape)

# Calcular porcentagem de acertos
accuracy = accuracy_score(y_test, y_pred)

print(f"Acurácia: {accuracy * 100:.2f}%")

# exemplo = X_test.iloc[100]   # pega a primeira linha do conjunto de teste
# exemplo_df = pd.DataFrame([exemplo], columns=X.columns)

# # Previsão final
# print("Previsão:", model.predict(exemplo_df)[0])

# # Probabilidades
# print("Probabilidades:", model.predict_proba(exemplo_df)[0])

# probs = model.predict_proba(exemplo_df)[0]

# # Classes
# classes = model.classes_

# # Gráfico
# plt.bar(classes, probs)
# plt.ylabel("Probabilidade")
# plt.title("Confiança do modelo para cada classe")
# plt.show()