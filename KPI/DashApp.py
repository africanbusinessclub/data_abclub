import pandas as pd
import matplotlib.pyplot as plt
import boto3
from io import BytesIO
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Load the CSV file
alumni_file_path = r'C:\Users\frup00090927\Code File\Code-File\Data\Annuaire Alumni ABC  - Annuaire Alumni ABC.csv'
alumni_df = pd.read_csv(alumni_file_path)

# Connect to S3 and load the CSV files
s3 = boto3.client('s3', aws_access_key_id='AKIARG7HIT7FMVUA4GNO', aws_secret_access_key='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')
bucket_name = 'abcstorages'

# Load the CSV files for data comparison
file1_path = r'C:\Users\frup00090927\Code File\Code-File\Data\Liste des invités - Gala des 10 ans .csv'
file2_path = r'C:\Users\frup00090927\Code File\Code-File\Data\Liste Finale Participants GALA.csv'
df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)

# Load the CSV files for candidatures analysis
candidatures_file1 = r'C:\Users\frup00090927\Code File\Code-File\Data\Liste des candidatures - Candidatures 2021-2022.csv'
candidatures_file2 = r'C:\Users\frup00090927\Code File\Code-File\Data\Liste des candidatures - Candidatures 2022-2023.csv'
candidatures_df1 = pd.read_csv(candidatures_file1)
candidatures_df2 = pd.read_csv(candidatures_file2)

# Specify the conditions for filtering in each file
condition_go1 = candidatures_df1['Go / No Go'] == 'GO'
condition_go2 = candidatures_df2['Go / No Go'] == 'GO'

# Filter the DataFrames based on the conditions
filtered_df1 = candidatures_df1[condition_go1]
filtered_df2 = candidatures_df2[condition_go2]

# Replace 'Réseaux' with 'Réseau' in the 2022-2023 DataFrame
filtered_df2['Pôle souhaité'] = filtered_df2['Pôle souhaité'].replace('Réseaux', 'Réseau')

# Count the occurrences of Pôle souhaité for each file
pole_counts1 = filtered_df1['Pôle souhaité'].value_counts()
pole_counts2 = filtered_df2['Pôle souhaité'].value_counts()



# Dash App
app = dash.Dash(__name__)

# Define layout for each tab
tab1_layout = html.Div([
    dcc.Graph(
        id='donut-chart',
        figure={
            'data': [
                {
                    'labels': ['Finance', 'IT', 'Consulting', 'Logistics', 'Marketing'],
                    'values': [alumni_df['Secteur d\'activité'].str.contains('Finance').sum(),
                               alumni_df['Secteur d\'activité'].str.contains('IT').sum(),
                               alumni_df['Secteur d\'activité'].str.contains('Consulting').sum(),
                               alumni_df['Secteur d\'activité'].str.contains('Logistics').sum(),
                               alumni_df['Secteur d\'activité'].str.contains('Marketing').sum()],
                    'type': 'pie',
                    'hole': 0.7,
                    'marker': {'colors': ['gold', 'lightcoral', 'lightskyblue', 'lightgreen', 'orange']}
                }
            ],
            'layout': {
                'title': 'Alumni par secteurs',
                'annotations': [
                    {
                        'font': {'size': 20},
                        'showarrow': False,
                        'text': 'Total',
                        'x': 0.5,
                        'y': 0.5
                    }
                ]
            }
        }
    )
])

tab2_layout = html.Div([
    dcc.Graph(
        id='data-comparison-chart',
        figure={
            'data': [
                {'x': df1['Catégorie'].value_counts().index, 'y': df1['Catégorie'].value_counts().values, 'type': 'bar', 'name': 'Gala 2013', 'marker': {'color': 'blue'}},
                {'x': df2['Catégorie'].value_counts().index, 'y': df2['Catégorie'].value_counts().values, 'type': 'bar', 'name': 'Gala 2023', 'marker': {'color': 'orange'}}
            ],
            'layout': {
                'title': 'Catégorie des invites',
                'xaxis': {'title': 'Category'},
                'yaxis': {'title': 'Count'},
                'barmode': 'group'
            }
        }
    )
])

tab3_layout = html.Div([
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

# Define the layout of the app
app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label='Alumni Analysis', children=tab1_layout),
        dcc.Tab(label='Data Comparison', children=tab2_layout),
        dcc.Tab(label='Candidatures Analysis', children=tab3_layout),
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
