import pandas as pd
import seaborn as sns
import plotly.graph_objects as go
import datetime
   



###############################################################################################################################################

def df_to_df_trastuzumab(df):
    # Regroupe chaque num de protocole d'un patient en une ligne (même protocole)

    df_trastuzumab = pd.DataFrame()
    nouvelles_lignes = []

    patient = protocole = None
    num_patients = 0


    for i in range(len(df)): # Itération dans toutes les lignes de df

        if df['IDPATIENT'].iloc[i] != patient: # Pour la première apparition du patient
            
            patient = df['IDPATIENT'].iloc[i]
            num_patients += 1
            protocole = 1

            # Nouvelle ligne pour le nouveau patient
            nouvelles_lignes.append({})
            
        if df['SUB_NUM_PROTO'].iloc[i] == protocole: # Changement de protocole
            nouvelles_lignes[num_patients - 1]['PROTOCOLE' + str(protocole)] = df['PROTO'].iloc[i]
            protocole += 1


    df_trastuzumab = pd.concat([df_trastuzumab, pd.DataFrame(nouvelles_lignes)], axis=1)



    # Regroupe les lignes identiques et rajoute une colonne pour leur nombre d'occurrence

    """Rajoute nombre d'occurrences des lignes et les regroupe"""

    df_trastuzumab.fillna("NaN", inplace=True) # Remplace les NaN par "NaNPlaceholder" pour enlever les erreurs causées par les NaN

    # Compte le nombre d'occurrence de chaque ligne et la met dans la colonne VALUE
    df_trastuzumab['VALUE'] = df_trastuzumab.apply(lambda row: (df_trastuzumab == row).all(axis=1).sum(), axis=1)

    #df_trastuzumab.replace("NaN", pd.NA, inplace=True) # Remet les NaN comme des NaN

    df_trastuzumab = df_trastuzumab.drop_duplicates().reset_index(drop=True) # Supprime les duplicatas de ligne et Réinitialise l'index pour l'avoir correspondant au numéro de ligne

    return df_trastuzumab














###############################################################################################################################################

def donnees_diagram(df_trastuzumab):

    # Nombre de protocoles différents

    # Crée liste vide pour stocker les valeurs uniques de protocoles
    unique_protocoles = []

    # Parcourt toutes les colonnes et trouve les valeurs uniques
    for col in df_trastuzumab.columns:
        if col != "VALUE":
            unique_protocoles.extend(pd.unique(df_trastuzumab[col]))

    # Supprime doublons (convertit en ensemble puis revient à une liste)
    unique_protocoles = list(set(unique_protocoles))


    #print("Valeurs uniques dans toutes les colonnes:", unique_protocoles) # Affiche la liste de toutes les valeurs distinctes

    num_protocoles = len(unique_protocoles)
    #print(num_protocoles)



    # Couleurs

    color_palette = sns.color_palette('husl', num_protocoles)

    label_color = dict(zip(unique_protocoles, ['#%02x%02x%02x' % (int(r * 255), int(g * 255), int(b * 255)) for r, g, b in color_palette]))




    # Données pour le Sankey diagramme

    colonnes = df_trastuzumab.columns.tolist()

    # Labels pour l'affichage
    labels_reel = []
    for c in range(len(colonnes) - 1):
        labels_reel.extend(df_trastuzumab[colonnes[c]].dropna().unique()) # Label (pour le graphique)


    # Ajoute un chiffre après les noms pour différencier les différentes colonnes
    for i in range(1, len(colonnes) - 1):
        df_trastuzumab[colonnes[i]] += str(i + 1)

    #print(df_trastuzumab)


    s = []
    t = []
    v = []
    labels = []

    # Récupère les données pour chaque lien
    for c in range(len(colonnes) - 2):
        s.extend(df_trastuzumab[colonnes[c]].tolist()) # Source
        t.extend(df_trastuzumab[colonnes[c + 1]].tolist()) # Target
        v.extend(df_trastuzumab["VALUE"].tolist()) # Value
        
        labels.extend(df_trastuzumab[colonnes[c]].dropna().unique()) # Label (pour le graphique)
    labels.extend(df_trastuzumab[colonnes[c + 1]].dropna().unique()) # Labels de la dernière colonne


    links = pd.DataFrame({"source": s, "target": t, "value": v})  
    links = links.groupby(["source", "target"], as_index=False).agg({"value": "sum"})

    for l in range(len(labels)):
        links = links.replace({labels[l]: l})

    return labels_reel, label_color, links




def cree_sankey(labels_reel, label_color, links):
    # Crée le diagramme Sankey
    fig = go.Figure(
        data=[
            go.Sankey(
                arrangement='snap',
                node=dict(
                    pad=15,
                    thickness=20,
                    line=dict(color="black", width=0.5),
                    label=labels_reel,
                    color=[label_color[label] for label in labels_reel],
                ),
                link=dict(
                    source=links["source"],
                    target=links["target"],
                    value=links["value"],
                    color=[label_color[labels_reel[source]] for source in links["source"]],
                )
            )
        ]
    )
    return fig



