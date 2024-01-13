import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = r'C:\Users\frup00090927\Code File\Code-File\Data\Annuaire Alumni ABC  - Annuaire Alumni ABC.csv'
df = pd.read_csv(file_path)

# Get the counts of each sector
sector_counts = df['Secteur d\'activité'].value_counts()

# Separate it into the main five sectors
finance_sectors = sector_counts.filter(like='Finance', axis=0).sum()
it_sectors = sector_counts.filter(like='IT', axis=0).sum()
consulting_sectors = sector_counts.filter(like='Consulting', axis=0).sum()
logistics_sectors = sector_counts.filter(like='Logistics', axis=0).sum()
marketing_sectors = sector_counts.filter(like='Marketing', axis=0).sum()

# Plot the counts for the main five sectors using a donut chart
labels = ['Finance', 'IT', 'Consulting', 'Logistics', 'Marketing']
sizes = [finance_sectors, it_sectors, consulting_sectors, logistics_sectors, marketing_sectors]
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen', 'orange']


# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes,labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Draw a white circle in the center to create the donut effect
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title('Alumni par secteurs')
plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is circular.

# Save the plot as an image
plt.savefig('Activité_alumni.png')

plt.tight_layout()
# Show the donut chart
plt.show()
