from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

# Load the CSV files
file1_path = r'C:\Users\frup00090927\Code File\Code-File\Data\Liste des candidatures - Candidatures 2021-2022.csv'
file2_path = r'C:\Users\frup00090927\Code File\Code-File\Data\Liste des candidatures - Candidatures 2022-2023.csv'

# Read the CSV files
df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)

# Specify the conditions for filtering in each file
condition_go1 = df1['Go / No Go'] == 'GO'
condition_go2 = df2['Go / No Go'] == 'GO'

# Filter the DataFrames based on the conditions
filtered_df1 = df1[condition_go1]
filtered_df2 = df2[condition_go2]

# Replace 'Réseaux' with 'Réseau' in the 2022-2023 DataFrame
filtered_df2['Pôle souhaité'] = filtered_df2['Pôle souhaité'].replace('Réseaux', 'Réseau')

# Count the occurrences of Pôle souhaité for each file
pole_counts1 = filtered_df1['Pôle souhaité'].value_counts()
pole_counts2 = filtered_df2['Pôle souhaité'].value_counts()

# Create Dash app
app = Dash(__name__)

# Define layout
app.layout = html.Div([
    html.H1(children='Candidatures Analysis', style={'textAlign': 'center'}),
    
    dcc.Tabs([
        dcc.Tab(label='2021-2022', children=[
            dcc.Graph(
                id='bar-plot-1',
                figure={
                    'data': [
                        {'x': pole_counts1.index, 'y': pole_counts1.values, 'type': 'bar', 'name': '2021-2022'},
                    ],
                    'layout': {
                        'title': 'Pôle souhaité Count (2021-2022)',
                        'xaxis': {'title': 'Pôle souhaité'},
                        'yaxis': {'title': 'Count'},
                    }
                },
            ),
        ]),
        
        dcc.Tab(label='2022-2023', children=[
            dcc.Graph(
                id='bar-plot-2',
                figure={
                    'data': [
                        {'x': pole_counts2.index, 'y': pole_counts2.values, 'type': 'bar', 'name': '2022-2023'},
                    ],
                    'layout': {
                        'title': 'Pôle souhaité Count (2022-2023)',
                        'xaxis': {'title': 'Pôle souhaité'},
                        'yaxis': {'title': 'Count'},
                    }
                },
            ),
        ]),
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)
