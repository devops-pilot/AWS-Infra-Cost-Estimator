import argparse
import json
from collections import defaultdict
from tabulate import tabulate
from parser import parse_tfstate
from cost_model import get_resource_cost

def load_tfstate_resources(file_path):
    with open(file_path, "r") as f:
        return json.load(f).get("resources", [])

def build_cost_report(tfstate_path):
    resources = load_tfstate_resources(tfstate_path)
    summary = defaultdict(lambda: {"count": 0, "cost": 0})

    for resource in resources:
        if not resource.get("provider_name", "").startswith("provider[\"registry.terraform.io/hashicorp/aws\"]"):
            continue

        r_type = resource["type"]
        for instance in resource.get("instances", []):
            attributes = instance.get("attributes", {})
            est_cost = get_resource_cost(r_type, attributes)
            summary[r_type]["count"] += 1
            summary[r_type]["cost"] += est_cost

    return summary

def print_report(summary):
    table = []
    total = 0

    for r_type, data in summary.items():
        table.append([r_type, data["count"], f"${data['cost']:.2f}"])
        total += data["cost"]

    print("\n📊 AWS Cost Estimate Summary")
    print(tabulate(table, headers=["Resource Type", "Count", "Estimated Monthly Cost"]))
    print("-" * 50)
    print(f"Total Estimated Cost: ${total:.2f}/month")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Estimate AWS monthly cost from Terraform state")
    parser.add_argument("tfstate_file", help="Path to tfstate JSON file")

    args = parser.parse_args()
    report = build_cost_report(args.tfstate_file)
    print_report(report)
