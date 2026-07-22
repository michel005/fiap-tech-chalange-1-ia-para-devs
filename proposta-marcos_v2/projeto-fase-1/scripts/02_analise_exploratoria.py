"""Gera gráficos para análise exploratória do dataset."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


# ===========================
# Dicionários de tradução
# ===========================

RACA = {
    1: "Branca",
    2: "Preta",
    3: "Amarela",
    4: "Parda",
    5: "Indígena",
    9: "Ignorado",
}

SITUACAO_CONJUGAL = {
    1: "Solteira",
    2: "Casada",
    3: "Viúva",
    4: "Separada",
    5: "União Estável",
    8: "Não se aplica",
    9: "Ignorado",
}

GESTANTE = {
    1: "1º Trimestre",
    2: "2º Trimestre",
    3: "3º Trimestre",
    4: "Idade Ignorada",
    5: "Não",
    6: "Não se Aplica",
    9: "Ignorado",
}


# ===========================
# Caminhos
# ===========================

raiz = Path(__file__).resolve().parent.parent

arquivo = raiz / "data" / "processed" / "VIOLBR25_SELECIONADO.xlsx"

pasta_graficos = raiz / "graficos"

pasta_graficos.mkdir(exist_ok=True)

print("Lendo dataset...")

df = pd.read_excel(arquivo)

print(f"Registros: {len(df):,}")

# ===========================
# Cor / Raça
# ===========================

print("Gerando gráfico de raça...")

df["Cor"] = df["CS_RACA"].map(RACA)

plt.figure(figsize=(10, 6))

df["Cor"].value_counts().plot(kind="bar")

plt.title("Distribuição das vítimas por raça")

plt.xlabel("Raça")

plt.ylabel("Quantidade")

plt.tight_layout()

plt.savefig(pasta_graficos / "01_raca.png")

plt.close()

# ===========================
# Estado Civil
# ===========================

print("Gerando gráfico de estado civil...")

df["EstadoCivil"] = df["SIT_CONJUG"].map(SITUACAO_CONJUGAL)

plt.figure(figsize=(10, 6))

df["EstadoCivil"].value_counts().plot(kind="bar")

plt.title("Estado Civil")

plt.xlabel("Situação")

plt.ylabel("Quantidade")

plt.tight_layout()

plt.savefig(pasta_graficos / "02_estado_civil.png")

plt.close()

# ===========================
# Gestantes
# ===========================

print("Gerando gráfico de gestantes...")

df["Gestante"] = (
    pd.to_numeric(df["CS_GESTANT"], errors="coerce")
    .astype("Int64")
    .map(GESTANTE)
)

# Ordem desejada das categorias
ordem = [
    "Não",
    "1º Trimestre",
    "2º Trimestre",
    "3º Trimestre",
    "Idade Ignorada",
    "Não se Aplica",
    "Ignorado",
]

contagem = (
    df["Gestante"]
    .value_counts()
    .reindex(ordem, fill_value=0)
)

plt.figure(figsize=(10, 6))

ax = contagem.plot(
    kind="barh",
    color="steelblue",
)

# Maior categoria no topo
ax.invert_yaxis()

plt.title("Distribuição das Gestantes", fontsize=16)
plt.xlabel("Quantidade", fontsize=12)
plt.ylabel("Situação", fontsize=12)

# Escreve a quantidade ao lado de cada barra
for barra in ax.patches:
    largura = barra.get_width()

    ax.annotate(
        f"{int(largura):,}".replace(",", "."),
        (
            largura,
            barra.get_y() + barra.get_height() / 2,
        ),
        xytext=(5, 0),
        textcoords="offset points",
        ha="left",
        va="center",
        fontsize=9,
    )

plt.tight_layout()

plt.savefig(
    pasta_graficos / "03_gestantes.png",
    dpi=300,
)

plt.close()



# ===========================
# Estado
# ===========================

UF = {
    11: "RO",
    12: "AC",
    13: "AM",
    14: "RR",
    15: "PA",
    16: "AP",
    17: "TO",
    21: "MA",
    22: "PI",
    23: "CE",
    24: "RN",
    25: "PB",
    26: "PE",
    27: "AL",
    28: "SE",
    29: "BA",
    31: "MG",
    32: "ES",
    33: "RJ",
    35: "SP",
    41: "PR",
    42: "SC",
    43: "RS",
    50: "MS",
    51: "MT",
    52: "GO",
    53: "DF",
}

print("Gerando gráfico por estado...")

# Converte código IBGE para a sigla do estado
df["UF"] = (
    pd.to_numeric(df["SG_UF"], errors="coerce")
    .astype("Int64")
    .map(UF)
)

# Conta os casos por estado
contagem_estados = df["UF"].value_counts().sort_values(ascending=False)

plt.figure(figsize=(14, 6))

ax = contagem_estados.plot(
    kind="bar",
    color="steelblue",
)

plt.title("Quantidade de Casos por Estado", fontsize=16)
plt.xlabel("Estado", fontsize=12)
plt.ylabel("Quantidade de Casos", fontsize=12)
plt.xticks(rotation=0)

# Escreve o valor acima de cada barra
for barra in ax.patches:
    altura = barra.get_height()

    ax.annotate(
        f"{int(altura):,}".replace(",", "."),
        (
            barra.get_x() + barra.get_width() / 2,
            altura,
        ),
        ha="center",
        va="bottom",
        fontsize=9,
    )

plt.tight_layout()

plt.savefig(
    pasta_graficos / "04_estados.png",
    dpi=300,
)

plt.close()

# ===========================
# Deficiência
# ===========================

print("Gerando gráfico de deficiência...")

deficiencias = {
    "Deficiência Física": (df["DEF_FISICA"] == 1).sum(),
    "Deficiência Mental": (df["DEF_MENTAL"] == 1).sum(),
    "Deficiência Visual": (df["DEF_VISUAL"] == 1).sum(),
    "Deficiência Auditiva": (df["DEF_AUDITI"] == 1).sum(),
    "Transtorno Mental": (df["TRAN_MENT"] == 1).sum(),
}

plt.figure(figsize=(10, 6))

plt.bar(deficiencias.keys(), deficiencias.values())

plt.title("Tipos de Deficiência")

plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig(pasta_graficos / "05_deficiencias.png")

plt.close()

# ===========================
# Tipos de Violência
# ===========================

print("Gerando gráfico dos tipos de violência...")

violencias = {
    "Física": (df["VIOL_FISIC"] == 1).sum(),
    "Psicológica": (df["VIOL_PSICO"] == 1).sum(),
    "Sexual": (df["VIOL_SEXU"] == 1).sum(),
    "Negligência": (df["VIOL_NEGLI"] == 1).sum(),
    "Financeira": (df["VIOL_FINAN"] == 1).sum(),
    "Tortura": (df["VIOL_TORT"] == 1).sum(),
}

plt.figure(figsize=(10, 6))

plt.bar(violencias.keys(), violencias.values())

plt.title("Tipos de Violência")

plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig(pasta_graficos / "06_tipos_violencia.png")

plt.close()

print()

print("Gráficos gerados com sucesso!")

print()

print(pasta_graficos)