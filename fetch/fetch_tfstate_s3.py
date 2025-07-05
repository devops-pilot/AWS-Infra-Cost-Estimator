import boto3
import argparse
import os

def download_tfstate(bucket_name, key, output_file):
    s3 = boto3.client("s3")
    try:
        s3.download_file(bucket_name, key, output_file)
        print(f"✅ Downloaded {key} from S3 bucket '{bucket_name}' to '{output_file}'")
    except Exception as e:
        print(f"❌ Error downloading file: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download Terraform state file from S3")
    parser.add_argument("--bucket", required=True, help="S3 bucket name")
    parser.add_argument("--key", required=True, help="S3 object key (path to tfstate)")
    parser.add_argument("--output", default="tfstate.json", help="Output file name (default: tfstate.json)")

    args = parser.parse_args()
    download_tfstate(args.bucket, args.key, args.output)
