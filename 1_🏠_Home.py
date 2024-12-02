import streamlit as st
import pandas as pd
from datetime import datetime

if "data" not in st.session_state:
    df_data = pd.read_csv('datasets\CLEAN_FIFA23_official_data.csv', index_col=0)
    df_data = df_data[df_data['Contract Valid Until']>= datetime.today().year]
    df_data = df_data[df_data['Value(£)']> 0]
    df_data = df_data.sort_values(by='Overall', ascending = False)



    st.session_state['data'] = df_data


st.markdown("# FIFA 2023 OFFICIAL DATASET ⚽")
st.sidebar.markdown("Desenvoldido por Ener e [Asimov](https://asimov.academy) ")

st.link_button("Acesse os dados no Kaggle", "https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database")

st.markdown(""" ## Dataset
The dataset contains **+17k unique players** and more than 60 columns, general information and all KPIs the famous videogame offers.
            As the esport scene keeps rising espacially on FIFA, I thought it can be useful for the community (kagglers and/or gamers)"

             ## Context
The data was retrieved thanks to a crawler that I implemented to retrieve:

Aggregated data such as name of the players, age, country
Detailed data such as offensive potential, defense, acceleration
I like football a lot and this dataset is for me the opportunity to bring my contribution for the realization of projects that can go from simple analysis to elaboration of strategies on optimal composition under constraints…

            ## Acknowledgements
We wouldn't be here without the help of others. I would like to thanks @karangadiya who I got inspiration from, check his repo here !"""
            )

