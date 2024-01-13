import os
import boto3
from botocore.exceptions import NoCredentialsError

def upload_to_s3(local_folder, bucket_name, s3_folder):
    # Set your AWS credentials (replace 'your_access_key' and 'your_secret_key' with your actual credentials)
    aws_access_key = 'AKIARG7HIT7FMTM65YTY'
    aws_secret_key = '2NYC6dFEadIiRNtxn/tn9PHyNqhT9tNVtOOaR2VG'

    # Create an S3 client
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

    # Loop through each file in the local folder
    for root, dirs, files in os.walk(local_folder):
        for file in files:
            # Construct the full path of the local file
            local_file_path = os.path.join(root, file)

            # Construct the S3 key (path within the bucket) based on the local file structure
            s3_key = os.path.join(s3_folder, file)

            try:
                # Upload the file to S3
                s3.upload_file(local_file_path, bucket_name, s3_key)
                print(f"Successfully uploaded {local_file_path} to {bucket_name}/{s3_key}")
            except FileNotFoundError:
                print(f"The file {local_file_path} was not found.")
            except NoCredentialsError:
                print("Credentials not available or incorrect.")

# Example usage:
local_output_folder = "C:/Users/Diane Tchuisseu/Documents/ABClub/Transformed_csv_Meet & Share"
s3_bucket_name = "abcstorages"
s3_output_folder = "Meet & Share/"

upload_to_s3(local_output_folder, s3_bucket_name, s3_output_folder)


