import streamlit as st # type: ignore

st.title("Calculadora de IMC")

peso = st.number_input("Digite o seu peso:")

altura = st.number_input("Digite a sua altura:")

if altura > 0 and peso > 0:
    IMC = peso / (altura**2) 
    st.text(f"O seu IMC é de {IMC}.")
