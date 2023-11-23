import streamlit as st
# Nom de l'onglet dans le navigateur
st.set_page_config(layout="wide", page_title="Sunburst Diagram")

from functions import *
from oracleconnect import *
from donnees import *


# If I want to write something in the sidebar according to the page which is open
#st.sidebar.header("Animation Demo")


st.markdown("# Sunburst diagram")
st.write(
    """Voici la représentation en sunburst des données du cgfl :"""
)

fig_cgfl_sunburst.update_layout(#title_text="Patients ayant reçu du trastuzumab (tous centres)", 
                  #title_font_size=20,
                  template="plotly_white",
                  
                  margin={"t": 0, "r": 0, "b": 0, "l": 0},
                  width=1800,  # Largeur du graphique
                  height=1100  # Hauteur du graphique
                  ) # Change la taille de police du TITRE
fig_cgfl_sunburst.update_traces(textfont_size=20) # Change la taille de police du texte des NOEUDS

#fig_cgfl_sunburst.update_traces(
#    marker=dict(colors=df_trastuzumab_cgfl.apply(lambda x: 'white' if 'NaN' else None, axis=1))
#)

#fig_cgfl_sunburst.update_traces(visible=False, selector=dict(type='sunburst', labels=['NaN']))
#fig_cgfl_sunburst.show()

fig_cgfl_sunburst.write_html('sunburst_graph.html') # save graph in an html file (if run file directly)

st.plotly_chart(fig_cgfl_sunburst)

