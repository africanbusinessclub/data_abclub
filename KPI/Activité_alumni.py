import pandas as pd
import matplotlib.pyplot as plt
import pycountry_convert as pc


# Charger le fichier CSV
chemin_fichier = r'C:\Users\frup00090927\Code File\Code-File\Data\Annuaire Alumni ABC  - Annuaire Alumni ABC.csv'
df = pd.read_csv(chemin_fichier)

# Obtenir le nombre d'occurrences de chaque secteur d'activité
comptes_secteurs = df['Secteur d\'activité'].value_counts()

# Séparer les cinq principaux secteurs
secteurs_finance = comptes_secteurs.filter(like='Finance', axis=0).sum()
secteurs_it = comptes_secteurs.filter(like='IT', axis=0).sum()
secteurs_conseil = comptes_secteurs.filter(like='Consulting', axis=0).sum()
secteurs_logistique = comptes_secteurs.filter(like='Logistics', axis=0).sum()
secteurs_marketing = comptes_secteurs.filter(like='Marketing', axis=0).sum()

# Tracer le nombre d'occurrences des cinq principaux secteurs avec un graphique en anneau
etiquettes = ['Finance', 'IT', 'Consulting', 'Logistics', 'Marketing']
tailles = [secteurs_finance, secteurs_it, secteurs_conseil, secteurs_logistique, secteurs_marketing]
couleurs = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen', 'orange']

# # Créer un graphique en secteurs
# plt.figure(figsize=(8, 8))
# plt.pie(tailles, labels=etiquettes, colors=couleurs, autopct='%1.1f%%', startangle=140)

# # Dessiner un cercle blanc au centre pour créer l'effet de donut
# cercle_central = plt.Circle((0, 0), 0.70, fc='white')
# fig = plt.gcf()
# fig.gca().add_artist(cercle_central)

# plt.title('Alumni par secteurs')
# plt.axis('equal')  # Un rapport d'aspect égal garantit que le graphique en secteurs est circulaire.

# # Enregistrer le graphique en tant qu'image
# plt.savefig('Activité_alumni.png')

# plt.tight_layout()
# # Afficher le graphique en donut
# plt.show()


# Afficher les informations sur les valeurs uniques dans la colonne 'Pays de résidence'
countries_residence_info = df['Pays de résidence'].value_counts(dropna=False)

# Créer un DataFrame à partir des informations
df_countries_info = pd.DataFrame({
    'Pays de résidence': countries_residence_info.index,
    'Nombre de personnes': countries_residence_info.values
})

# Afficher le DataFrame
print(df_countries_info)


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

# Afficher les listes d'entreprises
print("Entreprises en Afrique :", entreprises_afrique)
print("Entreprises en Europe :", entreprises_europe)

