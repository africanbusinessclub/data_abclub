import pandas as pd
import matplotlib.pyplot as plt

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

# Count the occurrences of Pôle souhaité for each file
pole_counts1 = filtered_df1['Pôle souhaité'].value_counts()
pole_counts2 = filtered_df2['Pôle souhaité'].value_counts()

# Check if the DataFrames are not empty before plotting

# Plot the bar plot for file 1
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
pole_counts1.plot(kind='bar', color='skyblue')
plt.title('Candidatures 2021-2022')
plt.xlabel('Pôle souhaité')
plt.ylabel('Count')



# Plot the bar plot for file 2
plt.subplot(1, 2, 2)
pole_counts2.plot(kind='bar', color='skyblue')
plt.title('Candidatures 2022-2023')
plt.xlabel('Pôle souhaité')
plt.ylabel('Count')

# # Save the plot as an image
# plt.savefig('candidatures.png')

# plt.tight_layout()
# plt.show()