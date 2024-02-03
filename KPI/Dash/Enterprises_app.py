import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import pycountry_convert as pc
import dash_table

# Charger le fichier CSV
chemin_fichier = r'C:\Users\frup00090927\Code File\Code-File\Data\Annuaire Alumni ABC  - Annuaire Alumni ABC.csv'
df = pd.read_csv(chemin_fichier)

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

# Créer le dash app
app = dash.Dash(__name__)

@app.callback(
    dash.dependencies.Output('table-emails', 'data'),
    [dash.dependencies.Input('dropdown-continent', 'value')]
)
def update_emails(continent_selected):
    emails_df = df[df['Continent'] == continent_selected][['Nom', 'Prénom', 'Entreprises', 'Email']]
    return emails_df.to_dict('records')

# Ajouter la table
app.layout = html.Div([
    html.H1('Annuaire Alumni ABC'),
    dcc.Dropdown(id='dropdown-continent', options=[{'label': continent, 'value': continent} for continent in df['Continent'].unique()], value=df['Continent'].unique()[0]),
    dash_table.DataTable(id='table-emails', columns=[{"name": i, "id": i} for i in ['Nom', 'Prénom', 'Entreprises', 'Email']], page_size=10)
])

# Exécuter le dash app
if __name__ == '__main__':
    app.run_server(debug=True)