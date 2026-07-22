"""Seleciona apenas as colunas utilizadas no projeto."""

from pathlib import Path

import pandas as pd


# Colunas que serão utilizadas no projeto
COLUNAS = [
    "NU_IDADE_N",
    "CS_RACA",
    "CS_ESCOL_N",
    "SIT_CONJUG",
    "CS_GESTANT",
    "DEF_TRANS",
    "DEF_FISICA",
    "DEF_MENTAL",
    "DEF_VISUAL",
    "DEF_AUDITI",
    "TRAN_MENT",
    "SG_UF",
    "LOCAL_OCOR",
    "VIOL_FISIC",
    "VIOL_PSICO",
    "VIOL_SEXU",
    "VIOL_NEGLI",
    "VIOL_FINAN",
    "VIOL_TORT",
    "LES_AUTOP",
    "AG_FORCA",
    "AG_CORTE",
    "AG_FOGO",
    "AG_AMEACA",
    "REL_CONJ",
    "REL_EXCON",
    "REL_NAMO",
    "REL_PAI",
    "REL_MAE",
    "AUTOR_SEXO",
    "AUTOR_ALCO",
    "NUM_ENVOLV",
    "OUT_VEZES",
]


def obter_arquivo_entrada(raiz_projeto: Path) -> Path:
    """Retorna o arquivo de entrada disponível."""

    candidatos = [
        raiz_projeto / "data" / "raw" / "VIOLBR25.xlsx",
        raiz_projeto / "data" / "raw" / "VIOLBR25_ptbr.csv",
    ]

    for caminho in candidatos:
        if caminho.exists():
            return caminho

    raise FileNotFoundError(
        "Nenhum arquivo encontrado em data/raw."
    )


def ler_dataset(arquivo: Path) -> pd.DataFrame:
    """Lê o dataset conforme a extensão."""

    if arquivo.suffix.lower() == ".xlsx":
        return pd.read_excel(arquivo)

    if arquivo.suffix.lower() == ".csv":
        return pd.read_csv(
            arquivo,
            sep=";",
            low_memory=False,
        )

    raise ValueError(
        f"Formato não suportado: {arquivo.suffix}"
    )


def main():
    """Seleciona as variáveis do projeto."""

    raiz_projeto = Path(__file__).resolve().parent.parent

    arquivo_entrada = obter_arquivo_entrada(raiz_projeto)

    pasta_saida = raiz_projeto / "data" / "processed"
    pasta_saida.mkdir(parents=True, exist_ok=True)

    print("Lendo dataset...")

    df = ler_dataset(arquivo_entrada)

    print(f"Registros: {len(df):,}")
    print(f"Colunas: {len(df.columns)}")

    print("\nFiltrando apenas mulheres...")

    df = df[df["CS_SEXO"] == "F"]

    print(f"Registros após filtro: {len(df):,}")

    colunas_faltantes = [
        coluna
        for coluna in COLUNAS
        if coluna not in df.columns
    ]

    if colunas_faltantes:
        raise ValueError(
            "As seguintes colunas não existem:\n"
            + "\n".join(colunas_faltantes)
        )

    print("\nSelecionando colunas...")

    df = df[COLUNAS]

    print(f"Colunas selecionadas: {len(df.columns)}")

    arquivo_saida = pasta_saida / "VIOLBR25_SELECIONADO.xlsx"

    print("\nSalvando arquivo...")

    df.to_excel(
        arquivo_saida,
        index=False,
    )

    print("\nProcesso concluído com sucesso!")

    print(f"\nArquivo gerado:\n{arquivo_saida}")


if __name__ == "__main__":
    main()