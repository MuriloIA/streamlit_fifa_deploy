import streamlit as st

st.set_page_config(
    page_icon='⚽',
    layout='wide'
)

df_data = st.session_state['data']

# Selecbox (Caixa de seleção) - Club
clubs = df_data['Club'].unique()
club  = st.sidebar.selectbox(label='Club', options=clubs)

# Filtrando os dados por clube
df_filtered = df_data[df_data['Club'] == club].set_index("Name")
st.image(df_filtered.iloc[0]['Club Logo'])
st.markdown(f"## {club}")

st.dataframe(df_filtered,
             column_config={
                 "Overall": st.column_config.ProgressColumn(
                     min_value=0, max_value=100, format="%d"
                 ),
                 "Wage(£)": st.column_config.ProgressColumn("Weekly Wage", format="£%f",
                                                            min_value=0, max_value=df_filtered['Wage(£)'].max()
                 ),
                 "Photo": st.column_config.ImageColumn(),
                 "Flag": st.column_config.ImageColumn("Country"),
                 "Club Logo": st.column_config.ImageColumn()
                
             })