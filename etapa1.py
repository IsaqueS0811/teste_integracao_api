"""
Teste Técnico – IntuitiveCare
Etapa 1 – Consolidação de Despesas (ANS)

Objetivo:
Consolidar dados de despesas dos últimos três trimestres
a partir das demonstrações contábeis da ANS.

Autor: Isaque
"""
import pandas as pd
import re
from pathlib import Path
import zipfile

# ============================
# CONFIGURAÇÕES
# ============================

PASTA_DADOS = Path("data")
ARQUIVO_SAIDA = Path("data/consolidado_despesas.csv")

# ===============================
# FUNÇÕES AUXILIARES
# ===============================

def extrair_zips(pasta_zip, pasta_destino):
    pasta_destino.mkdir(exist_ok=True)

    for zip_path in pasta_zip.glob("*.zip"):
        print(f"Extraindo {zip_path.name}")
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(pasta_destino)


def identificar_ano_trimestre(nome_arquivo):
    """
    Extrai ano e trimestre a partir do nome do arquivo.
    Exemplo esperado: 1T2025.csv
    """
    padrao = r"(\d)T(\d{4})"
    resultado = re.search(padrao, nome_arquivo)

    if not resultado:
        raise ValueError(f"Nome de arquivo fora do padrão esperado: {nome_arquivo}")

    trimestre = int(resultado.group(1))
    ano = int(resultado.group(2))

    return ano, trimestre


def ler_arquivo_despesas(caminho_arquivo, ano, trimestre):
    """
    Lê um arquivo CSV de despesas e retorna um DataFrame
    padronizado com as colunas necessárias.
    """

    df = pd.read_csv(
        caminho_arquivo,
        sep=";",
        decimal=","
    )

    # Filtrar apenas despesas com eventos/sinistros
    df = df[
        df["DESCRICAO"].str.contains("eventos", case=False, na=False)
        &
        df["DESCRICAO"].str.contains("sinistros", case=False, na=False)
    ]

    # Seleciona apenas as colunas necessárias
    df = df[[
        "REG_ANS",
        "VL_SALDO_FINAL"
    ]].copy()

    # Renomeia coluna de valor
    df.rename(columns={
        "VL_SALDO_FINAL": "ValorDespesas"
    }, inplace=True)

    # Adiciona período
    df["Ano"] = ano
    df["Trimestre"] = trimestre

    return df

# ===============================
# PIPELINE PRINCIPAL
# ===============================

def main():

    # Extração automática (se houver ZIPs)
    extrair_zips(Path("data"), PASTA_DADOS)

    dataframes = []

    arquivos_csv = list(PASTA_DADOS.glob("*.csv"))

    if not arquivos_csv:
        raise FileNotFoundError("Nenhum arquivo CSV encontrado na pasta 'data'.")

    for arquivo in arquivos_csv:
        if arquivo.name == "consolidado_despesas.csv":
            continue

        print(f"Processando: {arquivo.name}")

        ano, trimestre = identificar_ano_trimestre(arquivo.name)

        df = ler_arquivo_despesas(arquivo, ano, trimestre)

        dataframes.append(df)

    df_final = pd.concat(dataframes, ignore_index=True)

    df_final.to_csv(ARQUIVO_SAIDA, index=False, sep=";")

    print("Consolidação concluída com sucesso!")


if __name__ == "__main__":
    main()
