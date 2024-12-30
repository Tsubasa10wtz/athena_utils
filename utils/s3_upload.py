import os.path
import concurrent.futures
import boto3
from tqdm import tqdm
from botocore.exceptions import ClientError


def get_all_files_in_directory(directory):
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths


class S3Helper:
    def __init__(self, aws_access_key_id, aws_secret_access_key, bucket_name, num_threads):
        self.s3 = boto3.client('s3',
                               aws_access_key_id=aws_access_key_id,
                               aws_secret_access_key=aws_secret_access_key)
        self.bucket_name = bucket_name
        self.num_threads = num_threads
        self.err_list = []

    def upload_dir(self, local_dir_path, s3_dir_path):
        files = get_all_files_in_directory(local_dir_path)
        pairs = [(file, file.replace(local_dir_path, s3_dir_path)) for file in files]
        # Add a total progress bar for all files
        with tqdm(total=len(pairs), desc="Uploading Files") as pbar:
            self.upload_files(pairs, pbar)
        print(f"err_list: {self.err_list}")

    def upload_files(self, pairs, pbar):
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.num_threads) as thread_executor:
            futures = []
            for local_path, s3_path in pairs:
                futures.append(thread_executor.submit(self.upload_file, local_path, s3_path, pbar))
            for future in tqdm(concurrent.futures.as_completed(futures), total=len(futures), desc="Uploading"):
                future.result()

    def upload_file(self, local_path, s3_path, pbar):
        if self.check_if_file_exists(s3_path):
            return
        try:
            with open(local_path, 'rb') as file_data:
                self.s3.put_object(Bucket=self.bucket_name, Key=s3_path, Body=file_data)
            pbar.update(1)  # Update the total progress bar after each successful upload
        except ClientError as e:
            print(f"{local_path} -> {s3_path} failed: {e}")
            self.err_list.append((self.bucket_name, local_path, s3_path))
        else:
            pass

    def check_if_file_exists(self, object_key):
        try:
            self.s3.head_object(Bucket=self.bucket_name, Key=object_key)
        except ClientError as e:
            return False
        return True


if __name__ == '__main__':
    bucket_name = 'alluxiobucket'
    aws_access_key_id = ''
    aws_secret_access_key = ''
    num_threads = 64

    local_dir_path = "/Users/wangtianze/直博/项目/Athena/athena/lakebench/union/data"
    s3_dir_path = "alluxio/lakebench/union"
    s3 = S3Helper(aws_access_key_id, aws_secret_access_key, bucket_name, num_threads)
    s3.upload_dir(local_dir_path, s3_dir_path)

    print("finished")