import json
import argparse
from collections import Counter

def parse_tfstate(tfstate_file):
    with open(tfstate_file, 'r') as f:
        tfstate = json.load(f)

    resource_counter = Counter()

    for resource in tfstate.get("resources", []):
        if resource.get("provider_name", "").startswith("provider[\"registry.terraform.io/hashicorp/aws\"]"):
            resource_type = resource["type"]
            count = len(resource.get("instances", []))
            resource_counter[resource_type] += count

    return resource_counter

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse Terraform tfstate and list AWS resources")
    parser.add_argument("tfstate_file", help="Path to the Terraform state file (e.g., tfstate.json)")

    args = parser.parse_args()
    results = parse_tfstate(args.tfstate_file)

    print("\n🧾 AWS Resources Found:")
    for res_type, count in results.items():
        print(f"- {res_type}: {count}")
