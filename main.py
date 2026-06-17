import streamlit as st
import pandas as pd

st.title("Drogaria Sabrina")
st.write(
    "Importe a planilha exportada do Alpha7, bipe as notas e monte a lista de chaves para controle."
)

arquivo = st.file_uploader(
    "Escolha o arquivo das notas", type=["xlsx", "xls"]
)

if arquivo:
    df = pd.read_excel(arquivo)
    colunas = ["Chave Acesso", "Status", "Número"]
    df = df[colunas]
    st.write("Colunas encontradas:")
    
    st.write(df.columns)
    
    st.write(f"Quantidade de notas encontradas: {len(df)}")

    chave = st.text_input(
        "Bipe a nota",
        placeholder="Aguardando leitura..."
    )

    if chave:
        resultado = df[df["Chave Acesso"].astype(str) == chave]

        if not resultado.empty:
            status = resultado.iloc[0]["Status"]
            if status == "Conferida":
                st.success("Nota Conferida - OK!")
            elif status == "Recebida":
                st.warning("Nota recebida, mas ainda não conferida.")
            elif status == "Inicial" or status == "Cancelada":
                st.error(f"Nota com status '{status}' encontrada. Verificar a situação da nota!")
        else:
            st.error("Nota não encontrada.")