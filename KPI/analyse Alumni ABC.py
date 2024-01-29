# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 20:14:07 2024

@author: andre
"""

import numpy as np
import pandas as pd

# Spécifiez le nouveau chemin vers votre fichier CSV
chemin_fichier_csv = r'C:\Users\frup00090927\Code File\Code-File\Data\Annuaire Alumni ABC  - Annuaire Alumni ABC.csv'

# Utilisez la fonction read_csv() de pandas pour lire le fichier CSV
df_annuaire = pd.read_csv(chemin_fichier_csv)

# Afficher les données importées
print(df_annuaire)


#df_annuaire.info()

#df_annuaire_sans_na = df_annuaire.dropna()


# for nom_colonne in df_annuaire:
#     if df_annuaire[nom_colonne].dtype == 'object':
#         print(f"Statistiques pour la colonne : {nom_colonne}")
#         print(df_annuaire[nom_colonne].value_counts())
#         print("\n")



        
import os

# Spécifiez le chemin du nouveau répertoire
chemin_repertoire = "C:/Users/frup00090927/gitAbcData"

# Vérifier si le répertoire existe, sinon le créer
if not os.path.exists(chemin_repertoire):
    os.makedirs(chemin_repertoire)

personnes_paris = df_annuaire[df_annuaire['Ville de résidence'] == 'Paris']
personnes_abidjan = df_annuaire[df_annuaire['Ville de résidence'] == 'Abidjan']

# personnes_paris.to_excel(chemin_repertoire, index=False)
# personnes_abidjan.to_excel(chemin_repertoire, index=False)


##exporter les infos des personnes qui sont à paris et à Abidjan
personnes_paris.to_excel(os.path.join(chemin_repertoire, "personnes_paris.xlsx"), index=False, engine='openpyxl')
personnes_abidjan.to_excel(os.path.join(chemin_repertoire, "personnes_abidjan.xlsx"), index=False, engine='openpyxl')


#########################################################################################################

# """pour garder cela juste dans python"""
# # Initialiser un dictionnaire pour stocker les DataFrames de statistiques
# statistiques_par_colonne = {}

# # Boucle pour calculer les statistiques pour chaque colonne qualitative
# for nom_colonne in df_annuaire:
#     if df_annuaire[nom_colonne].dtype == 'object':
#         # Calculer les statistiques pour la colonne
#         statistiques_colonne = df_annuaire[nom_colonne].value_counts().reset_index()
#         statistiques_colonne.columns = [nom_colonne, 'Fréquence']

#         # Stocker les statistiques dans le dictionnaire
#         statistiques_par_colonne[nom_colonne] = statistiques_colonne

# # Afficher les DataFrames de statistiques
# for nom_colonne, df_statistiques in statistiques_par_colonne.items():
#     print(f"Statistiques pour la colonne : {nom_colonne}")
#     print(df_statistiques)
#     print("\n")
    
 ######################################################################################################


# Initialiser un dictionnaire pour stocker les DataFrames de statistiques
statistiques_par_colonne = {}

# Boucle pour calculer les statistiques pour chaque colonne qualitative
for nom_colonne in df_annuaire:
    if df_annuaire[nom_colonne].dtype == 'object':
        # Calculer les statistiques pour la colonne
        statistiques_colonne = df_annuaire[nom_colonne].value_counts().reset_index()
        statistiques_colonne.columns = [nom_colonne, 'Fréquence']

        # Stocker les statistiques dans le dictionnaire
        statistiques_par_colonne[nom_colonne] = statistiques_colonne

# Créer un fichier Excel pour stocker toutes les statistiques
fichier_excel_statistiques = os.path.join(chemin_repertoire, 'statistiques_par_colonne.xlsx')
with pd.ExcelWriter(fichier_excel_statistiques, engine='openpyxl') as writer:
    for nom_colonne, df_statistiques in statistiques_par_colonne.items():
        # Remplacer les espaces et les caractères spéciaux dans le nom de la colonne
        nom_colonne_modifie = nom_colonne.replace(' ', '_').replace('/', '_').replace('\\', '_')
        # Exporter le DataFrame dans une feuille Excel
        df_statistiques.to_excel(writer, sheet_name=nom_colonne_modifie, index=False)


# ## exporter les df en fichiers excel      
# for nom_colonne, df_statistiques in statistiques_par_colonne.items():
#     # Remplacez les espaces et les caractères spéciaux dans le nom de la colonne
#     nom_colonne_modifie = nom_colonne.replace(' ', '_').replace('/', '_').replace('\\', '_')
#     # Nom complet du fichier Excel avec le chemin
#     nom_fichier_excel = os.path.join(chemin_repertoire, f"{nom_colonne_modifie}_statistiques.xlsx")
#     # Exporter le DataFrame dans le fichier Excel
#     df_statistiques.to_excel(nom_fichier_excel, index=False)   
    