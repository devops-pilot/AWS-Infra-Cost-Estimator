# 💰 AWS Cost Inspector

A Python tool that estimates monthly AWS infrastructure cost by analyzing Terraform state files stored in S3.

## ✅ Features

- 🔁 Downloads `terraform.tfstate` from a specified S3 bucket
- 🔍 Parses AWS resources (EC2, S3, RDS, EBS, etc.)
- 💰 Estimates monthly cost using public pricing models
- 📊 Outputs clean CLI reports

## ⚙️ Setup

```bash
pip install -r requirements.txt
