import pandas as pd
import matplotlib.pyplot as plt
import pycountry_convert as pc


# Charger le fichier CSV
chemin_fichier = r'C:\Users\frup00090927\Code File\Code-File\Data\Annuaire Alumni ABC  - Annuaire Alumni ABC.csv'
df = pd.read_csv(chemin_fichier)


# Afficher les informations sur les valeurs uniques dans la colonne 'Pays de résidence'
countries_residence_info = df['Pays de résidence'].value_counts(dropna=False)

# Créer un DataFrame à partir des informations
df_countries_info = pd.DataFrame({
    'Pays de résidence': countries_residence_info.index,
    'Nombre de personnes': countries_residence_info.values
})

# Afficher le DataFrame
# print(df_countries_info)


# Définir une fonction pour obtenir le continent à partir du code ISO du pays
def get_continent(country):
    try:
        country_code = pc.country_name_to_country_alpha2(country, cn_name_format="default")
        continent_code = pc.country_alpha2_to_continent_code(country_code)
        continent_name = pc.convert_continent_code_to_continent_name(continent_code)
        return continent_name
    except:
        return 'Inconnu'

# Appliquer la fonction pour obtenir le continent pour chaque entreprise
df['Continent'] = df['Pays de résidence'].apply(get_continent)

# Filtrer les entreprises en Afrique
entreprises_afrique = df[df['Continent'] == 'Africa']['Entreprises'].unique()

# Filtrer les entreprises en Europe
entreprises_europe = df[df['Continent'] == 'Europe']['Entreprises'].unique()

# Initialiser un nouveau DataFrame pour stocker les résultats
resultats_df = pd.DataFrame(columns=['Entreprise', 'Continent', 'Emails'])

# Fonction pour extraire les adresses e-mail d'une entreprise (à adapter selon votre structure de données)
def extract_emails(entreprise):
    emails = df[df['Entreprises'] == entreprise]['Email'].unique()
    return emails

# Remplir le DataFrame avec les résultats
for entreprise in entreprises_afrique:
    emails_afrique = extract_emails(entreprise)
    resultats_df = pd.concat([resultats_df, pd.DataFrame({'Entreprise': [entreprise], 'Continent': ['Afrique'], 'Emails': [emails_afrique]})], ignore_index=True)

for entreprise in entreprises_europe:
    emails_europe = extract_emails(entreprise)
    resultats_df = pd.concat([resultats_df, pd.DataFrame({'Entreprise': [entreprise], 'Continent': ['Europe'], 'Emails': [emails_europe]})], ignore_index=True)


#Spécifier le chemin du dossier Data du drive
chemin_dossier = r'G:\Drive partagés\Général 2023-2024\Pôle IT & Data Management\Data\Résultats_Stats'
# Enregistrer le DataFrame dans un fichier Excel
nom_fichier_excel = fr'\Cordonnées_alumni_entreprises.xlsx'
chemin_fichier_excel = chemin_dossier + nom_fichier_excel

with pd.ExcelWriter(chemin_fichier_excel, engine='openpyxl') as writer:
    # Enregistrer le DataFrame dans une feuille nommée 'Resultats'
    resultats_df.to_excel(writer, index=False, sheet_name='Resultats')

    # Ajouter une feuille 'Description' avec une description du fichier
    description_sheet = writer.book.create_sheet('Description')
    description_sheet['A1'] = 'Description du fichier Excel'
    description_sheet['A2'] = 'Ce fichier contient les résultats de la recherche des entreprises en Afrique et en Europe.'

print(f"Fichier Excel enregistré : {chemin_fichier_excel}")
# Afficher le DataFrame final
print(resultats_df)