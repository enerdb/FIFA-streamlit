import streamlit as st

st.set_page_config(
    page_title="Players",
    page_icon='🏃‍♂️',
    layout = 'wide'
)

df_data = st.session_state['data']

clubes = df_data['Club'].unique()
club = st.sidebar.selectbox('Clube', clubes)

club_players = df_data[df_data['Club']==club].set_index('Name')

st.image(club_players['Club Logo'].iloc[0])
st.markdown(f'## {club}')

columns = ['Age','Photo','Flag','Overall','Value(£)', 'Wage(£)', 'Joined', 'Height(cm.)','Weight(lbs.)']
st.dataframe(club_players[columns], column_config={
    'Overall': st.column_config.ProgressColumn(
        label = 'Overall', format = '%i', min_value = 0, max_value = 100
    ),
    'Wage(£)': st.column_config.ProgressColumn(
        label = 'Remuneração', format='£%.2f', min_value=0, max_value = df_data['Wage(£)'].max()
    ),
   'Photo': st.column_config.ImageColumn(),
   'Flag': st.column_config.ImageColumn(label = 'País')

})