import streamlit as st
#Configuration de la page
st.set_page_config(layout="wide")

import pandas as pd
import numpy as np
import time 
import matplotlib.pyplot as plt
import plotly.express as px
from functions import *
from oracleconnect import *
from donnees import *
import datetime
import sys
import time






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



st.markdown(f"<h1 style='text-align: center;'>My first app</h1>", unsafe_allow_html=True)

st.write("""
Hello *world!*
""")


st.write(df_trastuzumab.head())
#st.line_chart(df)



fig.update_layout(title_text="Diagramme Sankey de Trastuzumab", 
                  title_font_size=30, 
                  title_x=0.5,
                  width=1700  # Largeur du graphique
                  ) # Change la taille de police du TITRE
fig.update_traces(textfont_size=12) # Change la taille de police du texte des NOEUDS


st.plotly_chart(fig)








