import pandas as pd
import streamlit as st

@st.cache_data
def get_data():
    df = pd.read_excel("essen.xlsx")
    mwe = df.mean()
    mwt = df.mean(axis=1)
    mwt.index = df.Name
    return df, mwe, mwt

df, mwe, mwt = get_data()


rand = st.sidebar.selectbox("Tiere oder Essen", ("Tiere", "Essen"))

if rand == "Tiere":
    col1, col2, col3, col4, col5 = st.columns(5)
    columns = [col1, col2, col3, col4, col5]
    for i in range(5):
        with columns[i]:
              st.metric(label= df.Name[i], value=mwt[i].round(1), delta=(mwt[i].round(1) -50).round())

if rand == "Essen":
    col1, col2, col3, col4, col5 = st.columns(5)
    columns = [col1, col2, col3, col4, col5]
    for i in range(5):
        with columns[i]:
              st.metric(label= df.columns[i+1], value=mwe[i].round(1), delta=(mwe[i].round(1) -50).round())

