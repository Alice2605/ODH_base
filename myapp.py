import streamlit as st
#Configuration de la page
st.set_page_config(layout="wide", page_title="Sankey Diagram")

import pandas as pd
from functions import *
from oracleconnect import *
from donnees import *



#Création d'une classe couleurs pour simplifier l'ajout de couleur dans les logs
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLUE = "\033[34m"






st.markdown(f"<h1 style='text-align: center;'>Diagrammes de Sankey ODH, médicaments injectables par protocole</h1>", unsafe_allow_html=True)

st.write("""
*Voici le début de la table :*
""")

st.write(df_trastuzumab_cgfl.head()) # Affiche les 5 premières lignes de la table



# CGFL
fig_cgfl_sankey.update_layout(title_text="Patients ayant reçu du trastuzumab au CGFL", 
                  title_font_size=30,
                  width=1700  # Largeur du graphique
                  ) # Change la taille de police du TITRE
fig_cgfl_sankey.update_traces(textfont_size=12) # Change la taille de police du texte des NOEUDS

#fig_cgfl_sankey.write_html('sankey_graph.html') # save graph in an html file

st.plotly_chart(fig_cgfl_sankey)


