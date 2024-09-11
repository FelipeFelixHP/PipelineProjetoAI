import streamlit as st
from datetime import datetime, time
import contrato



def main():

    st.title("Sistema de CRM Vendas da ZapFlow - Frontend Simples")
    email = st.text_input("Campo de texto para inserção do email do vendedor")
    data=  st.date_input("Campo para selecionar a data em que a venda foi realizada.", datetime.now())
    hora= st.time_input("Hora em que a venda foi realizada.", value=time(9,0))
    valor=st.number_input("valor monetário da venda realizada.", min_value=0.0, format="%.2f")
    quantidade=st.number_input("Quantidade de produtos vendidos.", min_value=1, step=1)
    produto=st.selectbox("Campo de seleção para escolher o produto vendido.", ["ZapFlow com Llama3.0", "ZapFlow com chatGPT", "ZapFlow com Gemini"])

    if st.button("Salvar"):
        st.write("**Dados da Venda:**")
        data_hora = datetime.combine(data, hora)
        
        st.write(f"Email do Vendedor: {email}")
        st.write(f"Data e Hora da Compra: {data_hora}")


if __name__ =="__main__":
    main()