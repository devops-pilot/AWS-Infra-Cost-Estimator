# 💰 AWS Cost Inspector

A Python-based tool that estimates your monthly AWS infrastructure costs by analyzing **Terraform state files** stored in **Amazon S3**.

---

## 🌟 Features

- 🧾 **Download `terraform.tfstate` from S3**
- 🔍 **Parse** Terraform-managed AWS resources
- 💰 **Estimate monthly cost** using a static cost model
- 📊 **Summarize** resource types, counts, and total cost
- 🔐 **Offline & secure** – no AWS billing API or credentials required

---

## 📁 Project Structure
```
aws-cost-inspector/
├── fetch/
│ └── fetch_tfstate.py # Downloads Terraform state file from S3
├── cost/
│ ├── parser.py # Parses AWS resource types from tfstate
│ ├── cost_model.py # Maps resource types to estimated costs
│ └── report.py # Generates a CLI report
├── examples/
│ └── sample_output.txt # Optional example output
├── requirements.txt
├── .gitignore
└── README.md ```

---
```
## 🔧 Setup Instructions

### 1. 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

## 2. 🔐 Set AWS Credentials
### Ensure you have permission to read the S3 bucket containing your terraform.tfstate:
```
export AWS_ACCESS_KEY_ID=your-key
export AWS_SECRET_ACCESS_KEY=your-secret
export AWS_DEFAULT_REGION=us-east-1
```
## 🚀 How to Use
### Step 1️⃣: Download the terraform.tfstate from S3
```
python fetch/fetch_tfstate.py --bucket my-bucket-name --key path/to/terraform.tfstate
```
###### This saves the file as tfstate.json by default.

## Step 2️⃣: Estimate AWS Resource Cost
``` python cost/report.py tfstate.json```
## 🧾 Example Output
```
📊 AWS Cost Estimate Summary
----------------------------
| Resource Type     | Count | Estimated Monthly Cost |
|-------------------|-------|-------------------------|
| aws_instance      |   2   | $16.00                 |
| aws_s3_bucket     |   1   | $1.15                  |
| aws_db_instance   |   1   | $15.00                 |
------------------------------------------------------
Total Estimated Cost: $32.15/month
```
## 📦 Supported Resources (Initial Set)
```
| AWS Resource Type | Cost Logic Used                           |
| ----------------- | ----------------------------------------- |
| `aws_instance`    | Based on instance type (e.g., `t3.micro`) |
| `aws_s3_bucket`   | Assumes 50 GB @ \$0.023/GB                |
| `aws_db_instance` | Based on DB instance class                |
| `aws_ebs_volume`  | Assumes 100 GB @ \$0.10/GB                |
| `aws_elb`         | Flat rate estimate                        |
| `aws_alb`         | Flat rate estimate                        |
```
##### 🛠️ Pricing is static and simplified for estimation purposes.

## 🛡️ Security Notes
- ❌ No actual billing data is pulled from AWS
- ✅ Only reads metadata from .tfstate
- ✅ Safe to run offline and in CI/CD environments
- ⚠️ Make sure not to expose real .tfstate publicly (they may contain outputs or sensitive info)

## 🚧 Future Enhancements
 - Region-specific pricing support
 - Reserved instance and savings plan logic
 - terraform show -json support
 - GitHub Actions workflow
 - Export reports to CSV/JSON
 - Email or Slack alerts for cost spikes

## 🤝 Contributions
- Feel free to fork this project, suggest improvements, or submit PRs. Contributions are always welcome!
## 📄 License
 - MIT



