from datetime import datetime
import streamlit as st
import pandas as pd
import webbrowser

st.set_page_config(
    page_icon='🏠'
)

if not "data" in st.session_state:
    df_data = pd.read_csv('datasets/CLEAN_FIFA23_official_data.csv', index_col=0)
    df_data = df_data[df_data['Contract Valid Until'] >= datetime.today().year]
    df_data = df_data[df_data['Value(£)'] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state['data'] = df_data

st.markdown("# FIFA23 OFFICIAL DATASET! ⚽")
st.sidebar.markdown(" ©️ Developed by [Murilo Rocha](https://github.com/MuriloIA)")

btn = st.button('Access the data on Kaggle')
if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

st.markdown("""
            The dataset contains over 17k unique players and over 60 columns, general information 
            and all the KPIs that the famous video game offers. As the eSports scene continues to 
            grow rapidly in FIFA, I thought it might be useful for the community (kagglers and/or 
            gamers)..
            
            **Context**
            The data was recovered thanks to a crawler that I implemented to recover:
            
            - Aggregated data such as player names, ages, countries
            - Detailed data such as offensive potential, defense, acceleration.
            """)

