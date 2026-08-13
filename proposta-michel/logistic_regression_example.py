import kagglehub
import pandas
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

kaggleHubDatasetName = "prasoonkottarathil/polycystic-ovary-syndrome-pcos"
datasetFileName = "PCOS_infertility.csv"
resultColumnName = "PCOS (Y/N)"
testSize = 0.25
maximumIteractions=250
lineExample = 2

def printLine():
    print('------------------------------------------------------------------')

print('Analise de dataset utilizando regração logistica')
printLine()

PossibleResults = {
    0: "Não",
    1: "Sim"
}

print(f'[LOG] Baixando dataset {kaggleHubDatasetName}...')
datasetPath = kagglehub.dataset_download(kaggleHubDatasetName)
print(f'[LOG] Dataset baixado na pasta {datasetPath}')

finalDatasetFilePath = f"{datasetPath}/{datasetFileName}"
print('[LOG] Carregando dataset da pasta:', finalDatasetFilePath)

file = pandas.read_csv(finalDatasetFilePath)
print(f'[LOG] Detalhamento do arquivo:\n\n{file.describe()}\n')

print(f'[LOG] Isolando coluna "{resultColumnName}"...')
X = file.drop(resultColumnName, axis=1) 
Y = file[resultColumnName]

print('[LOG] Dividindo dados de treino e teste...')
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=testSize, stratify=Y, random_state=42
)

print('[LOG] Normalizando dados...')
scaler = StandardScaler()
X_train = pandas.DataFrame(scaler.fit_transform(X_train), columns=X.columns)
X_test = pandas.DataFrame(scaler.transform(X_test), columns=X.columns)

print("[LOG] Iniciando modelo de regressão logistica...")
model = LogisticRegression(max_iter=maximumIteractions)
model.fit(X_train, Y_train)
classes = model.classes_

print("[LOG] Calculando dados de previsão...")
y_pred = model.predict(X_test)

print(f"[LOG] Medindo acurácia do modelo...")
accuracy = accuracy_score(Y_test, y_pred)

print(f"[INFO] Acurácia do modelo: {accuracy * 100:.2f}%")
print("[INFO] Total de linhas de treino:", X_train.shape)
print("[INFO] Total de linhas de teste:", X_test.shape)

report = classification_report(Y_test, y_pred, target_names=list(PossibleResults.values()))
print(f"[INFO] Relatório de classificação:\n\n{report}")
printLine()

print('')
print(f'Teste ultilizando exemplo na linha {lineExample}')
printLine()

print(f'[INFO] Linha:\n\n{file.iloc[lineExample]}')

testExample = X_test.iloc[lineExample]
testExampleDataFrame = pandas.DataFrame([testExample], columns=X.columns)
predictResult = model.predict(testExampleDataFrame)[0]

print("\n[INFO] Resultado:", PossibleResults[predictResult])

printLine()