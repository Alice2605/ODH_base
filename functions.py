import streamlit as st
import pandas as pd
import numpy as np
import time 
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from scipy.signal import savgol_filter
import datetime



def calctime(start_time,end_time):
    return(end_time-start_time)
def greentext(text):
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print("["+current_time+"]" "\033[32m" + text + "\033[0m")
def bluetext(text):
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print("["+current_time+"]"+blue_start+ text +blue_end)




@st.cache_data
def plot_metastase_femme_homme(metastaseFEMMEHOMME):
    # Compter le nombre de cas pour chaque sexe et type de métastase
    counts = metastaseFEMMEHOMME.groupby(['PASEX', 'MTYN']).size().reset_index(name='count')
    # Créer le diagramme Sunburst
    fig = px.sunburst(counts, path=['PASEX', 'MTYN'], values='count', color='MTYN',
                      color_discrete_map={'NON': 'rgb(158,202,225)', 'OUI': 'rgb(50,136,189)',
                                          'METASTATIQUE': 'rgb(94,79,162)', 'INITIAL': 'rgb(218,122,26)'})
    # Personnaliser les étiquettes
    fig.update_traces(textinfo='label+percent entry')
    # Afficher le diagramme
    st.plotly_chart(fig)
    st.write("Nous remarquons ici que la population de femmes est plus importante et donc en conséquence une plus grande partie des femmes n'est pas affectée par le taux de métastase. D'un autre côté, les hommes ne représentant que 15% de l'échantillon sont également en majorité non affectés par la métastase.")


@st.cache_data
def plot_smokingnbr(SMOKING_ORGANEFUSION):
# Filtrer les données pour les fumeurs
    smoker_data = SMOKING_ORGANEFUSION[SMOKING_ORGANEFUSION['SMYN'] == "FUMEUR"]
    
    # Grouper les données par organe et maladie, puis calculer le nombre de personnes affectées
    smoker_counts = smoker_data.groupby(['DIORG', 'DITYPE']).size().reset_index(name='Nombre de personnes')
    
    # Créer le graphique à barres empilées pour les fumeurs
    fig_smoker = px.bar(smoker_counts, x='DIORG', y='Nombre de personnes', color='DITYPE',
                        title="Corrélation entre les maladies et les organes touchés (Fumeurs)",
                        barmode='stack')
    
    # Afficher le graphique des fumeurs
    st.plotly_chart(fig_smoker)



@st.cache_data
def plot_smokingnbrno(SMOKING_ORGANEFUSION):
    # Filtrer les données pour les non fumeurs
    non_smoker_data = SMOKING_ORGANEFUSION[SMOKING_ORGANEFUSION['SMYN'] != "FUMEUR"]
    
    # Grouper les données par organe et maladie, puis calculer le nombre de personnes affectées
    non_smoker_counts = non_smoker_data.groupby(['DIORG', 'DITYPE']).size().reset_index(name='Nombre de personnes')
    
    # Créer le graphique à barres empilées pour les non fumeurs
    fig_non_smoker = px.bar(non_smoker_counts, x='DIORG', y='Nombre de personnes', color='DITYPE',
                            title="Corrélation entre les maladies et les organes touchés (Non fumeurs)",
                            barmode='stack')
    
    # Afficher le graphique des non fumeurs
    st.plotly_chart(fig_non_smoker)



@st.cache_data
def smoking_metastasis(FUSIONSMOKINGMETASTASIS, add_selectbox):
    for status in FUSIONSMOKINGMETASTASIS["SMYN_RECOD"].unique():
        datafiltered = FUSIONSMOKINGMETASTASIS[FUSIONSMOKINGMETASTASIS["SMYN_RECOD"] != "NR"]
        data = datafiltered[datafiltered["SMYN_RECOD"] == status]["MTLOC_RECOD"].value_counts().reset_index()
        data.columns = ['Tumeur', 'Nombre de cas']
        fig = px.bar(data, x="Tumeur", y="Nombre de cas", title=f"Répartition des tumeurs pour {status}")
        if add_selectbox == status:
            st.plotly_chart(fig)









