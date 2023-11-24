import plotly.express as px
from functions import *
from oracleconnect import *
import numpy as np



# Données
df_cgfl = searchtodf("""
        SELECT IDPATIENT, IDHOPITAL, DT1DATEADMP, PRODUIT1, SUB_NUM_PROTO, PROTO
				FROM ODH_SEIN
				WHERE IDHOPITAL = 210987731 AND IDPATIENT IN (SELECT DISTINCT IDPATIENT FROM ODH_SEIN WHERE PRODUIT1 = 'trastuzumab' OR
          PRODUIT1 = 'trastuzumab emtansine' OR PRODUIT1 = 'trastuzumab duocarmazine' OR PRODUIT1 = 'trastuzumab deruxtecan')
        ORDER BY IDPATIENT ASC, DT1DATEADMP ASC
        """)
df_trastuzumab_cgfl = df_to_df_trastuzumab(df_cgfl) # Crée la table avec les lignes de protocoles et leur fréquence

colonnes = df_trastuzumab_cgfl.columns[:-1].tolist()


# Sunburst
fig_cgfl_sunburst = px.sunburst(df_trastuzumab_cgfl[df_trastuzumab_cgfl != "NaN"], path=colonnes, values='VALUE')

df_trastuzumab_cgfl.fillna("NaN", inplace=True)



# Sankey
labels_reel, label_color, links = donnees_diagram(df_trastuzumab_cgfl) # Récupère les variables de label, couleur, source, target et valeur
fig_cgfl_sankey = cree_sankey(labels_reel, label_color, links)



# Commit and close when finished
connection.commit()
connection.close()
