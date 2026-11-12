import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.read_csv(r"C:\Users\26174746\Desktop\atividade\formativa03\dados_correlacao_pearson_industria.csv", sep=",")

st.subheader("Formativa 03")
st.dataframe(dados)

dados_corr = dados.drop(
    columns=["registro"]
)

matriz_corr = dados_corr.corr(
    numeric_only=True
)

# ==========================================================
# MATRIZ DE CORRELAÇÃO
# ==========================================================
st.subheader("Matriz de Correlação de Pearson")

fig, eixo = plt.subplots(
        figsize=(11,7)
    )

sns.heatmap(
    data=matriz_corr,
    annot=True,
    fmt=".2f",
    ax=eixo
)
eixo.set_title("Matriz de Correlação")
st.pyplot(fig)

# ==========================================================
# IDENTIFICANDO OS PARES
# ==========================================================

col1, col2, col3 = st.columns(3)


with col1:
# ------------------------------
# Maior correlação positiva
# ------------------------------
    maior_corr = -1
    coluna1 = ""
    coluna2 = ""

    for i in matriz_corr.columns:
        for j in matriz_corr.columns:

            if i != j:

                valor = matriz_corr.loc[i, j]

                if valor > maior_corr:
                    maior_corr = valor
                    coluna_pos1 = i
                    coluna_pos2 = j

    st.metric(
        label=f"Maior correlação positiva",
        value=f"{maior_corr:.4f}"
    )

with col2:
# ------------------------------
# Correlação negativa mais forte
# ------------------------------
    menor_corr = 1
    coluna1 = ""
    coluna2 = ""

    for i in matriz_corr.columns:
        for j in matriz_corr.columns:

            if i != j:

                valor = matriz_corr.loc[i, j]

                if valor < menor_corr:
                    menor_corr = valor
                    coluna_neg1 = i
                    coluna_neg2 = j

    st.metric(
        label=f"Correlação negativa mais forte",
        value=f"{menor_corr:.4f}"
    )

with col3:
# -------------------------------
# Correlação mais próxima de zero
# -------------------------------
    corr_zero = 1
    coluna1 = ""
    coluna2 = ""

    for i in matriz_corr.columns:
        for j in matriz_corr.columns:

            if i != j:

                valor = matriz_corr.loc[i, j]

                if abs(valor) < abs(corr_zero):
                    corr_zero = valor
                    coluna_zero1 = i
                    coluna_zero2 = j

    st.metric(
        label=f"Correlação mais próxima de zero",
        value=f"{corr_zero:.4f}"
    )

# ==========================================================
# SCATTERPLOTS
# ==========================================================

st.subheader("Scatterplots")

fig, eixo = plt.subplots(figsize=(8, 5))

sns.scatterplot(
    data=dados,
    x=coluna_pos1,
    y=coluna_pos2,
    ax=eixo
)

eixo.set_title("Maior Correlação Positiva")

st.pyplot(fig)


fig, eixo = plt.subplots(figsize=(8, 5))

sns.scatterplot(
    data=dados,
    x=coluna_neg1,
    y=coluna_neg2,
    ax=eixo
)

eixo.set_title("Correlação Negativa Mais Forte")

st.pyplot(fig)


fig, eixo = plt.subplots(figsize=(8, 5))

sns.scatterplot(
    data=dados,
    x=coluna_zero1,
    y=coluna_zero2,
    ax=eixo
)

eixo.set_title("Correlação Próxima de Zero")

st.pyplot(fig)

st.header("Interpretação")

st.write(
    f"""
    As variáveis {coluna_pos1} e {coluna_pos2} possuem uma correlação positiva de {maior_corr:.4f}, então elas tendem a aumentar juntas.

    As variáveis {coluna_neg1} e {coluna_neg2} possuem uma correlação negativa de {menor_corr:.4f}, então quando uma aumenta, a outra tende a diminuir.

    Já as variáveis {coluna_zero1} e {coluna_zero2} possuem correlação de {corr_zero:.4f}, que é próxima de zero, indicando pouca relação linear entre elas.

    """
)