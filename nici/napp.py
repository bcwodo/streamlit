import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

@st.cache_data
def get_data():
    df = pd.read_csv("https://raw.githubusercontent.com/bcwodo/streamlit/master/nici/data/essen.csv")
    mwe = df.mean(numeric_only=True)
    mwt = df.mean(axis=1, numeric_only=True)
    mwt.index = df.Name
    return df, mwe, mwt

df, mwe, mwt = get_data()


rand = st.sidebar.selectbox("Tiere oder Essen", ("Tiere", "Essen", "Balkengraph"))

if rand == "Tiere":
    col1, col2, col3, col4, col5 = st.columns(5)
    columns = [col1, col2, col3, col4, col5]
    for i in range(5):
        with columns[i]:
              st.metric(label= df.Name[i], value=mwt[i].round(1), delta=(mwt[i].round(1) -50).round())
    st.markdown(df.style.hide(axis="index").to_html(), unsafe_allow_html=True)

if rand == "Essen":
    col1, col2, col3, col4, col5 = st.columns(5)
    columns = [col1, col2, col3, col4, col5]
    for i in range(5):
        with columns[i]:
              st.metric(label= df.columns[i+1], value=mwe[i].round(1), delta=(mwe[i].round(1) -50).round())
    st.markdown(df.style.hide(axis="index").to_html(), unsafe_allow_html=True)

if rand == "Balkengraph":
     tiere = tuple(df.Name.values)
     auswahl = st.selectbox("Niki Teir", tiere)
     st.dataframe(df.loc[df.Name==auswahl])
     c = df.columns[1:]
     h = df.loc[df.Name==auswahl, c].values[0]
     fig, ax = plt.subplots()
     ax.bar(c, h, color="orange")
     plt.title(auswahl)
     st.pyplot(fig)

     

