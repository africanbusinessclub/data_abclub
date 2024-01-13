import boto3
from botocore.exceptions import NoCredentialsError

def remove_duplicates_in_s3(bucket_name, folder_path):
    # Set your AWS credentials (replace 'your_access_key' and 'your_secret_key' with your actual credentials)
    aws_access_key = 'AKIARG7HIT7FMVUA4GNO'
    aws_secret_key = 'IUiphTmli4ebUNmfxl9g0s/j6Xw5uvm8E1vSr/W+'

    # Create an S3 client
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

    # Get a list of objects in the specified folder
    objects = s3.list_objects(Bucket=bucket_name, Prefix=folder_path)['Contents']

    # Create a set to store unique file names
    unique_files = set()

    # Loop through each object in the folder
    for obj in objects:
        # Get the file name of the object
        file_name = obj['Key']

        # If the file name is not in the set, add it and upload it to S3
        if file_name not in unique_files:
            unique_files.add(file_name)
            s3.upload_file(file_name, bucket_name, file_name)
            print(f"Successfully uploaded {file_name} to {bucket_name}/{file_name}")
        else:
            # If the file name is already in the set, delete it from S3
            s3.delete_object(Bucket=bucket_name, Key=file_name)
            print(f"Deleted duplicate file {file_name} from {bucket_name}/{file_name}")

# Example usage:
bucket_name = "abcstorages"
folder_path = "General_2023-2024/"

remove_duplicates_in_s3(bucket_name, folder_path)
