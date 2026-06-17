import streamlit as st

st.title("Drogaria sabrina")
st.write("Importe a planilha exportada do Alpha7, bipe as notas e monte a lista de chaves para colar na planilha de controle do Drive.")

arquivo = st.file_uploader("Escolha o arquivo das notas", type=["xlsx", "xls"])