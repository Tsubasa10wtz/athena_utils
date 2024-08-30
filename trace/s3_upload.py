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
        self.upload_files(pairs)
        print(f"err_list: {self.err_list}")

    def upload_files(self, pairs):
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.num_threads) as thread_executor:
            futures = []
            for local_path, s3_path in tqdm(pairs):
                futures.append(thread_executor.submit(self.upload_file, local_path, s3_path))
            for future in tqdm(concurrent.futures.as_completed(futures)):
                future.result()

    def upload_file(self, local_path, s3_path):
        if self.check_if_file_exists(s3_path):
            # print(f"{local_path} -> {s3_path} existed")
            return
        try:
            self.s3.put_object(Bucket=self.bucket_name, Key=s3_path, Body=open(local_path, 'rb'))
        except ClientError as e:
            print(f"{local_path} -> {s3_path} failed: {e}")
            self.err_list.append((self.bucket_name, local_path, s3_path))
        else:
            # print(f"{local_path} -> {s3_path} uploaded")
            pass

    def check_if_file_exists(self, object_key):
        try:
            self.s3.head_object(Bucket=self.bucket_name, Key=object_key)
        except ClientError as e:
            return False
        return True


if __name__ == '__main__':
    bucket_name = 'alluxiobucket'
    aws_access_key_id = 'AKIAUTMJIZIJE5HMS7HY'
    aws_secret_access_key = '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'
    num_threads = 64

    local_dir_path = "cluster035/"
    s3_dir_path = "alluxio/twitter/cluster035/"
    s3 = S3Helper(aws_access_key_id, aws_secret_access_key, bucket_name, num_threads)
    s3.upload_dir(local_dir_path, s3_dir_path)

    print("finished")
