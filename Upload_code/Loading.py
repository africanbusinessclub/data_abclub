import schedule
import time
from Load_files_aws import upload_to_s3_with_duplicate_check


# Define the list of local directories and corresponding S3 base folders
directories = [
    {
        "local_directory": r"G:\Drive partagés\AMID 2023",
        "bucket_name": 'abcstorages',
        "s3_base_folder": "AMID 2023/"
    },
    # Add more directories as needed
    {
        "local_directory": r"G:\Drive partagés\Administration 2022-2023",
        "bucket_name": 'abcstorages',
        "s3_base_folder": "Administration 2022-2023/"
    },
    {
        "local_directory": r"G:\Drive partagés\Communication ABC",
        "bucket_name": 'abcstorages',
        "s3_base_folder": "Communication ABC/"
    },
    {
        "local_directory": r"G:\Drive partagés\Elit'",
        "bucket_name": 'abcstorages',
        "s3_base_folder": "Elit'/"
    },
    {
        "local_directory": r"G:\Drive partagés\Forum Elit 2018",
        "bucket_name": 'abcstorages',
        "s3_base_folder": "Forum Elit 2018/"
    },
    {
        "local_directory": r"G:\Drive partagés\Général 2023-2024",
        "bucket_name": 'abcstorages',
        "s3_base_folder": "Général 2023-2024/"
    },
    {
        "local_directory": r"G:\Drive partagés\Meet & Share",
        "bucket_name": 'abcstorages',
        "s3_base_folder": "Meet & Share/"
    }
]

# Define the function to run for each directory
def run_upload_for_directories():
    for directory_info in directories:
        upload_to_s3_with_duplicate_check(directory_info["local_directory"], directory_info["bucket_name"], directory_info["s3_base_folder"])

# Define the schedule
schedule.every().week.do(run_upload_for_directories)

# Run the schedule
while True:
    schedule.run_pending()
    time.sleep(1)