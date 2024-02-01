import base64
from io import BytesIO
from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import pycountry_convert as pc

app = Flask(__name__)

@app.route('/')
def dashboard():

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

        # Créer un graphique en secteurs
        plt.figure(figsize=(8, 8))
        plt.pie(tailles, labels=etiquettes, colors=couleurs, autopct='%1.1f%%', startangle=140)

        # Dessiner un cercle blanc au centre pour créer l'effet de donut
        cercle_central = plt.Circle((0, 0), 0.70, fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(cercle_central)

        plt.title('Alumni par secteurs')
        plt.axis('equal')  # Un rapport d'aspect égal garantit que le graphique en secteurs est circulaire.
        # Convertir le graphique en une image base64
        img_buf = BytesIO()
        plt.savefig(img_buf, format='png')
        img_buf.seek(0)
        img_base64 = base64.b64encode(img_buf.read()).decode('utf-8')
        plt.close()


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
        # Convertir le DataFrame en HTML
        resultats_html = resultats_df.to_html(classes='table table-striped', index=False)

        return render_template('dashboard.html', resultats_html=resultats_html,img_base64=img_base64)



if __name__ == '__main__':
    app.run(debug=True)