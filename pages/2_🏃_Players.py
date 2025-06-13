import streamlit as st

st.set_page_config(
    page_icon='🏃',
    layout='wide'
)

# Carrega os dados
df_data = st.session_state['data']

# 1 - Selectbox (Caixa de Seleção)
clubes = df_data['Club'].unique()
club   = st.sidebar.selectbox(label='Club', options=clubes)

# 2 - Selecbox (Caixa de Seleção)
df_players = df_data[df_data['Club'] == club]
players = df_players['Name']
player = st.sidebar.selectbox(label='Player', options=players)

# Imagem do jogador & Informações
status_player = df_data[df_data['Name'] == player].iloc[0]
st.image(status_player['Photo'])
st.title(status_player['Name'])
st.markdown(f"**Club**: {status_player['Club']}")
st.markdown(f"**Position**: {status_player['Position']}")

c1, c2, c3 = st.columns(3)
c1.markdown(f'**Age**: {status_player['Age']}')
c2.markdown(f"**Height(m.)**: {status_player['Height(cm.)']/100}")
c3.markdown(f"**Weight(kg.)**: {status_player['Weight(lbs.)']*0.453:.2f}")
st.divider()

# Segunda parte
st.subheader(f"Overall {status_player['Overall']}")
st.progress(int(status_player['Overall']))

c11, c22, c33 = st.columns(3)
c11.metric(label='Valor de mercado', value=f"£ {status_player['Value(£)']:,}")
c22.metric(label='Remuneração semanal', value=f"£ {status_player['Wage(£)']:,}")
c33.metric(label='Cláusula de rescisão', value=f"£ {status_player['Release Clause(£)']:,}")


