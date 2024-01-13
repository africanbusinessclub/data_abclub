import os
import pandas as pd

def convert_xlsx_to_csv(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through each folder in the input directory
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            # Check if the file is an XLSX file
            if file.endswith(".xlsx"):
                # Construct the full path of the input file
                input_path = os.path.join(root, file)

                # Read the XLSX file into a pandas DataFrame
                df = pd.read_excel(input_path, engine="openpyxl")

                # Construct the full path of the output CSV file
                output_file = os.path.splitext(file)[0] + ".csv"
                output_path = os.path.join(output_folder, output_file)

                # Save the DataFrame to CSV
                df.to_csv(output_path, index=False)


# Specify the root folder containing the Excel files
input_folder  = "G:/Drive partagés/Général 2023-2024"
output_folder = "C:/Users/Diane Tchuisseu/Documents/ABClub/Gala 2023-2024"

# Call the function to convert all Excel files to CSV
convert_xlsx_to_csv(input_folder, output_folder)
