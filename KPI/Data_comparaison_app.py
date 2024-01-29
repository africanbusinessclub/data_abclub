import pandas as pd
import matplotlib.pyplot as plt
import boto3
from io import BytesIO
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Connect to S3 and load the CSV file directly
s3 = boto3.client('s3', aws_access_key_id='AKIARG7HIT7FMVUA4GNO', aws_secret_access_key='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')
bucket_name = 'abcstorages'

# Load the CSV files
file1_path = r'C:\Users\frup00090927\Code File\Code-File\Data\Liste des invités - Gala des 10 ans .csv'
file2_path = r'C:\Users\frup00090927\Code File\Code-File\Data\Liste Finale Participants GALA.csv'

# obj1 = s3.get_object(Bucket=bucket_name, Key=file1_path)
# df1 = pd.read_csv(BytesIO(obj1['Body'].read()))
df1 = pd.read_csv(file1_path)
# obj2 = s3.get_object(Bucket=bucket_name, Key=file2_path)
# df2 = pd.read_csv(BytesIO(obj2['Body'].read()))
df2 = pd.read_csv(file2_path)

# Assuming 'Categorie' is the column you want to compare
categories_count_file1 = df1['Catégorie'].value_counts()
categories_count_file2 = df2['Catégorie'].value_counts()

# Create Dash App
app = dash.Dash(__name__)

# Define layout
app.layout = html.Div([
    dcc.Graph(
        id='data-comparison-chart',
        figure={
            'data': [
                {'x': categories_count_file1.index, 'y': categories_count_file1, 'type': 'bar', 'name': 'Gala 2013', 'marker': {'color': 'blue'}},
                {'x': categories_count_file2.index, 'y': categories_count_file2, 'type': 'bar', 'name': 'Gala 2023', 'marker': {'color': 'orange'}}
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

#if __name__ == '__main__':
 #   app.run_server(debug=True)
