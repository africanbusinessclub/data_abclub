import pandas as pd

# Load the CSV file
file_path = 'C:/Users/Diane Tchuisseu/Documents/ABClub/Code File/Liste des invités - Gala des 10 ans .csv'
df = pd.read_csv(file_path)

#Replace 'African Business Club' in the 'Categorie' column with 'Membre ABC'
#df['Catégorie'] = df['Catégorie'].replace('African Business Club ', 'Membre ABC')


#Replace 'Anciens' in the 'Categorie' column with 'ALUMNI ABC'
#df['Catégorie'] = df['Catégorie'].replace('Anciens', 'ALUMNI ABC')

#Replace 'unknown work' in the 'Categorie' column with 'EXTERIEURE'
df['Catégorie'] = df['Catégorie'].replace('unknown work', 'EXTERIEURE')

# Replace missing values in the "Categorie" column with "unknown work"
#df['Catégorie'].fillna('unknown work', inplace=True)

# Remove the last five columns
#df = df.iloc[:, :-5]

# Save the updated DataFrame back to the CSV file
df.to_csv(file_path, index=False)


#print("Missing values filled with 'unknown work'. Last five columns removed.")



