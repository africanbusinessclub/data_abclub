import os
import hashlib

def delete_csv_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.csv'):
                # Construct the full path to the CSV file
                csv_path = os.path.join(root, file)

                # Delete the CSV file
                os.remove(csv_path)
                print(f'Deleted {csv_path}')

# Specify the root folder containing the CSV files
root_folder = 'C:/Users/Diane Tchuisseu/Documents/ABClub/General_2023-2024'

# Call the function to delete all CSV files
delete_csv_files(root_folder)

