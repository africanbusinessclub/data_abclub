import os
import boto3

def upload_to_s3_with_duplicate_check(local_directory, bucket_name, s3_base_folder='', exclude_extension='.xlsx'):
    # Set your AWS credentials (replace 'your_access_key' and 'your_secret_key' with your actual credentials)
    aws_access_key = 'AKIARG7HIT7FMVUA4GNO'
    aws_secret_key = 'IUiphTmli4ebUNmfxl9g0s/j6Xw5uvm8E1vSr/W+'
    
    # Create an S3 client
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

    # Keep track of uploaded files to identify duplicates
    uploaded_files = set()

    for root, dirs, files in os.walk(local_directory):
        for file in files:
            if file.endswith(exclude_extension):
                continue

            local_path = os.path.join(root, file)

            # Convert the local path to Unicode, addressing the potential non-ASCII character issue
            local_path_unicode = local_path.encode('utf-8').decode('utf-8')

            # Use os.path.normpath to normalize the path
            local_path_normalized = os.path.normpath(local_path_unicode)

            # Use os.path.relpath to get the relative path
            relative_path = os.path.relpath(local_path_normalized, local_directory)

            # Construct the S3 key based on the relative path and the provided S3 base folder
            s3_key = os.path.join(s3_base_folder, relative_path)

            if s3_key in uploaded_files:
                # If the file already exists in S3, delete it before uploading the new version
                try:
                    s3.delete_object(Bucket=bucket_name, Key=s3_key)
                    print(f"Deleted existing file {s3_key} in {bucket_name}")
                except Exception as e:
                    print(f"Error deleting {s3_key} in {bucket_name}: {e}")

            try:
                # Upload the file to S3
                s3.upload_file(local_path_normalized, bucket_name, s3_key)
                uploaded_files.add(s3_key)  # Add the uploaded file to the set
                print(f"Successfully uploaded {local_path_normalized} to {bucket_name}/{s3_key}")
            except FileNotFoundError:
                print(f"The file {local_path_normalized} was not found.")
            except Exception as e:
                print(f"Error uploading {local_path_normalized}: {e}")

    print("Upload successful")

local_directory = r"G:\Drive partagés\Général 2023-2024"
bucket_name = 'abcstorages'
s3_base_folder = "Général 2023-2024/"