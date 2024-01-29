import pandas as pd
import matplotlib.pyplot as plt
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Load the CSV file
file_path = r'C:\Users\frup00090927\Code File\Code-File\Data\Annuaire Alumni ABC  - Annuaire Alumni ABC.csv'
df = pd.read_csv(file_path)

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
                    'values': [df['Secteur d\'activité'].str.contains('Finance').sum(),
                               df['Secteur d\'activité'].str.contains('IT').sum(),
                               df['Secteur d\'activité'].str.contains('Consulting').sum(),
                               df['Secteur d\'activité'].str.contains('Logistics').sum(),
                               df['Secteur d\'activité'].str.contains('Marketing').sum()],
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

# Define the layout of the app
app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label='Donut Chart', children=tab1_layout),
        # Add more tabs as needed
    ])
])

#if __name__ == '__main__':
 #   app.run_server(debug=True)
