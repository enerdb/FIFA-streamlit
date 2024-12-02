import streamlit as st

st.set_page_config(
    page_title="Players",
    page_icon='🏃‍♂️',
    layout = 'wide'
)

df_data = st.session_state['data']

clubes = df_data['Club'].unique()
club = st.sidebar.selectbox('Clube', clubes)
df_players = df_data[df_data['Club'] == club]

players = df_data['Name'].unique()
player = st.sidebar.selectbox('Jogador', players)

player_stats = df_data[df_data['Name']==player].iloc[0]


st.image(player_stats['Photo'])
st.title(player_stats['Name'])
st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f"**Posição:** {player_stats['Position']}")

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:** {player_stats['Age']}")
col2.markdown(f"**Altura:** {player_stats['Height(cm.)']/100}")
col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)']*0.453:.2f}")
#col1.markdown(f"**Idade:** {player_stats['Age']}")
st.divider()

st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))


col1, col2 = st.columns(2)
col1.metric(label='Valor de mercado', value = f"£ {player_stats['Value(£)']:,}")
#col2.metric(f"**Altura:** {player_stats['Height(cm.)']/100}")
#col3.metric(f"**Peso:** {player_stats['Weight(lbs.)']*0.453:.2f}")


st.write(df_data)
st.write(df_players)