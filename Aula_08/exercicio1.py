import streamlit as st # pyright: ignore[reportMissingImports]

st.title("Conversor de moedas")

# ENTRADA
dolar = st.number_input("Digite o valor em DÓLAR:",placeholder="Dólar", step=2)

# PROCESSAMENTO
reais = dolar * 5


# SAÍDA
st.text(f"O valor de {dolar:.2f} dolares é igual à {reais:.2f} reais")